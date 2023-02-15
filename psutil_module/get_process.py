import psutil

# pip install psutil

for proc in psutil.process_iter(['pid', 'ppid', 'name', 'username']):
    print(proc.info)
