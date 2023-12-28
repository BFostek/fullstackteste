-- CreateEnum
CREATE TYPE "FileStatus" AS ENUM ('PROCESSING', 'PROCESSED', 'ERROR');

-- CreateTable
CREATE TABLE "File" (
    "_id" TEXT NOT NULL,
    "path" TEXT NOT NULL,
    "status" "FileStatus" NOT NULL DEFAULT 'PROCESSING',

    CONSTRAINT "File_pkey" PRIMARY KEY ("_id")
);
