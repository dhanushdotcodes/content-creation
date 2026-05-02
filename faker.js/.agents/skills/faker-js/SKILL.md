# faker.js

## Description
This skill focuses on using the `faker.js` (or `@faker-js/faker`) library to generate realistic mock data for local testing, development, and seeding the database.

## When to Use
- When the user asks to mock/fake data for a new feature or testing purposes.
- When new schema tables or properties are added and need mock data generated.
- To populate the database with dummy/fake data upon environment startup or via script.

## Inputs
- `src/@types`: Types and interfaces describing the data models and schemas.
- `src/validation`: Validation schemas (e.g., Zod) that validate the shape and constraints of the data.
- `docs/DB_SCHEMA.md`: The documentation describing database tables, column definitions, and constraints.
- `docker-compose.yml`: Docker configuration to confirm services and healthcheck dependencies.
- `docs/API_SPEC.md`: API documentation to verify payload expectations.
- `.agents/skills/handle-db`: The skill handling database schemas and migrations.

## Steps
1. **Identify the Required Fields**: Review user instructions to identify the specific fields, tables, or models that need fake data generated.
2. **Read the Database Schema**: Consult both the database documentation (`docs/DB_SCHEMA.md`) and the Prisma schema (`prisma/schema.prisma`) to ensure all generated data aligns perfectly with the current schema constraints and relationships.
3. **Analyze Table Relationships**: Map out table dependencies to understand what depends on what and determine the correct generation order. Always generate parent/primary records first (e.g., users, organizations) before generating dependent child records that rely on foreign keys.
4. **Analyze Types and Validations**:
    - Consult the application types (`src/@types`) to match data model interfaces.
    - Check the validation schemas (`src/validation`) to ensure generated data satisfies length, regex, or value range constraints.
5. **Generate Fake Data**:
    - Use `@faker-js/faker` to generate the mock data.
    - Match specific field types to relevant Faker APIs (e.g., use `faker.person.fullName()` for names, `faker.internet.email()` for emails, etc.).
6. **Organize Source Files**:
    - Create a folder `src/lib/faker.js` if there is a lot of mock data or if multiple separate entities/files are required.
    - If the volume is small, a single file inside `src/lib` or a structured `src/lib/faker.js/` is acceptable.
7. **Integrate with Docker Healthcheck / Startup**:
    - Create or update the seeding script that runs automatically when `docker compose up` finishes and the database is completely healthy.

## Output
- A standalone or structured module within `src/lib/faker.js` exporting generator functions or seeding scripts.
- Scripts/commands used to run after the database is healthy.

## Example

### Generating Data for a Model

```typescript
import { faker } from '@faker-js/faker';

export function createFakeJobApplication() {
  return {
    id: faker.string.uuid(),
    company: faker.company.name(),
    position: faker.person.jobTitle(),
    salary: faker.finance.amount({ min: 50000, max: 150000, dec: 0 }),
    location: `${faker.location.city()}, ${faker.location.state()}`,
    status: faker.helpers.arrayElement(['APPLIED', 'INTERVIEWING', 'OFFERED', 'REJECTED']),
    jobUrl: faker.internet.url(),
    notes: faker.lorem.paragraph(),
    createdAt: faker.date.past(),
    updatedAt: faker.date.recent(),
  };
}
```

### Script Execution on Docker Startup

A wrapper or script that loops until the database is up and then runs the seeding command:

```bash
#!/bin/bash
# wait-for-db-and-seed.sh
echo "Waiting for database to be ready..."
until bunx prisma db push; do
  echo "Database is not ready yet. Sleeping..."
  sleep 2
done

echo "Database is ready! Running seed..."
bun run src/lib/faker.js/seed.ts
```