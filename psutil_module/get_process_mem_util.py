import psutil,sys

# pip install psutil

# Process Memory Usage
proc = psutil.Process(19288)
proc_name = proc.name()
proc_mem = proc.memory_info().rss   # RSS is non-swapped physical memory a process has used.

print("{0:>30} : {1}".format("Process Name", proc_name))
print("{0:>30} : {1:,} bytes".format("Used Memory", proc_mem))
