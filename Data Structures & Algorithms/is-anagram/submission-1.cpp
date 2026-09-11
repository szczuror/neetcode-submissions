class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.length() != t.length()) {
            return false;
        }

        // std::unordered_map<char, int> sMap;
        // std::unordered_map<char, int> tMap;

        // for (char c : s) {
        //     sMap[c]++;
        // }
        // for(char c : t) {
        //     tMap[c]++;
        // }

        // return sMap == tMap;
        int count[26] = {0};
        for (int i = 0; i < s.length(); ++i) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
};
