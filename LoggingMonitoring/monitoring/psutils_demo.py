import psutil

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(2)
    print(f"Utilisation cpu : {cpu_percent}%")
    return cpu_percent

def get_memory_usage():
    disk_usage = psutil.disk_usage('/')
    print(f"Utilisation Disque : {disk_usage.percent}%")
    return disk_usage

get_cpu_usage()
get_memory_usage()


