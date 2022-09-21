import gensim
tx = 'Consider the data for attribute“weight”:   Partition the data using equal width partitioning. . Number of intervals = 3. Normalize the weight = 34 using min-max method (min=1, max=2)'
tx = tx.translate({ord(i): '' for i in '—-:;'})
# tx = ['What', 'Motivated', 'data', 'Mining']
doc = gensim.utils.simple_preprocess(tx)
print(doc)