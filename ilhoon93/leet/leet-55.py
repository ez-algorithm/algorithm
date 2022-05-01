class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        if n ==1 :
            return True
        
        # 마지막 인덱스는 제외
        for i in range(n-1):
            
            if nums[i] == 0:
                # 0이 여러개 붙어있으면 맨 마지막 0의 인덱스로 이동
                if nums[i+1] == 0:
                    continue
                
                # 현재 0을 건너뛸수 있는 인덱스가 있는지 탐색
                r = i-1
                flag = False
                
                while r >= 0:
                    
                    if r + nums[r] >= i+1:
                        flag = True
                        break
                    r -= 1
                if flag == True:
                    continue
                else:
                    break
            if nums[i] >= (n-1-i):
                return True
        
        return False
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
