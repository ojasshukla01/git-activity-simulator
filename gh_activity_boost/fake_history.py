import os
import subprocess
from datetime import datetime, timedelta

def generate_commits(repo_path, start_date, end_date, commits_per_day, dry_run):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start

    for i in range(delta.days + 1):
        day = start + timedelta(days=i)
        for j in range(commits_per_day):
            time_str = day.strftime("%Y-%m-%dT%H:%M:%S")
            msg = f"Fake commit on {time_str}"
            if dry_run:
                print(f"[DRY-RUN] Would commit: {msg}")
            else:
                create_commit(repo_path, msg, time_str)

def create_commit(repo, msg, date_str):
    filepath = os.path.join(repo, "FAKE_ACTIVITY.md")
    with open(filepath, "a") as f:
        f.write(f"{msg}\n")
    subprocess.run(["git", "add", "."], cwd=repo)
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", msg], cwd=repo, env=env)
