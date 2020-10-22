import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmb

from bst import BST
from heap import Heap
from os import path

from random import shuffle


class TestGen(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.out_dir = ''

        self.proj_btn = tk.Button(self, text='Project path', command=self.get_output_path)
        self.proj_btn.pack()

        self.treeChoices = ['BST', 'Heap']
        self.trees = {'BST': BST, 'Heap': Heap}

        self.treeTypeVar = tk.StringVar(self)
        self.treeTypeVar.set('BST')
        self.numTrees = tk.StringVar(self)
        self.treeSize = tk.StringVar(self)
        self.includeNull = tk.BooleanVar(self)
        self.saveTraversals = tk.BooleanVar(self)

        treeTypeFrame = tk.Frame(self)
        tk.Label(treeTypeFrame, text='Type of Tree:').pack(side=tk.LEFT)
        treeTypesOptions = tk.OptionMenu(treeTypeFrame, self.treeTypeVar, *self.treeChoices)
        treeTypesOptions.pack(side=tk.LEFT)
        treeTypeFrame.pack()

        optionsFrame = tk.Frame(self)
        tk.Label(optionsFrame, text='Number of trees:').pack(side=tk.LEFT)
        tk.Entry(optionsFrame, textvariable=self.numTrees).pack(side=tk.LEFT)
        tk.Label(optionsFrame, text='Size of Trees:').pack(side=tk.LEFT)
        tk.Entry(optionsFrame, textvariable=self.treeSize).pack(side=tk.LEFT)
        tk.Checkbutton(optionsFrame, text='Include nulls', variable=self.includeNull).pack(side=tk.LEFT)
        tk.Checkbutton(optionsFrame, text='Save Traversals', variable=self.saveTraversals).pack(side=tk.LEFT)


        optionsFrame.pack()

        tk.Button(self, text='Generate Trees', command=self.gen_trees).pack()

        self.pack()

    def get_output_path(self):
        self.out_dir=tkfd.askdirectory(mustexist=True)
        self.proj_btn['text'] = self.out_dir

    def gen_trees(self):
        if self.out_dir == '':
            tkmb.showerror('Path error', 'Must specify an output path')
            return

        try:
            togen = int(self.numTrees.get())
            if togen <= 0:
                raise ValueError()
        except ValueError:
            tkmb.showerror('Value error', "Number of trees must be a positive integer")
            return
        try:
            numelms = int(self.treeSize.get())
            if numelms <= 0 or numelms >= 100:
                raise ValueError()
        except ValueError:
            tkmb.showerror('Value error', "Tree size must be > 0 and <=100")
            return
        donulls = bool(self.includeNull.get())

        vals = list(range(100))
        for i in range(togen):
            shuffle(vals)
            tree = self.trees[self.treeTypeVar.get()](vals[:numelms])
            tree.toPNG(path.join(self.out_dir, '{}{}-null{}'.format(self.treeTypeVar.get(), i, donulls)), donulls)
            if self.saveTraversals.get():
                with open('{}{}-null{}.traversal.txt', 'w') as f:
                    f.write('Preorder: {}\n'.format(','.join(tree.preOrder())))
                    f.write('Inorder: {}\n'.format(','.join(tree.inOrder())))
                    f.write('Postorder: {}\n'.format(','.join(tree.postOrder())))

        tkmb.showinfo('Success', 'Trees generated')


if __name__ == "__main__":
    root = tk.Tk()
    app = TestGen(root)
    app.mainloop()
