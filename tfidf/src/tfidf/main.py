# -*- encoding:latin-1 -*-
'''
Created on Jun 13, 2013

@author: netzsooc
'''
from nltk.corpus import stopwords
from nltk import PorterStemmer
from tf_idf import tfidf
from tf import ntf
from idf import idf

if __name__ == '__main__':
    stemmer = PorterStemmer()
    special_sw = [
                  "one", "two", "three", "four", "paper", "work", "present",
                  "elsevier", "springer", "berlin", "heidelberg", "published",
                  "springer-verlag", "ieee", "acm", "Â©".lower(), "press",
                  "authors", "rights", "reserved", "mexico", "abstract",
                  "copyright", "ltd", "bv", "new", "york", "publishing",
                  "limited", "amp", "gt", "and/or", "lt", "le", "ge", "eq"]
    sw = stopwords.words("english") + special_sw
    ignorelist = "!?.,;:_'\"#$&()%/*+-0123456789[]<>=\\`Î²{}^”›†’�ˆž|"
    
    D = dict()
    W = dict()
    
    with open("abstracts.txt", "rU") as abst:
        i = 1
        for line in abst:
            if line.strip():
                D[i] = []
                for word in line.strip().split():
                    word = word.lower().translate(None, ignorelist)
                    if word:
                        if word in sw:
                            continue
                        if len(word) < 4:
                            continue
                        word = stemmer.stem(word)
                        W.setdefault(word, {}).setdefault(i, 0)
                        W[word][i] += 1
                        D[i].append(word)
                i += 1

    inmutfable = W.copy()
    W_ = sorted(W.keys())
    W = dict()
    #IDFS = dict()
    D_ = sorted(D.keys())
    #print D
    print ["TERM"] + [d for d in D_]
    for term in W_:
        #W[term] = dict()
        temp = [term]
        #IDFS[term] = idf(term, D)

        for di in D_:
            if not di in inmutfable[term]:
                temp.append(0)
            else:
                t = inmutfable[term][di]
                temp.append(ntf(t, di, W=inmutfable, D=D) * idf(term, D))

        print temp
        #for di in inmutfable[term]:
            #t = inmutfable[term][di]
            #print inmutfable[term][di]
            #W[term][di] = ntf(t, di, W=inmutfable, D=D) * idf(term, D)
    
    #matrixtfidf = [["TERM"] + [d for d in D_]]
##    print ["TERM"] + [d for d in D_]
#    for t in W_:
#        temp = [w]
#        for di in D_:
#            if not di in W[w]:
#                temp.append(0)
#                continue
#            temp.append(W[t][di])
#        print temp
#        
#    #for line in matrixtfidf:
#        #print line
