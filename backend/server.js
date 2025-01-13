// backend/server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../frontend')));

// Database connection
mongoose.connect('mongodb://localhost:27017/career_portal', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Import routes
const internshipRoutes = require('./routes/internshipRoutes');
const jobRoutes = require('./routes/jobRoutes');
const hackathonRoutes = require('./routes/hackathonRoutes');
const applicationRoutes = require('./routes/applicationRoutes');
const activityRoutes = require('./routes/activityRoutes');

// Route middleware
app.use('/api/internships', internshipRoutes);
app.use('/api/jobs', jobRoutes);
app.use('/api/hackathons', hackathonRoutes);
app.use('/api/applications', applicationRoutes);
app.use('/api/activities', activityRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something went wrong!' });
});

// Serve frontend pages
app.get('/pages/:page', (req, res) => {
    res.sendFile(path.join(__dirname, `../frontend/pages/${req.params.page}`));
});

// Serve the main index.html for the root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;