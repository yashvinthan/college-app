import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: TimetableScreen(),
    );
  }
}

class TimetableScreen extends StatefulWidget {
  @override
  _TimetableScreenState createState() => _TimetableScreenState();
}

class _TimetableScreenState extends State<TimetableScreen> {
  List<dynamic> timetables = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchTimetables();
  }

  Future<void> fetchTimetables() async {
    final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/timetable/'));
    if (response.statusCode == 200) {
      setState(() {
        timetables = json.decode(response.body);
        isLoading = false;
      });
    } else {
      print('Failed to load timetables');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Timetable')),
      body: isLoading
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: timetables.length,
              itemBuilder: (context, index) {
                final timetable = timetables[index];
                return ListTile(
                  title: Text(timetable['subject']),
                  subtitle: Text('${timetable['day']} (${timetable['start_time']} - ${timetable['end_time']})'),
                );
              },
            ),
    );


  }
}
