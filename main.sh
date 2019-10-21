#!/bin/bash

set +e

psql --dbname=$DB_NAME --username=$USERNAME --port=$PORT --host=$HOST -f backup.sql

python main.py

exit 0
