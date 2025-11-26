def solution(numbers):
    # numbers 반복 후에 가장 큰 수가 있는 수 찾기
    nums = []
    for i in numbers:
        nums.append(str(i))
        
    # nums에 있는 문자열들 3번씩 반복하여 내림차순 정렬 (중요)#
    nums.sort(key=lambda x : x*3 , reverse=True)
    
    # join을 활용하여 붙이기 
    answer = ''.join(nums)
    
    # 0일때는 0 출력
    if answer[0] == '0':
        return '0'
    
    return answer