import React, { useState } from 'react';

const SearchFilter = ({ courses }) => {
    const [searchTerm, setSearchTerm] = useState('');

    const filteredCourses = courses.filter(course =>
        course.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div>
            <input
                type="text"
                placeholder="Search courses..."
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <ul>
                {filteredCourses.map(course => (
                    <li key={course.id}>{course.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default SearchFilter;