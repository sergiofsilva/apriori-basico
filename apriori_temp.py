"""
Description     : Simple Python implementation of the Apriori Algorithm

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence

    $python apriori.py -f DATASET.csv -s 0.15 -c 0.6
"""

import sys

from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser


def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSetVar, transactionList, minSupport, freqSet):
        """calculates the support for items in the itemSet and returns a subset
       of the itemSet each of whose elements satisfies the minimum support"""
        _itemSet = set()
        _itemSetRemoved = set()
        localSet = defaultdict(int)

        freqSetVar = [list() for i in range(numVars)]
        for idVar in range(numVars):
            freqSetVar[idVar] = [list() for _ in range(len(freqSetVar[idVar]))]
            for idItem in range(itemSetVar[idVar]):
                freqSetVar[idVar][idItem] = [[0] for _ in range(tCiclo)]
                


                for j in range(tCiclo):

                    for
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, count in localSet.items():
                support = float(count)/len(transactionList)
                if support >= minSupport:
                        _itemSet.add(item)
                else:
                    _itemSetRemoved.add(item)

        return _itemSet, _itemSetRemoved


def joinSet(itemSet, removedSet, length):
        """Join a set with itself and returns the n-element itemsets"""
        filteredSet = set()
        flagAddItem = True
        composed_set = set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
        newremovedSet = set()
        for item in composed_set:
            if removedSet != set([]):
                for itemR in removedSet:
                    if itemR.issubset(item):
                        flagAddItem = False
                        break
            if flagAddItem == True:
                filteredSet.add(item)
            else:
                newremovedSet.add(item)
        return filteredSet

def getItemSetTransactionList(data_iterator):
    transactionList = list()
    numVars = 4
    itemSetVar = [set() for i in range(numVars)]
    for transaction in data_iterator:
        transactionList.append(transaction)
        for i in range(numVars):
            itemSetVar[i].add(transaction[i])              # Generate 1-itemSets
    return itemSetVar, transactionList


def runApriori(data_iter, minSupport, minConfidence):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules

    oneCSet, removedCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet)

    currentLSet = oneCSet
    removedLSet = removedCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, removedLSet, k)
        currentCSet, removedCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet)
        currentLSet = currentCSet
        removedLSet = removedCSet
        k = k + 1

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items():
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item)/getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence))
    return toRetItems, toRetRules


def printResults(items, rules):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""
    for item, support in sorted(items, key=lambda tp: tp[1]):
        print("item: %s , %.3f" % (str(item), support))
    print("\n------------------------ RULES:")
    for rule, confidence in sorted(rules, key=lambda tp: tp[1]):
        pre, post = rule
        print("Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence))


def dataFromFile(fname):
    """Function which reads from the file and yields a generator"""
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',')                         # Remove trailing comma
        record = list(line.split(','))
        yield record


if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minS',
                         help='minimum support value',
                         default=0.15,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minC',
                         help='minimum confidence value',
                         default=0.6,
                         type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
            inFile = sys.stdin
    elif options.input is not None:
            inFile = dataFromFile(options.input)
    else:
            print('No dataset filename specified, system with exit')
            sys.exit('System will exit')

    minSupport = options.minS
    minConfidence = options.minC

    items, rules = runApriori(inFile, minSupport, minConfidence)

    printResults(items, rules)
