from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        pascal_triangle = [[number] for number in range(num_rows)]
        # pascal_triangle.append()
        print(pascal_triangle)

if __name__ == "__main__":
    a = Solution()
    print(a.generate(5))
