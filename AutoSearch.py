# -*- coding: UTF-8 -*-
import os
import requests
import csv
import xlrd
import hashlib
chromedriver_path=""#chromedriver的存放位置
path=""#要下載的資料夾位置
limit="10"
delay="1"
def file_md5(file_name, block_size=2**20):
    if not os.path.isfile(file_name):
        return
    hash = hashlib.md5()
    with open(file_name, 'rb') as f:
        while True:
            b = f.read(block_size)
            if not b:
                break
            hash.update(b)
        return hash.hexdigest()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limt", type=str,
                    help="下載圖片的數量")
    parser.add_argument("-d", "--delay", type=str,
    help="下載圖片的間隔秒數")
    parser.add_argument("-p", "--downloadpath", type=str,
    help="下載圖片的存放位置")
    parser.add_argument("-cp", "--chromedriverpath", type=str,
    help="chromedriver存放位置")
    parser.add_argument("-wp", "--workbookpath", type=str,
    help="excel表單存放位置")
    args = parser.parse_args()
    flag=False
    if any(args.workbookpath):
        # 打開excel文件
        print(args.workbookpath)
        workbook = xlrd.open_workbook(args.workbookpath)
        sheet = workbook.sheet_by_index(0)
        print("Open Excel workbook :"+args.workbookpath)
        flag=True
    else:
        flag=False
        print("請輸入完整路徑")
    if any(args.downloadpath):
        path=args.downloadpath
        print("downloadpath:"+path)
        flag=True
    else:
        flag=False
        print("請輸入完整路徑")
    if any(args.chromedriverpath):
        chromedriver_path=args.chromedriverpath
        print("chromedriver_path:"+chromedriver_path)
        flag=True
    else:
        flag=False
        print("請輸入完整路徑")

    # 获取整行和整列的值（数组）
    for r in range(1,sheet.nrows):
        print(sheet.row_values(r)[1]+"開始搜尋")
        file_name=(str)(r)+"."+sheet.row_values(r)[0]# 获取第四列内容
        downloadpath=path+"/"+file_name
        os.mkdir(downloadpath)#製作路徑資料夾
        Pypath= "python3 bing_scraper.py --url 'https://www.bing.com/images/search?q="+sheet.row_values(r)[1]+"' --limit "+limit+" --delay "+delay+" --download --output_directory '"+downloadpath+"' --chromedriver "+chromedriver_path
        os.system(Pypath)
        for root, dirs, files in os.walk(downloadpath):
            for file in files:
                file_path = os.path.join(root, file)
                md5 = file_md5(file_path)
                print (file_path, md5)
                if md5:
                    os.rename(file_path, os.path.join(root, md5)+'.jpg')
        