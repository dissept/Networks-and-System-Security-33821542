import os
import csv
import hashlib

FOLDER = "files_to_monitor"

# Load baseline
baseline = {}
with open("baseline.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        baseline[row["filename"]] = row["sha256"]

# Hash current files
def hash_file(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()

current = {}
for filename in os.listdir(FOLDER):
    path = os.path.join(FOLDER, filename)
    if os.path.isfile(path):
        current[filename] = hash_file(path)

# Detect modifications, deletions, new files
print("\n--- Integrity Check Report ---\n")

for filename, old_hash in baseline.items():
    if filename not in current:
        print(f"[DELETED] {filename}")
    elif current[filename] != old_hash:
        print(f"[MODIFIED] {filename}")

for filename in current:
    if filename not in baseline:
        print(f"[NEW FILE] {filename}")

print("\nDone.")
