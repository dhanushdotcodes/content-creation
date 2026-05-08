# Product Requirements Document

## TodoApp

TodoApp helps me manage my daily tasks and organize them into categories in a simple and installable web application.

## Core Modules
- Authentication Management - Password based access using a stored hashed password.
- Category Management - Add, Edit, Delete Categories to group todos.
- Todo Management - Add, Edit, Delete Todos linked to Categories.
- Progress Tracking - Track completion percentage of todos within categories.
- PWA Support - Installable mobile-friendly application experience.

## Success Metrics
- Successfully creating and managing categories.
- Successfully creating and completing todos associated with categories.
- Correct calculation of category completion percentage.
- Correctly identifying overdue todos.
- Containerisation and successful deployment of the application.
- Successful generation of fake todo and category data for testing purposes using faker.js.

## User Flow

### Core loop
- User enters the password to access the application.
- User creates a category (e.g., "Work", "Personal").
- User adds todos associated with the category.
- User completes todos progressively.
- Application updates the category completion percentage.
- User views completed todos and manages active ones.

## Milestones

| Milestone | Description |
| :--- | :--- |
| **M1** | Adding rules, agents, project specifications, and defining the MVP architecture. |
| **M2** | Setting up PostgreSQL with Docker and migrating schema using Alembic. |
| **M3** | Implementing password-based authentication using FastAPI and secure hashed password validation. |
| **M4** | Creating CRUD operations for Categories and Todos based on the user flow and DB schema. |
| **M5** | Building the Next.js dashboard interface with progress tracking and todo lists. |
| **M6** | Configuring the application as a PWA with installable support and responsive layouts. |
| **M7** | Implementing faker.js scripts and Docker Compose setup for local development and testing. |
| **M8** | Writing integration tests using pytest and TestClient for all APIs and flows. |