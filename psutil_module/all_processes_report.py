import psutil
import sys 


def get_process_list():
    proc = []
    for p in psutil.process_iter(['pid', 'name']):
        try:
            p.cpu_percent()
            proc.append(p)
        except Exception as e:
            print(e)
        
    return proc


def process_iterator(kids_iterator, key_iterator):
    for kids in kids_iterator.children():
        if len(kids.children()) == 0:
            key_iterator[kids.pid] = [kids, len(kids.children())]
        else:
            key_iterator[kids.pid] = [kids, len(kids.children()), {}]
            process_iterator(key_iterator[kids.pid][0], key_iterator[kids.pid][2])


def get_process_dict(proc):
    processes = {}
    for p in proc:
        if p.pid != 0:                      # skip initial process
            if psutil.pid_exists(p.pid):    # prevents error if process closes between list creation and running this function.
                if len(p.children()) == 0:  # Filter process except those with no reported parents 
                    # print(len(p.children(recursive = True)))
                    if len(p.children()) == 0: #Skip additional walks because there no children
                        processes[p.pid] = [p, len(p.children())]
                    else:
                        processes[p.pid] = [p, len(p.children()), {}]

                        kids_iterator = p   # parent process to investigate
                        key_iterator = processes[p.pid][2]  # Reference to nested dict inside processes dict

                        process_iterator(kids_iterator, key_iterator)   # iterate through the root process to fill out their children
    
    return processes



# Search process Dict for specified PID, responds as Bool
def search_processes(pid, proc_dict):
    global found 
    for pid_keys in proc_dict.keys():
        if pid == pid_keys:
            found = True

        if proc_dict[pid_keys][1] != 0:
            search_processes(pid, proc_dict[pid_keys][2])

    return found


def parent_process_count(proc_dict, parent_pid):
    global found, process_counter
    found = False 
    search_processes(parent_pid, proc_dict)

    if found:
        parent_process_count_iterator(proc_dict, parent_pid)
    else:
        process_counter = -1


def parent_process_count_iterator(proc_dict, parent_pid):
    for pid_keys  in proc_dict.keys():
        if parent_pid == pid_keys:
            if proc_dict[pid_keys][1] != 0:
                process_count(proc_dict[pid_keys][2])
        elif proc_dict[pid_keys][1] != 0:
            parent_process_count_iterator(proc_dict[pid_keys][2], parent_pid)

    
def process_count(proc_dict):
    global process_counter 
    process_counter += len(proc_dict.keys())
    for pid_keys in proc_dict.keys():
        if proc_dict[pid_keys][1] != 0:
            process_count(proc_dict[pid_keys][2])


def total_processes(dict):
    global process_counter 
    process_counter = 0
    process_count(dict)
    print("There are a total of", process_counter, "processes in this processes dictionary")


def parent_processes(dict, Parent_PID):
    global process_counter
    process_counter = 0
    parent_process_count(dict, Parent_PID)
    print("There are", process_counter, "processes under the parent PID", Parent_PID)


def main():
    try:
        thisdict = get_process_dict(get_process_list())
    except Exception as e:
        print(e)
        sys.exit()

    print(thisdict)

    total_processes(thisdict)
    parent_processes(thisdict, 16252)


if __name__ == "__main__":
    main()
