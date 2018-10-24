import sys
import shutil
import zipfile
from pathlib import Path

def extract(zfile, path):
    f = zipfile.ZipFile(zfile, 'r')
    for file in f.namelist():
        f.extract(file, path)


def example():
    look_dir = Path(__file__).resolve().parents[0]
    extract(look_dir / 'look_example.zip', Path.cwd())

    print('\n生成 look example 成功')
