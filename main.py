import datetime
import random
import math
import pandas as pd

from config import CONFIG


# print (CONFIG['nature_stats'])

# x = [random.randint(0, 9) for p in range(0, 10)]
# print(x)

# print(random.randrange(4, 8))


# sampleList = [10, 20, 30, 40]
# print(random.choice(sampleList))


# numberList = [111, 222, 333, 444, 555]
# print(random.choices(numberList, weights=(10, 20, 30, 40, 50), k=5))

# destinations = list(CONFIG['dest_stats'].keys())
# dest_probs = list(CONFIG['dest_stats'].values())

# # print(destinations)
# # print()
# # print(dest_probs)
# print( random.choices(destinations, weights=dest_probs, k=100) )

df = pd.DataFrame(columns=['ArrFlight', 'ACType', 'bookload', 'STD', 'ATA', 'ArrRoute', 'DepRoute'])

total_records = random.randrange(int(CONFIG['total_records']*0.9), int(CONFIG['total_records']*1.1))
months = math.ceil(total_records / CONFIG['average_per_month'])
# print(records, months)

recs = 0

while recs < total_records:

    arrFlight = 

    recs += 1
    pass



