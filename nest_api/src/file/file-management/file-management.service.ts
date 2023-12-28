import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../common/prisma/prisma.service';

@Injectable()
export class FileManagementService {
  constructor(private dbService: PrismaService) {}

  public async createFile(file: string) {
    await this.dbService.file.create({
      data: {
        path: file,
      },
    });
  }

  async updateFileStatus(param: { path: string; status: boolean }) {
    await this.dbService.file.update({
      // @ts-ignore
      where: { path: param.path },
      data: {
        status: param.status ? 'PROCESSED' : 'ERROR',
      },
    });
  }
}
