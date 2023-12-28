import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { FileModule } from './file/file.module';
import { InvoicesModule } from './invoices/invoices.module';

@Module({
  controllers: [AppController],
  imports: [FileModule, InvoicesModule],
  providers: [AppService],
})
export class AppModule {}
