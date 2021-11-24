from utils import stop_words
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import csr_matrix

def get_similarities(df):
	author_count = CountVectorizer(stop_words=stop_words)
	author_matrix = author_count.fit_transform(df["author"])
	author_sim = linear_kernel(author_matrix, author_matrix, dense_output=False)
	author_sim = author_sim / np.max(author_sim) * 20
	author_sim = author_sim.astype("uint8")

	category_count = CountVectorizer(stop_words=stop_words)
	category_matrix = category_count.fit_transform(df["category"])
	category_sim = linear_kernel(category_matrix, category_matrix, dense_output=False)
	category_sim = category_sim / np.max(category_sim) * 20
	category_sim = category_sim.astype("uint8")

	editorial_count = CountVectorizer(stop_words=stop_words)
	editorial_matrix = editorial_count.fit_transform(df["editorial"])
	editorial_sim = linear_kernel(editorial_matrix, editorial_matrix, dense_output=False)
	editorial_sim = editorial_sim / np.max(editorial_sim) * 20
	editorial_sim = editorial_sim.astype("uint8")

	review_count = TfidfVectorizer(stop_words=stop_words)
	review_matrix = review_count.fit_transform(df["review"])
	review_sim = linear_kernel(review_matrix, review_matrix, dense_output=False)
	review_sim = review_sim / np.max(review_sim) * 20
	review_sim = review_sim.astype("uint8")

	discount_list = df["discount"].values / max(df["discount"])
	discount_matrix = np.tile(discount_list, (df.shape[0], 1)) * 20
	discount_matrix = discount_matrix.astype("uint8")
	discount_matrix = csr_matrix(discount_matrix)

	return 2*author_sim + 2*category_sim + editorial_sim + 4*review_sim + discount_matrix