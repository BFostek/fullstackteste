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


def convert_to_json(file):
    return json.dumps(file, cls=ComplexEncoder)


def send_file_processed(redis_client, result):
    logging.info(f"Sending file")
    logging.info(f"Result: {convert_to_json(result)}")
    redis_client.publish('file-processed', convert_to_json(result))


def process_file(file_path):
    try:
        parser = ElectricityBillParser(pdf_to_array(file_path))
        result = parser.parse()

        return {
            "success": True,
            "file": file_path,
            "content": {
                "type": "invoices",
                "result": result
            }
        }

    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        return {
            "success": False,
            "file": file_path,
            "content": None,
            "reason": f'File not found: {file_path}'
        }
    except Exception as e:
        logging.error(f'Error processing file: {file_path}, {e}')
        return {
            "success": False,
            "file": file_path,
            "content": None,
            "reason": e
        }


def connect_redis():
    redis_client = redis.Redis(host='redis', port=6379)
    for _ in range(3):  # try three times
        try:
            redis_client.ping()
            break
        except redis.exceptions.ConnectionError:
            logging.error('Redis client could not connect.')
            continue
    logging.info(f'Redis client connected: {redis_client}')
    return redis_client


def subscribe_to_channel(redis_client, channel_name):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel_name)
    return pubsub


def main():
    redis_client = connect_redis()
    pubsub = subscribe_to_channel(redis_client, 'process-file')
    for event in pubsub.listen():
        if event['type'] == 'message':
            data = json.loads(event['data'].decode('utf-8'))
            file_name = data['data']['fileName']
            logging.info(f'Received file name from process_file event: {file_name}')
            processed_file = process_file(file_name)
            send_file_processed(redis_client, processed_file)


if __name__ == "__main__":
    main()
