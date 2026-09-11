class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // only one valid answer
        std::unordered_map<int, int> mymap;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            // if diff is already in map then return them.
            if (mymap.find(diff) != mymap.end()) {
                return {mymap[diff], i};
            }

            mymap[nums[i]] = i;
        }

        return {};
    }
};
