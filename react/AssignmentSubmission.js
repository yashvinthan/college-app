import React, { useState } from 'react';
import axios from 'axios';

const AssignmentSubmission = ({ assignmentId }) => {
    const [file, setFile] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('assignment', assignmentId);
        formData.append('file', file);
        await axios.post('/api/submissions/', formData);
        // Handle successful submission (e.g., show notification)
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} required />
            <button type="submit">Submit Assignment</button>
        </form>
    );
};

export default AssignmentSubmission;