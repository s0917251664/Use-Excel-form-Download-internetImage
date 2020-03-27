# Use-Excel-form-Download-internetImage
Use Excel form automatically download internet images.

<h1>Introduction</h1>
<p>The source of the main code is from <br>
https://github.com/ultralytics/google-images-download and https://github.com/ultralytics/google-images-download.<br>
This code Only extended form query functions are provided here.<br>
Want to know more ways to use. Please visit their page for various examples.<br>
利用excel表單，自動讀取表單內容開始逐一下載至指定位置中<br>
</p>
<h1>Install</h1>
<p>
  <ul>
    <li>git clone https://github.com/s0917251664/Use-Excel-form-Download-internetImage
    <li>cd Use-Excel-form-Download-internetImage</li>
    <li>pip install -U -r requirements.txt</li>
</ul>

</p>
<h1>Requirements</h1>
<ul>
    <li>Python 3.7 later</li>
    <li>xlrd</li>
</ul>

<h1>Use</h1>
<ol>
    <li>請先確定Chrome版本號，再依照版本載入對應的chromedriver：https://chromedriver.chromium.org/</li>
    <li>開啟附錄的excel表格參考輸入對應查詢格式</li>
    <li>執行AutoSearch.py -p (欲存放的位置) -cp (chromedriver存放位置)  -wp sample.xlsx  </li>
</ol>
  <p>
  --limt可控制下載數量<br>
  --delay可控制下載圖片的間隔秒數
  </p>
