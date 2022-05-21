from queue import PriorityQueue

r, c, k = map(int, input().split())

table = []

for _ in range(3):
    table.append(list(map(int, input().split())))


result = 0

while True:

    row_len = len(table)
    col_len = len(table[0])

    #[r][c]에 들어있는 값이 k인지 확인
    if r-1 < row_len and c-1 < col_len and table[r-1][c-1] == k:
        print(result)
        break

    #열 개수가 행 개수보다 크면 전치
    if col_len > row_len:
        table = list(map(list, zip(*table)))

    for idx in range(len(table)):

        item_list = table[idx]
        #담겨있는 아이템의 중복을 제거
        distinct_list = list(set(item_list))

        priority_que = PriorityQueue()

        for i in range(len(distinct_list)):
            if distinct_list[i] != 0:
                priority_que.put((item_list.count(distinct_list[i]), distinct_list[i]))

        #아이템 개수에 따라 정렬된 결과 리스트 생성
    

        sorted_list = []
        while priority_que.qsize() != 0: 
            temp = priority_que.get()
            sorted_list.append(temp[1])
            sorted_list.append(temp[0])

        #만약 sorted_list의 길이가 100을 넘으면 넘는 원소들은 삭제
        over_size = len(sorted_list) - 100
        for _ in range(over_size):
            sorted_list.pop()

        #기존 리스트를 결과 리스트로 변경
        for i in range(max(len(sorted_list), len(item_list))):
            if len(item_list) <= i:
                item_list.append(sorted_list[i])
            elif len(sorted_list) <= i:
                item_list[i] = 0
            else:
                item_list[i] = sorted_list[i]

    #길이가 맞지 않는 행이 있다면 0으로 채움
    max_len = -1
    for item_list in table:
        max_len = max(max_len, len(item_list))
    for item_list in table:
        diff_size = max_len - len(item_list)
        for _ in range(diff_size):
            item_list.append(0)
    
    #전치된 리스트라면 다시 원복
    if col_len > row_len:
        table = list(map(list, zip(*table)))

    result += 1

    #100초가 지나도 도달할 수 없다면 -1을 출력
    if result > 100:
        print(-1)
        break
    