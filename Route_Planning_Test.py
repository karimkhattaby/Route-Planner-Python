from Route_Planning_Helpers import Map, intersections, roads
from Shortest_Path import shortest_path

M = Map(intersections, roads)
print(shortest_path(M, 5, 34))
#[5, 16, 37, 12, 34]

print(shortest_path(M, 5, 5))
#5

print(shortest_path(M, 8, 24))
#[8, 14, 16, 37, 12, 17, 10, 24]