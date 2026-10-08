import os
import shlex
import time
from pathlib import Path
from subprocess import run

repo = os.environ.get("DEMO_REPO", "https://github.com/jupyterhealth/demos")
ref = os.environ.get("DEMO_REF", "main")
refresh_interval = int(os.environ.get("DEMO_PULL_SECONDS", "30"))

repo_path = Path("demos")


def git(args, **kwargs):
    cmd = ["git"] + args
    print(f"{shlex.join(cmd)}")
    kwargs.setdefault("check", True)
    return run(cmd, **kwargs)


def refresh():
    if not repo_path.exists():
        git(["clone", repo, str(repo_path)])
    git(["fetch", "origin", ref], cwd=repo_path)
    git(["checkout", "FETCH_HEAD"], cwd=repo_path)


def keep_fresh():
    while True:
        try:
            refresh()
        except Exception as e:
            print("Error:", e)
        time.sleep(refresh_interval)


if __name__ == "__main__":
    keep_fresh()
