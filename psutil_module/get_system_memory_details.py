import psutil,sys

# pip install psutil

# System Memory Usage
virtual_memory = psutil.virtual_memory()
print(virtual_memory)

total_mem = virtual_memory.total
used_mem = virtual_memory.used
percent_used_mem = virtual_memory.percent
free_mem = virtual_memory.free

print("{0:>30} : {1} bytes".format("Total Memory", total_mem))
print("{0:>30} : {1} bytes".format("Used Memory", used_mem))
print("{0:>30} : {1} bytes".format("Free Memory", free_mem))
print("{0:>30} : {1}%".format("Used Memory in %", percent_used_mem))
