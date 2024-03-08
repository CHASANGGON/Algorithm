# m명의 친구
# n * n 크기의 격자 모양 나무
# 각 나무마다 가능한 열매 수확량
# 서로 다른 위치에서 출발
# 1초에 1칸씩 상하좌우 인접한 칸 -> dfs
# 최종적으로 모든 열매 수확량의 합을 최대
# 열매를 수확하는데 걸리는 시간은 0초
# 여러 친구가 방문하게 되더라도 열매는 딱 한 번만 수확
# 친구들끼리 이동하는 도중 만나게 되는 것 역시 가능
# m명의 친구들이 3초 동안 최대로 얻을 수 있는 열매 수확량의 총 합

# 인덱스 검사
def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < N

# 좌표, 경로, 수확량, 탐색 깊이
def P(i, j, S, D):
    global max_path
    global max_S
    # 기저 조건
    if D == 3:
        if S > max_S:
            max_S = S # 최대 수확량 갱신
            max_path = copy.deepcopy(path)  # 최대 수확량 경로 갱신
            
    else:
        # 방문 체크
        V[i][j] = 0
        
        # 네 방향 완전 탐색 -> 중복 허용 순열
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 검사
            if in_range(ni,nj) and V[ni][nj]:
                path.append([ni,nj]) # 경로 추가 후 재귀 호출
                P(ni, nj, S+arr[ni][nj], D+1)
                path.pop() # 복구
        # 방문 복구
        V[i][j] = 1

import copy
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

m_lst = []
for _ in range(M):
    m_lst.append(list(map(int,input().split())))
    
# 탐색에 필요한 것들
V = [[1]*N for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
s = 0
for i,j in m_lst:
    i -= 1
    j -= 1
    max_S = 0
    path = [[i,j]]
    max_path = []
    # 좌표, 경로, 수확량, 탐색 깊이
    P(i, j, arr[i][j], 0)
    for i, j in max_path:
        s += arr[i][j]
        arr[i][j] = 0
        
print(s)