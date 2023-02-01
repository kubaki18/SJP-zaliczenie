import csv
import pandas as pd
from datetime import datetime

file = "data.csv"
fieldnames = ["date", "hour", "minute", "contents"]

def add_log(contents):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        temp_time = datetime.now().strftime("%Y-%m-%d %H %M").split()
        writer.writerow([*temp_time, contents])

def handle_command(command):
    response = ""
    match command:
        case "show":
            with open(file) as f:
                reader = csv.reader(f, delimiter=',')
                response = ""
                for row in reader:
                    response += ' '.join(row) + '\n'
        case "freq":
            df = pd.read_csv(file)
            response = df.groupby(["date","hour", "minute"])["hour"].count().sort_values(ascending=False).head(5).to_string()
        case _:
            response = "OK"
    return response


def initialize_server():
    with open(file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
