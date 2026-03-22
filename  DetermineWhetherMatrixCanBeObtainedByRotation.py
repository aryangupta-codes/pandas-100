class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False

if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 1], [1, 0]]
    target = [[1, 0], [0, 1]]
    print(sol.findRotation(mat, target))