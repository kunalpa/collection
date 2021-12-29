"""Unit tests for all functions in the project"""
"""I had to delete some of my unit tests after making my data dynamic -- mainly the sorting functions"""
"""I also was forced to test that the data pulled correctly manually because I didn't know how to do it otherwise"""

from ex_nodes import *
from BST import *
from ArrSorts import *

nodes1 = [testNode4, testNode2, testNode1, testNode3]
nodes2 = [testNode2, testNode3, testNode4, testNode1]
correctSortNames = ['first', 'second', 'third', 'fourth']
correctSortNodes = [testNode1, testNode2, testNode3, testNode4]

"""Testing trees"""
def testMCTree():
    MCTree = Tree()
    MCTree.insert(testNode1, "market cap")  # mc = 1
    MCTree.insert(testNode2, "market cap")  # mc = 2
    MCTree.insert(testNode3, "market cap")  # mc = 3
    assert MCTree.root == testNode1
    assert testNode1.left is None
    assert testNode1.right == testNode2
    assert testNode2.left is None
    assert testNode2.right == testNode3
    assert testNode3.left is None
    assert testNode3.right is None
    testNode1.left = None
    testNode1.right = None
    testNode2.left = None
    testNode2.right = None
    testNode3.left = None
    testNode3.right = None

def testVolumeTree():
    volumeTree = Tree()
    volumeTree.insert(testNode1, "volume")  # volume = 1
    volumeTree.insert(testNode2, "volume")  # volume = 2
    volumeTree.insert(testNode3, "volume")  # volume = 3
    assert volumeTree.root == testNode1
    assert testNode1.left is None
    assert testNode1.right == testNode2
    assert testNode2.left is None
    assert testNode2.right == testNode3
    assert testNode3.left is None
    assert testNode3.right is None
    testNode1.left = None
    testNode1.right = None
    testNode2.left = None
    testNode2.right = None
    testNode3.left = None
    testNode3.right = None

def testBetaTree():
    betaTree = Tree()
    betaTree.insert(testNode1, "beta")  # beta = 1
    betaTree.insert(testNode2, "beta")  # beta = 2
    betaTree.insert(testNode3, "beta")  # beta = 3
    assert betaTree.root == testNode1
    assert testNode1.left is None
    assert testNode1.right == testNode2
    assert testNode2.left is None
    assert testNode2.right == testNode3
    assert testNode3.left is None
    assert testNode3.right is None
    testNode1.left = None
    testNode1.right = None
    testNode2.left = None
    testNode2.right = None
    testNode3.left = None
    testNode3.right = None

def testEpsTree():
    epsTree = Tree()
    epsTree.insert(testNode1, "eps")  # eps = 1
    epsTree.insert(testNode2, "eps")  # eps = 2
    epsTree.insert(testNode3, "eps")  # eps = 3
    assert epsTree.root == testNode1
    assert testNode1.left is None
    assert testNode1.right == testNode2
    assert testNode2.left is None
    assert testNode2.right == testNode3
    assert testNode3.left is None
    assert testNode3.right is None
    testNode1.left = None
    testNode1.right = None
    testNode2.left = None
    testNode2.right = None
    testNode3.left = None
    testNode3.right = None

def testPeTree():
    peTree = Tree()
    peTree.insert(testNode1, "pe")  # pe = 1
    peTree.insert(testNode2, "pe")  # pe = 2
    peTree.insert(testNode3, "pe")  # pe = 3
    assert peTree.root == testNode1
    assert testNode1.left is None
    assert testNode1.right == testNode2
    assert testNode2.left is None
    assert testNode2.right == testNode3
    assert testNode3.left is None
    assert testNode3.right is None
    testNode1.left = None
    testNode1.right = None
    testNode2.left = None
    testNode2.right = None
    testNode3.left = None
    testNode3.right = None

def testClearBase():
    tree = Tree()
    tree.insert(testNode1, "pe")
    tree.insert(testNode2, "pe")
    tree.insert(testNode3, "pe")
    tree.insert(testNode4, "pe")
    tree.clear()
    assert testNode1.left is None
    assert testNode2.left is None
    assert testNode3.left is None
    assert testNode1.right is None
    assert testNode2.right is None
    assert testNode3.right is None
    assert testNode4.right is None
    assert testNode4.left is None

def testClearMultiple():
    totalNodes = [testNode1, testNode2, testNode3, testNode4, testNode5, testNode6]
    tree = Tree()
    for node in totalNodes:
        tree.insert(node, "pe")
    tree.clear()
    for node in totalNodes:
        tree.insert(node, "eps")
    tree.clear()
    for node in totalNodes:
        tree.insert(node, "market cap")
    tree.clear()
    for node in totalNodes:
        tree.insert(node, "volume")
    tree.clear()
    for node in totalNodes:
        tree.insert(node, "beta")
    tree.clear()
    assert testNode1.left is None
    assert testNode2.left is None
    assert testNode3.left is None
    assert testNode1.right is None
    assert testNode2.right is None
    assert testNode3.right is None
    assert testNode4.right is None
    assert testNode4.left is None

def testTreeSort():
    tree = Tree()
    tree.insert(testNode3, "pe")
    tree.insert(testNode1, "pe")
    tree.insert(testNode4, "pe")
    tree.insert(testNode2, "pe")
    assert tree.sort() == [testNode1, testNode2, testNode3, testNode4]
    testNode1.left = None
    testNode1.right = None
    testNode2.left = None
    testNode2.right = None
    testNode3.left = None
    testNode3.right = None



"""Testing ArrSorts"""

def testMergeSortPE1():
    nodes = ArrSorts(nodes1)
    assert nodes.mergeSort("pe") == correctSortNodes

def testMergeSortPE2():
    nodes = ArrSorts(nodes2)
    assert nodes.mergeSort("pe") == correctSortNodes

def testMergeSortEPS1():
    nodes = ArrSorts(nodes1)
    assert nodes.mergeSort("eps") == correctSortNodes

def testMergeSortEPS2():
    nodes = ArrSorts(nodes2)
    assert nodes.mergeSort("eps") == correctSortNodes

def testMergeSortVolume1():
    nodes = ArrSorts(nodes1)
    assert nodes.mergeSort("volume") == correctSortNodes

def testMergeSortVolume2():
    nodes = ArrSorts(nodes2)
    assert nodes.mergeSort("volume") == correctSortNodes

def testMergeSortBeta1():
    nodes = ArrSorts(nodes1)
    assert nodes.mergeSort("beta") == correctSortNodes

def testMergeSortBeta2():
    nodes = ArrSorts(nodes2)
    assert nodes.mergeSort("beta") == correctSortNodes

def testMergeSortMC1():
    nodes = ArrSorts(nodes1)
    assert nodes.mergeSort("market cap") == correctSortNodes

def testMergeSortMC2():
    nodes = ArrSorts(nodes2)
    assert nodes.mergeSort("market cap") == correctSortNodes

def testInsertionSortPE1():
    nodes = ArrSorts(nodes1)
    assert nodes.insertionSort("pe") == correctSortNames

def testInsertionSortPE2():
    nodes = ArrSorts(nodes2)
    assert nodes.insertionSort("pe") == correctSortNames
    
def testInsertionSortEPS1():
    nodes = ArrSorts(nodes1)
    assert nodes.insertionSort("eps") == correctSortNames

def testInsertionSortEPS2():
    nodes = ArrSorts(nodes2)
    assert nodes.insertionSort("eps") == correctSortNames

def testInsertionSortVolume1():
    nodes = ArrSorts(nodes1)
    assert nodes.insertionSort("volume") == correctSortNames

def testInsertionSortVolume2():
    nodes = ArrSorts(nodes2)
    assert nodes.insertionSort("volume") == correctSortNames

def testInsertionSortBeta1():
    nodes = ArrSorts(nodes1)
    assert nodes.insertionSort("beta") == correctSortNames

def testInsertionSortBeta2():
    nodes = ArrSorts(nodes2)
    assert nodes.insertionSort("beta") == correctSortNames

def testInsertionSortMC1():
    nodes = ArrSorts(nodes1)
    assert nodes.insertionSort("market cap") == correctSortNames

def testInsertionSortMC2():
    nodes = ArrSorts(nodes2)
    assert nodes.insertionSort("market cap") == correctSortNames

def main():
    """I had trouble configuring pytest, so I have to test this way"""
    testInsertionSortBeta1()
    testInsertionSortBeta2()
    testInsertionSortEPS1()
    testInsertionSortEPS2()
    testInsertionSortMC1()
    testInsertionSortMC2()
    testInsertionSortPE1()
    testInsertionSortPE2()
    testInsertionSortVolume1()
    testInsertionSortVolume1()

    testMergeSortBeta1()
    testMergeSortBeta2()
    testMergeSortEPS1()
    testMergeSortEPS2()
    testMergeSortMC1()
    testMergeSortMC2()
    testMergeSortPE1()
    testMergeSortPE2()
    testMergeSortVolume1()
    testMergeSortVolume1()

    testTreeSort()
    testPeTree()
    testEpsTree()
    testVolumeTree()
    testBetaTree()
    testMCTree()
    testClearBase()
    testClearMultiple()

if __name__ == '__main__':
    main()