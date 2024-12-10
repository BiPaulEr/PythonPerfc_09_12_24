import threading

def initialize_data():
    ref = []
    ref.append(f"INIT {threading.current_thread().name}")
    return ref

def process_data(ref):
    ref.append(f"PROCESS {threading.current_thread().name}")

def display_data(ref):
    print(f"DISPLAY  {threading.current_thread().name} data: {ref}")

def worker():
    ref = initialize_data()
    process_data(ref)
    display_data(ref)

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
