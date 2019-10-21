from datetime import datetime
import json
import os

from dotenv import find_dotenv, load_dotenv
import requests


load_dotenv(find_dotenv())

month_dict = {
    "1": "january",
    "2": "february",
    "3": "march",
    "4": "april",
    "5": "may",
    "6": "june",
    "7": "july",
    "8": "august",
    "9": "september",
    "10": "october",
    "11": "november",
    "12": "december",
}

headers = {
    "Authorization": os.getenv("ACCESS_TOKEN"),
    "Content-Type": "multipart/related"
}

now = datetime.now()

if now.month == 1:  # new year, previous month should be december
    month = month_dict["12"]
    year = now.year - 1
else:
    month = month_dict[str(now.month - 1)]
    year = now.year

filename = f"test_backup_{month}_{year}.csv"
parameters = {"name": filename, "parents": [os.getenv("FOLDER_ID")]}
files = {
    "data": (
        "metadata",
        json.dumps(parameters),
        "application/json; charset=UTF-8",
    ),  # noqa: E501
    "file": open("./test_backup.csv", "rb"),
}

r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files,
)
print(r.text)

# Reference: https://gist.github.com/tanaikech/8cdfd23807372657dc63d81e25e35153
