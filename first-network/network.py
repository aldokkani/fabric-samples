import os
import subprocess
import re
import argparse
import json
import base64
from uuid import uuid4

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--card", help="Admin card's name")
parser.add_argument(
    "-t", "--trans", help="Submit a transaction. You should provide argument -f with the file path", action="store_true")
parser.add_argument("-f", "--file", help="File path")
parser.add_argument("--ping", help="Check network health", action="store_true")
parser.add_argument(
    "-l", "--list", help="List all files on the network", action="store_true")
parser.add_argument("-r", "--retrieve",
                    help="Download a file with file ID. You should provide argument -i with the file ID", action="store_true")
parser.add_argument("-i", "--id", help="File's ID to be downloaded")
args = parser.parse_args()

ADMIN = "org1admin@block-drive"
cmd = []
trans_data = {
    "$class": "org.example.blockdrive.FileUpload",
    "fileId": str(uuid4()),
    "fileData": None,
    "filename": None
}


def getFiles():
    cmd = ['composer', 'network', 'list', '-c',
           args.card if args.card else ADMIN]
    result = subprocess.run(cmd, stdout=subprocess.PIPE).stdout
    result = subprocess.run(["sed", "-r", r"s/\x1B\[[0-9;]*[JKmsu]//g"],
                            stdout=subprocess.PIPE, input=result).stdout.decode()
    fids = re.compile(r'(?:id\:\s+)(.+)').findall(result)
    owners = re.compile(r'(?:uploader\:.+#)(.+)').findall(result)
    data = re.compile(r'(?:data\:\s+)(.+?)(?=\s)', re.DOTALL).findall(result)
    filenames = re.compile(r'(?:filename\:\s+)(.+)').findall(result)
    return fids[1:], owners, data, filenames


if args.trans:
    with open(args.file, 'r') as f:
        trans_data['fileData'] = base64.b64encode(f.read().encode()).decode()
        trans_data['filename'] = args.file.split("/")[-1]

    cmd = ['composer', 'transaction', 'submit', '-c',
           args.card if args.card else ADMIN, '-d', json.dumps(trans_data)]
    print(subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode())

elif args.ping:
    cmd = ['composer', 'network', 'ping', '-c',
           args.card if args.card else ADMIN]
    print(subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode())

elif args.list:
    for fid, owner, _, name in zip(*getFiles()):
        print(f'File: {name} - Uploaded By: {owner} - ID: {fid}')

elif args.retrieve:
    download_dir = 'downloads/'
    fids, owners, data, filenames = getFiles()
    try:
        index = fids.index(args.id)
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        with open(download_dir + filenames[index], 'w') as f:
            f.write(base64.b64decode(data[index]).decode())
    except ValueError:
        print("Make sure you provide the right file ID..")
    else:
        print('File was downloaded at downloads/'+filenames[index])
