import threading

local_data = threading.local()

def initialize_data():
    local_data.ref = []
    local_data.ref.append(f"INIT {threading.current_thread().name}")

def process_data():
    local_data.ref.append(f"PROCESS {threading.current_thread().name}")

def display_data():
    print(f"DISPLAY {threading.current_thread().name} data: {local_data.ref}")

def worker():
    initialize_data()
    process_data()
    display_data()

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
