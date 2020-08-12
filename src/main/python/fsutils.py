import re
from pathlib import Path


numbers = re.compile(r'(\d+)')
image_extensions = ['jpg', 'JPG', 'jpeg', 'JPEG', 'tif', 'tiff','TIF', 'TIFF', 'png', 'PNG']

def numsort(value):
    """Use this as the key function to sort filenames
    numerically.
    """
    parts = numbers.split(str(value))
    parts[1::2] = map(int, parts[1::2])
    return parts

def list_files(directory, extension, sort=True):
    pat = f'*.{extension}'
    files = Path(directory).glob(pat)

    if sort:
        files = sorted(files, key=numsort)

    return files

def list_images(path):
    files = []
    for ext in image_extensions:
        pattern = f'*.{ext}'
        fs = Path(path).glob(pattern)
        files.extend(fs)
    files = sorted(files, key=numsort)
    return files