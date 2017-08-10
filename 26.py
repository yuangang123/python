from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    input = re.sub('\n+'," ",input).lower()
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +'," ",input)
    input = bytes(input,"UTF-8")
    input = input.decode("ascii","ignore")
    cleanInput=[]
    input = input.split(' ')
    
    for item in input:
        item =item.strip(string.punctuation)
        if len(item)>0 or (item.lower()=='a' or item.lower()=='i'):
            cleanInput.append(item)
    return cleanInput

def isCommon(ngrams):
    commonWords=["the", "be", "and", "of", "a", "in", "to", "have",
                   "it", "i", "that", "for", "you", "he", "with", "on", "do", "say",
                   "this", "they", "is", "an", "at", "but","we", "his", "from", "that",
                   "not", "by", "she", "or", "as", "what", "go", "their","can", "who",
                   "get", "if", "would", "her", "all", "my", "make", "about", "know",
                   "will","as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take", "out",
                   "into", "just", "see", "him", "your", "come", "could", "now", "than",
                   "like", "other", "how", "then", "its", "our", "two", "more", "these",
                   "want", "way", "look", "first", "also", "new", "because", "day", "more",
                   "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in ngrams:
        if word in commonWords:
            return True
    return False

def ngrams(input,n):
    input = cleanInput(input)
    
    output = {}
    for i in range(len(input)-n+1):
        #join的作用是将空格“ ”和后面的input内容连接起来
        ngramTemp = " ".join(input[i:i+n])
        
        #print("ngramTemp:"+ngramTemp)
        
        #去掉英语语言里面常用的没有的词语
        if isCommon(ngramTemp.split(" ")):
            pass
        else:
            if ngramTemp not in output:
                output[ngramTemp] =0
            output[ngramTemp]+=1
    return output


#根据核心词汇提取核心句子
def getFirstSentenceContaining(ngram, content):
    #print(ngram)
    sentences = content.split(".")
    for sentence in sentences:
        if ngram in sentence:
            return sentence
    return ""
    
content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
print(content)
ngrams = ngrams(content,2)


sortedNGrams = sorted(ngrams.items(),key=operator.itemgetter(1),reverse=True)
for sortedNGram in sortedNGrams:
    print(sortedNGram)
print(len(sortedNGrams))

#提取前四个核心句子
for top4 in range(4):
    print(sortedNGrams[top4][0])
    print("###"+getFirstSentenceContaining(sortedNGrams[top4][0],content.lower())+"###")
