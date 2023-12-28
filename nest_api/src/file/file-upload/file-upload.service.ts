import { Injectable } from '@nestjs/common';
import { existsSync, mkdirSync, writeFileSync } from 'fs';
import { createHash } from 'crypto';

@Injectable()
export class FileUploadService {
  public saveFile(file: Express.Multer.File): string | null {
    const directory = '/app/invoices';
    if (!existsSync(directory)) {
      mkdirSync(directory);
    }

    const hash = createHash('sha256');
    hash.update(file.buffer);

    const fileHash = hash.digest('hex');
    const filePath = `${directory}/${fileHash}.pdf`;

    if (existsSync(filePath)) {
      return null; //File already exists
    }
    writeFileSync(filePath, file.buffer);
    return filePath; //Returning the file path if successfully created
  }
}
