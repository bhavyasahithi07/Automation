import datetime
from hashing import scanning_directory
from baseline import loading_baseline

def running_check(directory):
    baseline=loading_baseline()
    if not baseline:
        return None
    
    baseline_files=baseline["files"]
    print("Scanning current directory state\n")
    current_hashes=scanning_directory(directory)
    check_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_files=[]
    modified_files=[]
    deleted_files=[]

    for path,current_hash in current_hashes.items():
        if path not in baseline_files:
            new_files.append(path)

        elif baseline_files[path]!= current_hash:
            modified_files.append(path)

    for path in baseline_files:
        if path not in current_hashes:
            deleted_files.append(path)

    total_issues=len(new_files)+len(modified_files)+len(deleted_files)

    return {
        "directory"     : directory,
        "baseline_time" : baseline["created_at"],
        "check_time"    : check_time,
        "baseline_count": len(baseline_files),
        "current_count" : len(current_hashes),
        "new_files"     : new_files,
        "modified_files": modified_files,
        "deleted_files" : deleted_files,
        "total_issues"  : total_issues,
    }

