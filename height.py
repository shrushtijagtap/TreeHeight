#python3
import queue
import sys

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
            nodes = [Node(i) for i in range(self.n)]
            for i in range(self.n):
                if self.parent[i] == -1:
                    self.root = nodes[i]
                else:
                    nodes[self.parent[i]].addChild(nodes[i])
            q = queue.Queue()
            q.put(self.root)
            height = 0
            while(not q.empty()):
                size = q.qsize()
                if size > 0:
                    height = height + 1
                for j in range(size):
                    item = q.get()
                    for i in item.children:
                        q.put(i)
            return height


if __name__ == '__main__':
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())
