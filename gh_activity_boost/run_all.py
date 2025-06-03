import os
import subprocess
import sys
from datetime import datetime, timedelta

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    repo_path = os.path.join(project_root, "../my-fake-history")
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
        subprocess.run(["git", "init"], cwd=repo_path)
        print("✅ Initialized local repo: my-fake-history")

    today = datetime.today()
    start_date = (today - timedelta(days=365)).strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    print(f"✅ Generating commits from {start_date} to {end_date}...")

    subprocess.run([
        sys.executable, "-m", "gh_activity_boost.cli",
        "--repo", repo_path,
        "--start", start_date,
        "--end", end_date,
        "--commits-per-day", "3"
    ])

    print("🎉 Done! Check your new repo in 'my-fake-history'.")

if __name__ == "__main__":
    main()