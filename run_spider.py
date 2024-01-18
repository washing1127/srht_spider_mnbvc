import os
import json
import shutil
import subprocess
import traceback

with open("repo_list.jsonl", "r", encoding="utf-8")as r:
    data = r.readlines()

err_count = 0
if not os.path.exists("output"): os.mkdir("output")
for line in data:
    try:
        dic = json.loads(line.strip())
        clone_url = dic["git"].replace("//", "/").replace(":/", "://")
        repo_name = dic["name"]
        clone_path = os.path.join("output", repo_name)
        os.system(f"git clone {clone_url} {clone_path}")
    except: 
        traceback.print_exc()
        err_count += 1
        if err_count >= 5:
            raise OSError("too many errors")
