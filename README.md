# PythonExchangeRate
Python換歲匯率

設計概念

包含基底類別（System）—包含的變數及變數功能
#匯率資料（_Currency = []）
#我的匯率（MyCurrency = 'NTD'）
#顯示的匯率（MyShowCurrency = ['USD', 'HKD', 'MYR', 'CNY']）
#歷史匯率（MyhistoryCurrency = []）
#檔案名稱（files = 'ExchangeRate@202005291603.csv'）
#現在時間（nowDate = datetime.now()）

以及函式
#設定匯率資料（makeCurrency）
#設定輸出字串長度（makeString）
#匯率換算（getExchangeRate）

子類別一 使用者資料（User(System) ）—包含的函式
#所有可用匯率（getAvailableCurrency）
#我的匯率（getMyCurrency）
#所有可新增的顯示匯率（getCurrency）
#設定我的匯率（setMyCurrency）
#新增顯示匯率（setShowCurrency）
#刪除顯示匯率（setDeleteShowCurrency）
子類別二 歷史紀錄（history(System) ）—包含的函式
#新增歷史紀錄（historyCurrency）
#獲取歷史紀錄（gethistoryCurrency）
#手動更新資料（updateCurrency）
測試方式
需下載” C108156102-1.py”、”
ExchangeRate@202005291603.csv”
執行 C108156102-1.py 檔案，進入匯率換算
選單，請輸入 1~6
