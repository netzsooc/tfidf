# -*- encoding:latin-1 -*-
'''
Created on Jun 13, 2013

@author: netzsooc
'''
from nltk.corpus import stopwords
from nltk import PorterStemmer
from tf_idf import tfidf

if __name__ == '__main__':
    stemmer = PorterStemmer()
    special_sw = [
                  "one", "two", "three", "four", "paper", "work", "present",
                  "elsevier", "springer", "berlin", "heidelberg", "published",
                  "springer-verlag", "ieee", "acm", "Â©".lower(), "2013",
                  "2012", "2011", "2010", "press", "authors", "rights",
                  "reserved", "mexico", "abstract", "copyright", "ltd", "bv",
                  "new", "york", "publishing", "limited", '#', '#17', ")",
                  "(", "amp", "gt", "gt10", "gt109", "gt120", "and/or", "1",
		  "2"]
    sw = stopwords.words("english") + special_sw
    ignorelist = "!?.,;:_'\"#$&()"
    
    D = dict()
    W = dict()
    
    with open("abstracts.txt", "rU") as abst:
        i = 1
        for line in abst:
            if line.strip():
#                 temp_line = list()
                D[i] = []
                for word in line.strip().split():
                    word = word.lower().translate(None, ignorelist)
                    if word in sw:
                        continue
                    if word:
                        W.setdefault(word, []).append(i)
                        D[i].append(word)
                i += 1

    W_ = sorted(W.keys())
    keys_ = sorted(D.keys())
    tfmatrix = [["Term"] + [k for k in keys_]]

    for term in W_[:10]:
        temp = [term]

        for k in keys_[:20]:
	    d = D[k]
	    tf = d.count(term)
	    temp.append(tf)

        tfmatrix.append(temp)
     
    #print ("W =", len(W), "W =", len(secondW))
    for r in tfidfmatrix[:20]:
        print r
