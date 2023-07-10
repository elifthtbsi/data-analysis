#en fazla progress log'u olan 50 kullanıcının id'lerini ve progress log sayılarını verir

import csv

progress_log_numbers={}

with open ('users_progress.csv', 'r') as csv_file:
	csv_reader=csv.reader(csv_file) 
	temp_id="id"
	for line in csv_reader:
		user_id=line[0]
		progress_log=line[4]
		if user_id!=temp_id:
			progress_log_numbers[user_id]=0
		if progress_log=="started" or progress_log=="completed":
			progress_log_numbers[user_id]+=1
		
		temp_id=user_id
			
for i in range(50):
	max_key=max(progress_log_numbers, key=progress_log_numbers.get)
	print(max_key,":",progress_log_numbers[max_key])
	progress_log_numbers.pop(max_key)







