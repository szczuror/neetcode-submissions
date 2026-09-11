class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> numbersMap;
        for(int num : nums){
            numbersMap[num]++;
        }
        std::vector<std::vector<int>> buckets(nums.size() + 1);
        for(const auto& [num, freq] : numbersMap) {
            buckets[freq].push_back(num);
        }
        
        std::vector<int> result;
        for (int i = nums.size(); i >= 0 && result.size() < k; i--) {
            if (!buckets[i].empty()) {
                for (int num : buckets[i]) {
                    result.push_back(num);
                    if (result.size() == k) {
                        return result;
                    }
                }
            }
        }

        return result;
    }
};
