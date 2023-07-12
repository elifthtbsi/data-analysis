"""
en çok log'u olan 50 training set ve bu training set'lerin log sayısını verir
"""
import csv

itemId_log_numbers={}
item_ids=[]
log_numbers=[]

with open ('users_progress.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)

    for line in reader:
        item_id=line[1]
        item_type=line[3]
        log_name=line[4]

        if item_type=="training_set_article":
            if item_id not in itemId_log_numbers:
                itemId_log_numbers[item_id]=0
            if log_name=='started' or log_name=='completed':
                itemId_log_numbers[item_id]+=1

for i in range(50):
    max_key=max(itemId_log_numbers, key=itemId_log_numbers.get)
    item_ids.append(max_key)
    log_numbers.append(itemId_log_numbers[max_key])
    itemId_log_numbers.pop(max_key)

with open ('training.csv', 'w') as export_file:
    headers=['item_id','log_numbers']
    writer=csv.DictWriter(export_file, fieldnames=headers)
    writer.writeheader()

    for i in range(50):
        items_and_logs={'item_id': 0, 'log_numbers': 0}
        items_and_logs['item_id']=item_ids[i]
        items_and_logs['log_numbers']=log_numbers[i]
        writer.writerow(items_and_logs)