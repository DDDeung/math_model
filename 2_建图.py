import tqdm
import numpy as np
import networkx as nx


G = nx.Graph()
# data = np.loadtxt('result.txt', dtype=str, delimiter='\t')
# for i in tqdm.tqdm(range(len(data))):
#     temp_list = data[i][1].split()
#     for j in range(len(temp_list)):
#         G.add_edge(data[i][0], temp_list[j])
#
# G.remove_edges_from(nx.selfloop_edges(G))

#使用分词结果建图
with open('result.txt', encoding='utf8') as f4:     # 打开一个文件临时交给给变量ll
    for line in tqdm.tqdm(f4.readlines()):    # for循环遍历readlines()取到的所有的文件内容
        temp_list = line.split()
        for i in range(1,len(temp_list)):
            G.add_edge(temp_list[0], temp_list[i])
G.remove_edges_from(nx.selfloop_edges(G))

# dict=nx.pagerank(G)
# print(dict)
# for i in dict.items():

# degree_dict=nx.degree_centrality(G.copy())#度中心性
# word_order=sorted(degree_dict.items(),key=lambda x:x[1],reverse=True)
# print([i for i in word_order][:10])

#pagerank算法
pr=nx.pagerank(G.copy(),alpha=0.85)
pr_order=sorted(pr.items(),key=lambda item:item[1],reverse=True)
# print(type(pr_order))
print([i for i in pr_order][:10])
