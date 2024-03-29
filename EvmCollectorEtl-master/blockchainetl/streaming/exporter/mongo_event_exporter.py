import logging
from pymongo import UpdateOne
import time
from pymongo import MongoClient
from configs.config import MongoDBConfig

logger = logging.getLogger("MongodbStreamingExporter")


class MongodbEventExporter(object):
    """Manages connection to  database and makes async queries
    """

    def __init__(self, connection_url, collector_id, db_prefix=""):
        self._conn = None
        # url = f"mongodb://{MongoDBConfig.NAME}:{MongoDBConfig.PASSWORD}@{MongoDBConfig.HOST}:{MongoDBConfig.PORT}"
        url = connection_url
        self.mongo = MongoClient(url)
        if db_prefix:
            mongo_db_str = db_prefix + "_" + MongoDBConfig.DATABASE
        else:
            mongo_db_str = MongoDBConfig.DATABASE
        self.mongo_db = self.mongo[mongo_db_str]
        self.mongo_collectors = self.mongo_db[MongoDBConfig.COLLECTORS]
        self.event = self.mongo_db[MongoDBConfig.LENDING_EVENTS]
        for collector in MongoDBConfig.EVENTS:
            if collector in collector_id:
                self.event = self.mongo_db[collector]

        self.collector_id = collector_id

    def get_collector(self, collector_id):
        key = {"id": collector_id}
        collector = self.mongo_collectors.find_one(key)
        if not collector:
            collector = {
                "_id": collector_id,
                "id": collector_id
            }
            self.update_collector(collector)
        return collector

    def get_event_items(self, filter):
        return list(self.event.find(filter))

    def update_collector(self, collector):
        key = {'id': collector['id']}
        data = {"$set": collector}

        self.mongo_collectors.update_one(key, data, upsert=True)

    def update_latest_updated_at(self, collector_id, latest_updated_at):
        key = {'_id': collector_id}
        update = {"$set": {
            "last_updated_at_block_number": latest_updated_at
        }}
        self.mongo_collectors.update_one(key, update)

    def open(self):
        pass

    def export_items(self, items):
        self.export_events(items)

    def export_events(self, operations_data):
        if not operations_data:
            logger.debug("Error: Don't have any data to write")
            return
        start = time.time()
        bulk_operations = [UpdateOne({'_id': data['_id'], 'block_number': data['block_number']},
                                     {"$set": data}, upsert=True) for data in operations_data]
        logger.info("Updating into events ........")
        try:
            self.event.bulk_write(bulk_operations)
        except Exception as bwe:
            logger.error(f"Error: {bwe}")
        end = time.time()
        logger.info(f"Success write events to database take {end - start}s")

    def close(self):
        pass
