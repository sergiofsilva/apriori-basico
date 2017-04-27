Python Implementation of Apriori Algorithm 
==========================================


The code attempts to do same modification in Asaini implementation (https://github.com/asaini/Apriori/blob/master/apriori.py) of the Apriori algorithm. Bellow we list the main modifications:
1) Compatibilite with Python 3.6 (The original Asaini code was not compatible with Python 3.6
2) Addition of a prune implementation step in the construction of n-size itemsets based on (n-1)-size itemsets 

The apriori algorithm is described on the paper:

> *Agrawal, Rakesh, and Ramakrishnan Srikant. "Fast algorithms for mining association rules." Proc. 20th int. conf. very large data bases, VLDB. Vol. 1215. 1994.*

List of files
-------------
1. apriori.py
2. INTEGRATED-DATASET.csv
3. README(this file)

The dataset INTEGRATED-DATASET.csv is a copy of the “Online directory of certified businesses with a detailed profile” file from the Small Business Services (SBS) 
dataset in the `NYC Open Data Sets <http://nycopendata.socrata.com/>`_

Usage
-----
To run the program with dataset provided and default values for *minSupport* = 0.15 and *minConfidence* = 0.6

    python apriori.py -f INTEGRATED-DATASET.csv

To run program with dataset  

    python apriori.py -f INTEGRATED-DATASET.csv -s 0.17 -c 0.68

For the INTEGRATED-DATASET.csv, the best results are obtained for the following values of support and confidence:  

Support     : Between 0.1 and 0.2  

Confidence  : Between 0.5 and 0.7 

License
-------
MIT-License

-------
