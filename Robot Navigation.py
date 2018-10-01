def a_star(start ,goal): #start = {post_x ,post_y}       goal = {post_x , post_y}
    closed_set = set()
    open_set = set([start]) #ex [ [post_x ,post_y}] ]
    came_from = {}

    g_score = {}
    h_score = {}
    f_score = {}

    g_score[start] = 0  #ex [ {(0 ,0) : 0} ]   dist start to pos
    h_score[start] = heuristic_cost_estimate(start, goal)
    f_score[start] = g_score[start] + h_score[start] #dist pos to goal

    while( len(open_set) > 0 ):
        curr_node = set()
        curr_f_score = 0

        '''print("came_from ",came_from)
        print("open_set " ,open_set)
        print("f_score " ,f_score)'''
        for pos in open_set:
            print("positon = ",pos ,": f_score = " ,f_score[pos])
            if (curr_node == set() or f_score[pos] < curr_f_score):
                curr_f_score = f_score[pos]
                curr_node = pos

        print("\nmin f_score = ",curr_node ,": f_score = ",f_score[curr_node])

        #lowest_f(f_score[start])   guideline https://rosettacode.org/wiki/A*_search_algorithm#Python
        if(curr_node == goal):
            print("GOAL!!")
            #return reconstruct_path(came_from ,came_from[goal])
            path = [curr_node]
            while( curr_node in came_from):
                print("curr_node = ",curr_node,": came_from ", came_from[curr_node])
                curr_node = came_from[curr_node]
                path.append(curr_node)
            path.reverse()
            return path ,f_score[goal]


        open_set.remove(curr_node) #remove curr_node
        closed_set.add(curr_node) #add tail
        neighbor_nodes_list = neighbor_nodes(curr_node ,start ,goal) #ex [  {1,5} ,{2,4} ...]

        for next_node in neighbor_nodes_list : # next_node = [ {... } ]
            '''
          (x-1,y+1)  (x,y+1)  (x+1,y+1)
                  \     |    /
                    \   |  /
           (x-1,y) -- (x,y) -- (x+1,y)
                    /   |  \
                  /     |    \
          (x-1,y-1)  (x,y-1)   (x+1,y-1)
            '''

            if(next_node in closed_set):
                continue #We have already processed this node exhaustively

            tentative_g_score = g_score[curr_node] + dist_between(curr_node ,next_node)

            if( next_node not in open_set):
                open_set.add(next_node) #Discovered a new vertex
            elif(tentative_g_score >= g_score[next_node]):
                continue #This G score is worse than previously found

			#Adopt this G score
            came_from[next_node] = curr_node
            g_score[next_node] = tentative_g_score
            h_score[next_node] = heuristic_cost_estimate(next_node ,goal)
            f_score[next_node] = g_score[next_node] + h_score[next_node]


    return "canot"


def heuristic_cost_estimate(start ,goal):  #game sri
    D = 1
    D2 = 1
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def dist_between(curr_node ,next_node):  #game wan

    #dist = abs(curr_node[0] - next_node[0]) + abs(curr_node[1] - next_node[1])
    return 1

def neighbor_nodes(pos,start,goal): # game wan

    '''n = ( curr_node[0] ,curr_node[1]+1 )
    e = ( curr_node[0]+1 ,curr_node[1] )
    s = ( curr_node[0] ,curr_node[1]-1 )
    w = ( curr_node[0]-1 ,curr_node[1] )
    return [ n ,e ,s ,w]'''
    n = []
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
    #for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        x2 = pos[0] + dx
        y2 = pos[1] + dy
        '''if x2 < start[0] or x2 > goal[0] or y2 < start[1] or y2 > goal[1]:
            continue'''
        n.append((x2, y2))
    return n

start = (int(input("start_x = ")) ,int(input("start_y = ")))
goal = (int(input("goal_x = ")) ,int(input("goal_y = ")))

path ,cost = a_star(start ,goal)
print("path " ,path )
print("cost ",cost)

#https://rosettacode.org/wiki/A*_search_algorithm#Python
