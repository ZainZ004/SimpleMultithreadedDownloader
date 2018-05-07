# -*- encoding: utf-8 -*-
# Author: Epix
import json
import os

import sys
import zipfile
from multiprocessing.dummy import Pool

import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from urllib3 import Retry

BASE_DOWNLOAD_URL = "https://minecraft.curseforge.com/projects/{}/files/{}/download"
pack_name = ''

THREAD_NUMBER = 100

s = requests.Session()
retries = Retry(total=5, status_forcelist=[500, 502, 503, 504])
s.mount('https://', HTTPAdapter(max_retries=retries, pool_connections=THREAD_NUMBER, pool_maxsize=THREAD_NUMBER))


def download_pack(file_path):
    global pack_name
    pack_name = os.path.splitext(os.path.basename(file_path))[0]
    os.makedirs(pack_name, exist_ok=True)
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        zip_file.extractall(pack_name)
    manifest = json.load(open(os.path.join(pack_name, 'manifest.json'), 'r'))
    mod_files = manifest['files']

    pool = Pool(THREAD_NUMBER)
    results = []
    for result in tqdm(pool.imap_unordered(download_mod, mod_files), total=len(mod_files), ascii=True):
        results.append(result)
    [print(result) for result in results if result]
    print("mc version: {}".format(manifest['minecraft']['version']))
    print("require: {}".format(','.join([i['id'] for i in manifest['minecraft']['modLoaders']])))
    input("press enter to exit...")
    pass


def download_mod(mod_file: dict):
    url = BASE_DOWNLOAD_URL.format(mod_file['projectID'], mod_file['fileID'])
    r = s.get(url, timeout=30)
    if r.status_code == 200:
        filename = os.path.basename(r.url)
        with open(os.path.join(pack_name, 'overrides', 'mods', filename), 'wb') as out:
            out.write(r.content)
    else:
        return 'download failed {}'.format(url)


def main():
    file_path = r"C:\Users\Epix\Downloads\allthemods+3+v.5.8.zip"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    download_pack(file_path)


if __name__ == '__main__':
    main()
