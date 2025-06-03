import os
import tempfile
from gh_activity_boost import fake_history

def test_generate_commits_dry_run():
    with tempfile.TemporaryDirectory() as repo:
        # Initialize a git repo
        os.system(f"git init {repo}")
        
        # Run the commit generator in dry-run mode
        fake_history.generate_commits(
            repo_path=repo,
            start_date="2024-01-01",
            end_date="2024-01-01",
            commits_per_day=1,
            dry_run=True
        )
        
        # Dry-run shouldn't create any commits
        result = os.popen(f"git -C {repo} log").read()
        assert "Fake commit" not in result

def test_generate_commits_real():
    with tempfile.TemporaryDirectory() as repo:
        os.system(f"git init {repo}")
        
        # Actually create commits
        fake_history.generate_commits(
            repo_path=repo,
            start_date="2024-01-01",
            end_date="2024-01-01",
            commits_per_day=1,
            dry_run=False
        )
        
        # Should have a commit
        result = os.popen(f"git -C {repo} log --oneline").read()
        assert "Fake commit" in result
