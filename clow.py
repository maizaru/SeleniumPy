from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import os

driver = webdriver.Chrome("C:\Selenium\chromedriver_win32\chromedriver")
html = ""
htmlT = ""

#driver.find_element_by_name("q").send_keys("キーワード",Keys.ENTER)
def start(webURL):
    #C:\Selenium\chromedriver_win32\chromedriver
    URL = driver.get(webURL)#指定のWebサイトになる
    global html
    html = requests.get(driver.current_url).text
    global htmlT
    htmlT = driver.page_source

    driver.close()


    #driver.quit()

#画像クローリング
def imagesClow():
    soup = BeautifulSoup(html,'lxml')
    images = soup.find_all("img",limit=10)
    for i,img in enumerate(images, start=1):
        src  = img.get("src")
        print("src = ",src)
        print("******************")
        try:
          responce = requests.get(src)
          print("responce = ",responce)
          print("******************")
          with open("img/" + "{}.jpg".format(i), "wb") as f:#要改良
              f.write(responce.content)
              time.sleep(3)#キチンと間隔を２秒以上空けよう
        except:
          print("だめでした")

#テキストのクローリング
def textClow():
    soupT = BeautifulSoup(htmlT,"lxml")
    for i in soupT(['script','style']):#ここでscript,styleタグ（＋それらの子要素も）追加
        i.decompose()#そしてそれらを削除
        #time.sleep(2)#テキストに関して２秒以上止める意味

    text = ' '.join(soupT.stripped_strings)#テキストにしてPrint
    print('***************************************')
    print(text)

if __name__ == "__start__":
    start()
if __name__ == "__imagesClow":
    imagesClow()
if __name__ == "__textClow":
    textClow()