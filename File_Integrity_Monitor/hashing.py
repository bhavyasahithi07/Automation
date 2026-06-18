import os
import hashlib

def hashing_file(filepath):
    sha256=hashlib.sha256()

    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (IOError,PermissionError) as e:
        print(f"couldnt read this file- '{filepath}':{e}")
        return None
    
def scanning_directory(directory):
    file_hashes={}
    print(f"Scanning- {os.path.abspath(directory)}\n")
    for root,_,files in os.walk(directory):
        for filename in files:
            full_path=os.path.join(root,filename)
            rel_path=os.path.relpath(full_path,directory)
            file_hash=hashing_file(full_path)

            if file_hash:
                file_hashes[rel_path]=file_hash
                print(f"hashed- {rel_path}")
    return file_hashes
