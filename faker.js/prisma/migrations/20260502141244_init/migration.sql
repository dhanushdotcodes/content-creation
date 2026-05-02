-- CreateEnum
CREATE TYPE "ApplicationStatus" AS ENUM ('applied', 'interviewing', 'offered', 'rejected');

-- CreateTable
CREATE TABLE "job_applications" (
    "id" UUID NOT NULL,
    "company" VARCHAR NOT NULL,
    "position" VARCHAR NOT NULL,
    "salary" VARCHAR,
    "location" VARCHAR,
    "status" "ApplicationStatus" NOT NULL DEFAULT 'applied',
    "job_url" VARCHAR,
    "notes" TEXT,
    "created_at" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(6) NOT NULL,

    CONSTRAINT "job_applications_pkey" PRIMARY KEY ("id")
);
