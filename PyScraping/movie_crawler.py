import scrapy


class MovieSpider(scrapy.Spider):
    #name od my bot or spider it should be unique
    name="moviebot"

#from here it starts to crawl
    start_urls=['https://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_2']

#after each succesful crawl this method will be called where you implememnt
    #your code to parse data and save
    def parse(self,response):
        movie_name=response.xpath('//h3[@class="lister-item-header"]/a/text()').extract()
        year=response.xpath('//span[@class="lister-item-year text-muted unbold"]/text()').extract()
        director_name=response.xpath('//div[@class="lister-item-content"]/p[3]/a[1]/text()').extract()

        for item in zip(movie_name,year,director_name):
            #putting data as dicts
            info_items={
                'Movie':item[0],
                'Year':item[1],
                'Director':item[2]
                }
            #printing dubgging messeges
            self.logger.info("Amit Kumar")

            yield info_items
             

        
