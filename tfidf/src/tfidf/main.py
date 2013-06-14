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
                  "reserved", "mexico", "abstract", "copyright", "ltd" "bv",
                  "new", "york", "publishing", "limited", '#', '#17', ")",
                  "("]
    sw = stopwords.words("english") + special_sw
    
    D = dict()
    W = dict()
    
    with open("abstracts.txt", "rU") as abst:
        i = 1
        for line in abst:
            if line.strip():
                temp_line = list()
                D[i] = []
                for word in line.strip().split():
                    word = word.lower().translate(None, "!?.,;:_'\"")
                    if word not in sw:
                        if word:
                            W.setdefault(word, i)
                            D[i].append(word)
                i += 1

    keys_ = sorted(D.keys())
    terms = sorted(W.keys())
    print keys_[:10]
    print terms[:10]
#     quit()
    tfidfmatrix = ["Term"] + [k for k in keys_]
    
    for w in terms:
        row = [w]
        for i in keys_:
            d = D[i]
            print w, d
            row.append(tfidf(w, d, D))
            
    
    for r in tfidfmatrix[:20]:
        print r[:10]