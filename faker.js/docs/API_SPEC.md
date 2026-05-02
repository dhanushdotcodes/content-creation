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

## Job Applications
---
POST /applications — create a new job application.

GET /applications — list all applications.

GET /applications/:id — get one application by ID.

PATCH /applications/:id — update part of an application, like status or notes.

DELETE /applications/:id — delete an application