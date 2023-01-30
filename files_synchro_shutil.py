import shutil
import os
import time
import logging

src_folder = "C:\Python_projects\Veeam\Source"
dest_folder = "C:\Python_projects\Veeam\Replika"

def sync_f (src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(d):
            if os.path.exists(d):
                shutil.rmtree(d)
                logging.info(f"Deleting folder: {d}")
                print(f"Deleting folder: {d}")
            shutil.copytree(s, d)
            logging.info(f"Copied directory {s} to {d}")
            print(f"Copied directory {s} to {d}")
        else:
            if os.path.exists(d):
                os.remove(d)
                logging.info(f"Deleting file: {d}")
                print(f"Deleting file: {d}")
            shutil.copy2(s, d)
            logging.info(f"Copied file {s} to {d}")
            print(f"Copied file {s} to {d}")

if __name__ == "__main__":
    logging.basicConfig(filename="C:\Python_projects\Veeam\log.txt", level=logging.INFO)
    while True:
        sync_f(src_folder, dest_folder)
        time.sleep(60)

