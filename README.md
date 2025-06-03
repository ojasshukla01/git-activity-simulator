🟩 git-activity-simulator

Supercharge your GitHub contribution graph with a single command-line tool!  
Generate fake commit histories, mock PRs, issues, and stars – perfect for testing, demos, and learning Git workflows.

---

🚀 Features

✅ Generate fake commit history across any date range  
✅ Simulate PRs, issues, and starring repositories (API-ready)  
✅ Dry-run mode for safe previews before executing  
✅ Fully automated CLI – no manual steps needed  
✅ Modular, well-documented, and cross-platform  

---

⚙️ Installation

1️⃣ Clone the repository:
git clone https://github.com/ojasshukla01/git-activity-simulator.git
cd git-activity-simulator

2️⃣ Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows: venv\Scripts\activate
pip install -r requirements.txt

---

📦 Usage

Run the CLI tool to generate fake Git activity:

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

--repo             Path to your local Git repository  
--start            Start date (YYYY-MM-DD)  
--end              End date (YYYY-MM-DD)  
--commits-per-day  Number of commits per day (default: 1)  
--pr-count         Number of PRs to simulate (default: 0)  
--issues-count     Number of issues to simulate (default: 0)  
--stars-count      Number of repositories to star (default: 0)  
--dry-run          Preview actions without executing  

---

🎯 Customization

- Change date ranges, commit counts, PRs, issues, and stars to fit your demo or learning goals.
- Use --dry-run first to preview everything safely.
- You can extend modules to make real API calls for live GitHub activity (e.g., PRs and stars).

---

💡 Possible Achievements & Effects

Achievement          How?  
-------------------- ---------------------------------------------  
🟩 Green Squares     Fake commit history fills your contribution graph  
🏁 YOLO / PR Shark   Mock PRs help simulate real activity (in real usage)  
🚀 Active Profile    Stars, issues, and commits create an active profile look  

---

🧪 Running Tests

We use pytest to ensure everything works as expected:

pytest tests/

---

🪄 Extend & Contribute

This project is modular and easy to extend:
- Add random commit messages.
- Visualize your contribution stats with shields.io.
- Build real API integrations for PRs and stars.

Pull requests welcome! 🚀

---

⚠️ Disclaimer

This tool is for educational, demo, and fun purposes only.  
Do not use it to misrepresent your contributions or deceive others.

---

📄 License

MIT License. See LICENSE for full details.

---

Happy hacking! 🌟
