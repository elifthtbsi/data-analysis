"""
en çok "completed" yapan 50 kullanıcı ve bu kullancıların "completed" sayısı
"""

import csv 

completed={}
users_id=[]
comp_numbers=[]

with open ('users_progress.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)

    for line in reader:
        user_id=line[0]
        log_name=line[4]

        if user_id not in completed and log_name=='started':
            completed[user_id]=0

        elif log_name=='completed':
            if user_id not in completed:
                completed[user_id]=1
            else:
                completed[user_id]+=1

for i in range(50):
    max_key=max(completed, key=completed.get)
    users_id.append(max_key)
    comp_numbers.append(completed[max_key])
    completed.pop(max_key)


with open ('completed.csv', 'w') as export:
    headers=['user_id', 'completed_numbers']
    writer=csv.DictWriter(export, fieldnames=headers)
    writer.writeheader()

    for i in range(50):
        comp={'user_id':0, 'completed_numbers':0}
        comp['user_id']=users_id[i]
        comp['completed_numbers']=comp_numbers[i]
        writer.writerow(comp)
