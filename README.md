# AI-Powered Digital Addiction Prevention Platform

## Project Description

The AI-Powered Digital Addiction Prevention Platform is an intelligent web-based system designed to monitor, analyze, and reduce excessive digital device usage. The platform uses Artificial Intelligence and Machine Learning techniques to identify signs of digital addiction based on user behavior, screen time, social media usage, gaming habits, and sleep patterns.

The system helps users maintain a healthy digital lifestyle by generating addiction risk scores, providing personalized recommendations, visualizing usage trends, and offering preventive interventions before addiction becomes severe. The platform is particularly useful for students, professionals, parents, educational institutions, and organizations seeking to promote digital wellness.

---

## Problem Statement

Excessive usage of smartphones, social media, online gaming, and internet services has become a major concern worldwide. Prolonged screen exposure can lead to reduced productivity, poor academic performance, sleep disorders, anxiety, depression, and digital addiction.

Existing screen-time monitoring tools provide usage statistics but lack intelligent prediction and personalized intervention mechanisms. This project aims to address this issue by developing an AI-powered platform capable of predicting addiction risks and encouraging healthier digital habits.

---

## Objectives

- Monitor user digital activities.
- Analyze screen time patterns.
- Predict digital addiction risk using Machine Learning.
- Generate personalized recommendations.
- Encourage healthy digital habits.
- Improve productivity and mental well-being.
- Provide real-time alerts and notifications.
- Visualize user behavior through dashboards and reports.

---

## Features

### User Authentication

- User Registration
- User Login
- Secure Session Management
- Password Protection
- Profile Management

### Digital Activity Monitoring

- Screen Time Tracking
- Social Media Usage Monitoring
- Gaming Time Monitoring
- Sleep Pattern Tracking
- Daily Activity Logging

### AI-Based Addiction Prediction

- Addiction Risk Analysis
- Behavioral Pattern Recognition
- Risk Classification
- Predictive Analytics

### Smart Recommendation System

- Personalized Suggestions
- Digital Detox Plans
- Screen Time Reduction Goals
- Productivity Improvement Tips

### Alert System

- Screen Time Warnings
- Usage Limit Notifications
- Break Reminders
- Wellness Recommendations

### Dashboard Analytics

- Daily Reports
- Weekly Reports
- Monthly Reports
- Usage Trend Visualization
- Addiction Score History

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend

- Python
- Flask

### Database

- SQLite
- SQLAlchemy

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy

### Visualization

- Matplotlib
- Chart.js

---

## System Architecture

User

↓

Web Interface

↓

Flask Backend

↓

Database Storage

↓

Machine Learning Model

↓

Addiction Risk Prediction

↓

Recommendation Engine

↓

Dashboard and Reports

---

## Modules

### Module 1: User Management

Functions:

- Registration
- Login
- Profile Management

### Module 2: Activity Monitoring

Functions:

- Screen Time Collection
- Social Media Tracking
- Gaming Activity Tracking
- Sleep Data Collection

### Module 3: Machine Learning Prediction

Functions:

- Data Preprocessing
- Feature Extraction
- Risk Prediction
- Risk Classification

### Module 4: Recommendation Engine

Functions:

- Personalized Advice
- Goal Setting
- Digital Wellness Guidance

### Module 5: Dashboard

Functions:

- Usage Statistics
- Trend Analysis
- Addiction Reports

---

## Dataset Information

Dataset Name:

addiction_dataset.csv

Dataset Features:

| Feature | Description |
|----------|-------------|
| screen_time | Total daily screen time (hours) |
| social_media | Social media usage time (hours) |
| gaming | Gaming duration (hours) |
| sleep | Sleep duration (hours) |
| risk | Addiction risk level |

Risk Labels:

| Value | Meaning |
|---------|---------|
| 0 | Low Risk |
| 1 | Moderate Risk |
| 2 | High Risk |

---

## Machine Learning Workflow

### Input

- Screen Time
- Social Media Usage
- Gaming Duration
- Sleep Duration

### Processing

- Data Cleaning
- Feature Selection
- Model Training
- Model Evaluation

### Output

- Low Addiction Risk
- Moderate Addiction Risk
- High Addiction Risk

---

## Database Design

### User Table

| Field | Type |
|---------|---------|
| id | Integer |
| username | String |
| password | String |

### Activity Table

| Field | Type |
|---------|---------|
| id | Integer |
| username | String |
| screen_time | Float |
| social_media | Float |
| gaming | Float |
| sleep | Float |

---
## Project Structure

```text
digital-addiction-prevention/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   └── addiction_model.pkl
│
└── data/
    └── addiction_dataset.csv
```

---

## Expected Output

The system predicts addiction risk based on user behavior and displays one of the following results:

### Low Risk

- Healthy Usage
- Good Sleep Pattern
- Balanced Screen Time

### Moderate Risk

- Increased Usage
- Potential Addiction Symptoms
- Recommendations Provided

### High Risk

- Excessive Screen Time
- Poor Sleep Pattern
- Strong Addiction Indicators
- Immediate Intervention Suggested

---

## Future Enhancements

- Android Mobile Application
- Real-Time Screen Monitoring
- App Blocking System
- AI Wellness Chatbot
- Wearable Device Integration
- Parent Monitoring Dashboard
- Email and SMS Alerts
- Deep Learning Models
- Mental Health Assessment
- Emotion Detection using Computer Vision

---

## Benefits

- Prevents Digital Addiction
- Improves Productivity
- Encourages Healthy Habits
- Enhances Mental Well-being
- Promotes Better Sleep Quality
- Provides Personalized Guidance
- Supports Students and Professionals

---

## Conclusion

The AI-Powered Digital Addiction Prevention Platform provides an innovative solution for identifying and preventing digital addiction using Artificial Intelligence and Machine Learning. By continuously monitoring user behavior, predicting addiction risks, and delivering personalized recommendations, the system promotes healthier technology usage and improves overall well-being. The project demonstrates the practical application of AI in digital wellness and can be further expanded into a full-scale commercial solution for individuals, families, educational institutions, and organizations.

