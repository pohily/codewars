import queue
from collections import namedtuple




def queue_time(customers, n):
    next_customer = namedtuple('next_customer', 'time till')
    sim_time = 0
    busy_tills = queue.PriorityQueue(maxsize=n)
    

    for till in range(n): # while tills
        if customers:
            next_buyer = next_customer(customers.pop(0), till)
            print(next_buyer)
            busy_tills.put(next_buyer)
        else:
            break
    print(customers)
    while customers:
        sim_time, till = busy_tills.get()
        next_buyer = next_customer(customers.pop(0) + sim_time, till)
        print(next_buyer)
        busy_tills.put(next_buyer)
            
    for i in range(busy_tills.qsize()):
        sim_time, till = busy_tills.get()
        #busy_tills.get_nowait()
    return sim_time

print(queue_time([0], 1))
