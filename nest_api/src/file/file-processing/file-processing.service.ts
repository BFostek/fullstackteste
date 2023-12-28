import { Inject, Injectable } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';

@Injectable()
export class FileProcessingService {
  constructor(@Inject('FILE_PROCESSING_SERVICE') private client: ClientProxy) {}
  public async processFile(fileName: string): Promise<boolean> {
    try {
      this.client.emit('process-file', { fileName });
      return true;
    } catch (error) {
      console.error(`Error processing file: ${fileName}`);
      console.error(error);
      return false;
    }
  }
}
