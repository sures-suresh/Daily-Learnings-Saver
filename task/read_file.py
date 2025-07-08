from pathlib import Path
from datetime import date

# 1) stored the  path to variable
TARGET_DIR = Path(r"C:\Users\USER\Music\Desktop\task\note_saver")
# TARGET_DIR.mkdir(parents=True, exist_ok=True)   # creates the whole path if needed

# 2) Build today’s file name inside that folder, e.g. 2025-06-19.txt
today      = date.today().isoformat()
#  to jonin both
file_path  = TARGET_DIR / f"{today}.txt"  

print(f"Date: {today}")
print("What did you learn today?")

# 3) Collect three inputs and write them to the fileuj
with file_path.open("w", encoding="utf-8") as f:
    for i in range(1, 4):
        answer = input(f"{i} – Enter: ")
        f.write(f"{i}. {answer}\n")

print(f"\n✅ Notes saved to {file_path}")
