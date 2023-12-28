import {
  Controller,
  HttpStatus,
  ParseFilePipeBuilder,
  Post,
  Res,
  UploadedFile,
  UseInterceptors,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { Response } from 'express';
import { FileUploadService } from './file-upload.service';
import { FileProcessingService } from '../file-processing/file-processing.service';
import { FileManagementService } from '../file-management/file-management.service';

@Controller('file-upload')
export class FileUploadController {
  constructor(
    private fileService: FileUploadService,
    private fileProcessingService: FileProcessingService,
    private fileManagementService: FileManagementService,
  ) {}

  @Post('')
  @UseInterceptors(FileInterceptor('file'))
  async uploadFile(
    @UploadedFile(
      new ParseFilePipeBuilder()
        .addFileTypeValidator({ fileType: '.pdf' })
        .addMaxSizeValidator({ maxSize: 60000 })
        .build(),
    )
    file: Express.Multer.File,
    @Res() res: Response,
  ) {
    const fileName = await this.saveAndValidateFile(file, res);

    if (!fileName) {
      return;
    }

    const success = await this.processAndCreateFile(fileName, res);

    if (!success) {
      return;
    }

    return res
      .status(HttpStatus.OK)
      .json({ message: 'File uploaded successfully' });
  }

  private async saveAndValidateFile(
    file: Express.Multer.File,
    res: Response,
  ): Promise<string | undefined> {
    const filePath = this.fileService.saveFile(file);
    if (!filePath) {
      res.status(HttpStatus.CONFLICT).json({ message: 'File already exists' });
      return undefined;
    }

    return filePath;
  }

  private async processAndCreateFile(
    filePath: string,
    res: Response,
  ): Promise<boolean> {
    const processSuccess =
      await this.fileProcessingService.processFile(filePath);
    await this.fileManagementService.createFile(filePath);
    if (!processSuccess) {
      res
        .status(HttpStatus.INTERNAL_SERVER_ERROR)
        .json({ message: 'Error while processing file' });
      return false;
    }

    return true;
  }
}
