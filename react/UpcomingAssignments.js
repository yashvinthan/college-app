import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UpcomingAssignments = () => {
    const [assignments, setAssignments] = useState([]);

    useEffect(() => {
        const fetchAssignments = async () => {
            const response = await axios.get('/api/assignments/');
            setAssignments(response.data);
        };
        fetchAssignments();
    }, []);

    return (
        <div>
            <h2>Upcoming Assignments</h2>
            <ul>
                {assignments.map(assignment => (
                    <li key={assignment.id}>{assignment.title} - Due: {new Date(assignment.due_date).toLocaleDateString()}</li>
                ))}
            </ul>
        </div>
    );
};

export default UpcomingAssignments;