# 作業目標　ルカリオの画像スレで画像を抽出してダウンロードする　半達成

from bs4 import BeautifulSoup
import requests
import os
import re
import time
from time import sleep


def init_local():  # ダウンロードするための環境を整える
    """引数　反し値　無し
    ローカルにページソースや画像をダウンロードするためのディレクトリを用意する
    """
    nowdir = os.getcwd()  # 現在のディレクトリを取得

    imgdir = os.path.join(nowdir, "imgdir")  # 画像をダウンロードするディレクトリのパスを作成
    make_or_None_dir(imgdir)
    print("makedirs 1")

    srcdir = os.path.join(nowdir, "sources")  # ソースコードをダウンロードするディレクトリのパスを作成
    make_or_None_dir(srcdir)
    return srcdir, imgdir


def make_or_None_dir(path):
    """引数　作ろうとしているディレクトリのパス　反し値　ブール代数
    受け取ったディレクトリがあるかどうか判定する。
    無ければ作る。有れば何もしない
    """
    if not os.path.exists(path):  # dirが存在しない場合は作成
        os.mkdir(path)
        return True
    else:
        return None


def download_webPage(url, load_dir):
    """引数　webページのurl    返し値　ここでダウンロードしたページのpath
    直下ディレクトリ(srcdir)にsource_(soup.title).txtを作成。
    urlからページタイトル、htmlソースを取得してダウンロード。
    最後にダウンロードファイルのpathを返却
    """
    page = requests.get(url_example)
    page_source = page.text

    soup = BeautifulSoup(page.content, "lxml")
    title = soup.find("title")

    # フォルダとファイル名の設定
    file_path = os.path.join(srcdir, f"source_{title.string}.html")
    return make_or_None_file(file_path, page_source)


def make_or_None_file(file_path, page_source):
    """引数　作ろうとしているディレクトリのパス　反し値　ブール代数
    受け取ったディレクトリがあるかどうか判定する。
    無ければ作る。有れば何もしない
    """
    # ページソースを取得
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(page_source)
    return file_path


def request_for_web(req_interval):
    """webへのリクエストをする(web_)メソッドには必ずつける"""
    sleep(req_interval)
    pass


def web_download_img(req_interval, image_url, imgdir):
    """Download image of image_url into imgdir.
    Must call request_for_web(req_interval).
    (req_interval: interval for requests.get()
    image_url: src in webpage, imgdir: directry to download image)"""
    request_for_web(req_interval)

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


srcdir, imgdir = init_local()

# url_example = "https://moeimg.net/9977.html"
url_example = "http://lucalucagogo.blog103.fc2.com/"

example_path = download_webPage(url_example, srcdir)

html_doc = open(example_path)
soup = BeautifulSoup(html_doc, features="lxml")
soup = soup.body
soup_list = soup.find_all("img", alt=True, src=re.compile('.jpg$'))
for term in range(len(soup_list)):
    soup_list[term] = soup_list[term]['src']

req_interval = 3
for term in range(len(soup_list)):
    print("start downloading {0}".format(soup_list[term]))
    time_start = time.time()
    web_download_img(req_interval, soup_list[term], imgdir)
    time_end = time.time()

    print("success download {0}\n".format(soup_list[term]))
    print("loading interval {0}".format(time_end - time_start))
