'''
Created on Jun 13, 2013

@author: netzsooc
'''

#normalized TF a + (1 - a) * (tf(t, d) / tf(max(d)))


def tf(t, d):
    #d is a list of words in a document and not in stoplist
    #t is the term looked
    return float(d.count(t))


def maxtf(d, W, D):
    #d is a list of words in a document and not in stoplist
    #t is the term looked
    if W:
        if D:
            temp = []
            for t in D[d]:
                temp.append(W[t][d])
        else:
            print "Error, Missing dictionary"
            quit()

    else:
        temp = [tf(t, d) for t in d]
    #print(temp)
    return float(max(temp))
    

def ntf(t, d, a=0.4, W=None, D=None):
    #d is a list of values of terms
    #t is the term looked
    #a is a number thus 0 <= a <= 1
    
    if type(t) == str:
        t = tf(t, d)
    
    #print type(maxtf(d,W))
    return a + (1 - a) * (float(t) / maxtf(d, W, D))