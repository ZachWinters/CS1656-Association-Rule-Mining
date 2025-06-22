from collections import defaultdict
from pandas import Series, DataFrame
import itertools as it
import pandas as pd
import math
import csv
import sys
import argparse
import collections
import glob
import os
import re
import requests
import string
import sys
class Armin:
    def apriori(self, input_filename, output_filename, min_support_percentage, min_confidence):
        #Read in the file csv
        #Organize and create supp
        #Create k=2,k=3, recursive?
        #Create confidence
            #Organize alphabetically
        #append to output
        
        
        # input file
        transactions = []
        with open(input_filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue
                # ignore transaction ID, strip whitespace
                items = [item.strip() for item in row[1:] if item.strip()]
                if items:
                    transactions.append(set(items))
        total_transactions = len(transactions)
        if total_transactions == 0:
            return

        # CFI(1)
        all_items = sorted({item for transaction in transactions for item in transaction})
        C1 = [frozenset([item]) for item in all_items]

        # filters candidates by support threshold
        support_data = {}
        def scan_transactions(candidates):
            counts = {}
            for t in transactions:
                for candidate in candidates:
                    if candidate.issubset(t):
                        counts[candidate] = counts.get(candidate, 0) + 1
            Lk = []
            for candidate, count in counts.items():
                support = count / total_transactions
                support_data[candidate] = support
                if support >= min_support_percentage:
                    Lk.append(candidate)
            return Lk

        # First 
        L = []
        L1 = scan_transactions(C1)
        Lk = L1
        L.append(L1)
        k = 2

        #  frequent itemsets for k >= 2
        while Lk:
            prev_L = Lk
            prev_L_set = set(prev_L)
            Ck = []
            len_prev = len(prev_L)
            for i in range(len_prev):
                for j in range(i+1, len_prev):
                    l1 = prev_L[i]
                    l2 = prev_L[j]
                    union = l1.union(l2)
                    if len(union) == k:
                        # pruneing: all (k-1)-subsets must be frequent
                        subsets = it.combinations(union, k-1)
                        if all(frozenset(sub) in prev_L_set for sub in subsets):
                            Ck.append(union)
            Ck = list(set(Ck))
            Lk = scan_transactions(Ck)
            if Lk:
                L.append(Lk)
                k += 1
            else:
                break

        # frequent itemsets
        frequent_itemsets = [itemset for level in L for itemset in level]

        # association rules
        rules = []
        for itemset in frequent_itemsets:
            if len(itemset) < 2:
                continue
            for i in range(1, len(itemset)):
                for antecedent in it.combinations(itemset, i):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    if not consequent:
                        continue
                    support = support_data[itemset]
                    confidence = support_data[itemset] / support_data[antecedent]
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, support, confidence))

        # output file
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # frequent itemsets
            for itemset in sorted(frequent_itemsets, key=lambda x: (len(x), sorted(x))):
                support = support_data[itemset]
                row = ['S', f"{support:.4f}"] + sorted(itemset)
                writer.writerow(row)
            # association rules
            for antecedent, consequent, support, confidence in sorted(rules, key=lambda x: (sorted(x[0]), sorted(x[1]))):
                row = ['R', f"{support:.4f}", f"{confidence:.4f}"] + sorted(antecedent) + ['\'=>\''] + sorted(consequent)
                writer.writerow(row)
if __name__ == "__main__":
    armin = Armin()
    armin.apriori('input.csv', 'output.sup=0.5,conf=0.7.csv', 0.5, 0.7)
    armin.apriori('input.csv', 'output.sup=0.5,conf=0.8.csv', 0.5, 0.8)
    armin.apriori('input.csv', 'output.sup=0.6,conf=0.8.csv', 0.6, 0.8)