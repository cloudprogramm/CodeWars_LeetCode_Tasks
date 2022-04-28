class Solution:

    def digitSum(self, s: str, k: int) -> str:
        if s == "1" or k >= len(s):
            return s

        groups = self.division_into_groups(s, k)
        string_res = self.concat_list(groups)

        while len(string_res) > k:
            groups = self.division_into_groups(string_res, k)
            string_res = self.concat_list(groups)
        return string_res

    @staticmethod
    def division_into_groups(s: str, k: int) -> list:
        results = []
        starts = 0
        ends = k

        while True:
            results.append(s[starts:ends])
            if ends == len(s):
                break

            starts += k
            ends += k

            if ends > len(s):
                ends = len(s)
        return results

    @staticmethod
    def concat_list(groups: list) -> str:
        string_res = ""

        for i, value in enumerate(groups):
            temp = 0

            for j in value:
                temp += int(j)

            string_res += str(temp)
        return string_res
