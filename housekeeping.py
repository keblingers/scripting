from datetime import datetime
import os
import argparse
from pathlib import Path
import shutil

def get_dir():
    parser = argparse.ArgumentParser(prog="housekeeping directory/files",description="python script for housekeeping directories and files base on datetime")
    parser.add_argument('-d','--directory',required=True,help="path that will be delete")
    args = vars(parser.parse_args())
    housekeeping_dir(args['directory'])


def housekeeping_dir(folder_path, retention_days=7):
    now = datetime.now()
    for x in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, x)
        if os.path.isdir(dir_path):
            dir_creatime_time = datetime.fromtimestamp(os.path.getctime(dir_path))
            #print(dir_creatime_time)
            age = now - dir_creatime_time
            #print(age)
            if age.days > retention_days:
                shutil.rmtree(dir_path)
                #print(dir_path,age.days)


if __name__ == '__main__':
    get_dir()
