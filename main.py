import csv,os,wget
from decimal import Decimal
from datetime import datetime, timedelta

class System():
    #匯率資料
    _Currency = []
    #我的匯率
    MyCurrency = 'NTD'
    #MyShowCurrency = ['USD', 'HKD', 'GBP', 'AUD', 'CAD', 'SGD', 'CHF', 'JPY', 'SEK', 'NZD', 'THB', 'PHP', 'IDR', 'EUR', 'KRW', 'VND', 'MYR', 'CNY']
    #顯示的匯率
    MyShowCurrency = ['USD', 'HKD', 'MYR', 'CNY']
    #歷史匯率
    MyhistoryCurrency = []
    files = 'ExchangeRate@202005291603.csv'
    nowDate = datetime.now()
    date = '20200529'
    
    def __init__(self):
        pass

    #設定匯率資料
    def makeCurrency(self):
        todo = ['美元','港幣','英鎊','澳大利亞元','加拿大元','新加坡元','瑞士法郎','日元','南非蘭特','瑞典克朗','新西蘭元','泰銖','菲律賓比索','印尼盾','歐元','韓元','越南盾','馬來西亞林吉特','人民幣']
        try:
            with open(self.files,newline='') as csv_file:
                datas = csv.DictReader(csv_file)
                self._Currency =[{'EngCurrency':d['嚜澧urrency'], 'Currency':todo[i], 'Price':d['Cash']} for i,d in enumerate(datas) if (str(d['Cash']) != '0.00000')]
        except ValueError:
            with open(self.files,newline='', encoding='utf-8') as csv_file:
                datas = csv.DictReader(csv_file)
                self._Currency =[{'EngCurrency':d['\ufeff幣別'], 'Currency':todo[i], 'Price':d['現金']} for i,d in enumerate(datas) if (str(d['現金']) != '0.00000')]
        except FileNotFoundError:
            history.updateCurrency()
            opens.makeCurrency()

    #設定輸出字串長度
    def makeString(self,d1,d2):
        text = d1+"（"+d2+"）"
        for i in range(len(text),12):
            text+="　"
        return text
    
    #匯率換算
    def getExchangeRate(self,money):
        try:
            if self.MyCurrency == 'NTD':
                for data in self._Currency:
                    if data['EngCurrency'] in self.MyShowCurrency:
                        print(self.makeString(data['Currency'],data['EngCurrency']),end="   ")
                        print("$ {:>.3f}".format(int(money) / Decimal(data['Price'])))
            else:
                for data in self._Currency:
                    if data['EngCurrency'] == self.MyCurrency:
                        MyNT = Decimal(data['Price'])
                print('台幣（NTD）          ',end="   ")
                print("$ {:.3f}".format(int(money) * MyNT))
                for data in self._Currency:
                    if data['EngCurrency'] != self.MyCurrency and data['EngCurrency'] in self.MyShowCurrency:
                        print(self.makeString(data['Currency'],data['EngCurrency']),end="   ")
                        print("$ {:>.3f}".format(int(money) * (MyNT / Decimal(data['Price']))))
        except ValueError:
            clear()
            print('\n數字輸入有誤，請輸入數字\n')


class User(System):
    def __init__(self):
        super().__init__()

    #所有可用匯率
    def getAvailableCurrency(self):
        for data in self._Currency:
            print(data['EngCurrency'],end='、')
    
    #我的匯率
    def getMyCurrency(self):
        for data in self._Currency:
            if not(data['EngCurrency'] in self.MyShowCurrency):
                print(data['EngCurrency'],end='、')
        print('')    
    
    #所有可新增匯率
    def getCurrency(self):
        for data in self.MyShowCurrency:
            print(data,end='、')
        print('')    

    #設定匯率
    def setMyCurrency(self,MyCurrency):
        for data in self._Currency:
            if data['EngCurrency'] == MyCurrency.upper() or "NTD" == MyCurrency.upper():
                self.MyCurrency = MyCurrency.upper()
                return "匯率切換成功"
        return "您輸入錯誤的匯率，請再嘗試一遍"

    #新增顯示匯率
    def setShowCurrency(self,ShowCurrency):
        if ShowCurrency[0] == "all":
            self.MyShowCurrency = []            
            for data in self._Currency:
                self.MyShowCurrency.append(data['EngCurrency'])
            return self.MyShowCurrency
        else:
            text = []
            for data in self._Currency:
                text.append(data['EngCurrency'])

            for d in ShowCurrency:
                if d.upper() in text:
                    if not(d.upper() in self.MyShowCurrency):
                        self.MyShowCurrency.append(d.upper())
                    else:
                        return "以輸入重複資料\n顯示匯率為："+str(self.MyShowCurrency)
                else:
                   return "資料輸入有誤\n顯示匯率為："+str(self.MyShowCurrency)
            return "新增成功\n顯示匯率為："+str(self.MyShowCurrency)
    #刪除顯示匯率
    def setDeleteShowCurrency(self,ShowCurrency):
        for d in ShowCurrency:
            if d.upper() in self.MyShowCurrency:
                self.MyShowCurrency.remove(d.upper())
            else:
                return "資料輸入有誤\n顯示匯率為："+str(self.MyShowCurrency)
        return "刪除成功\n顯示匯率為："+str(self.MyShowCurrency)


class history(System):
    def __init__(self):
        super().__init__()
    #新增歷史紀錄
    def historyCurrency(self,money):
        try:
            #print(self.MyhistoryCurrency)
            self.MyhistoryCurrency.append([int(money),self.MyCurrency])
        except ValueError:
            return 
    #獲取歷史紀錄
    def gethistoryCurrency(self):
        
        for d in self.MyhistoryCurrency:
            print('     歷史金額：  ('+d[1]+")   $ "+str(d[0]))
            opens.setMyCurrency(d[1])
            opens.getExchangeRate(d[0])
            print('－－－－－－－－－－－－－－－－－－－－－')
    #手動更新資料
    def updateCurrency(self):
        url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
        if opens.nowDate.hour < 17:
            self.nowDate = self.nowDate + timedelta(days=-1)
        opens.date = self.nowDate.strftime("%Y%m%d")
        wget.download(url, './ExchangeRate@'+opens.date+'1603.csv')
        opens.files = 'ExchangeRate@'+opens.date+'1603.csv'
        print('\n資料更新成功，使用日期為：'+opens.date)
        
opens = User()
history = history()
opens.makeCurrency()
clear = lambda: os.system('cls')
clear()
while(True):
    print('\n---------------匯率換算選單---------------')
    print('{:>3７s}'.format('資料版本：'+opens.date))
    print('\n　　1.開始換匯　　　　　2.設定其他換匯　　')
    print('　　3.新增顯示換匯　　　4.刪除顯示換匯　　')
    print('　　5.手動更新匯率　　　6.顯示歷史換匯　　')
    print('－－－－－－－－－－－－－－－－－－－－－')
    num = input('輸入數字開始：')
    if num == "1":
        clear()
        text = input('請輸入金額　'+opens.MyCurrency+' $　')
        history.historyCurrency(text)
        while(text.upper() != "ESC"):
            opens.getExchangeRate(text)
            print('－－－－－－－－－－－－－－－－－－－－－')
            print('跳回畫面請輸入：ESC\n')
            text = input('請輸入金額　'+opens.MyCurrency+' $　')
            history.historyCurrency(text)
        clear()
    if num == "2":
        clear()
        print('您可使用的匯率為：',end='')
        opens.getAvailableCurrency()
        print("NTD")
        print(opens.setMyCurrency(input('請輸入匯率：')))
    if num == "3":
        clear()
        print('您可修改顯示的匯率為：',end='')
        opens.getMyCurrency()
        print('可輸入一個或多個，輸入方式為 EX:USD HKD')
        text = input().split(' ')
        print(opens.setShowCurrency(text))
    if num == "4":
        clear()
        print('您可修改顯示的匯率為：',end='')
        opens.getCurrency()
        print('可輸入一個或多個，輸入方式為 EX:USD HKD')
        text = input().split(' ')
        clear()
        print(opens.setDeleteShowCurrency(text))
    if num == "5":
        clear()
        print(history.updateCurrency())
        opens.makeCurrency()
    if num == "6":
        clear()
        history.gethistoryCurrency()
        text = input('跳回畫面請輸入：ESC\n')
        while(text.upper() != "ESC"):
            history.gethistoryCurrency()
            text = input('跳回畫面請輸入：ESC\n')
        clear()