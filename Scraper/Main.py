"""This program sorts, develops trees, and offers recommendations on stocks based on their tickers"""

import requests
from bs4 import BeautifulSoup
from StockNode import Node
from BST import Tree
from timeit import default_timer as timer
from time import sleep
from ArrSorts import ArrSorts

def main():  # gathers user input and redirects to corresponding functions
    file = "data/S&P500.csv"
    file = "data/tiny.csv"
    nodes = []
    print('Current file: ' + file)
    while True:
        val = input("Sort, get stats, view trees, or exit: ")
        if val.lower() == 'exit':
            break
        elif val.lower() == "sort":
            if len(nodes) == 0:
                print('Pulling info... It will take a little less than one second per company')
                nodes = createNodes(file)
            sort(nodes)
        elif val.lower() == "get stats" or val.lower() == "stats":
            if len(nodes) == 0:
                print('Pulling info... It will take a little less than one second per company')
                nodes = createNodes(file)
            getStats(nodes)
        elif val.lower() == "view" or val.lower() == "trees" or val.lower() == "view tree":
            if len(nodes) == 0:
                print('Pulling info... It will take a little less than one second per company')
                nodes = createNodes(file)
            showTrees(nodes)
        else:
            print("Invalid argument... try again")

def showTrees(nodes) -> None:  # Updates trees in the trees.txt file
    tree = Tree()
    for node in nodes:
        tree.insert_MC(node)
    tree.display("trees/marketCapTree.txt")
    tree.clear()

    for node in nodes:
        tree.insert_PE(node)
    tree.display("trees/peTree.txt")
    tree.clear()

    for node in nodes:
        tree.insert_EPS(node)
    tree.display("trees/epsTree.txt")
    tree.clear()

    for node in nodes:
        tree.insert_volume(node)
    tree.display("trees/volumeTree.txt")
    tree.clear()

    for node in nodes:
        tree.insert_beta(node)
    tree.display("trees/betaTree.txt")
    tree.clear()

    print('Everything is updated')
    print('Check txt files under the trees folder for updated values')
    print('If there is a problem, just rerun the code')

def getStats(nodes) -> None:
    # Returns stats on company, compares company to the rest of the data, and compares competitors
    inp = input("Which ticker do you want to examine? ")
    inp = inp.upper()
    
    # Checks to see if the company is within the dataset
    exists = False
    i = 0
    while i < len(nodes):
        if nodes[i].name == inp:
            exists = True
            break
        i += 1

    if not exists:
        try:
            soup = createSoup(inp)
            node = createNode(soup, inp, industry="Unknown")
        except LookupError:
            print("Could not find stats on " + inp)
            return
        nodes.append(node)
        i = len(nodes) - 1

    print('Ticker name: ' + nodes[i].name)
    print('Market Cap: ' + str(nodes[i].marketCap))
    print('Previous Close: ' + nodes[i].prevClose)
    print('Open: ' + nodes[i].open)
    print('Bid: ' + nodes[i].bid)
    print('Ask: ' + nodes[i].ask)
    print('Day Range: ' + nodes[i].dayRange)
    print('Year Range: ' + nodes[i].yearRange)
    print('Volume: ' + str(nodes[i].volume))
    print('Beta: ' + str(nodes[i].beta))
    print('Price to Earnings Ratio: ' + str(nodes[i].PE))
    print('Earnings Per Share: ' + str(nodes[i].EPS))
    print('Forward Dividend & Yield: ' + nodes[i].forwardDivAndYield)
    print('Ex-Dividend Date: ' + nodes[i].exDivDate, end='\n')
    print()


    arr = ArrSorts(nodes)
    similar_companies = []
    stockIndex = -1
    sorted = arr.mergeSort('market cap')
    for i in range(len(sorted)):
        if inp == sorted[i].name:
            stockIndex = i
            percentile = (i + 1) / len(sorted)
            print(inp + ' is the ' + str(percentile * 100) + 'th percentile for market cap.')
            for j in range(len(sorted)):
                if sorted[i].industry == sorted[j].industry and j != i:
                    similar_companies.append(sorted[j])
            break
    
    if stockIndex == -1:
        print("Ticker does not exist within this dataset")
    if len(similar_companies) == 0:
        return

    # I don't want to show all competitors in the industry -- reducing clutter
    displayedComps = []
    for i in range(len(similar_companies)):
        if similar_companies[i].name == inp:
            j = i - 2
            while j < i + 2:
                try:
                    displayedComps.append(similar_companies[j])
                    j += 1
                except:  # Fewer than 4 similar companies
                    break


    if len(displayedComps) == 1:
        print(inp + "'s competitor is " + displayedComps[0].name +'.')
    elif len(displayedComps) > 1:
        print("Some of " + inp + "'s competitors are ")
        for i in range(len(displayedComps)):
            if i != len(displayedComps) - 1:
                print(displayedComps[i].name, end=', ')
            else:
                print('and ' + displayedComps[i].name +'.')

    # Generating recommendations
    similar_companies.append(sorted[stockIndex])
    competitors = ArrSorts(similar_companies)
    epsCompetitors = competitors.insertionSort("eps")
    epsComps = epsCompetitors[-5:]
    highValue = []
    for node in epsComps:
        highValue.append(node)

    lowPE = []
    highPE = []
    peCompetitors = competitors.insertionSort("pe")
    for i in range(len(peCompetitors)):
        if i < len(peCompetitors) // 2:
            lowPE.append(peCompetitors[i])
        else:
            highPE.append(peCompetitors[i])
    
    # Comparing the stock to the entire dataset
    sorted = arr.insertionSort('pe')
    for i in range(len(sorted)):
        if inp == sorted[i]:
            percentile = (i + 1) / len(sorted)
            print(inp + ' is the ' + str(percentile * 100) + 'th overall percentile for Price to Earnings Ratio.')
            break
    
    sorted = arr.insertionSort('eps')
    for i in range(len(sorted)):
        if inp == sorted[i]:
            percentile = (i + 1) / len(sorted)
            print(inp + ' is the ' + str(percentile * 100) + 'th overall percentile for Earnings Per Share.')
            break
    
    sorted = arr.insertionSort('volume')
    for i in range(len(sorted)):
        if inp == sorted[i]:
            percentile = (i + 1) / len(sorted)
            print(inp + ' is the ' + str(percentile * 100) + 'th overall percentile for volume.')
            break
    
    sorted = arr.insertionSort('beta')
    for i in range(len(sorted)):
        if inp == sorted[i]:
            percentile = (i + 1) / len(sorted)
            print(inp + ' is the ' + str(percentile * 100) + 'th overall percentile for beta.')
            break
    
    # printing recommendations
    print("The highest value companies in the " + similar_companies[0].industry + " industry and within this dataset: ")
    print(highValue)
    print("For more value per share and a more reliable investment, check out these companies: ")
    print(lowPE[:6])
    print("If you suspect high growth in " + similar_companies[0].industry + ", then maybe look into these companies:")
    print(highPE[-6:])

def sort(nodes) -> None:
    # Compares sorting algorithms and appends a sorted list based on user input to sortedData.txt
    while(True):
        val = input("Sort by EPS, Market Cap, PE, Beta, or Volume: ")
        val = val.lower()
        if val == "eps" or val == "market cap" or val == "pe" or val == "beta" or val == "volume":
            break
        print("unfamiliar input; must enter eps, market cap, pe, or volume")
    print()

    # Timed different sorting algorithms to figure out which one was most efficient
    arr = ArrSorts(nodes)
    mergeStart = timer()
    list = arr.mergeSort(val)
    mergeEnd = timer()

    tree = Tree()
    for node in nodes:
        tree.insert(node, val)
    bstStart = timer()
    tree.sort()
    bstEnd = timer()
    tree.clear()  # clean up tree for reuse

    arr = ArrSorts(nodes)
    insertStart = timer()
    arr.insertionSort(val)
    insertEnd = timer()

    print("time taken to sort via mergeSort: " + str(mergeEnd - mergeStart) + " seconds")
    print("time taken to sort via bst: " + str(bstEnd - bstStart) + " seconds")
    print("time taken to sort via insertionSort " + str(insertEnd - insertStart) + " seconds")

    file = open("data/sortedData.txt", "w")
    file.write("Data Sorted By " + val.upper() + ":\n")
    for i in list:
        file.write(i.name)
        file.write('\n')
    file.close()
    print("Check sortedData.txt file in data folder for sorted tickers by " + val.upper() + ".")

def createNode(soup, ticker, industry) -> Node:  # each company is stored as a node
    stat_names = soup.findAll(class_='Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)')
    node = Node(ticker)
    node.industry = industry
    node.prevClose = stat_names[0].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.open = stat_names[1].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.bid = stat_names[2].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.ask = stat_names[3].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.dayRange = stat_names[4].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.yearRange = stat_names[5].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.volume = float(stat_names[6].find(class_="Ta(end) Fw(600) Lh(14px)").string.replace(',',''))
    if(stat_names[8].find(class_="Ta(end) Fw(600) Lh(14px)").string != 'N/A'):
        node.beta = float(stat_names[8].find(class_="Ta(end) Fw(600) Lh(14px)").string)
    else:
        node.beta = stat_names[8].find(class_="Ta(end) Fw(600) Lh(14px)").string
    
    if(stat_names[9].find(class_="Ta(end) Fw(600) Lh(14px)").string != 'N/A'):
        node.PE = float(stat_names[9].find(class_="Ta(end) Fw(600) Lh(14px)").string.replace(',',''))
    else:
        node.PE = stat_names[9].find(class_="Ta(end) Fw(600) Lh(14px)").string

    if(stat_names[10].find(class_="Ta(end) Fw(600) Lh(14px)").string != 'N/A'):
        node.EPS = float(stat_names[10].find(class_="Ta(end) Fw(600) Lh(14px)").string.replace(',',''))
    else:
        node.EPS = stat_names[10].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.forwardDivAndYield = stat_names[12].find(class_="Ta(end) Fw(600) Lh(14px)").string
    node.exDivDate = stat_names[13].find(class_="Ta(end) Fw(600) Lh(14px)").string
    marketCap = stat_names[7].find(class_="Ta(end) Fw(600) Lh(14px)").string
    if marketCap == 'N/A':
        return
    # modifying market cap values
    num = 0
    if(marketCap[-1] == 'T'):
        marketCap = marketCap.replace('T','')
        num = float(marketCap)
        num *= 10**12
    elif(marketCap[-1] == 'B'):
        marketCap = marketCap.replace('B','')
        num = float(marketCap)
        num *= 10**9
    elif(marketCap[-1] == 'M'):
        marketCap = marketCap.replace('M','')
        num = float(marketCap)
        num *= 10**6
    node.marketCap = num

    return node

def createSoup(ticker) -> BeautifulSoup:  # creates usable soup object for pulling data
    url = "https://finance.yahoo.com/quote/%s?p=%s&.tsrc=fin-srch" %(ticker, ticker)
    soup_url = BeautifulSoup(requests.get(url).text, 'html.parser')
    return soup_url

def createNodes(file_name) -> list:  # Creates a node for each ticker
    nodes = []
    f = open(file_name, "r")
    f.readline()  # get to first stock
    for line in f:
        ticker = line.split(',')[0].replace('\"', '')
        industry = line.split(',')[4].replace('\"', '')
        try:
            soup = createSoup(ticker)
            node = createNode(soup, ticker, industry)
            nodes.append(node)
            sleep(.1)
        except LookupError:
            pass
    return nodes

if __name__ == "__main__":
    main()
