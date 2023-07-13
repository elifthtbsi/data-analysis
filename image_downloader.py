import csv
import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
url=os.getenv("LINK")

users_with_pic=[]

with open ('users.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)
    
    for line in reader:
        user_id=line[0]
        is_pic=line[10]
            
        if is_pic=="True":
            users_with_pic.append(user_id)

for i in users_with_pic:
    link=url + "/" + i + ".jpg"
    img=requests.get(link)
    with open(i+'.jpg', 'wb') as f:
        f.write(img.content)
