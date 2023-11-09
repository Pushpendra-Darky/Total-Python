'''
from collections import deque

cities_list = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])

cities_list.appendleft("New York")
cities_list.appendleft("Los Angeles")

print(cities_list)

leftmost_city = cities_list.popleft()
print("Removed from the left:", leftmost_city)

print(cities_list)
'''

from collections import deque
cities_list = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])
