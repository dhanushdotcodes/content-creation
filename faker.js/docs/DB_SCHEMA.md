# Database Schema
---
## Core Tables
---

job_applications

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the job application |
| company | varchar | | Name of the company |
| position | varchar | | Job title or role applied for |
| salary | varchar | | Target or offered salary |
| location | varchar | | Job location (e.g., Remote, On-site) |
| status | enum | `'applied', 'interviewing', 'offered', 'rejected'` | Current stage of the job application |
| job_url | varchar | | Direct link to the job posting |
| notes | text | | Additional context and details |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |
