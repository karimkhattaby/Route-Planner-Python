from Route_Planning_Helpers import get_distance
import heapq # used to create a min heap

# A* shortest path implementation.
def shortest_path(M,start,goal):
    # since we always want to keep track of the minimum distance,
    # a min-heap is the perfect data structure choice for this problem
    # the min heap uses total_f distance to keep track of the shortest path, and it also stores
    # the current total cost of the path taken, and a list of nodes in the path
    paths = [ (get_distance(M.intersections[start], M.intersections[goal]), 0, [start]) ]
    # 0 because the starting point has 0 total path so far
    
    # create the heap
    heapq.heapify(paths)
    
    # we keep looping until we find the shortest path to our goal node
    while True:
        # extract the saved total_f distance, current accumulated cost so far, and a list of the nodes in the current path
        total_f, current_cost, current_path = heapq.heappop(paths)
        
        # extract the current node, will always be the last element in the list
        current_node = current_path[-1]
        
        # if the current node popped from the min heap is our goal,
        # it means the current path is the shortest path to the goal node, so we return the path as a list
        if current_node == goal:
            return current_path
        
        # otherwise, we get the list of neighbors/roads of the current node
        neighbors = M.roads[current_node]

        # loop through all the neighbors
        for neighbor in neighbors:
            # calculate the path cost between the current node and the neighbor
            path_cost = get_distance(M.intersections[current_node], M.intersections[neighbor])
            # calculate the heuristic (estimated distanct) between the neighbor and the goal node
            estimated_distance = get_distance(M.intersections[neighbor], M.intersections[goal])
            # calulcate the total_f distance used to keep track of the shortest path in the min-heap
            total_f = current_cost + path_cost + estimated_distance #NOTE: include the cost of the path taken so far

            # push all the information to the heap
            # total_f distance, true path cost from the start until this node, and the list of nodes in this path
            heapq.heappush(paths, (total_f, current_cost+path_cost, current_path+[neighbor]) )
