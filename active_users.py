"""
aktif kullanıcı sayısını, aktif kullanıcı sayısının premium kullanıcı sayısına oranını ve 
aktif olup premium olmayan kullanıcı sayısını verir
"""
import csv
from datetime import datetime,timedelta
count=0
today=datetime.today().date()
one_week_ago=today-timedelta(days=7)
active_users=[]
premiums=[]
not_premiums=[]
active_and_notpremiums=0
with open ('users.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file)
	
	for line in csv_reader:
		user_id=line[0]
		premium=line[7]
		if premium=='False':
			premium=False
			not_premiums.append(user_id)
		elif premium=='True':
			premium=True
			premiums.append(user_id)

with open ('users_progress.csv', 'r') as csv_file:
	csv_reader=csv.reader(csv_file) 
	
	for line in csv_reader:
		user_id=line[0]
		date=line[2].split(" ")[0]
		date=date.split("-")
		
		if user_id not in active_users:
			for i in range(len(date)):
				if i==0:
					year=date[0]
				elif i==1:
					month=date[1]
				elif i==2:
					day=date[2]
					date=day+"/"+month+"/"+year
					date_obj=datetime.strptime(date, "%d/%m/%Y").date()
					if one_week_ago<date_obj<today:
						active_users.append(user_id)
	
for i in active_users:
	if i in not_premiums:
		active_and_notpremiums+=1

with open ('active_users.csv', 'w') as export_file:
		headers=['title', 'value']
		writer=csv.DictWriter(export_file, fieldnames=headers)
		writer.writeheader()

		dictionary=[{'title': 'number_of_active_users', 'value': len(active_users)},
		{'title': 'the_ratio(active/premium)', 'value': len(active_users)/len(premiums)},
		{'title' : 'active_and_notpremiums', 'value': active_and_notpremiums}]

		writer.writerows(dictionary)

