import os
import time
import logging

src_folder = "C:\Python_projects\Veeam\Source"
dest_folder = "C:\Python_projects\Veeam\Replika"

def sync_f (src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isfile(s):
            if not os.path.exists(d):
                logging.info(f"Creating file: {d}")
                print(f"Creating file: {d}")
                open(d, "w").close()
            elif os.stat(s).st_mtime > os.stat(d).st_mtime:
                logging.info(f"Updating file: {d}")
                open(d, "w").close()
        elif os.path.isdir(s):
            if not os.path.exists(d):
                logging.info(f"Creating folder: {d}")
                print(f"Creating folder: {d}")
                os.makedirs(d)
            sync_f(s, d)


if __name__ == "__main__":
    logging.basicConfig(filename="C:\Python_projects\Veeam\log.txt", level=logging.INFO)
    while True:
        sync_f(src_folder, dest_folder)
        time.sleep(60)