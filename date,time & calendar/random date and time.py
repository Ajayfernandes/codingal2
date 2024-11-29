import random 
import time

def random_date_time(start_date, end_date):
    print(f"printing random dates between {start_date} and {end_date}")
    random_gen = random.random()
    date_format = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(start_date,date_format))
    end_time = time.mktime(time.strptime(end_date,date_format))
    random_time = start_time + random_gen * (end_time - start_time)
    random_date = time.strftime(date_format,time.localtime(random_time))
    print(random_time)
    return random_date

print("Random Date = ", random_date_time("01/05/2009", "11/22/2024"))