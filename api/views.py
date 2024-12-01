from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Assignment, Grade, CustomUser 
from .serializers import CourseSerializer, AssignmentSerializer, GradeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacher
from django.contrib.auth import get_user_model
from rest_framework import generics

# User Management
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser .objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Course Management
class CourseView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        courses = Course.objects.filter(teacher=request.user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Assignment Management
class AssignmentView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        assignments = Assignment.objects.filter(course__teacher=request.user)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Grade Management
class GradeView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        grades = Grade.objects.filter(assignment__course__teacher=request.user)
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser .objects.all()
    serializer_class = UserSerializer

class AssignmentSubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        submissions = AssignmentSubmission.objects.filter(student=request.user)
        serializer = AssignmentSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)