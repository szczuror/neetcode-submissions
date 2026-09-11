class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> my_set;
        for(const auto& num : nums) {
            auto res = my_set.insert(num);
            if (!res.second) {
                return true;
            }
        }
        return false;
    }
};