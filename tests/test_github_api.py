from gh_activity_boost import github_api

def test_simulate_github_activity_dry_run(capfd):
    github_api.simulate_github_activity(
        pr_count=1,
        issues_count=1,
        stars_count=1,
        dry_run=True
    )
    
    captured = capfd.readouterr()
    assert "Would create Issue 1" in captured.out
    assert "Would create PR 1" in captured.out
    assert "Would star Repo 1" in captured.out
