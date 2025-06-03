🟩 git-activity-simulator

Supercharge your GitHub profile with automated activity for testing, demos, and fun!  
This CLI tool generates fake commit histories and simulates PRs, issues, and stars to help you visualize a more active contribution graph – all in a safe, controlled way.

---

🚀 Features

✅ Generate fake commits across any date range  
✅ Simulate pull requests, issues, and starring repositories (API-ready)  
✅ Dry-run mode to preview actions without making real changes  
✅ Fully automated CLI – no manual Git commands needed  
✅ Modular, well-documented, and cross-platform  

---

⚙️ Prerequisites

- Python 3.8+ installed  
- Git installed and in your system PATH  

---

🔧 Installation – Step by Step

1️⃣ Clone the Repository  
Open your terminal and run:
git clone https://github.com/ojasshukla01/git-activity-simulator.git  
cd git-activity-simulator

2️⃣ Set Up a Virtual Environment  
This keeps your project dependencies isolated.
python -m venv venv

3️⃣ Activate the Virtual Environment  
- On macOS/Linux:
  source venv/bin/activate
- On Windows (PowerShell):
  .\venv\Scripts\Activate.ps1
- On Windows (Command Prompt):
  venv\Scripts\activate.bat

4️⃣ Install Project Dependencies  
pip install -r requirements.txt

---

📦 Usage – Generate Fake Git Activity

1️⃣ Create a Dummy Local Repository for Testing  
To avoid affecting real repos, make a safe test repo:
mkdir /path/to/dummy-repo  
cd /path/to/dummy-repo  
git init

2️⃣ Run the Activity Simulator  
Back in your project root (git-activity-simulator):
python -m gh_activity_boost.cli \
  --repo /path/to/dummy-repo \
  --start 2024-01-01 \
  --end 2024-01-03 \
  --commits-per-day 2 \
  --dry-run

Remove --dry-run if you want to actually create the commits:
python -m gh_activity_boost.cli \
  --repo /path/to/dummy-repo \
  --start 2024-01-01 \
  --end 2024-01-03 \
  --commits-per-day 2

---

🗂️ Command-Line Options

--repo             Path to your local Git repository  
--start            Start date for fake commits (YYYY-MM-DD)  
--end              End date for fake commits (YYYY-MM-DD)  
--commits-per-day  Number of commits per day (default: 1)  
--pr-count         Number of pull requests to simulate (default: 0)  
--issues-count     Number of issues to simulate (default: 0)  
--stars-count      Number of repositories to star (default: 0)  
--dry-run          Preview actions without making any real changes  

---

🏆 Achievements You Can Earn

By running this tool (especially if real API calls are added), you might see:

🟩 Green Squares          – Fill your contribution graph with commit activity  
🏁 Pull Shark             – Create (even fake) PRs in real/private repos  
🏆 YOLO                   – Merge PRs without review in private repos  
⭐ Starstruck             – Star other repositories  
💬 Galaxy Brain           – Create issues/comments (future module!)  
📦 Arctic Code Vault      – Not achievable – historical snapshot only  

---

🎨 Show Off with GitHub Badges

Add these dynamic badges to your README.md to highlight activity:

Commits:  
https://img.shields.io/badge/commits-daily-brightgreen

Issues:  
https://img.shields.io/badge/issues-active-blue

Pull Requests:  
https://img.shields.io/badge/PRs-daily-purple

Stars:  
https://img.shields.io/badge/stars-daily-yellow

---

🧪 Run Tests

We use pytest to ensure everything works:
pytest tests/

---

🔄 How to Undo Fake Commits

If you want to remove fake commits in your local repo:
python -m gh_activity_boost.cleanup --repo /path/to/dummy-repo

This will remove the last 100 commits. Adjust as needed!

For fake issues, PRs, or stars (if real API calls are used):
- Un-star repos manually on GitHub.
- Close fake issues/PRs in the GitHub UI.

❌ GitHub doesn’t provide a way to “reset” your contribution graph to its exact historical state.

---

⚠️ Disclaimer

This tool is for educational and demonstration purposes only.  
Please don’t use it to misrepresent your actual contributions or deceive others.

---

📄 License

MIT License. See LICENSE for details.

---

Happy hacking, and enjoy the green squares! 🌟
