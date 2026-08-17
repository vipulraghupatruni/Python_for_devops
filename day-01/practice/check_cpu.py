import psutil
# You have to do work on monitoring user CPU threshold(limit)
# current cpu usage to know
# if cpu usage threshold is increased, send an email 

def check_cpu_threshold():
    cpu_threshold = int(input("enter the cpu threshold "))
    
    current_cpu =psutil.cpu_percent(interval=1)
    print("Current CPU % : ",current_cpu)
    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent ...")
        
    else:
        print("CPU in safe state")

check_cpu_threshold()