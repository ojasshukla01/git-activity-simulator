import argparse
from gh_activity_boost import fake_history, github_api

def main():
    parser = argparse.ArgumentParser(description="gh-activity-boost: Fill your GitHub activity graph!")
    parser.add_argument("--repo", required=True, help="Path to local Git repo")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--commits-per-day", type=int, default=1, help="Number of commits per day")
    parser.add_argument("--pr-count", type=int, default=0, help="Number of PRs to create")
    parser.add_argument("--issues-count", type=int, default=0, help="Number of issues to create")
    parser.add_argument("--stars-count", type=int, default=0, help="Number of repos to star")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without executing")

    args = parser.parse_args()

    fake_history.generate_commits(
        repo_path=args.repo,
        start_date=args.start,
        end_date=args.end,
        commits_per_day=args.commits_per_day,
        dry_run=args.dry_run
    )

    github_api.simulate_github_activity(
        pr_count=args.pr_count,
        issues_count=args.issues_count,
        stars_count=args.stars_count,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()
