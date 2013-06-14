'''
Created on Jun 13, 2013

@author: netzsooc
'''
from tf import ntf
from idf import idf

def tfidf(t, d, D):
    return ntf(t, d) * idf(t, D)