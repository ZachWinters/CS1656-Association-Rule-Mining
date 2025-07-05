# Association Rule Mining with A-Priori Algorithm
## Overview
This project implements the A-Priori algorithm for association rule mining in Python. The algorithm discovers frequent itemsets and generates association rules from market basket data, with configurable minimum support and confidence thresholds. The solution is optimized for performance and handles all specificed input/output requirements.

## Key Features
### Data Processing
* **CSV Input Handling**: Reads transaction data while ignoring empty values and whitespaces
* **Transaction Representation**: Uses Python sets for efficient subset ooperations
*** Lexicographic Ordering**: Maintains consistent item ordering throughout processing

### Algorithm Implementation
* **Candidate Generation**: Implements level-wise candidate generation with pruning
* **Support Counting**: Counts occurrences using dictionary lookups
* Subset Validation: Verifies all (k-1) subsets are frequent before considering k-itemsets
* Rule Generation: Creates all valid rules from frequent itemsets with confidence calculations

### Output Formatting
* Precise Formatting: Ensures 4 decimal places for support and confidence values
* Structured Output: Properly formates both frequent itemsets and association rules
* Sorting: Orders output by itemset size and lexicographic item order

## Technical Highlights
1. Optimized Data Structures:
   * Use of frozenset for hashable itemsets
2. Algorithm Efficiency:
   * Implemets the A-Priori property to prune candidate itemsets
   * Avoids redundant computations through careful candidate generation
3. I/O Handling 

Grade Percentage: 100%
