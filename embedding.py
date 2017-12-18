import embeddings

emb = embeddings.EmbeddingsDictionary(100000)

'''
first task
'''

tmp = emb.emb2neighbors(emb.embed('geek'), 10)[1]
for t in tmp: print(emb.words[t])

'''
second task
'''

emb.analog('king', 'woman', 'man')
