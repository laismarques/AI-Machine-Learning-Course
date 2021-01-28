people = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'), 
           ('Dublin', 'DUB'), 
           ('Bruxelas', 'BRU'), 
           ('London', 'LHR')]

destination = 'FCO'
flights = {}
for i in open('flights.txt'):
    origin, destination, departure, arrive, price = i.split(',')
    flights.setdefault((origin, destination), [])
    flights[(origin, destination)].append((departure, arrive, int(price)))

#print(flights[('LIS', 'FCO')])

def show_flights(schedule):
    id_flight = -1
    total_price = 0

    for i in range(len(schedule)//2):
        name = people[i][0]
        origin = people[i][1]
        id_flight += 1
        outward_flight = flights[origin, destination][schedule[id_flight]]
        total_price += outward_flight[2]
        id_flight += 1
        flight_back = flights[destination, origin][schedule[id_flight]]
        total_price += flight_back[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (name, origin, outward_flight[0], outward_flight[1], outward_flight[2],
                                                    flight_back[0], flight_back[1], flight_back[2]))
    print('Total Price: ', total_price)
#schedule represents the city and the flight that the person wants, 
# so the first person lives in Lisboa and wants the tird flight of the day. 
schedule = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]
#show_flights(schedule)