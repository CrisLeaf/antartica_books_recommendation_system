from stop_words import get_stop_words

stop_words = get_stop_words("es")
stop_words = " ".join(stop_words)
stop_words = stop_words.replace("á", "a")
stop_words = stop_words.replace("é", "e")
stop_words = stop_words.replace("í", "i")
stop_words = stop_words.replace("ó", "o")
stop_words = stop_words.replace("ú", "u")
stop_words = stop_words.split(" ")

def df_fill_na(df):
	df["author"].fillna(value="", inplace=True)
	df["category"].fillna(value="", inplace=True)
	df["discount"].fillna(value=0, inplace=True)
	df["editorial"].fillna(value="", inplace=True)
	df["language"].fillna(value="", inplace=True)
	df["pages"].fillna(value=0, inplace=True)
	df["review"].fillna(value="", inplace=True)
	return df
