# OOP Conversion Rate

## Introduction

使用python OOP設計一款匯率換算程式



## Description

OOP設計模式，製作匯率換算，可使設定匯率，設定換匯幣別，更新匯率資料，顯示歷史患會記錄

<img title="" src="https://s2.loli.net/2022/01/29/1QpYVF7WqMvR23k.jpg" alt="img1.jpg" data-align="center">

## Getting Started

1.  Download file
   
   - main.py
   
   - ExchangeRate@202005291603.csv

2. install python packget
   
   ```
   pip install wgetpip install wget
   ```

---

執行main.py進入匯率換算選單，輸入 1~6即可使用各項功能

<img title="" src="https://s2.loli.net/2022/01/29/1QpYVF7WqMvR23k.jpg" alt="Screenshot 2022-01-29 161245.jpg" data-align="center">

輸入1，開始換匯

<img title="" src="https://s2.loli.net/2022/01/29/AjnkGwmQvFHeIhN.jpg" alt="img2.jpg" data-align="center">

輸入2，設定本身的換匯幣別

<img title="" src="https://s2.loli.net/2022/01/29/4wzsFBgUkuiXNly.jpg" alt="img3.jpg" data-align="center">

輸入3，設定顯示換匯幣別

輸入4，刪除顯示換匯幣別

<img title="" src="https://s2.loli.net/2022/01/29/b3N2Bfa1Wj7vIm9.jpg" alt="img4.jpg" data-align="center">

輸入5，更新匯率

<img title="" src="https://s2.loli.net/2022/01/29/yd7TnR2Ys8bHmBi.jpg" alt="img6.jpg" data-align="center">

輸入6，顯示換匯歷史紀錄



<img title="" src="https://s2.loli.net/2022/01/29/3wFdmYbISaqD1Co.jpg" alt="img5.jpg" data-align="center">

---

#### 設計概念

###### 包含基底類別（System）

1. 變數及變數功能
   
   - 匯率資料（_Currency = []）
   
   - 我的匯率（MyCurrency = 'NTD'）
   
   - 顯示的匯率（MyShowCurrency = ['USD', 'HKD', 'MYR', 'CNY']）
   
   - 歷史匯率（MyhistoryCurrency = []）
   
   - 檔案名稱（files = '[ExchangeRate@202005291603.csv](mailto:ExchangeRate@202005291603.csv)'）
   
   - 現在時間（nowDate = datetime.now()）

2. 函式
   
   - 設定匯率資料（makeCurrency）
   
   - 設定輸出字串長度（makeString）
   
   - 匯率換算（getExchangeRate）
     
     

###### 子類別

1. 使用者資料（User(System) ）—包含的函式 
   
   - 所有可用匯率（getAvailableCurrency）
   
   - 我的匯率（getMyCurrency）
   
   - 所有可新增的顯示匯率（getCurrency）
   
   - 設定我的匯率（setMyCurrency）
   
   - 新增顯示匯率（setShowCurrency）
   
   - 刪除顯示匯率（setDeleteShowCurrency）

2. 歷史紀錄（history(System) ）—包含的函式 
   
   - 新增歷史紀錄（historyCurrency）
   
   - 獲取歷史紀錄（gethistoryCurrency） 
   
   - 手動更新資料（updateCurrency）

## 

## Use of Resources

[Bank Of Taiwan](https://rate.bot.com.tw/)

---
