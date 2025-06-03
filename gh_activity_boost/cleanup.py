import os
import subprocess

def undo_local_fake_commits(repo_path):
    print("⚠️ WARNING: This will remove the last commits. Use with caution!")
    # Remove the last 100 commits (or a safe number)
    subprocess.run(["git", "reset", "--hard", "HEAD~100"], cwd=repo_path)
    print("✅ Local commits removed.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Cleanup local fake commits")
    parser.add_argument("--repo", required=True, help="Path to local Git repo")
    args = parser.parse_args()

    undo_local_fake_commits(args.repo)
