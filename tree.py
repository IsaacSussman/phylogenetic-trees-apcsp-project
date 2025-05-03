from __future__ import annotations
import matplotlib
import matplotlib.axes
import matplotlib.pyplot
class Node:
    def __init__(self, left:Node, right:Node, animal:str, parent:Node):
        self.left = left
        self.right = right
        self.parent = parent
        self.animal = animal
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
        self.score = None
        self.pair = None
        self.point = None
        self.order =  -1

    def set_values(self, left:Node, right:Node, animal:str, parent:Node):
        self.left = left
        self.right = right
        self.parent = parent
        self.animal = animal
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def inorder(self, root = False):
        l = []
        if self.left:
            l.extend(self.left.inorder())
        l.append(self)
        if self.right:
            l.extend(self.right.inorder())
        if not root:
            return l
        else:
            for i in range(len(l)):
                l[i].order = i
            return l


    def all_leaves(self):
        l = []
        if not self.left and not self.right:
            return [self.animal]
        elif not self.right:
            l.extend(self.left.all_leaves())
        elif not self.left:
            l.extend(self.right.all_leaves()) 
        else:
            l.extend(self.right.all_leaves())
            l.extend(self.left.all_leaves())
        return l
    
    def __str__(self):
        return f"[{self.left} --{self.animal}-- {self.right}]"
    
    @staticmethod
    def cluster(left, right, score, pairs):
        l = left
        while l.parent:
            l = l.parent
        r = right
        while r.parent:
            r = r.parent
        if l == r:
            return None
        n = Node(l, r, None, None)
        n.score = score
        n.pair = pairs
        return n
    
    def points(self, leaves_order, base):
        l = []

        if not (self.left or self.right):
            self.point = (base,self.order)
            return l
        l.append((self.score,self.order))
        self.point = (self.score,self.order)
        if self.left:
            l.extend(self.left.points(leaves_order, base))
        if self.right:
            l.extend(self.right.points(leaves_order, base))
        return l

    def draw_lines(self, x1:list = [], y1:list = []):
        x = x1.copy()
        y = y1.copy()
        if self.left == None and self.right == None:
            return x, y
        if self.left:
            x.append((self.point[0], self.left.point[0]))
            y.append((self.point[1], self.left.point[1]))
            l = self.left.draw_lines()
            x.extend(l[0])
            y.extend(l[1])
        if self.right:
            x.append((self.point[0], self.right.point[0]))
            y.append((self.point[1], self.right.point[1]))
            r = self.right.draw_lines()
            x.extend(r[0])
            y.extend(r[1])
        
        
        return x, y
        

            
    
    
    
