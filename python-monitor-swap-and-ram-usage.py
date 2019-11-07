import psutil
import pprint
import pandas as pd
import datetime
import time
def mem_swap():
    a = psutil.virtual_memory()
    a = (a.total - a.available) / 1.074e+9
    b = psutil.swap_memory()
    b = (b.total - b.free) / 1.074e+9
    return (a, b)




d = {"Time" : [], "Ram-Used[GB]" : [], "Swap-Used[GB]" : []}
try: 
    while True:
        time.sleep(1)
        ram, swap = mem_swap()
        a = datetime.datetime.now()
        d["Time"].append(':'.join(map(str, [int(a.hour), int(a.minute), int(a.second)])))
        d["Ram-Used[GB]"].append(round(ram, 2))
        d["Swap-Used[GB]"].append(round(swap, 2))
except KeyboardInterrupt:
    dd = pd.DataFrame(d)
    print("Max_Ram: ", dd["Ram-Used[GB]"].max())
    print("Max_Swap: ", dd["Swap-Used[GB]"].max())
    print("\n")
    dd.plot()
    print("\n")
    pprint.pprint(dd.sort_values("Ram-Used[GB]",ascending=False))