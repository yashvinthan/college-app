import React, { useEffect, useState } from reactjsx
import axios from 'axios';

const GradeView = () => {
    const [grades, setGrades] = useState([]);

    useEffect(() => {
        const fetchGrades = async () => {
            const response = await axios.get('/api/grades/');
            setGrades(response.data);
        };
        fetchGrades();
    }, []);

    return (
        <div>
            <h2>Your Grades</h2>
            <ul>
                {grades.map(grade => (
                    <li key={grade.id}>
                        {grade.assignment.title}: {grade.score}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default GradeView;