summa=0
mylist = ['robot','girl', 'men','doctor', 'scientist','ceo' ]
for a in mylist:
    summa = len(a) +  summa
    if a=='ceo':
        midscore=summa/len(mylist)
        print(midscore)