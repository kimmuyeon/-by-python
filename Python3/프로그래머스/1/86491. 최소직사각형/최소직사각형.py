def solution(sizes):
    # sizes = [[60, 50],[30, 70],...]
    
    # 각 명함의 가로,세로 중 긴 것들을 구하기 (그 중에서 가장 긴놈 구하기)
    # 각 명함의 가로,세로 중 짧은 것들을 구하기 (그 중에서 가장 긴놈 구하기)
    big = []
    small = []
    for i in sizes:
        if i[0] >= i[1]:
            big.append(i[0])
            small.append(i[1])
        else:
            big.append(i[1])
            small.append(i[0])

    answer = max(big) * max(small)
    return answer