

#
#   main.py
#

import os
import pandas as pd
import zipfile

import argparse

from pathlib import Path

MONTHS = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
]

DATA_PATH = 'data/'

conifg = None


def main():

   df = ingest_month()
   print(df)


def ingest_month():

    month_frame = pd.DataFrame()
    print("Ingesting Data for: {} \n".format(config.month))

    for i in range(0, 100):

        f = readfile(i)
        if f is not None:
           month_frame = month_frame.append(f)

    return month_frame


def unzip(filename):

    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(DATA_PATH)


def readfile(id):

    filename = str(id).rjust(12, '0') + "-1"
    file_path = os.path.join(DATA_PATH, filename)

    if config.unzip:
        unzip(filename)

    if Path(file_path).is_file():
        return pd.read_csv(file_path)
    else:
        print("No file found for: {}".format(file_path))
        return None






if __name__ == '__main__':

    global config

    parser = argparse.ArgumentParser(description='Process Inrix Data!')
    parser.add_argument('month', help='Name of month of looking at')
    parser.add_argument('--data',  default="data/" , help='Path to directory of source Inrix data  ')
    parser.add_argument('--unzip', default=False, help='Whether to unzip the input files or not ')

    config = parser.parse_args()
    main ()