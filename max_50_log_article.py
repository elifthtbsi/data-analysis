"""
en çok log'u olan 50 article'ı ve bu article'ların log sayılarını verir
"""
import csv

itemId_log={}
item_ids=[]
log_numbers=[]

with open ('users_progress.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)

    for line in reader:
        item_id=line[1]
        item_type=line[3]
        log_name=line[4]

        if item_type=="article":
            if item_id not in itemId_log:
                itemId_log[item_id]=0
            if log_name=="started" or log_name=="completed":
                itemId_log[item_id]+=1
        
for i in range(50):
    max_key=max(itemId_log, key=itemId_log.get)
    item_ids.append(max_key)
    log_numbers.append(itemId_log[max_key])
    itemId_log.pop(max_key)

with open('articles.csv', 'w') as export_file:
    headers=['item_id', 'log_numbers']
    writer=csv.DictWriter(export_file, fieldnames=headers)
    writer.writeheader()
    
    for i in range(50):
        items_and_logs={'item_id': 0, 'log_numbers': 0}
        items_and_logs['item_id']=item_ids[i]
        items_and_logs['log_numbers']=log_numbers[i]
        writer.writerow(items_and_logs)