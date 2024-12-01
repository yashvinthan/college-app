import React from 'react';
import Notifications from './Notifications';
import CourseList from './CourseList';
import UpcomingAssignments from './UpcomingAssignments';

const Dashboard = () => {
    return (
        <div style={{ display: 'flex', flexDirection: 'column', padding: '20px' }}>
            <h1>Dashboard</h1>
            <UpcomingAssignments />
            <CourseList />
            <Notifications />
        </div>
    );
};

export default Dashboard;