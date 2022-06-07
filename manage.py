#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
import pymongo
from pymongo import MongoClient

"""
# database
db = conn.database
  
# Created or Switched to collection names: my_gfg_collection
collection = db.my_gfg_collection
"""
try:
    DB_URI = "mongodb+srv://MangoDBTester:0TeEaRuCdH5yqRpJ@dogbookdb.w3p76.mongodb.net/TaskManagerWithPython?retryWrites=true&w=majority"
    cluster = MongoClient(DB_URI)
    db = cluster["TaskManagerWithPython"]
    collection = db["tasks"]
    print("Connected successfully!!!")
except Exception as e:
    logging.critical(e, exc_info=True)
    print("Could not connect to MongoDB")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskManagerWithDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

