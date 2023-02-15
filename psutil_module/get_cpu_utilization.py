import psutil,sys

# pip install psutil

# CPU Utilization, based on interval
try:
    while True:
        print(psutil.cpu_percent(interval=3, percpu=True))
except KeyboardInterrupt:
    print("Exiting")
    sys.exit(0)
except Exception as e:
    print(e)
