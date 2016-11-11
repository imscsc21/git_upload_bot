import os

def doWordChain():
    import random
    def getNewWord(output,data):
        print("gen new game")
        next_word=data[random.randint(0,len(dict)-1)]
        output.write(next_word+"\n")
        return next_word
    
    dictfp = open("dictionary.txt","r")
    if(not os.path.exists("chain.txt")):
        output = open("chain.txt","a")
        output.close()
    output = open("chain.txt","r+")
    dict = dictfp.read()
    dict = dict.split("\n")
    dictfp.close()
    del dictfp
    next_word = "==end-Game=="
    beforechain = output.read()
    if(len(beforechain)==0):
        next_word=getNewWord(output,dict)
    else:
        beforechain=beforechain.split("==end-Game==")
        if(len(beforechain)>0):
            beforechain=beforechain[-1]
        else:
            beforechain=beforechain[0]
        beforechain=beforechain.split("\n")
        #if(len(beforechain)>1 and len(beforechain[-1])==0):
        #    del beforechain[-1]
        tmplst = []
        for v in beforechain:
            if(len(v)>1):
                tmplst.append(v)
        del beforechain
        beforechain=tmplst
        if(len(beforechain)<1 ):
            new_word= getNewWord(output,dict)
            output.close()
            return new_word
        prefix=str((beforechain[-1])[-1])
        if(prefix!="="):
            available_wordlist=[]
            for someword in dict:
                if(len(someword)>1 and someword[0]==prefix and someword not in beforechain):
                    available_wordlist.append(someword)
            if(len(available_wordlist)>0):      
                next_word=available_wordlist[random.randint(0,len(available_wordlist)-1)]
                
            #print("show data before append word: ",ne)
            output.write(next_word+"\n")
        else:
            next_word = getNewWord(output,dict)
    output.close()
    del output
    return next_word
doWordChain()