'''
Created on Jun 13, 2013

@author: netzsooc
'''

#normalized TF a + (1 - a) * (tf(t, d) / tf(max(d)))


def tf(t, d):
    #d is a list of words in a document and not in stoplist
    #t is the term looked
    return d.count(t)


def maxtf(d):
    #d is a list of words in a document and not in stoplist
    #t is the term looked
    temp = sorted([(tf(t, d), t) for t in d], reverse=True)
    return temp[0][0]
    

def ntf(t, d, a=0.4):
    #d is a list of words in a document and not in stoplist
    #t is the term looked
    #a is a number thus 0 <= a <= 1
    return a + (1 - a) * (tf(t, d) / maxtf(d))