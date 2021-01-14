import zipfile
import os
import sys
from parse_utilities import *


parsed_directory_list = []
zip_file_list = []


def initiate_unzipper(source, destination):
    source = replace_forward_slashes(source)
    destination = replace_forward_slashes(destination)

    walk_directories(source, destination)


def walk_directories(source, destination):
    try:
        for root, dirs, files in os.walk(source):
            for file in files:
                zip_file_list.append(file)
                unzip(os.path.join(root, file), destination, file)

        print(zip_file_list)

    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)


def unzip(src, dest, filename):
    try:
        dest__path_with_date_center_route = dest + '\\' + find_date(src) + '\\' + 'US\\' + find_center(src) + '\\' + find_route(src) + '\\'
        dest_full_path = make_dirs(dest__path_with_date_center_route, filename)

        with zipfile.ZipFile(src, 'r') as zip_ref:
            zip_ref.extractall(dest_full_path)

    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)


def make_dirs(root, leaf):
    try:
        # remove .zip
        leaf = leaf[:-4]

        path = os.path.join(root, leaf)
        os.makedirs(path)

        return path
    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)


def find_date(src):
    try:
        splits = find_splits(src, '\\')
        return splits[1]

    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)


def find_center(src):
    try:
        splits = find_splits(src, '\\')
        return splits[3]

    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)


def find_route(src):
    try:
        splits = find_splits(src, '\\')
        return splits[4]

    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)


# source = 'Z:\\2021.01.09\\US\\ALANN\\11A'
# destination = 'C:\\Users\\tonyd\\Documents\\Work\\unzippedLogs'

# if __name__ == '__main__':
#     get_log_file_paths(source)
    # unzip(
    #     'C:\\Users\\tonyd\\Documents\\Work\\TimmLogs\\06Fzipped\\2020.12.17_09.54.42_US_NCWCH_06F_OnRoadOptimizationInputDirtied.zip',
    #     'C:\\Users\\tonyd\\Documents\\Work\\unzippedLogs')
