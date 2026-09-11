class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> groups;

        for(const auto& str : strs) {
            std::string key(26, 0);
            for (char c : str) {
                key[c - 'a'] ++;
            }
            groups[key].push_back(str);
        }

        std::vector<std::vector<std::string>> result;
        result.reserve(groups.size());
        for (auto& [key, value] : groups){
            result.push_back(value);
        }

        return result;
    }
};
