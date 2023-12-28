import { Module } from '@nestjs/common';
import { FileProcessingService } from './file-processing.service';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { FileProcessingController } from './file-processing.controller';
import { FileManagementModule } from '../file-management/file-management.module';

@Module({
  imports: [
    FileManagementModule,
    ClientsModule.register([
      {
        name: 'FILE_PROCESSING_SERVICE',
        transport: Transport.REDIS,
        options: {
          host: 'redis',
          port: 6379,
        },
      },
    ]),
  ],
  providers: [FileProcessingService],
  exports: [FileProcessingService],
  controllers: [FileProcessingController],
})
export class FileProcessingModule {}
