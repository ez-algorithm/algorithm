import collections

t = int(input())

for _ in range(t):
    shop_cnt = int(input())
    start_x, start_y = map(int, input().split())

    shop_list = []
    for _ in range(shop_cnt):
        templist = list(map(int, input().split()))
        templist.append(0)
        shop_list.append(templist)
    
    end_x, end_y = map(int, input().split())

    ### 편의점과 페스티벌 좌표 탐색을 위한 BFS ###

    myq = collections.deque()
    myq.append([start_x, start_y])
    is_finish = False

    while myq:

        cur_x, cur_y = myq.popleft()

        #이동 가능한 범위 내에 페스티벌 좌표가 있으면 happy
        if 1000 >= (abs(cur_x-end_x) + abs(cur_y-end_y)):
            is_finish = True
            break

        #이동 가능한 범위 내의 편의점이 있다면 enque
        for k in range(len(shop_list)):
            if shop_list[k][2] == 0 and 1000 >= (abs(cur_x-shop_list[k][0]) + abs(cur_y-shop_list[k][1])):
                shop_list[k][2] = 1
                myq.append([shop_list[k][0], shop_list[k][1]])

    if not(is_finish):
        print("sad")
    else:
        print("happy")


        

