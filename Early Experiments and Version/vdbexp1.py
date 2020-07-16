import numpy as np
from datetime import datetime, timedelta

date_time_str = '2000-01-01 00:00:00'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
lst = np.array(date_time_obj)
for i in range(1, 48) :
    lst = np.append(lst, date_time_obj + timedelta(hours=i))
for d in lst :
    print(str(d))
