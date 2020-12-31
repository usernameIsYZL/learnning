import csv
import json
import time
from pprint import pprint
from threading import Thread
from multiprocessing import Process
from queue import Queue
# from urllib import parse
import requests, data_headers, pymongo


class XiaomiSpider:
    def __init__(self):
        # 创建空队列
        self.url_queue = Queue()
        self.url = 'http://app.mi.com/categotyAllListApi?page ={}& categoryId = 5 & pageSize = 30'
        self.app_href_url = 'http://app.mi.com/details?id={}'
        self.headers = data_headers.headers

    # URL地址入队列
    def url_in(self):
        for page in range(100):
            url = self.url.format(str(page))
            self.url_queue.put(url)

    def parse_page(self, html):
        app_json = json.loads(html)
        app_info_list = []
        for app in app_json['data']:
            name = app['displayName']
            href_url = self.app_href_url.format(app['packageName'])
            app_info_list.append([name,href_url])
        return app_info_list

    def save_page_infos(self,ls):
        with open('小米商城—单进程.csv','a',encoding='utf-8') as f:
            writer = csv.writer(f)
            for l in ls:
                writer.writerow(l)

    # 线程的事件函数（请求、解析、保存）
    def get_data(self):
        while True:
            # 从队列中获取URL
            if not self.url_queue.empty():
                url = self.url_queue.get()
                # 发请求，获取响应，提取数据
                html = requests.get(url, headers=self.headers).text
                # 解析
                app_href_list =self.parse_page(html)
                # 保存
                self.save_page_infos(app_href_list)
            else:
                break

    def main(self):
        self.url_in()
        # 创建线程
        t_list = []
        for i in range(1):
            t = Process(target=self.get_data())
            t_list.append(t)
            t.start()
        # 回收线程
        for j in t_list:
            j.join()

if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间：%.2f' % (end - start))
