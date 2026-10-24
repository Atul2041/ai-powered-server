import os
import subprocess
import sys

# List of required packages
packages = [
    "parler-tts",
    "piper-tts",
    "neon-memory",
    # Specific libraries for Maya OS logic
    # "library1", "library2"
]

def install_packages():
    print("Installing required packages...")
    for package in packages:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("All packages installed.")

def run_integration():
    print("Starting integration script...")
    # Assuming the integration script is named maya_tts_integration.py
    os.system("python maya_tts_integration.py")

if __name__ == "__main__":
    install_packages()
    run_integration()
