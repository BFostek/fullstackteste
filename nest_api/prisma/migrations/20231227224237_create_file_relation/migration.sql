/*
  Warnings:

  - Added the required column `fileId` to the `Invoice` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Invoice" ADD COLUMN     "fileId" TEXT NOT NULL;

-- AddForeignKey
ALTER TABLE "Invoice" ADD CONSTRAINT "Invoice_fileId_fkey" FOREIGN KEY ("fileId") REFERENCES "File"("_id") ON DELETE RESTRICT ON UPDATE CASCADE;
