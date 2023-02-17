import psutil, os, sys, time
from prettytable import PrettyTable
from psutil import cpu_percent
from psutil import process_iter

def Create_Process_List():
    proc = []
    for p in psutil.process_iter(['pid', 'name']):
        try:
            p.cpu_percent()
            proc.append(p)
        except Exception as e:
            print(e)
        
    return proc 


def main():
    try:
        while True:
            process_cpu_table = PrettyTable(['PID', 'PNAME', 'STATUS', 'CPU', 'NUM THREADS', 'MEMORY (MB)'])
            top_cpu = {}
            top_mem = {}
            time.sleep(0.5)

            for p in Create_Process_List():
                if p.pid != 0:
                    top_cpu[p] = p.cpu_percent() / psutil.cpu_count()
                    top_mem[p] = p.memory_info().rss

            top_cpu_list = sorted(top_cpu.items(), key=lambda c: c[1], reverse=True)
            top_mem_list = sorted(top_mem.items(), key=lambda c: c[1], reverse=True)

            top_10_cpu = top_cpu_list[:10]
            top_10_mem = top_mem_list[:10]

            for p, cpu_percent in top_10_cpu:
                try:
                    with p.oneshot():
                        process_cpu_table.add_row([
                            str(p.pid),
                            p.name(),
                            p.status(),
                            f'{cpu_percent:.2f}' + '%',
                            p.num_threads(),
                            f'{p.memory_info().rss / 1e6:.3f}'
                        ])

                except Exception as e:
                    print(e)

            process_mem_table = PrettyTable(['PID', 'PNAME', 'STATUS', 'CPU', 'NUM THREADS', 'MEMORY (MB)'])

            for p, mem in top_10_mem:
                try:
                    with p.oneshot():
                        process_mem_table.add_row([
                            str(p.pid),
                            p.name(),
                            p.status(),
                            f'{cpu_percent:.2f}' + '%',
                            p.num_threads(),
                            f'{mem / 1e6:.3f}'
                        ])

                except Exception as e:
                    print(e)

            os.system('cls')
            print(process_cpu_table)
            print(process_mem_table)


    except KeyboardInterrupt:
        print('Exiting!')
        sys.exit(0)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()
