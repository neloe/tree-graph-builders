import networkx as nx
from collections import defaultdict

class BT:
    def __init__(self):
        self.tree = defaultdict(lambda: [None, None])
        self.root = None
        self.dy = .5

    def toDigraph(self, addnulls = False):
        graph = nx.DiGraph()
        nullct = 0
        for n in list(self.tree.keys()):
            #print(n)
            if self.tree[n][0]:
                graph.add_edge(n, self.tree[n][0])
                if not n in self.tree:
                    l = 'nulll' + str(nullct)
                    nullct+=1
                    r = 'nullr' + str(nullct)
                    nullct+=1
                    self.tree[n] = [l,r]
            elif addnulls:
                graph.add_edge(n, 'nulll'+str(nullct))
                self.tree[n][0] = 'nulll'+str(nullct)
                nullct += 1
            if self.tree[n][1]:
                graph.add_edge(n, self.tree[n][1])
            elif addnulls:
                graph.add_edge(n, 'nullr' + str(nullct))
                self.tree[n][1] = 'nullr' + str(nullct)
                nullct += 1
        return graph

    def height(self):
        return self._height(self.root)

    def _height(self, n):
        if not n or str(n).startswith('null'):
            return -1
        return 1 + max(self._height(self.tree[n][0]), self._height(self.tree[n][1]))

    def nodePos(self, includeNulls = False):
        pos = dict()
        parents = dict()
        levels = dict()
        for n in self.tree:
            for c in self.tree[n]:
                if c:
                    parents[c] = n;

        tovisit = [self.root]
        treeheight = self.height() + includeNulls
        while len(tovisit) > 0:
            n = tovisit.pop()
            tovisit.extend([x for x in self.tree[n] if x])
            if n == self.root:
                pos[n] = (0,0)
                levels[n] = 0
            else:
                ppos = pos[parents[n]]
                levels[n] = 1 + levels[parents[n]]
                dx = (2 ** (treeheight-levels[n])) / 2
                if not str(n).startswith('nullr'):
                    if str(n).startswith('nulll') or n < parents[n]:
                        dx *= -1
                pos[n] = (ppos[0]+dx, ppos[1] - self.dy)
        return pos

    def toPNG(self, filename, withNulls = False):
        import networkx as nx
        import matplotlib.pyplot as plt
        g = self.toDigraph(withNulls)
        labels = {x: x for x in g.nodes}
        for x in g.nodes:
            if str(x).startswith('null'):
                labels[x] = '\u2205'
        nx.draw(g, labels=labels, pos=self.nodePos(withNulls), node_color='w')
        plt.tight_layout()
        plt.savefig('{}.png'.format(filename))
        plt.clf()





