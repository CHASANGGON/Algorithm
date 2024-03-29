# 풍선팡2 D2
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())

    balloons = [list(map(int,input().split())) for _ in range(N)]
    
    # 델타
    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    # 최댓값을 저장할 변수
    max_total = 0
    
    # 모든위치에서 탐색
    for i in range(N):
        for j in range(M):
            
            # 현재 위치의 값
            total = balloons[i][j]
            
            # 상하좌우로 델타 탐색
            for k in range(4):
                
                # 인덱스 체크
                if 0 <= i + di[k] <= N-1 and 0 <= j + dj[k] <= M-1:
                    total += balloons[i+di[k]][j+dj[k]]
            
            # 최댓값 갱신
            max_total = max(max_total, total)
            
    print(f'#{test_case} {max_total}')