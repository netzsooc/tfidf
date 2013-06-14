'''
Created on Jun 13, 2013

@author: netzsooc
'''
from math import log

#idf measure of whether the term is common or rare across all documents.
def idf(t, D):
    return log(float(len(D)) / len([d for d in D if t in d]))