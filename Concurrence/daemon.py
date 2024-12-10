from threading import Thread
import time

def worker(caractere):
    for i in range(0,10):
        print(caractere, flush = True, end='')
        time.sleep(1)   

t_asterix = Thread(target=worker, args=("*",), daemon=True)
t_asterix.start()

time.sleep(5)
t_underscore = Thread(target=worker, args=("_",), daemon=True)
t_underscore.start()
t_point = Thread(target=worker, args=(".",), daemon=True)

t_point.start()

#*****_.*_.*_.*._*._*._._._._._  # all daemon = False

#*****_.*_.*_.*_.*_.*_. #  t_asterix daemon = False   t_underscore /  t_point  daemon = TRue

#*****_. # all t_asterix / t_underscore /  t_point  daemon = True