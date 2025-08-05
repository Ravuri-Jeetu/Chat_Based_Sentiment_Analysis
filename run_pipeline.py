import subprocess
import sys
import os

def install_requirements():
    req_file = 'requirements.txt'
    if os.path.exists(req_file):
        print(f"Installing dependencies from {req_file}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
    else:
        print(f"{req_file} not found.")

def run_main():
    main_file = 'main.py'
    if os.path.exists(main_file):
        print(f"Running {main_file}...")
        subprocess.check_call([sys.executable, main_file])
    else:
        print(f"{main_file} not found.")

if __name__ == "__main__":
    install_requirements()
    run_main()