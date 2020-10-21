from bt import BT


class BST(BT):
    def __init__(self, data = []):
        super().__init__()
        for d in data:
            self.insert(d)

    def insert(self, data):
        if not self.root:
            self.root = data
            return
        n = self.root
        while (data < n and self.tree[n][0]) or (data > n and self.tree[n][1]):
            if data < n:
                n = self.tree[n][0]
            else:
                n = self.tree[n][1]
        if data < n:
            self.tree[n][0] = data
        else:
            self.tree[n][1] = data
        self.tree[data] = [None, None]


if __name__ == "__main__":

    from random import shuffle
    vals = list(range(100))
    shuffle(vals)
    t = BST(vals[:6])
    t.toPNG('test2', True)
    '''
    for i in range(10):
        t.insert(vals[i])
    print(t.tree)
    g = t.toDigraph()
    print(g.nodes)
    print(t.height())
    import networkx as nx
    import matplotlib.pyplot as plt
    labels = {x:x for x in g.nodes}
    for x in g.nodes:
        if str(x).startswith('null'):
            labels[x] = '\u2205'
    print(t.nodePos())
    nx.draw(g, labels=labels, pos=t.nodePos(), node_color='w')
    plt.tight_layout()
    plt.savefig('test.png')
    '''
