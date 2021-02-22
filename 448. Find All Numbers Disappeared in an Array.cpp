class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result;
        int newind;
        for (int i = 0; i < nums.size(); i++) {
            newind = abs(nums[i]) - 1;
            if (nums[newind] > 0)
                nums[newind] *= -1;
        }
        
        for (int i = 1; i < nums.size()+1; i++) {
            if (nums.at(i-1) > 0) result.push_back(i);
        }
        
        return result;
    }
};
