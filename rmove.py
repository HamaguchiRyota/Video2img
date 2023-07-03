import os
import hashlib
import shutil
from difflib import SequenceMatcher

def remove_duplicate_images(dir_path, threshold=0.4):
    file_list = os.listdir(dir_path)
    hashes = {}

    duplicate_dir = os.path.join(dir_path, 'remove')
    os.makedirs(duplicate_dir, exist_ok=True)

    for filename in file_list:
        filepath = os.path.join(dir_path, filename)

        with open(filepath, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()

        is_duplicate = False

        for hash_value, existing_path in hashes.items():
            similarity = SequenceMatcher(None, filehash, hash_value).ratio()
            if similarity >= threshold:
                is_duplicate = True
                duplicate_path = os.path.join(duplicate_dir, filename)
                shutil.move(filepath, duplicate_path)
                print("Remove:", filepath)
                break

        if not is_duplicate:
            hashes[filehash] = filepath

# 使用例
remove_duplicate_images('output/2023-07_03-15_37_53')

