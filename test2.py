class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stark = []
        self.min_val = float('inf')

    def push(self, x: int) -> None:
        self.stark.append(x)
        if x < self.min_val:
            self.min_val = x

    def pop(self) -> None:
        res = self.stark.pop()
        if res == self.min_val:
            new_min = float('inf')
            for num in self.stark:
                if num < new_min:
                    new_min = num
            self.min_val = new_min

    def top(self) -> int:
        return self.stark[-1]

    def getMin(self) -> int:
        return self.min_val

import sys
if __name__ == "__main__":
    # 读取第一行的n
    stack = MinStack()
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        opr = list(line.split())
        if opr[0] == "push":
            stack.push(int(opr[1]))
        elif opr[0] == "pop":
            stack.pop()
        elif opr[0] == "getMin":
            print(stack.getMin())
