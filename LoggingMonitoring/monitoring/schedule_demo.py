import schedule
import time 

def task1():
    print(f"TASK 1 {time.asctime()}")

def task2():
    print(f"TASK 2 {time.asctime()}")

def task3():
    print(f"TASK 3 {time.asctime()}")

job1 = schedule.every(1).minutes.do(task1)
schedule.every(20).seconds.do(task2)
schedule.every(5).hours.do(task3)
schedule.cancel_job(job1)
while True:
    schedule.run_pending()
    time.sleep(5)
