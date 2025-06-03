import os
import random

def simulate_github_activity(pr_count, issues_count, stars_count, dry_run):
    for i in range(issues_count):
        if dry_run:
            print(f"[DRY-RUN] Would create Issue {i+1}")
        else:
            print(f"[SIMULATED] Created fake Issue {i+1}")

    for i in range(pr_count):
        if dry_run:
            print(f"[DRY-RUN] Would create PR {i+1}")
        else:
            print(f"[SIMULATED] Created fake PR {i+1}")

    for i in range(stars_count):
        if dry_run:
            print(f"[DRY-RUN] Would star Repo {i+1}")
        else:
            print(f"[SIMULATED] Starred repo {i+1}")
