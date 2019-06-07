import argparse
import shutil
import ntpath
import time
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Tool made to archive log file - (Stefano Crapanzano - s.crapanzano@gmail.com)")
    parser.add_argument('--log_path', help='Full path of the log to archive',
                        required=True)
    parser.add_argument('--log_extension', help='Extension of the log to archive',
                        required=True)
    parser.add_argument('--destination_directory', help='Directory where the log will be placed',
                        required=True)

    args = parser.parse_args()
    log_path = vars(args)['log_path']
    log_extension = vars(args)['log_extension']
    destination_directory = vars(args)['destination_directory']

    if not str(destination_directory).endswith("\\"):
        destination_directory += "\\"

    if not os.path.isdir(destination_directory):
        try:
            os.mkdir(destination_directory)
        except:
            print("An exception occurred while creating the destination folder " + destination_directory)
            sys.exit(0)

    if not os.path.isfile(log_path):
        print("File " + log_path + " not present")
        sys.exit(0)
    log_file_name = path_leaf(log_path)

    if not str(log_extension).startswith('.'):
        ".".join(log_extension)

    log_name = log_file_name.split(log_extension)

    timestamp = time.localtime()
    date_exec = str(timestamp.tm_year) + str(timestamp.tm_mon).zfill(2) + str(timestamp.tm_mday).zfill(2)

    log_name_with_date = str(date_exec) + "-" + str(log_name[0])

    shutil.move(log_path, destination_directory + log_name_with_date + log_extension)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


if __name__ == "__main__":
    main()
