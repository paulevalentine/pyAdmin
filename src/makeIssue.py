#!/usr/bin/env python3.13
""" Script to create issue folder and open """
from pathlib import Path
from datetime import date
import subprocess

today_str = date.today().strftime("%Y%m%d")
user_id = input("Enter descriptor: ")
loc = "./Issued/" + today_str + " " + user_id
path = Path(loc)
path.mkdir(parents=True, exist_ok=True)
subprocess.run(["open", loc])
