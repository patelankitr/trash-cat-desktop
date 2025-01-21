import time

from alttester import AltDriver
import subprocess

# Full path to the application
app_path = r"D:\Projects\trash-cat-desktop\app\TrashCat.exe"

# Function to initialize AltTester driver
def init_alt_tester_driver(host="127.0.0.1", port=13000, app_name="__default__"):
    alt_tester_driver = AltDriver(host=host, port=port, app_name=app_name)
    return alt_tester_driver

def launch_app():
    try:
        subprocess.Popen([app_path])
        time.sleep(10)
    except FileNotFoundError:
        print("Application not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")