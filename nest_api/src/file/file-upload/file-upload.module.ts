import { Module } from '@nestjs/common';
import { FileUploadService } from './file-upload.service';
import { FileUploadController } from './file-upload.controller';
import { FileProcessingModule } from '../file-processing/file-processing.module';
import { FileManagementModule } from '../file-management/file-management.module';

@Module({
  imports: [FileProcessingModule, FileManagementModule],
  providers: [FileUploadService],
  controllers: [FileUploadController],
})
export class FileUploadModule {}
