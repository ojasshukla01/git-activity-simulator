
🟩 git-activity-simulator

Supercharge your GitHub contribution graph with realistic fake commits!
Perfect for testing, demos, and safely filling out your green squares.

---

🚀 How To Use

✅ Ensure you have Git and Python 3.8+ installed.
✅ Clone this repo and set up your environment:

```
git clone https://github.com/ojasshukla01/git-activity-simulator.git
cd git-activity-simulator
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

✅ Generate your commits in a new local repo:

```
python -m gh_activity_boost.run_all
```

This command creates a **my-fake-history** folder and generates commits with these default settings:
- Date range: Last 365 days
- Commits per day: 3
- Frequency: Commits for every day
- Distribution: Evenly spread out for realism

✅ Create a private repo on GitHub and push the changes:

```
cd my-fake-history
git remote add origin git@github.com:<USERNAME>/my-fake-history.git
git push -u origin main
```

✅ Done! Check your GitHub profile for an active contribution graph. 😉

---

🗂️ Command-Line Options

If you’d like more control, run the simulator manually:

```
python -m gh_activity_boost.cli   --repo /path/to/repo   --start 2024-01-01   --end 2024-01-07   --commits-per-day 3   --dry-run
```

Options:
- --repo: Local Git repo path
- --start: Start date for fake commits (YYYY-MM-DD)
- --end: End date for fake commits (YYYY-MM-DD)
- --commits-per-day: Number of commits per day (default: 1)
- --pr-count: Number of pull requests to simulate (default: 0)
- --issues-count: Number of issues to simulate (default: 0)
- --stars-count: Number of repositories to star (default: 0)
- --dry-run: Preview actions without making any real changes

---

🏆 Achievements You Can Earn

By using this tool (especially with real API calls in the future), you might see:
- 🟩 Green Squares – Fill your contribution graph
- 🏁 Pull Shark – Create PRs (even fake ones!)
- 🏆 YOLO – Merge PRs without review (in private repos)
- ⭐ Starstruck – Star other repositories
- 💬 Galaxy Brain – Create issues/comments (future module!)
- 📦 Arctic Code Vault – Not achievable (historical snapshot only)

---

🎨 Show Off with GitHub Badges

Add these dynamic badges to your profile README:

Commits: https://img.shields.io/badge/commits-daily-brightgreen
Issues: https://img.shields.io/badge/issues-active-blue
Pull Requests: https://img.shields.io/badge/PRs-daily-purple
Stars: https://img.shields.io/badge/stars-daily-yellow

---

🧪 Run Tests

We use pytest to ensure everything works:

```
pytest tests/
```

---

🔄 How to Undo Fake Commits

If you want to remove fake commits from your local repo:

```
python -m gh_activity_boost.cleanup --repo /path/to/repo
```

This will remove the last 100 commits (adjust as needed!).

For fake issues, PRs, or stars (if real API calls are implemented):
- Un-star repos manually on GitHub.
- Close fake issues or PRs in the GitHub UI.

❌ Note: GitHub doesn’t provide a way to “reset” your contribution graph to its exact historical state.

---

⚠️ Disclaimer

This tool is for educational and demonstration purposes only.
Please don’t use it to misrepresent your real contributions or deceive others.

---

📄 License

MIT License. See LICENSE for details.

---

Happy hacking, and enjoy the green squares! 🌟
