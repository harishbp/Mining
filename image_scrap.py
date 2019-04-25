from icrawler.examples import GoogleImageCrawler
import os

def crawl(dst_path, search, number_of_images):
    path_to_download = dst_path
    search_name = search

    try:
        google_crawler = GoogleImageCrawler(path_to_download)
        google_crawler.crawl(keyword= search_name, offset=0, max_num=number_of_images,
                                 date_min=None, date_max=None, feeder_thr_num=1,
                                 parser_thr_num=1, downloader_thr_num=4,
                                 min_size=(100,100), max_size=None)
    except:
        print("download failed, downloading next image")


# crawl('./crawler_test/test_01', 'Mona Meshram')
