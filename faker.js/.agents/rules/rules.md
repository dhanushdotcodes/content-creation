---
trigger: always_on
---

# Rules

You are an expert developer assistant specializing in Bun.js, TypeScript, and Prisma.

---

## 1. General Principles

- Do not go out of the scope of the problem asked.
- Do not fix, refactor, or improve existing code conventions unless explicitly asked.
- Always follow existing patterns in the codebase.
- Comments must explain "Why", not "What".

---

## 2. Core Stack

- Runtime: Bun.js
- Framework: Express.js
- Language: TypeScript (strict mode)
- Database: PostgreSQL (Docker)
- ORM: Prisma


---

## 3. Project Structure

src/
  controllers/   -> Handles request/response only
  routes/        -> Route definitions only
  helpers/       -> Helper functions for services handlers
  services/      -> Business logic only
  validation/    -> Zod input validation schemas
  @types/        -> Centralized TypeScript types

prisma/
  schema.prisma

---

## 4. Layer Responsibilities (STRICT)

- Routes:
  - Only define endpoints
  - No business logic

- Controllers:
  - Parse request
  - Call services
  - Return response
  - No database access

- Services:
  - Contain all business logic
  - Only layer allowed to interact with Prisma
  - Must not depend on HTTP layer

---

## 5. Data Flow (MANDATORY)

Route → Controller → Service → Prisma

Never bypass layers.

---

## 6. Prisma Usage

- Prisma must ONLY be used inside services
- Never use Prisma in controllers or routes
- Always use generated Prisma types

---

## 7. TypeScript Rules

- `any` is strictly forbidden
- Use `unknown` or explicit interfaces
- All types must be in `src/@types/`
- Do not define types inside business logic files

---

## 8. Naming Conventions

- Files: Use kebab-case with a clear layer suffix (e.g., `user-controller.ts`, `post-service.ts`, `auth-routes.ts`, `data-helper.ts`).
- Types/Interfaces: PascalCase
- Functions/Variables: camelCase
- DB fields: snake_case (via Prisma schema)


---

## 9. Error Handling

- Services throw errors
- Controllers handle and format responses
- All API responses must follow:

{
  success: boolean,
  data?: unknown,
  error?: string
}

---

## 10. Validation

- Input validation must happen at controller level
- Services assume validated data

---

## 11. Git & Workflow

- All commits MUST follow Conventional Commits format:
  
  `<type>(<scope>): <short description>`

- Always update `faker.js/CHANGELOG.md` immediately after you commit to track changes.

---

### 1. Types

- feat     → New feature
- fix      → Bug fix
- refactor → Code change without behavior change
- test     → Adding or updating tests
- docs     → Documentation changes
- chore    → Maintenance (configs, deps)

---

### 2. Scope (MANDATORY)

Scope must reflect the layer or module:

- prisma
- api
- controllers
- services

Examples:
- feat(auth): add login endpoint
- fix(users): handle null email edge case
- refactor(services): extract payment logic

---

### 3. Description Rules

- Max 72 characters
- Use present tense
- No vague words like "stuff", "changes", "update"

---

### 4. Good Examples

feat(users): add user registration service  
fix(auth): handle invalid JWT token error  
refactor(orders): move pricing logic to service  
test(users): add unit tests for user service  

---

### 5. Bad Examples (DO NOT DO)

fix: bug  
feat: changes  
update code  
misc fixes  

---

### 6. Commit Size

- Keep commits small and focused (<50 LOC preferred)
- One logical change per commit


---

## 12. Prisma Workflow

- Run `bunx prisma generate` after schema changes

---

## 13. Testing Philosophy

- Unit tests: Use mocks (no DB)
- Integration tests: Use real DB + API
- Do not mix both approaches

---

## 14. Makefile & Commands

- Create a `Makefile` in the root directory to manage and execute all project commands.
- Use Makefile commands for all terminal operations.
- Always add any new command (i.e., any command not already present in the `Makefile`) to the `Makefile` before execution.

---

## 15. Architectural Rules
- **Separation of Concerns**: Never put database logic in Routes. Routes call Services.
- **Helper Isolation**: Services should not contain generic logic (e.g., date formatting, string parsing). Move these to `src/helpers/`.
- **Database Access**: Use the singleton Prisma client located at `src/lib/prisma.ts`.
- **Type Safety**: Prefer explicit types for function returns. Use `Prisma.ResourceCreateInput` for service arguments.

---

## 16. Environment Variables
- **Storage**: Store environment variables in `.env`.
- **Syncing Template**: You must update `_env.local` when you add or remove any variable in `.env`.
- **Access**: Access environment variables only through the centralized config located at `src/lib/config.ts`. Direct use of `process.env` outside of `src/lib/config.ts` is strictly prohibited.

