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

# last_date = datetime.datetime.strptime(CONFIG['last_date'], '%y-%m-%d %H:%M:%S')
last_date = datetime.datetime.fromisoformat(CONFIG['last_date'])
records_time_diff = CONFIG['average_per_month'] / 30 / 24 * 60  # mins
last_count = 0


while recs < total_records:

    airlines = list(CONFIG['airlines_stats'].keys())
    airlines_probs = list(CONFIG['airlines_stats'].values())
    randFlights = random.choices(airlines, weights=airlines_probs, k=2)

    arrFlight = randFlights[0] + random.choice(list(CONFIG['airlines_flightnums'][randFlights[0]]))
    depFlight = randFlights[1] + random.choice(list(CONFIG['airlines_flightnums'][randFlights[1]]))

    ACType = random.choice(CONFIG['ACType'])

    pax = list(CONFIG['PAXBookLoad_stats'].keys())
    pax_probs = list(CONFIG['PAXBookLoad_stats'].values())
    bookload = random.choices(pax, weights=pax_probs, k=1)[0]

    dests = list(CONFIG['dest_stats'].keys())
    dests_probs = list(CONFIG['dest_stats'].values())
    routes = random.choices(dests, weights=dests_probs, k=2)

    time1 = random.choice( range(int(records_time_diff)) )
    last_date -= datetime.timedelta(minutes=time1) + datetime.timedelta(seconds=random.choice( range(59) ))
    sta_time = last_date
    # print(last_date, time1)

    delay_mins = random.choice( range(-99, 99) )
    ata_time = sta_time + datetime.timedelta(minutes=delay_mins) + datetime.timedelta(seconds=random.choice( range(59) ))

    # print(arrFlight, depFlight, ACType, bookload, route, sta_time, ata_time)
    df.loc[len(df.index)] = [arrFlight, ACType, bookload, sta_time, ata_time, routes[0], routes[1]]

    recs += 1

print(df)
df.to_csv('flights.csv')
    


