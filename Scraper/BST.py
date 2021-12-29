"""Creates a binary search tree based on market cap, beta, PE, EPS, or volume"""

# from StockNode import Node

class Tree():
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def insert(self, node, val) -> None:  # default insert by market cap
        if val == "market cap":
            self.insert_MC(node)
        elif val == "pe":
            self.insert_PE(node)
        elif val == "eps":
            self.insert_EPS(node)
        elif val == "beta":
            self.insert_beta(node)
        else:
            self.insert_volume(node)
    
    def sort(self) -> list:  # returns a list of names
        return self.root.sort()

    def display(self, txtFile) -> None:  # sends call to the root node
        if self.root is None:
            return
        self.root.display(txtFile)

    def insert_MC(self, node) -> None:  # inserts node into tree based on market cap
        self.size += 1
        if self.root is None:
            self.root = node
            return
        else:
            self.insert_MC_r(self.root, node)
    
    def insert_MC_r(self, prior, node) -> None:
        try:
            if node.marketCap > prior.marketCap:
                if prior.right is None:
                    prior.right = node
                    return
                self.insert_MC_r(prior.right, node)
            elif node.marketCap < prior.marketCap:
                if prior.left is None:
                    prior.left = node
                    return
                self.insert_MC_r(prior.left, node)
        except:
            return
        
    def insert_volume(self, node) -> None:  # inserts node into tree based on volume
        self.size += 1
        if self.root is None:
            self.root = node
            return
        else:
            self.insert_volume_r(self.root, node)
    
    def insert_volume_r(self, prior, node) -> None:
        try:
            if node.volume > prior.volume:
                if prior.right is None:
                    prior.right = node
                    return
                self.insert_volume_r(prior.right, node)
            elif node.volume < prior.volume:
                if prior.left is None:
                    prior.left = node
                    return
                self.insert_volume_r(prior.left, node)
        except:
            return

    def insert_beta(self, node) -> None:  # inserts node into tree based on beta
        if node.beta == 'N/A':
            print(node.name + " has not published its beta values")
            return

        self.size += 1
        if self.root is None:
            self.root = node
            return
        else:
            self.insert_beta_r(self.root, node)
    
    def insert_beta_r(self, prior, node) -> None:
        try:
            if node.beta > prior.beta:
                if prior.right is None:
                    prior.right = node
                    return
                self.insert_beta_r(prior.right, node)
            else:
                if prior.left is None:
                    prior.left = node
                    return
                self.insert_beta_r(prior.left, node)
        except:
            return
    
    def insert_PE(self, node) -> None:  # inserts node into tree based on price to earnings
        if node.PE == 'N/A':
            print(node.name + " has not published its PE values")
            return

        self.size += 1
        if self.root is None:
            self.root = node
            return
        else:
            self.insert_PE_r(self.root, node)
    
    def insert_PE_r(self, prior, node) -> None:
        try:
            if node.PE > prior.PE:
                if prior.right is None:
                    prior.right = node
                    return
                self.insert_PE_r(prior.right, node)
            else:
                if prior.left is None:
                    prior.left = node
                    return
                self.insert_PE_r(prior.left, node)
        except:
            return

    def insert_EPS(self, node) -> None:  # inserts node into tree based on earnings per share
        if node.EPS == 'N/A':
            print(node.name + " has not published its EPS values")
            return

        self.size += 1
        if self.root is None:
            self.root = node
            return
        else:
            self.insert_EPS_r(self.root, node)
    
    def insert_EPS_r(self, prior, node) -> None:
        try:
            if node.EPS > prior.EPS:
                if prior.right is None:
                    prior.right = node
                    return
                self.insert_EPS_r(prior.right, node)
            else:
                if prior.left is None:
                    prior.left = node
                    return
                self.insert_EPS_r(prior.left, node)
        except:
            return

    def clear(self) -> None:  # clears the tree
        self.root.killAllChildren()
        self.root = None
        self.size = 0
