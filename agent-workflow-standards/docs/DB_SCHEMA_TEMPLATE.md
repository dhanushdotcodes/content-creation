# Database Schema
---
## Core Tables
---

todos

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | Primary Key | Unique identifier for the todo |
| title | varchar | | Todo Title |
| completed | boolean | | Todo completion status |
| category_id | uuid | Foreign Key | Link to parent category |
| created_at | timestamp | | Todo creation timestamp |
| updated_at | timestamp | | Todo last updated timestamp |

---
categories
---

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | Primary Key | Unique identifier for the category |
| title | varchar | | Category Title |
| description | varchar | Optional | Optional category description |
| created_at | timestamp | | Category creation timestamp |
| updated_at | timestamp | | Category last updated timestamp |
