import { Module } from '@nestjs/common';
import { FileProcessingModule } from './file-processing/file-processing.module';
import { FileUploadModule } from './file-upload/file-upload.module';
import { FileManagementModule } from './file-management/file-management.module';

@Module({
  imports: [FileProcessingModule, FileUploadModule, FileManagementModule],
})
export class FileModule {}
