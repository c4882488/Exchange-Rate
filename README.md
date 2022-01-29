# OOP Conversion Rate

## Introduction

Designing an exchange rate conversion program using python OOP

## Description

OOP design mode, create exchange rate conversion, set the exchange rate, set the exchange rate currency, update the exchange rate data, and display the history of the meeting

<img title="" src="https://s2.loli.net/2022/01/29/1QpYVF7WqMvR23k.jpg" alt="img1.jpg" data-align="center">

## Getting Started

1. Download file
   
   - main.py
   
   - ExchangeRate@202005291603.csv

2. install python packget
   
   ```
   pip install wgetpip install wget
   ```

---

Run main.py to enter the exchange rate conversion menu, enter 1~6 to use the functions

<img title="" src="https://s2.loli.net/2022/01/29/1QpYVF7WqMvR23k.jpg" alt="Screenshot 2022-01-29 161245.jpg" data-align="center">

Enter 1 to start the exchange

<img title="" src="https://s2.loli.net/2022/01/29/AjnkGwmQvFHeIhN.jpg" alt="img2.jpg" data-align="center">

Enter 2, set your own exchange currency

<img title="" src="https://s2.loli.net/2022/01/29/4wzsFBgUkuiXNly.jpg" alt="img3.jpg" data-align="center">

Enter 3 to set the displayed exchange rate

Enter 4 to delete the displayed exchange rate

<img title="" src="https://s2.loli.net/2022/01/29/b3N2Bfa1Wj7vIm9.jpg" alt="img4.jpg" data-align="center">

Enter 5 and update the exchange rate

<img title="" src="https://s2.loli.net/2022/01/29/yd7TnR2Ys8bHmBi.jpg" alt="img6.jpg" data-align="center">

Enter 6 to display the exchange history

<img title="" src="https://s2.loli.net/2022/01/29/3wFdmYbISaqD1Co.jpg" alt="img5.jpg" data-align="center">

---

#### Design Concept

###### Substrate type included（System）

1. Variables
   
   - Exchange Rate Information（_Currency = []）
   
   - My Exchange Rate（MyCurrency = 'NTD'）
   
   - Displayed exchange rates（MyShowCurrency = ['USD', 'HKD', 'MYR', 'CNY']）
   
   - Historical Exchange Rates（MyhistoryCurrency = []）
   
   - File Name（files = '[ExchangeRate@202005291603.csv](mailto:ExchangeRate@202005291603.csv)'）
   
   - Now Time（nowDate = datetime.now()）

2. Functions
   
   - Set up exchange rate information（makeCurrency）
   
   - Set the output string length（makeString）
   
   - Exchange rate conversion（getExchangeRate）

###### Subcategory

1. User Information（User）—Included functions
   
   - All available exchange rates（getAvailableCurrency）
   
   - My Exchange Rate（getMyCurrency）
   
   - All new display rates available（getCurrency）
   
   - Set my exchange rate（setMyCurrency）
   
   - New Display Rate（setShowCurrency）
   
   - Delete Show Rate（setDeleteShowCurrency）

2. Historical Record（history）—Included functions
   
   - New Historical Records（historyCurrency）
   
   - Historical Records（gethistoryCurrency） 
   
   - Manual update of data（updateCurrency）

## 

## Use of Resources

[Bank Of Taiwan](https://rate.bot.com.tw/)

---

[中文](https://github.com/c4882488/PythonExchangeRate/blob/master/README_china.md)
