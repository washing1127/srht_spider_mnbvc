import os
import json
import subprocess
import traceback

with open("repo_list.jsonl", "r", encoding="utf-8")as r:
    data = r.readlines()

err_count = 0

for line in data:
    try:
        dic = json.loads(line.strip())
        clone_url = dic["git"].replace("//", "/").replace(":/", "://")
        repo_name = dic["name"]
        clone_path = os.path.join("output", repo_name)
        os.makedirs(os.path.dirname(clone_path), exist_ok=True)
        subprocess.run(['git', 'clone', clone_url, clone_path])
    except: 
        traceback.print_exc()
        err_count += 1
        if err_count >= 5:
            raise OSError("too many errors")
