import { Injectable } from '@nestjs/common';
import { PrismaService } from '../common/prisma/prisma.service';

@Injectable()
export class InvoicesService {
  constructor(private dbService: PrismaService) {}
  public saveInvoice(path) {}
}
