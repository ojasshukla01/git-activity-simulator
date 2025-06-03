🟩 git-activity-simulator

Supercharge your GitHub profile with automated activity for testing, demos, and fun!  
This CLI tool generates fake commit histories and simulates PRs, issues, and stars to help you visualize a more active contribution graph – all in a safe, controlled way.

---

🚀 Features

✅ Generate fake commits across any date range  
✅ Simulate pull requests, issues, and starring repositories (API-ready)  
✅ Dry-run mode to preview actions without changing anything  
✅ Fully automated CLI – no manual Git commands needed  
✅ Modular, well-documented, and cross-platform  

---

⚙️ Installation

git clone https://github.com/ojasshukla01/git-activity-simulator.git  
cd git-activity-simulator  
python -m venv venv  
source venv/bin/activate  # macOS/Linux  
# Windows: venv\Scripts\activate  
pip install -r requirements.txt  

---

📦 Usage

python -m gh_activity_boost.cli \
  --repo /path/to/your/repo \
  --start 2024-01-01 \
  --end 2024-01-07 \
  --commits-per-day 3 \
  --pr-count 2 \
  --issues-count 2 \
  --stars-count 1 \
  --dry-run

Arguments:

--repo             Local Git repo path  
--start            Start date (YYYY-MM-DD)  
--end              End date (YYYY-MM-DD)  
--commits-per-day  Number of commits per day (default: 1)  
--pr-count         Number of PRs to simulate (default: 0)  
--issues-count     Number of issues to simulate (default: 0)  
--stars-count      Number of repositories to star (default: 0)  
--dry-run          Preview actions only  

---

🏆 Achievements You Can Earn

By running this tool (especially with real GitHub API calls), you might see:

🟩 Green Squares          – Fill your GitHub contribution graph with fake commit activity  
🏁 Pull Shark             – Create PRs (even fake ones!) in real repos  
🏆 YOLO                   – Merge your own PRs without review (in private repos)  
⭐ Starstruck             – Star other repositories  
💬 Galaxy Brain           – Create issues or comments (future module!)  
📦 Arctic Code Vault      – Not achievable – historical snapshot only  

---

🎨 GitHub Badges

Running this repo can indirectly boost your GitHub profile appearance.  
Add these dynamic badges to your README.md to show off your activity:

Commits: https://img.shields.io/badge/commits-daily-brightgreen  
Issues: https://img.shields.io/badge/issues-active-blue  
Pull Requests: https://img.shields.io/badge/PRs-daily-purple  
Stars: https://img.shields.io/badge/stars-daily-yellow  

---

🧪 Tests

Use pytest to validate core logic:

pytest tests/

---

⚠️ Disclaimer

This tool is for educational and demonstration purposes only.  
Please don’t use it to misrepresent your actual contributions or deceive others.

---

📄 License

MIT License. See LICENSE for details.

---

Happy hacking, and enjoy the green squares! 🌟
