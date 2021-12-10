import json
import jieba
import re

with open('ci.json','r',encoding='utf-8') as f:
    read_ci=json.load(f)

#处理停用词
stop_word_list=[]
with open('stop_words.txt','r') as f2:
    for line in f2.readlines():
        line = line.strip('\n')
        stop_word_list.append(line)
# print(stop_word_list)
stop_word_set=set(stop_word_list)
# print(stop_word_set)

all_word_list=[]#所有的单词 含重复
wordDict={} #将释义分词 释义对应的字典
word_count={}
for d in read_ci:
    pattern = re.compile(u'[^\u4e00-\u9fa5]')  # 中文的范围为\u4e00-\u9fa5 生成正则表达式
    line = re.sub(pattern, '', d['explanation'])  # 将其中所有非中文字符替换
    # print(line)
    segList = jieba.lcut(line)
    seg_set=set(segList)-stop_word_set
    all_word_list.append(d['ci'])#增加词条
    for c in seg_set:
        # if c in word_count:
        #     word_count[c]+=1
        # else:
        #     word_count[c]=1
        word_count[c]=word_count.get(c,0)+1
        all_word_list.append(c)

    wordDict[d['ci']] = seg_set;#将释义分词


# 将分词结果写到文件中
with open('result.txt', 'w',encoding='utf8') as f3:
    for d in read_ci:
        f3.write(d['ci']+'\t');
        for c in wordDict[d['ci']]:
            f3.write(c+' ');
        f3.write('\r\n');

# word_count_order=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
#
# all_word_set=set(all_word_list)#所有的单词 不含重复
#
# all_word_count={}#统计所有词的频次
# for w in all_word_list:
#     all_word_count[w]=all_word_count.get(w,0)+1
#
# all_word_order=sorted(all_word_count.items(),key=lambda x:x[1],reverse=True)
# print([i for i in all_word_order][:10])
# # print(len(wordDict))
# print(len(all_word_count))
# print([i for i in word_count_order][:10])
#



