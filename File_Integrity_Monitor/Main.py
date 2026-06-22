import os
from baseline import saving_baseline,viewing_baseline
from checking  import running_check                         
from reporting import generate_report 

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def banner():
    print("        FILE INTEGRITY MONITOR")
    print("        Cybersecurity Automation Tool")
    print()

def get_directory():
    path = input("\nEnter the folder path to monitor\n").strip()
 
    if not os.path.isdir(path):
        print(f"\n'{path}' is not a valid directory.")
        return None
    return path

def main():
    clear()
    banner()
 
    while True:
        print("MENU")
        print("1. Create baseline snapshot")
        print("2. Check integrity (compare now)")
        print("3. View baseline info")
        print("4. Exit")
 
        choice = input("\nChoose an option [1-4]: ").strip()
 
        if choice=="1":
            directory=get_directory()
            if directory:
                saving_baseline(directory)           
 
    
        elif choice=="2":
            directory=get_directory()
            if directory:
                results=running_check(directory)    
                generate_report(results)          
 
        elif choice=="3":
            viewing_baseline()                 
 
        elif choice=="4":
            print("\nExiting,Stay secure!\n")
            break
 
        else:
            print("\nInvalid option.Please enter 1, 2, 3, or 4.")
 
        input("\nPress Enter to return to menu...")
        clear()
        banner()
 

if __name__ == "__main__":
    main()
 