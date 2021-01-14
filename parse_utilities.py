def find_splits(line, delimiter=' '):
    try:
        split = tuple([x.strip() for x in line.split(delimiter) if x.strip()])
        return split
    except Exception as e:
        print(e)


def replace_forward_slashes(string):
    return string.replace('/', '\\')


def replace_single_backslash(string):
    return string.replace('\\', '\\')


# replace_forward_slashes('z:/myfolder/yours/his/')
# replace_single_backslash('c:\folder\folder\folder')
