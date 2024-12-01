import React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Dashboard from './Dashboard';
import { useState } from 'react';

const App = () => {
    const [darkMode, setDarkMode] = useState(false);
    const theme = createTheme({
        palette: {
            mode: darkMode ? 'dark' : 'light',
        },
    });

    return (
        <ThemeProvider theme={theme}>
            <div>
                <button onClick={() => setDarkMode(!darkMode)}>
                    Toggle Dark Mode
                </button>
                <Dashboard />
            </div>
        </ThemeProvider>
    );
};

export default App;