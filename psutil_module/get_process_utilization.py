import psutil,sys

# pip install psutil

# CPU percent per process, based on interval
proc = psutil.Process(19288)    # Process takes PID
proc_name = proc.name()

try:
    while True:
        print("Process {} has utilization of {}%".format(proc_name, proc.cpu_percent(interval=3)))
except KeyboardInterrupt:
    print("Exiting")
    sys.exit(0)
except Exception as e:
    print(e)
