import random
import pandas as pd

class Recommendations():
	def __init__(self, df, similarity):
		self.df = df
		self.similarity = similarity
		self.indexes = pd.Series(df.index, index=df["link"])

	def recommend(self, link):
	    index = self.indexes[link]
	    scores = list(enumerate(self.similarity.toarray()[index]))
	    scores = sorted(scores, key=lambda x: x[1], reverse=True)
	    max_score = max(scores, key=lambda x: x[1])
	    max_indexes = [i[0] for i in scores if i[1] == max_score[1]]
	    if index in max_indexes:
	        max_indexes.remove(index)
	    if len(max_indexes) > 5:
	        link_indexes = random.sample(max_indexes, 5)
	    else:
	        scores = [i[0] for i in scores]
	        scores.remove(index)
	        link_indexes = random.sample(scores[0:5], 5)
	    return self.df["link"].iloc[link_indexes]

	def random_recommendation(self):
	    link_index = random.sample(sorted(self.indexes), 1)
	    return self.df["link"].iloc[link_index]

	def get_recommendations(self, link):
	    print(f"Input link:\n {link}")
	    recos = self.recommend(link)
#	    random_reco = self.random_recommendation()
	    print(f"Output links:")
	    reco_list = [rec for rec in recos]
#	    reco_list.append(random_reco.iloc[0])
	    reco_list = random.sample(reco_list, len(reco_list))
	    for reco in reco_list:
	        print(" " + reco)
	    return reco_list