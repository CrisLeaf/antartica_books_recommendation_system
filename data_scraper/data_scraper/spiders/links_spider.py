import scrapy
from data_scraper.items import BooksScraperItem
from scrapy.loader import ItemLoader
import pandas as pd
import os

class LinksSpider(scrapy.Spider):
	name = "links"
	start_urls = [
		"https://www.antartica.cl/libros/arte-y-arquitectura.html", #1647
		"https://www.antartica.cl/libros/ciencias.html", #875
		"https://www.antartica.cl/libros/ciencias-exactas.html", #888
		"https://www.antartica.cl/libros/ciencias-humanas.html", #4943
		"https://www.antartica.cl/libros/computacion-e-informacion.html", #172
		"https://www.antartica.cl/libros/cuerpo-y-mente.html", #1868
		"https://www.antartica.cl/libros/economia-y-administracion.html", #687
		"https://www.antartica.cl/libros/entretencion-y-manual.html", #320
		"https://www.antartica.cl/libros/gastronomia-y-vinos.html", #505
		"https://www.antartica.cl/libros/guias-de-viaje-y-tur.html", #582
		"https://www.antartica.cl/libros/infantil-y-juvenil/juegos-ocio-y-actividades.html", #706
		"https://www.antartica.cl/libros/infantil-y-juvenil/libros-infantiles.html", #3254
		"https://www.antartica.cl/libros/infantil-y-juvenil/literatura-juvenil.html", #1304
		"https://www.antartica.cl/libros/literatura.html", #7434
		"https://www.antartica.cl/libros/mundo-comic.html", #1176
		"https://www.antartica.cl/libros/referencias.html" #154
	]

	def parse(self, response):	
		for book in response.xpath(".//div[@class='product-item-info']"):
			book_link = book.xpath(".//a[contains(@class, 'photo')]/@href").get()
			if book_link is not None:
				yield {
					"link": book_link
				}
		next_page = response.xpath(".//a[@class='next-page']/@href").get()
		yield response.follow(url=next_page, callback=self.parse)

links_path = os.getcwd() + "/links.csv"
links = pd.read_csv(links_path)
links.drop_duplicates(inplace=True, ignore_index=True)
links_list = [links.iloc[i][0] for i in range(links.shape[0])]

class AntarticaSpider(scrapy.Spider):
	name = "antartica"
	start_urls = links_list

	def parse(self, response):
		loader = ItemLoader(item=BooksScraperItem(), selector=response)
		loader.add_xpath("name", ".//h1[@class='page-title']/span/text()")
		loader.add_xpath("author", ".//div[@class='autor']/a/text()")
		loader.add_xpath("editorial", ".//div[@class='editorial']/a/text()")
		loader.add_xpath("price", ".//span[@class='price']/text()")
		loader.add_xpath("discount", ".//span[@class='discount-percent-configurable']/text()")
		loader.add_xpath("category", ".//span[@id='attr_sub_tema']/text()")
		loader.add_xpath("language", ".//span[@id='attr_idioma']/text()")
		loader.add_xpath("pages", ".//span[@id='attr_n_pagina']/text()")
		loader.add_xpath("review", ".//div[@class='accordion-body']/text()")
		loader.add_xpath("link", "head/meta[@property='og:url']/@content")
		yield loader.load_item()