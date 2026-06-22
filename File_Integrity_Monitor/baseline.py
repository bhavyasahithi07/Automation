import os
import json
import datetime
from hashing import scanning_directory
BASELINE_FILE="baseline.json"

def saving_baseline(directory):
    print(f"Creating baseline snapshot\n")
    hashes=scanning_directory(directory)
    baseline={
        "directory": os.path.abspath(directory),
        "created_at": datetime.datetime.now().isoformat(), 
        "files": hashes
    }

    with open(BASELINE_FILE, 'w') as f:
        json.dump(baseline,f,indent=4)
    print(f"Baseline saved-'{BASELINE_FILE}'")
    print(f"Total files tracked: {len(hashes)}")

def loading_baseline():
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found, create in option 1")
        return None
    
    with open(BASELINE_FILE, "r") as f:
        baseline=json.load(f)
    print("Baseline loaded")
    return baseline

def viewing_baseline():
    baseline=loading_baseline()
    if not baseline:
        return
    
    print(f"\n directory : {baseline['directory']}\n")
    print(f"Created : {baseline['created_at']}\n")
    print(f"Files : {len(baseline['files'])}\n")

    print("files currently tracked:")
    for path in baseline["files"]:
        print(f"    {path}")
        


    



