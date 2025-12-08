import os
import re

FOLDER = "files_to_monitor"

SIGNATURES = [
    r"eval\(",
    r"base64\.b64decode",
    r"socket\.connect",
    r"exec\(",
    r"import os"
]

compiled = [re.compile(sig) for sig in SIGNATURES]

for filename in os.listdir(FOLDER):
    path = os.path.join(FOLDER, filename)

    if not os.path.isfile(path):
        continue

    with open(path, "r", errors="ignore") as f:
        content = f.read()

    for sig in compiled:
        if sig.search(content):
            print(f"[SUSPICIOUS] Pattern '{sig.pattern}' found in {filename}")
