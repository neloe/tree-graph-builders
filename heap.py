from bt import BT
from heapq import heapify, heappush

class Heap(BT):
    def __init__(self, data = []):
        super().__init__()
        self.heap = data[:]
        heapify(self.heap)
        self._updateTree()

    def insert(self, value):
        heappush(self.heap, value)
        self._updateTree()

    def _updateTree(self):
        self.root = self.heap[0]
        self.tree.clear()
        for i,v in enumerate(self.heap):
            self.tree[v] = [None, None]
            if 2*i+1 < len(self.heap):
                self.tree[v][0] = self.heap[2*i+1]
            if 2*i+2 < len(self.heap):
                self.tree[v][1] = self.heap[2*i+2]