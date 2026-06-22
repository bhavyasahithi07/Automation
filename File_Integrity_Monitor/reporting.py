import os
REPORT_FILE = "fim_report.txt"

def building_report_lines(results):
     lines = []
     lines.append("FILE INTEGRITY MONITOR-SCAN REPORT")
     lines.append(f"Scanned directory : {os.path.abspath(results['directory'])}")
     lines.append(f"Baseline created  : {results['baseline_time']}")
     lines.append(f"Scan timestamp    : {results['check_time']}")
     lines.append(f"Files in baseline : {results['baseline_count']}")
     lines.append(f"Files now         : {results['current_count']}")

     lines.append(f"[NEW FILES]-{len(results['new_files'])} found")
     