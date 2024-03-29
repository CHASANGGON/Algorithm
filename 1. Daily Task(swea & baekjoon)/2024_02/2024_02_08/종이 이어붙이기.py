T = int(input())

for test_case in range(1,T+1):
    n = int(input())//10
    first, second = 1, 3

    if n == 1:
        cnt = first
    elif n == 2:
        cnt = second
    else:
        for i in range(n-2):
            first, second = second, second + first*2
        cnt = second
    print(f'#{test_case} {cnt}')

# 이런 문제는 수의 규칙을 찾으라는 문제에요
# 그냥 규칙을 찾을 수 있게 적당히 네 번째나 다섯 번째까지 직접 그려서 개수를 세어보고,
# 그 수들에서 규칙을 찾아야 해요
# 그런데 수를 셀 때 실수하지 않게 조심하세요ㅠ 실수하면 규칙을 절대 못 찾으니까요..
    
# 저는 다섯 개 까지 나열해봤는데, 1 3 5 11 21 이 나왔어요.
# 5 = 3 + 1*2
# 11 = 5 + 3*2
# 이걸 for 문으로 풀어도 되고, 재귀함수로 풀어도 되고 상관없어요
# 저는 그냥 for 문으로 풀었어요
# 그냥 두드리다 보면 나오는 거 같아요..
# 그리고 어차피 백준에서도 그렇고 여러가지 문제들 풀다보면 수학과 연관이 있어서 그런지
# 여러 가지 규칙을 가진 수열들을 많이 접하게 돼서, 몇 번 접하다 보면 충분히 풀 수 있을 거라고 생각해요 화이팅