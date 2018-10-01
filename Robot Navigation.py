def a_star(start ,goal ,barriers): # function a_star
    closed_set = set() #เซตของโหนดที่พิจารณาแล้ว
    open_set = set([start]) #เซตของโหนดที่ยังไม่ได้พิจารณา เริ่มด้วยใส่โหนดเริ่มต้นลงไป
    came_from = {}  #เพื่อหาโหนดที่ผ่านมา ซึ่งจะใช้ในการระบุเส้นทาง

    g_score = {}
    h_score = {}
    f_score = {}

    g_score[start] = 0  #ค่าระยะทางของจุดเริ่มต้น
    h_score[start] = heuristic_cost_estimate(start, goal) #เป็นฟังก์ชันที่ใช้หาค่าประมาณฮิวริสติก
    f_score[start] = g_score[start] + h_score[start] #ค่าประมาณการของจุดเริ่มไปยังจุดเป้าหมาย

    while( len(open_set) > 0 ): #ถ้า open_set ไม่มี node แล้วจะหยุด
        curr_node = set() #node ปัจจุบัน
        curr_f_score = 0 #ค่า f_score node ปัจจุบัน

        for pos in open_set: #เอา node ที่ยังไม่ได้พิจารณา จาก open_set
            print("position = ",pos ,": f_score = " ,f_score[pos])#พิมพ์ ตำแหน่ง และ f_score
            if (curr_node == set() or f_score[pos] < curr_f_score):#ถ้า node ปัจจุบันว่าง หรือ มีf_score ตำแน่งอื่นน้องกว่า f_scoreปัจจุบัน
                curr_f_score = f_score[pos]#เปลี่ยนค่า f_score
                curr_node = pos #เปลี่ยนnode ปัจจุบัน ให้เป็นnodeที่มี f_score น้อยกว่า

        print("\nmin f_score = ",curr_node ,": f_score = ",f_score[curr_node]) #พิมพ์ ตำแหน่ง และ f_score ที่น้อยที่สุด

        if(curr_node == goal):#ถ้าnode ปัจจุบันมีตำแหน่งเท่ากับgoalแล้ว จะหยุดทำงาน
            print("GOAL!!")
            path = [curr_node]#เก็บpath ที่start เดินไปถึง goal
            while( curr_node in came_from):#เอา node ก่อนหน้า node ปัจจุบัน
                print("curr_node = ",curr_node,": came_from ", came_from[curr_node]) #พิมพ์ node ปัจจุบัน และ node ก่อนหน้า
                curr_node = came_from[curr_node] #ให้node ปัจจุบัน เป็นnodeก่อนหน้า
                path.append(curr_node) #นำตำแหน่งไปเก็บในpath
            path.reverse() #สลับหน้าหลัง
            return path ,f_score[goal] #return path กับ cost


        open_set.remove(curr_node) #remove node ปัจจุบันใน open_set เพราะ เรากำลังเอามาพิจารณา
        closed_set.add(curr_node) #add node ปัจจุบันใน open_set
        neighbor_nodes_list = neighbor_nodes(curr_node) #list ตำแหน่งรอบๆ

        for next_node in neighbor_nodes_list : # พิจารณา node ถัดไปจาก ตำแหน่งรอบๆ
            '''
          (x-1,y+1)  (x,y+1)  (x+1,y+1)
                  \     |    /
                    \   |  /
           (x-1,y) -- (x,y) -- (x+1,y)
                    /   |  \
                  /     |    \
          (x-1,y-1)  (x,y-1)   (x+1,y-1)
            '''

            if(next_node in closed_set): #ตำแหน่ง ของ node ถัดไปอยุ่ใน node ที่พิจารณาแล้ว จะเอาnode ใหม่
                continue #We have already processed this node exhaustively

            tentative_g_score = g_score[curr_node] + dist_between(next_node ,barriers)
            #g_score ที่คาด = node ปัจจุบัน + cost ของnode ถัดไป

            if( next_node not in open_set):#ถ้า node ถัดไป ไม่ได้อยู่ใน เซตของโหนดที่ยังไม่ได้พิจารณา จะเอามาใส่
                open_set.add(next_node) #Discovered a new vertex
            elif(tentative_g_score >= g_score[next_node]): #แล้วถ้า g_score ที่คาด >= g_score ของ node ถัดไป จะเอาnode ใหม่
                continue #This G score is worse than previously found

			#Adopt this G score
            came_from[next_node] = curr_node#เพิ่ม node ถัดไป ใน came_from และบอกว่ามาจาก nodeไหน
            g_score[next_node] = tentative_g_score
            h_score[next_node] = heuristic_cost_estimate(next_node ,goal)
            f_score[next_node] = g_score[next_node] + h_score[next_node]


    return "canot find" ,"." #ถ้าไปถึงgoalไม่ได้


def heuristic_cost_estimate(start ,goal):
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    return (dx + dy) # H(s,g) = |xs-xg| + |ys-yg|

def dist_between(next_node ,barriers):
    for barrier in barriers :
        if(next_node in barrier):   #ถ้า next_node ชน barrier จะreturn ค่ามากๆ
            return 1000
    return 1 #ถ้าไม่ชน จะreturn1

def neighbor_nodes(pos):
    n = []

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]: #หา ตำแหน่ง ของ next_node
        x2 = pos[0] + dx
        y2 = pos[1] + dy
        n.append((x2, y2))
    return n

start = (int(input("start_x = ")) ,int(input("start_y = ")))
goal = (int(input("goal_x = ")) ,int(input("goal_y = ")))

barriers = []
barriers.append([(3,3) ,(4,3) ,(5,3) ,(6,3),
                                      (6,2),
                                      (6,1)])

''' ex
    x = barrier
    s = (3,1)
    g = (5,4)
    P = path

    5| . . . . . . .
    4| . . . . g . .
    3| . . x x x x .
    2| . . . . . x .
    1| . . s . . x .
     |______________
    0  1 2 3 4 5 6 7

    |
    |
    v

    5| . . . . . . .
    4| . . P P g . .
    3| . P x x x x .
    2| . . P . . x .
    1| . . s . . x .
     |______________
    0  1 2 3 4 5 6 7

'''
path ,cost = a_star(start ,goal ,barriers)

print("path " ,path )
print("cost ",cost)

#https://rosettacode.org/wiki/A*_search_algorithm#Python
