import os

from icrawler.builtin import BingImageCrawler

def download(keyword:str,number:int,image_dir:str)->None:

    if not(os.path.exists(image_dir)):
        os.mkdir(image_dir)
    for filename in os.listdir(image_dir):
        os.remove(os.path.join(image_dir,filename))
    bing_crawler = BingImageCrawler(storage={'root_dir': image_dir})
    bing_crawler.crawl(keyword=keyword, max_num=number)