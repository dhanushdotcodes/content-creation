import prisma from "../lib/prisma";
import type { Prisma, ApplicationStatus } from "@prisma/client";

export async function createApplication(data: {
  company: string;
  position: string;
  salary?: string | null;
  location?: string | null;
  status?: ApplicationStatus;
  jobUrl?: string | null;
  notes?: string | null;
}) {
  return await prisma.jobApplication.create({
    data: {
      company: data.company,
      position: data.position,
      salary: data.salary,
      location: data.location,
      status: data.status,
      jobUrl: data.jobUrl,
      notes: data.notes,
    },
  });
}

export async function listApplications() {
  return await prisma.jobApplication.findMany({
    orderBy: {
      createdAt: "desc",
    },
  });
}

export async function getApplicationById(id: string) {
  return await prisma.jobApplication.findUnique({
    where: { id },
  });
}

export async function updateApplication(
  id: string,
  data: {
    company?: string;
    position?: string;
    salary?: string | null;
    location?: string | null;
    status?: ApplicationStatus;
    jobUrl?: string | null;
    notes?: string | null;
  }
) {
  // First ensure it exists
  const existing = await prisma.jobApplication.findUnique({
    where: { id },
  });
  if (!existing) {
    throw new Error("NOT_FOUND");
  }

  return await prisma.jobApplication.update({
    where: { id },
    data: {
      company: data.company,
      position: data.position,
      salary: data.salary,
      location: data.location,
      status: data.status,
      jobUrl: data.jobUrl,
      notes: data.notes,
    },
  });
}

export async function deleteApplication(id: string) {
  // First ensure it exists
  const existing = await prisma.jobApplication.findUnique({
    where: { id },
  });
  if (!existing) {
    throw new Error("NOT_FOUND");
  }

  return await prisma.jobApplication.delete({
    where: { id },
  });
}
