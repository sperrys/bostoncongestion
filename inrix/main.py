

#
#   main.py
#

import os, sys, argparse, shutil, gzip
import pandas as pd
import zipfile


import urllib
from smb.SMBHandler import SMBHandler

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

BASE_PATH = 'DATA_ARCHIVE_DONT_TOUCH/s19_uep294/boston/ctps/INRIX/unzipped'
LOCAL_PATH = '/Volumes/as_rsch_uds01\$/' + BASE_PATH
TMP_DIR = 'temp/'



conifg = None


def main():

   df = ingest_month()
   print(df)


def ingest_month():

    month_frame = pd.DataFrame()
    print("Ingesting Data for: {} \n".format(config.month))

    for i in range(0, 100):

        f = readfile(config.month, i)

        if f is not None:
            month_frame = month_frame.append(f)

        sys.exit()

    return month_frame



#
#   Return a file object from the remote smb server
#

def read_remote(path):

    opener = urllib.request.build_opener(SMBHandler)
    fh = opener.open('smb://sperry02:Winter2016@rstore1.uit.tufts.edu/as_rsch_uds01$/' + path)
    data = fh.read()
    fh.close()

    return data

#
#   Copy the remote file object to the local file object
#

def copy_remote(remote_p, l_f):

    data = read_remote(remote_p)
    l_f.write(data)
    print("Copied file: {} to: {}".format(remote_p, l_f.name))

    l_f.close()


#
#   Upload a local file object to the remote server
#

def upload(remote_path, l_f):

    director = urllib.request.build_opener(SMBHandler)

    # Upload by providing the `data` parameter with a file object
    fh = director.open('smb://sperry02:Winter2016@rstore1.uit.tufts.edu/as_rsch_uds01$/' + remote_path, data=l_f)
    fh.close()
    l_f.close()



def unzip(month, filename):

    id = os.path.join(month, filename)
    temp_p = os.path.join(TMP_DIR, id)

    try:

        remote_p = BASE_PATH + '/' + id
        l_f = open(temp_p, 'wb+')

        copy_remote(remote_p, l_f)

        unzipped = gzip.open(temp_p, 'rb+')

        temp_csv = open(temp_p + ".csv", 'wb+')

        data = unzipped.read()

        temp_csv.write(data)
        temp_csv.seek(0)

        upload(remote_p + ".csv", temp_csv)

        # Cleanup

        unzipped.close()
        temp_csv.close()

        os.remove(temp_p + ".csv")
        os.remove(temp_p)


    except Exception as e:
        print(e)
        print("Could Not Unzip File: {}".format(id))


def temp(filepath):
    pass




#
#   @param month :  unique month id (1-12)
#   @param id    :  unique file id  (0-99)
#

def readfile(month, id):

    month = str(month).rjust(2, '0') + "2015"
    filename = str(id).rjust(12, '0')

    if config.unzip:
        unzip(month, filename)

    # file_path = os.path.join(LOCAL_PATH, month, filename + '.csv')

    #if Path(file_path).is_file():
    #    return None #pd.read_csv(file_path)
    #else:
    #    print("No file found for: {}".format(file_path))
    #    return None







if __name__ == '__main__':

    global config

    parser = argparse.ArgumentParser(description='Process Inrix Data!')
    parser.add_argument('month', help='Name of month of looking at', type=str)
    parser.add_argument('--data',  default="data/", help='Path to directory of source Inrix data  ')
    parser.add_argument('--unzip', default=False, help='Whether to unzip the input files or not ')

    config = parser.parse_args()
    main ()