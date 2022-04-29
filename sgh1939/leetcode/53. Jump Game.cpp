class Solution {
    bool isZero(vector<int> &v, int start){
        if(find(v.begin()+ start, v.end(), 0) == v.end()) return false;
        return true;
    }
    
public:
    bool canJump(vector<int>& nums) {
        if(!isZero(nums, 0)) return true;
        int lastIdx = nums.size()-1;


        t[0] = 1;

        for(int i=0; i<nums.size(); i++){

                    tmp++;
                }
            }
        }	

        return false;	
    }

};
