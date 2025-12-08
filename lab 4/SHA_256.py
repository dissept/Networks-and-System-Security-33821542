import os
import hashlib
import csv
from datetime import datetime

# 1. Path to your folder
FOLDER = "files_to_hash"


# 2. Function to hash a file
def hash_file(path: str) -> str:
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()

# 3. Create baseline CSV
with open("baseline.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "sha256", "timestamp"])

    for filename in os.listdir(FOLDER):
        path = os.path.join(FOLDER, filename)

        if os.path.isfile(path):
            file_hash = hash_file(path)
            timestamp = datetime.now().isoformat()
            writer.writerow([filename, file_hash, timestamp])

print("Baseline created in baseline.csv ")
