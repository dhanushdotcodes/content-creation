# Tired of Empty Databases? Meet Faker.js

Whenever you start an application expecting it to have some dummy data, seeing a blank screen is a letdown.

It’s a frustrating position to be in—especially when it happens at the wrong time:
- Demonstrating your application to a friend or peer.
- Presenting during a high-stakes interview.
- Testing APIs or features while your manager is observing.
- Reviewing UI flows that depend on existing data.


While searching the web to solve this recurring headache, I was introduced to a gem called **faker.js**.

As simple as it is powerful, `faker.js` is the ultimate tool for mocking your data in local development.

---

## The Solution: Seamless Data Mocking

With `faker.js`, you don't have to spend hours manually entering dummy values in your database.

Simply install the package, write a seeding script, run it, and you'll find rich, realistic data stored in your database—just like magic!

Let's see exactly how to set it up.

### 1. Install the Package

You can install `@faker-js/faker` as a dependency in your project:

```bash
bun add @faker-js/faker
```

_(Or use your package manager of choice, like `npm install @faker-js/faker` or `pnpm add @faker-js/faker`)._

### 2. Write Your Seeding Script

Here is an example script that uses `faker.js` to clear and repopulate a job applications table. We generate 15 unique and realistic applications including companies, positions, salaries, locations, and random statuses.

```typescript
import { faker } from "@faker-js/faker";
import prisma from "./prisma";

async function main() {
  console.log("Clearing existing job applications...");
  await prisma.jobApplication.deleteMany({});

  console.log("Generating fake job applications using faker.js...");

  const statuses = ["APPLIED", "INTERVIEWING", "OFFERED", "REJECTED"] as const;

  const applications = Array.from({ length: 15 }).map(() => ({
    company: faker.company.name(),
    position: faker.person.jobTitle(),
    salary: `$${faker.number.int({ min: 60, max: 180 })}k`,
    location: `${faker.location.city()}, ${faker.location.state({ abbreviated: true })}`,
    status: faker.helpers.arrayElement(statuses),
    jobUrl: faker.internet.url(),
    notes: faker.lorem.paragraph(),
  }));

  console.log(
    `Inserting ${applications.length} fake applications into database...`,
  );
  await prisma.jobApplication.createMany({
    data: applications,
  });

  console.log("Seeding completed successfully!");
}

main()
  .catch((e) => {
    console.error("Error during seeding:", e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
```

### 3. Run Your Script

Run the seeding script via Bun.js:

```bash
bun run src/lib/seed.ts
```

---

### 💡 Pro Tip: Auto-Seeding with Docker Compose

If you're using Docker Compose, you can take this automation one step further. You can configure your local environment so that a single command spins up both your database and your app, runs migrations/schemas, and automatically seeds the database with `faker.js` on startup.

Here is how you can set it up in your `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:alpine
    # ... postgres config

  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - postgres
    command:
      ["sh", "-c", "bunx prisma db push && bun run db:seed && bun run dev"]
```

By chaining the Prisma push, seeding script (`db:seed`), and the app startup command (`dev`), your local environment will always spin up with fresh, rich test data.

For a complete working example, you can check out the source code of this setup: [docker-compose.yml on GitHub](https://github.com/dhanushdotcodes/content-creation/faker.js/docker-compose.yml).

Tadah! Just like that, your database is fully populated with rich, dynamic test data. No more blank screens, no more awkward manual data entry in front of friends, interviewers, or managers.

Let `faker.js` do the heavy lifting so you can focus on building what matters.

---

## 🛠️ Getting Started Locally

If you cloned this repository and want to test it out:

### 1. Installation
Install the project dependencies via Bun:
```bash
bun install
```

### 2. Environment Setup
Create a `.env` file in the root directory:
```env
DATABASE_URL="postgresql://postgres:postgrespassword@localhost:5432/faker_db?schema=public"
PORT=3000
```

### 3. Initialize Prisma & Seed Data
Push the schema to your PostgreSQL instance and populate the database with faker data:
```bash
bunx prisma db push
bun run db:seed
```

### 4. Run the Development Server
```bash
bun run dev
```

---

### 📂 Explore the Code

The complete source code for this setup is available in the repository. Feel free to explore, clone, and build upon it:

🔗 **GitHub Repository:** [dhanushdotcodes/content-creation](https://github.com/dhanushdotcodes/content-creation)

---


### 📬 Drop a follow if you found this useful!

- 🐦 **X (formerly Twitter):** [@dhanushdotcodes](https://x.com/dhanushdotcodes)
- 💼 **LinkedIn:** [Dhanush D]()
- 💻 **GitHub:** [dhanushdotcodes](https://github.com/dhanushdotcodes)