def a_star(start ,goal): #start = {post_x ,post_y}       goal = {post_x , post_y}
    closed_set = set()
    open_set = set([start]) #ex [ [{'x' : post_x ,'y' : post_y}] ]
    came_from = {}

    '''g_score = [ {str(start[x])) + str(start[y])) : 0 } ]  #ex [ {'15' : 0} ]
    h_score = [ {str(start[x])) + str(start[y])) : heuristic_cost_estimate(start, goal)} ]
    f_score = [ {str(start[x])) + str(start[y])) : g_score(str(start[x])) + str(start[y]))) +
                                                h_score(str(start[x])) + str(start[y])))} ]
                                                '''
    g_score[start] = 0  #ex [ {'15' : 0} ]
    h_score[start] = heuristic_cost_estimate(start, goal)
    f_score[start] = g_score[start] + h_score[start]

    while( len(open_set) > 0 ):
        curr_node = #lowest_f(f_score[start])   guideline https://rosettacode.org/wiki/A*_search_algorithm#Python
        if(curr_node == goal):
            return reconstruct_path(came_from ,came_from[goal])

        open_set.pop(0) #remove curr_node
        closed_set.append(curr_node) #add tail
        neighbor_nodes_list = neighbor_nodes(curr_node) #ex [  {1,5} ,{2,4} ...]

        for(next_node in neighbor_nodes_list): # next_node = [ {... } ]
            '''
                      (x,y+1)
                        |
                        |
           (x-1,y) -- (x,y) -- (x+1,y)
                        |
                        |
                     (x,y-1)
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

            '''if(next_node in closed_set): #
                continue

            tentative_g_score = g_score[curr_node] + dist_between(curr_node ,next_node)

            if(next_node not in open_set):
                open_set.append(next_node)
                tentative_is_better = True
            elif(tentative_g_score < g_score[str(next_node[0][x]) + str(next_node[0][y])]):
                tentative_is_better = True
            else
                tentative_is_better = False

            if(tentative_is_better):
                came_from[next_node] = curr_node
                g_score[next_node] = tentative_g_score
                h_score[next_node] = heuristic_cost_estimate(next_node[0] ,goal)
                f_score[next_node] = g_score[next_node] + h_score[next_node]'''

    return False


def heuristic_cost_estimate(start ,goal):  #game sri
    w = 1.0  # weight of heuristic
    d = w * math.sqrt((start[0] - goal[0])**2 + (start[1] - goal[1])**2)
    return d

def lowest_f(f_score_node):  #jo

def dist_between(curr_node ,next_node):  #game wan
    dist = abs(curr_node[0] - next_node[0]) + abs(curr_node[1] - next_node[1])
    return dist

def neighbor_nodes(curr_node): # game wan
    n = { curr_node[0] ,curr_node[1]+1 }
    e = { curr_node[0]+1 ,curr_node[1] }
    s = { curr_node[0] ,curr_node[1]-1 }
    w = { curr_node[0]-1 ,curr_node[1] }
    return [ n ,e ,s ,w]

def reconstruct_path(came_from ,curr_node):
    if(type(came_from[curr_node]) is set):
        path = reconstruct_path(came_from ,came_from[curr_node])
        return (p + curr_node)
    else
        return curr_node
