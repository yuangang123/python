#利用马尔科夫模型
#生成文字生成器
from urllib.request import urlopen
from random import randint

#计算wordList的value和
def wordListSum(wordList):
    sum=0
    for word,value in wordList.items():
        sum += value
    return sum
#按照词语的概率选取最合适单词
#慢慢体会有道理
#例如
#{word_a:{word_b:1,word_c:2,word_d:1},
 #word_e:{word_b:5,word_d:2,...}
 #}
 #对于单词a，和为4
 #随机数可以为1,2,3,4
 #其中1,2,的时候，会选择单词b，
 #为3的时候会选择单词c
 #为1的时候会选择单词d
 #和单词的频率是一致的
 
#这种方法按照权重选取随机数，思想第一次接触，值得记下来，说不定以后有用
def retrieveRandomWord(wordList):
    randIndex= randint(1,wordListSum(wordList))
    for word,value in wordList.items():
        randIndex -=value
        if randIndex <=0:
            return word
#创建形如如下的二维字典
#{word_a:{word_b:2,word_c:1,word_d:1},
 #word_e:{word_b:5,word_d:2,...}
 #}
def buildWordDict(text):
    text = text.replace("\n"," ")
    text = text.replace("\"","")
    
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        text = text.replace(symbol," "+symbol+" ")
        
    words = text.split(" ")
    words =[word for word in words if word != ""]
    
    wordDict = {}
    
    for i in range(1,len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]]={}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] =0
        wordDict[words[i-1]][words[i]] =wordDict[words[i-1]][words[i]]+1
        
    return wordDict

text =str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),"utf-8")
wordDict = buildWordDict(text)

for item in wordDict.items():
    print(item)

length=100
chain=""
currentWord = "I"
for i in range(0,length):
    chain+=currentWord+" "
    currentWord=retrieveRandomWord(wordDict[currentWord])
    
print(chain)
