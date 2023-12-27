import json
import logging
import redis
import dataclasses

from parsers.ElectricityBillParser import ElectricityBillParser
from pdfFormatter import pdf_to_array

logging.basicConfig(level=logging.INFO)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        return super().default(obj)


def send_file_processed(redis_client, result):
    redis_client.publish('file-processed', json.dumps(result, cls=ComplexEncoder))


def process_file(file_path):
    try:
        parser = ElectricityBillParser(pdf_to_array(file_path))
        result = parser.parse()
        return result

    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
    except Exception as e:
        logging.error(f'Error processing file: {file_path}, {e}')


def main():
    directory = '/app/invoices/'
    redis_client = redis.Redis(host='redis', port=6379)
    logging.info(f'Redis client connected: {redis_client}')
    pubsub = redis_client.pubsub()
    pubsub.subscribe('process-file')

    for event in pubsub.listen():
        if event['type'] == 'message':
            data = json.loads(event['data'].decode('utf-8'))
            file_name = data['data']['fileName']
            logging.info(f'Received file name from process_file event: {file_name}')
            file = process_file(file_name)
            if not file:
                return
            send_file_processed(redis_client, file)


if __name__ == "__main__":
    main()
