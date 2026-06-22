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
     if results["new_files"]:
        for f in results["new_files"]:
            lines.append(f"   + {f}")
     else:
        lines.append("None")
     lines.append("")

     lines.append(f"[MODIFIED FILES]-{len(results['modified_files'])} found")
     if results["modified_files"]:
        for f in results["modified_files"]:
            lines.append(f"   {f}")
     else:
        lines.append("None")
     lines.append("")

     lines.append(f"  [DELETED FILES]-{len(results['deleted_files'])} found")
     if results["deleted_files"]:
        for f in results["deleted_files"]:
            lines.append(f"   - {f}")
     else:
        lines.append("None")
     lines.append("")

     if results["total_issues"] > 0:
        status = f"{results['total_issues']} ISSUE(S) DETECTED — Review findings above."
     else:
        status = "No changes detected."
 
     lines.append(f"  SUMMARY: {status}")
     return lines

def generate_report(results):
    if not results:
        print("\n No results to report")
        return
 
    
    lines =building_report_lines(results)
 
    print()
    for line in lines:
        print(line)
 
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
 
    print(f"\n Report saved->'{REPORT_FILE}'")

    




     