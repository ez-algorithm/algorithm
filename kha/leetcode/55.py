class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #도달가능한 인덱스인지 체크하기 위한 값
        cnt = 1
        
        for i in range(len(nums)):
            
            #현재 인덱스가 도달할 수 없는 인덱스라면 뒤 인덱스도 도달할 수 없음
            if i >= cnt:
                return False
            
            #도달 가능한 최대 인덱스 구하기
            cnt = max(cnt, i+1+nums[i])
            
            if cnt >= len(nums):
                return True