import embeddings

emb = embeddings.EmbeddingsDictionary(100000)

tmp = emb.emb2neighbors(emb.embed('geek'), 10)[1]
for t in tmp: print(emb.words[t])
