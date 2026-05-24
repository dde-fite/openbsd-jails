import os
import subprocess
import sys

BASE_URL = "https://cdn.openbsd.org/pub/OpenBSD/7.9/amd64/base79.tgz"
DEFAULT_DESTINATION = os.path.join(os.getcwd(), "base")

# Choosing destination
try:
    destination = input(f"Enter destination folder [{DEFAULT_DESTINATION}]: ").strip()
except EOFError:
    destination = ""

if not destination:
    destination = DEFAULT_DESTINATION

print(f"\nCreating directory (if not exist): {destination} ...")
os.makedirs(destination, exist_ok=True)

tmp_file = "/tmp/base.tgz"

print(f"\nDownloading base image from mirror: {BASE_URL} ...")
subprocess.run(
        ["wget", "-O", tmp_file, BASE_URL],
    check=True
)

print("\nDecompressing image...")
subprocess.run(
    ["tar", "-C", destination, "-xzf", tmp_file],
    check=True
)

os.remove(tmp_file)

print("\nDone ✔")
