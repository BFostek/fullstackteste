import { Module } from '@nestjs/common';
import { FileManagementService } from './file-management.service';
import { PrismaModule } from '../../common/prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  providers: [FileManagementService],
  exports: [FileManagementService],
})
export class FileManagementModule {}
