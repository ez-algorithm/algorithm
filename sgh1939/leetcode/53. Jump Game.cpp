class Solution {
    bool isZero(vector<int> &v, int start){
        if(find(v.begin()+ start, v.end(), 0) == v.end()) return false;
        return true;
    }
    
public:
    bool canJump(vector<int>& nums) {
        if(!isZero(nums, 0)) return true;
        int lastIdx = nums.size()-1;

        vector<int> visit;
        visit.assign(nums.size(), 0);

        visit[0] = 1;

        for(int i=0; i<nums.size(); i++){
            if(visit[lastIdx] == 1) return true;
            if(visit[i] == 1){
                int tmp = i+1;
                
            for(int j=0; j<nums[i]; j++){
                    // overflow 
                    if(tmp > lastIdx)break;
                   
                    visit[tmp] = 1;
                    tmp++;
                }
            }
        }	

        return false;	
    }

};
