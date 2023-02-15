from os import system
import platform

system_info = platform.uname()

system = system_info.system
node = system_info.node
release = system_info.release
version = system_info.version
machine = system_info.machine
processor = system_info.processor

print("{0:>10} : {1:<30}".format("System", system))
print("{0:>10} : {1:<30}".format("Node", node))
print("{0:>10} : {1:<30}".format("Release", release))
print("{0:>10} : {1:<30}".format("Version", version))
print("{0:>10} : {1:<30}".format("Machine", machine))
print("{0:>10} : {1:<30}".format("Processor", processor))

# Get windows info
win32_ver = platform.win32_ver()
win32_edition = platform.win32_edition()
win32_is_iot = platform.win32_is_iot()

print('=' * 70)
print("{0} : {1}".format("Windows Version", win32_ver))
print("{0} : {1}".format("Windows Edition", win32_edition))
print("{0} : {1}".format("Windows IoT", win32_is_iot))
