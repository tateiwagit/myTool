# 作業目標　ルカリオのエロ画像スレで画像を抽出してダウンロードする　半達成

from bs4 import BeautifulSoup
import requests
import os
import re
import time
from time import sleep

import urllib.robotparser
import re


class downloader():
    imgdir = ""
    srcdir = ""
    is_robot_ok = None
    
    def __init__(self, imgdir, srcdir):  # ダウンロードするための環境を整える
        """
        preparate directry to download source or img
        """
        self.make_or_None_dir(imgdir)
        self.make_or_None_dir(srcdir)

        self.imgdir = imgdir
        self.srcdir = srcdir

    def make_or_None_dir(self, path):
        """
        make directry that is not exits yet.
        """
        if not os.path.exists(path):# dirが存在しない場合は作成
            os.mkdir(path)
            return True
        else: return None
    
    def download_webPage(self, url, load_dir):
        """
        make file that named source_(soup.title).txt in load_dir. return path.
        """
        def url_check(url):
            tester = self.robots_tester(url)
            judge = tester.check_is_robots_ok(url, tester.robot_url)
            return judge

        self.is_robot_ok = url_check(url)
        
        page = requests.get(url)
        page_source = page.text
    
        soup = BeautifulSoup(page.content, "lxml")
        title = soup.find("title")
    
        # フォルダとファイル名の設定
        file_path = os.path.join(srcdir, f"source_{title.string}.html")
        return self.make_or_None_file(file_path, page_source)


    def make_or_None_file(self, file_path, page_source):
        """
        make file that is not exits.
        """
        # ページソースを取得    
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(page_source)
        return file_path 

    def request_for_web(self, req_interval):
        """(web_)method is always call this method"""
        sleep(req_interval)
        pass

    def web_download_img(self, req_interval,image_url, imgdir):
        """Download image of image_url into imgdir. Must call request_for_web(req_interval).
        (req_interval: interval for requests.get() image_url: src in webpage, imgdir: directry to download image)"""
        self.request_for_web(req_interval)

        # 画像をダウンロードして保存
        response = requests.get(image_url)
        if response.status_code == 200:
            image_filename = os.path.basename(image_url)  # URLからファイル名を取得
            image_path = os.path.join(imgdir, image_filename)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
                print(f"Image downloaded and saved to {image_path}")
        else:
            print("Failed to download image")


    class robots_tester():
        """check url that is ok or out to scrapying"""
        is_robots_ok = None
        robot_url = ""
        
        def __init__(self, url):
            self.robot_url = self.make_robots_url(url)
            
        def make_robots_url(self, url):
            # 正規表現によりサイトのURLを取得
            def get_root_url(url):
                pattern = r'(?P<root>https?://.*?)\/.*'
                result = re.match(pattern, url)
                if result is not None:
                    return result.group('root')

            # サイトのURLからrobots.txtのURLを生成
            def get_robots_txt_path(root_url):
                return root_url + '/robots.txt'

            root_url = get_root_url(url)
            robots_txt_url = get_robots_txt_path(root_url)
            return robots_txt_url

        def check_is_robots_ok(self, check_url, robot_url):
            # インスタンスの作成
            ur = urllib.robotparser.RobotFileParser()
            # robots.txtのURLセット
            ur.set_url(robot_url)
            # robot.txtの解析
            ur.read()

            # スクレイピング可能かチェック
            self.is_robots_ok = ur.can_fetch("*", check_url)
            print("check ok? {0} : {1}".format(check_url, self.is_robots_ok))
            
            ur = None
            return self.is_robots_ok


nowdir = os.getcwd()  # 現在のディレクトリを取得            
imgdir = os.path.join(nowdir, "imgdir")  # 画像をダウンロードするディレクトリのパスを作成        
srcdir = os.path.join(nowdir, "sources") # ソースコードをダウンロードするディレクトリのパスを作成
dw = downloader(imgdir, srcdir)
#url_example = "https://moeimg.net/9977.html"
url_example = "http://lucalucagogo.blog103.fc2.com/"
url = 'https://nijie.info/view.php?id=554023'
example_path = dw.download_webPage(url, dw.srcdir)


# html_doc = open(example_path)
# soup = BeautifulSoup(html_doc, features="lxml")
# soup = soup.body
# soup_list = soup.find_all("img", alt=True, src=re.compile('.jpg$'))
# for term in range(len(soup_list)):
#     soup_list[term] = soup_list[term]['src']

# req_interval = 3
# for term in range(len(soup_list)):
#     print("start downloading {0}".format(soup_list[term]))
#     time_start = time.time()
#     dw.web_download_img(req_interval, soup_list[term], dw.imgdir)
#     time_end = time.time()

#     print("success download {0}\n".format(soup_list[term]))
#     print("loading interval {0}".format(time_end - time_start))
