from datetime import datetime, date
import json
import pprint
import os


class Loger:

    def __init__(self, msg):
        self.msg = msg

    def log(self):
        now = datetime.now()
        month_year = now.strftime("%m-%Y")
        day = now.strftime("%d")
        file_name = f"{now.strftime("%H-%M-%S")}.txt"
        file_path = os.path.join(month_year, day, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        massege = {
            "timestamp": datetime.now().isoformat(),
            "msg": self.msg,
        }
        with open(file_path, "w") as f:
            json.dump(massege, f)

        with open(file_path, "r") as f:
            res = json.load(f)
            pprint.pprint(res)


a = Loger("Привет")
a.log()
a.log()