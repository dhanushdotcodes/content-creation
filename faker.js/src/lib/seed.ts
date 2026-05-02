import { faker } from '@faker-js/faker';
import prisma from './prisma';

async function main() {
  console.log('Clearing existing job applications...');
  await prisma.jobApplication.deleteMany({});

  console.log('Generating fake job applications using faker.js...');

  const statuses = ['APPLIED', 'INTERVIEWING', 'OFFERED', 'REJECTED'] as const;

  const applications = Array.from({ length: 15 }).map(() => ({
    company: faker.company.name(),
    position: faker.person.jobTitle(),
    salary: `$${faker.number.int({ min: 60, max: 180 })}k`,
    location: `${faker.location.city()}, ${faker.location.state({ abbreviated: true })}`,
    status: faker.helpers.arrayElement(statuses),
    jobUrl: faker.internet.url(),
    notes: faker.lorem.paragraph(),
  }));

  console.log(`Inserting ${applications.length} fake applications into database...`);
  await prisma.jobApplication.createMany({
    data: applications,
  });

  console.log('Seeding completed successfully!');

  console.log('Fetching and listing all generated fake data from the database:');
  const allApplications = await prisma.jobApplication.findMany();
  console.log(JSON.stringify(allApplications, null, 2));
}

main()
  .catch((e) => {
    console.error('Error during seeding:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
