from datetime import datetime,timezone
from pathlib import Path

now = datetime.now(timezone.utc)
timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")

file = Path("activity.txt")

with file.open("a",encoding="utf-8") as f:
    f.write(f"{timestamp} - Automated activity log update\n")

print(f"Activity log updated at {timestamp}")
