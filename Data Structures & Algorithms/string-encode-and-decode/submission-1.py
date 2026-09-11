class Solution:

    def encode(self, strs: List[str]) -> str:
        # kot, psot, lotr
        # 3kot4psot4lotr
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        # first character is len of the first str
        result = []
        i = 0

        while i < len(s):
            idx = s.find("#", i)
            length = int(s[i:idx])

            start = idx + 1
            end = start + length
            result.append(s[start:end])

            i = end
        return result