import random
import pandas as pd
import re
import jieba
from collections import Counter
from functools import reduce
from operator import add, mul
import matplotlib.pyplot as plt
import numpy as np
import random

#A "movie comment" language can be defined as
commenter = """
sentence = noun_phrase verb_phrase 
noun_phrase = noun 
noun  = 这部电影 | 剧情 |故事
verb_phrase = verb adj_phrase
verb = 是   |  感觉 |  演的 
adj_phrase = adj
adj = 最好看 | 好看 | 不好看 |可以 |喜欢 | 很好看

"""
def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar

choice = random.choice

def generate(gram, target):
    if target not in gram: return target # means target is a terminal expression
    
    expaned = [generate(gram, t) for t in choice(gram[target])]
    return ' '.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

random.choice(range(100))
filename = 'C:/Users/38079/OneDrive/桌面/NLP/Assignment/l1/movie_comments.csv'
content = pd.read_csv(filename, encoding='UTF-8', low_memory=False)
# print(content.head())
articles = content['comment'].tolist()
# print((articles[0]))

def token(string):
    # we will learn the regular expression next course.
    return re.findall('\w+', string)
# print(token(articles[1]))
# print(list(jieba.cut(articles[110])))
# with_jieba_cut = Counter(jieba.cut(articles[110]))
# print(with_jieba_cut.most_common()[:10])
# print(''.join(token(articles[110])))
articles_clean = [''.join(token(str(a)))for a in articles]
# print(len(articles_clean))
# print((articles_clean[1]))

with open('article.txt', 'w', encoding='utf-8') as f:
    for a in articles_clean:
        f.write(a + '\n')

def cut(string): return list(jieba.cut(string))
TOKEN = []
for i, line in enumerate((open('article.txt',encoding='utf-8'))):
    # if i % 100 == 0: print(i)
    
    # replace 10000 with a big number when you do your homework. 
    
    if i > 10000: break    
    TOKEN += cut(line)

# words_count = Counter(TOKEN)
# # print(words_count.most_common(100))
# frequiences = [f for w, f in words_count.most_common(100)]
# x = [i for i in range(100)]

# fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1) # 画2行1列个图形的第1个
# ax2 = fig.add_subplot(2,1,2) # 画2行1列个图形的第2个
# ax1.plot(x, frequiences)
# # print(plt.plot(x, np.log(frequiences)))
# ax2.plot(x, np.log(frequiences))
# plt.show()

# def prob_1(word):
#     return words_count[word] / len(TOKEN)
# print(prob_1('我们'))
TOKEN[:10]
TOKEN = [str(t) for t in TOKEN]
TOKEN_2_GRAM = [''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]
# Connect adjacent participles into new participles and store them in a list
TOKEN_2_GRAM[:10]
words_count_2 = Counter(TOKEN_2_GRAM)

def prob_2(word1, word2):
    if word1 + word2 in words_count_2: return words_count_2[word1+word2] / len(TOKEN_2_GRAM)#pr(w1|w2)=pr(w1w2)/pr(w2)
    else:#out of vocabulary problem
        return 1 / len(TOKEN_2_GRAM)
# print(prob_2('我们', '在'))

def get_probablity(sentence):
    words = cut(sentence)
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        next_ = words[i+1]
        probability = prob_2(word, next_)
        sentence_pro *= probability
    return sentence_pro

# print(get_probablity('吴京演技不错'))
# for sen in [generate(gram=create_grammar(host, split='='), target='sentence') for i in range(10)]:
#     print('sentence: {} with Prb: {}'.format(sen, get_probablity(sen)))

def generate_best(grammer):
    sentences=[]
    for sen in [generate(gram=grammer, target='sentence') for i in range(10)]:
        sentence=()
        sentence= (sen, get_probablity(sen))
        sentences.append(sentence)
    sentences=sorted(sentences, key=lambda x: x[1], reverse=True)
    print(sentences[0])

generate_best(create_grammar(commenter, split='='))