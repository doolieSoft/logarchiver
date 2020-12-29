import argparse
import shutil
import ntpath
import time
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Script used to archive log files - (Stefano Crapanzano - s.crapanzano@gmail.com)")
    parser.add_argument('--log_fullpath', help='Full path of file to archive',
                        required=True)
    parser.add_argument('--dest_dir', help='Directory where the archived log file will be moved',
                        required=True)

    args = parser.parse_args()
    log_fullpath = vars(args)['log_fullpath']
    dest_dir = vars(args)['dest_dir']

    if not os.path.isfile(log_fullpath):
        print(f"{log_fullpath} doesn't exist")
        sys.exit(-1)

    if not os.path.isdir(dest_dir):
        try:
            os.mkdir(dest_dir)
        except:
            print(f"An exception occurred while creating the destination folder {dest_dir}")
            sys.exit(-1)

    if not str(dest_dir).endswith(os.sep):
        dest_dir += os.sep

    log_filename = path_leaf(log_fullpath)
    log_filename_and_ext = os.path.splitext(log_filename)

    timestamp = time.localtime()
    date_exec = str(timestamp.tm_year) + str(timestamp.tm_mon).zfill(2) + str(timestamp.tm_mday).zfill(2)

    log_name_with_date = f"{date_exec}-{log_filename_and_ext[0]}"

    shutil.move(log_fullpath, os.path.join(dest_dir, log_name_with_date + log_filename_and_ext[1]))
    print(f"Log {log_filename} has been archived")
    sys.exit(0)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


if __name__ == "__main__":
    main()
