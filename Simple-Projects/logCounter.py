from pathlib import Path

script_dir = Path(__file__).resolve().parent
log_file_path = script_dir / "log-sample.txt"

with open(log_file_path, "r") as log_file:
    log_contents = log_file.readlines()
    log_contents = [line.strip() for line in log_contents]

records = []

for line in log_contents:
    parts = line.split()

    entry = {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "category": parts[3],
        "action": parts[4],
        "user": parts[5],
        "result": parts[6],
    }

    records.append(entry)

print(records[0])
print(records[0]["level"])
print(records[0]["user"])