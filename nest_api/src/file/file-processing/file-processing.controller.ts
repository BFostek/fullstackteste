import { Controller } from '@nestjs/common';
import {
  Ctx,
  MessagePattern,
  Payload,
  RedisContext,
} from '@nestjs/microservices';
import { FileManagementService } from '../file-management/file-management.service';

@Controller('file-processing')
export class FileProcessingController {
  constructor(private fileManagementService: FileManagementService) {}

  @MessagePattern('file-processed')
  async getFileProcessed(@Payload() data: any, @Ctx() context: RedisContext) {
    await this.fileManagementService.updateFileStatus({
      path: data.file,
      status: data.success,
    });
  }
}
