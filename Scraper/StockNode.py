"""Stores relevant values on each company"""

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.prevClose = ""
        self.open = ""
        self.bid = ""
        self.ask = ""
        self.dayRange = ""
        self.yearRange = ""
        self.volume = 0
        self.beta = 0
        self.PE = 0
        self.marketCap = 0
        self.EPS = 0
        self.forwardDivAndYield = ""
        self.exDivDate = ""
        self.industry = ""

        self.left = None
        self.right = None
        
    def sort(self) -> list:  # returns a list of names
        return self.sort_r([])

    def sort_r(self, currList) -> list:  # sorts via bst structure
        if self.left is not None:
            self.left.sort_r(currList)
        currList.append(self)
        if self.right is not None:
            self.right.sort_r(currList)
        return currList

    def display(self, file) -> None:  # displays the tree under a given node
        f = open(file, "w")
        lines, *_ = self.display_r()
        for line in lines:
            f.write(line)
            f.write('\n')
        f.close()

    def display_r(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.name
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_r()
            s = '%s' % self.name
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_r()
            s = '%s' % self.name
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_r()
        right, m, q, y = self.right.display_r()
        s = '%s' % self.name
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def killAllChildren(self):  # recursively removes pointers to all children
        if self.left is not None:
            self.left.killAllChildren()
            self.left = None
        if self.right is not None:
            self.right.killAllChildren()
            self.right = None
        
        