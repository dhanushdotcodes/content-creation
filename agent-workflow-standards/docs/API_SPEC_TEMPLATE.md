# API Specification
---
Base URL: /api/v1

All endpoints return JSON responses:
```
{
  "data": {},
  "error": null,
  "message": "success"
}
```
Error response:
```
{
  "data": null,
  "error": "VALIDATION_ERROR",
  "message": "Email is required"
}
```

## Authentication
---
POST /api/v1/auth/login - login

## Category management
---
GET /api/v1/categories - get all categories
POST /api/v1/categories - create a new category
GET /api/v1/categories/{id} - get a specific category
PUT /api/v1/categories/{id} - update a specific category
DELETE /api/v1/categories/{id} - delete a specific category

## Todo management
---
GET /api/v1/todos - get all todos
GET /api/v1/categories/{id}/todos - get all todos for a category
POST /api/v1/categories/{id}/todo - create a new todo for a category
GET /api/v1/categories/{id}/todo/{todo_id} - get a specific todo
PUT /api/v1/categories/{id}/todo/{todo_id} - update a specific todo
DELETE /api/v1/categories/{id}/todo/{todo_id} - delete a specific todo
PATCH /api/v1/categories/{id}/todo/{todo_id}/complete - complete a specific todo