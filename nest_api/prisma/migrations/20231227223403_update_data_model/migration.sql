-- CreateTable
CREATE TABLE "NfeInfos" (
    "id" SERIAL NOT NULL,
    "dueDate" TIMESTAMP(3) NOT NULL,
    "totalAmount" DOUBLE PRECISION NOT NULL,
    "nfCode" TEXT NOT NULL,
    "clientNumber" TEXT NOT NULL,
    "installationNumber" TEXT NOT NULL,
    "referenceMonth" TEXT NOT NULL,
    "issueDate" TIMESTAMP(3) NOT NULL,
    "accessKey" TEXT NOT NULL,

    CONSTRAINT "NfeInfos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ConsumptionHistory" (
    "id" SERIAL NOT NULL,
    "date" TIMESTAMP(3) NOT NULL,
    "totalConsumption" DOUBLE PRECISION NOT NULL,
    "meanConsumption" DOUBLE PRECISION NOT NULL,
    "totalDays" INTEGER NOT NULL,
    "nfeInfosId" INTEGER NOT NULL,

    CONSTRAINT "ConsumptionHistory_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "InvoiceItem" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "unity" TEXT NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "unitPrice" DOUBLE PRECISION NOT NULL,
    "value" DOUBLE PRECISION NOT NULL,
    "invoiceId" INTEGER NOT NULL,

    CONSTRAINT "InvoiceItem_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Invoice" (
    "id" SERIAL NOT NULL,
    "nfeInfosId" INTEGER NOT NULL,

    CONSTRAINT "Invoice_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "ConsumptionHistory" ADD CONSTRAINT "ConsumptionHistory_nfeInfosId_fkey" FOREIGN KEY ("nfeInfosId") REFERENCES "NfeInfos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "InvoiceItem" ADD CONSTRAINT "InvoiceItem_invoiceId_fkey" FOREIGN KEY ("invoiceId") REFERENCES "Invoice"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Invoice" ADD CONSTRAINT "Invoice_nfeInfosId_fkey" FOREIGN KEY ("nfeInfosId") REFERENCES "NfeInfos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
