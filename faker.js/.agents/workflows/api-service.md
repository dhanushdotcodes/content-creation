---
description: Create a full API stack with separate types, helpers, services, controllers, and routes following strict layer responsibilities.
---

1. **Information Gathering**: Ask for the entity name (e.g., "order") and the Prisma model it maps to.

2. **Generate Types**: Create `src/@types/[entity].ts`.
   - Define custom Request/Response interfaces.
   - Do not define types inside business logic files.
   - Export explicit types for the frontend to consume.

3. **Steps**
   - **Service**: Create `src/services/[entity]-service.ts`.
     - Implement CRUD and all business logic using `prisma.[model]`.
     - Only layer allowed to interact with Prisma (using the singleton Prisma client at `src/lib/prisma.ts`).
     - Must not depend on the HTTP layer.
     - Calls helpers for any generic data manipulation or formatting.
     - Throws errors when something goes wrong.
   - **Helper**: Create `src/helpers/[entity]-helper.ts`.
     - Add pure, generic functions for formatting, parsing, or any service-specific helpers.
   - **Controller**: Create `src/controllers/[entity]-controller.ts`.
     - Parse requests and handle input validation.
     - Call services to complete the task.
     - Do not interact with Prisma directly.
     - Handle errors and format all API responses using the standard structure:
       ```typescript
       {
         success: boolean,
         data?: unknown,
         error?: string
       }
       ```
   - **Route**: Create `src/routes/[entity]-routes.ts`.
     - Only define endpoints and map to controller handlers.
     - No business logic or database access.

4. **Database Sync**
   - Run `bunx prisma generate` to ensure the local client is aware of any schema changes.

5. **Integration**: 
   - Add the new route to the main server entry point.
   - Run unit tests and type-checks to verify the correct flow: `Route → Controller → Service → Prisma`.