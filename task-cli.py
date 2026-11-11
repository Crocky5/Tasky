import json
import sys 
import os
import time
import datetime 


# To check if file exists if not then creates a new file

if os.path.isfile("list.json"):
	print("File Exists")
else:
	with open("list.json","w") as file:
		json.dump({"tasks":[]},file,indent=4)

with open("list.json","r") as file:
		data = json.load(file)


def list_all():
	
		len_data = len(data["tasks"])
		
		for i in range(len_data):
			print("-"*40)
			print(data["tasks"][i]["id"])
			print(data["tasks"][i]["description"])
			print(data["tasks"][i]["status"])
			print(data["tasks"][i]["createdAt"])
			print(data["tasks"][i]["updatedAt"])
			print("-"*40)	


def add_item(arg2):
	with open("list.json","r") as file:
		data = json.load(file)
	id_list = len(data["tasks"])

		
	add_data = {
      "id": id_list +1,
      "description": arg2,
      "status": "todo",
      "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "updatedAt": "2026-11-08T09:00:00Z"
    }

	data["tasks"].append(add_data)

	with open("list.json","w") as file:
		json.dump(data,file,indent=4)
		print(f"Task Added Successfully (ID:{add_data["id"]})")

# try: 
arg1 = sys.argv[1]
if arg1 == "list":
	list_all()
elif arg1 == "add":
	arg2 = sys.argv[2]
	add_item(arg2)
# except:
# 	print("Help Menu: ")



