def a_star(start ,goal):
    closed_set = set({})
    open_set = set({start})
    came_from = set({})

    g_score[start] = 0
    h_score[start] = heuristic_cost_estimate(start, goal)
    f_score[start] = g_score[start] + h_score[start]

    while(open_set is not {}):
        curr_node = #lowest_f(f_score[start])
        if(curr_node == goal):
            return reconstruct_path(came_from ,came_from[goal])

            open_set.remove(curr_node)
            closed_set.add(curr_node)
            for(next_node in neighbor_nodes(curr_node)):
                if(next_node in closed_set):
                    continue

                tentative_g_score := g_score[x] + dist_between(curr_node ,next_node)

                if(next_node not in open_set):
                    open_set.add(next_node)
                    tentative_is_better = True
                elif(tentative_g_score < g_score[next]):
                    tentative_g_score = False

                if(tentative_is_better):
                    came_from[next_node] = curr_node
                    g_score[next_node] = tentative_g_score
                    h_score[next_node] = heuristic_cost_estimate(next_node ,goal)
                    f_score[next_node] = g_score[next_node] + h_score[next_node]

    return False

def heuristic_cost_estimate(start ,goal):  #game sri

def lowest_f(f_score_node):  #jo

def dist_between(curr_node ,next_node):  #game wan

def reconstruct_path(came_from ,curr_node):
    if(type(came_from[curr_node]) is set):
        path = reconstruct_path(came_from ,came_from[curr_node])
        return (p + curr_node)
    else
        return curr_node
