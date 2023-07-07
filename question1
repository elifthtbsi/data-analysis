"""
son 1 haftada, 1 ayda ve 3 ayda kayıt olan kullanıcı sayısı
1 ay 30 gün, 3 ay 90 gün olarak alınmıştır
"""
import csv
from datetime import datetime,timedelta

one_week_ago_counter=0
one_month_ago_counter=0
three_month_ago_counter=0

today=datetime.today().date()
one_week_ago=today-timedelta(days=7)
one_month_ago=today-timedelta(days=30)
three_month_ago=today-timedelta(days=90)

with open('users.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	
	for line in csv_reader:
		line[9]=line[9].split(" ")[0]
		date=line[9].split("-")
		
		for i in range(len(date)):
			if i==0:
				year=date[i]
			elif i==1:
				month=date[i]
			elif i==2:
				day=date[i]
				date=day+"/"+month+"/"+year
				date_object = datetime.strptime(date, "%d/%m/%Y").date()
				
				if one_week_ago<date_object<today:
					one_week_ago_counter+=1
				if one_month_ago<date_object<today:
					one_month_ago_counter+=1
				if three_month_ago<date_object<today:
					three_month_ago_counter+=1
				else:
					continue




print("last week:",one_week_ago_counter)
print("last month:",one_month_ago_counter)
print("last three months:",three_month_ago_counter)			
		
		
		
		
		
		
		
		
		
		
		
				
