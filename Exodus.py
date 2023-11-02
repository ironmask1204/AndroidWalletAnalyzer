"""
Exodus.py

author: ironmask

blog: https://ironmask.net
"""


import sqlite3
import json
import time



# ================== Exodus 시작 ==========================================

class Exodus:

    def __init__(self, db_conn):
        print("Hello, Now is " + time.ctime() + "\n")

        self.db_conn = db_conn

        self.address = " "
        self.dict_trans_list = []
        self.app_ins_time = " "
        self.app_start_time = " "

# =====================지갑주소
    def proc_address(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'!blockchain!!v1!!states!exodus_0:dogecoin\'")  
        all = self.db_conn.fetchone()
  
        str = ",".join(all)
        str.find("address")

        # "address":" 이후에 " 인덱스 찾기
        idx_address_start = str.find("address")+10
        idx_address_end = idx_address_start + str[str.find("address")+10:].find("\"")

        print(str[idx_address_start:idx_address_end])
        self.address = str[idx_address_start:idx_address_end]
        print("============================== 지갑 주소 끝 ============================== \n")

# ===================== 거래내역
    def proc_transaction(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'!blockchain!!v1!!txs!exodus_0:dogecoin\'")
        all = self.db_conn.fetchone()

        str = ",".join(all)
        idx_address_start = str.find("[")

        str = str[idx_address_start:]
        json_str = json.loads(str)

        
        

    # json dict 구조 {}는 dict 이고, []는  list 인 것을 주의!!
        for i in range(0, len(json_str)):
            dict = {'txid':' ', 'date':' ', 'amount':' ', 'coinName':' ', 'from_sent':' ', 'to':' '}
            
            dict['txid'] = json_str[i].get('txId')
            dict['date'] = json_str[i].get('date')
            dict['amount'] = json_str[i].get('coinAmount')
            dict['coinName'] = json_str[i].get('coinName')
            if(json_str[i].get('from') == None):
                dict['from_sent'] = json_str[i].get('data').get('sent')[0].get('address')
            else:
                dict['from_sent'] = json_str[i].get('from')[0]
            dict['to'] = json_str[i].get('addresses')[0].get('address')

            self.dict_trans_list.append(dict)
            print(dict)
            print('=========================================')

          #  print(dict_list[i]['from_sent'])

        print("============================== 거래 내역 끝 ============================== \n")


# ===================== 앱 설치 시간
    def proc_app_ins_time(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'wallet:account0.config\'")
        all = self.db_conn.fetchone()

        str = ",".join(all)
        idx_address_start = str.find("{")

        str = str[idx_address_start:]
        #print(str)
        json_str = json.loads(str)

        self.app_ins_time = json_str.get('wentThroughOnboarding')
        print(self.app_ins_time)

        print("============================== 앱 설치 시간 끝 ============================== \n")

# ===================== 앱 시작 시간
    def proc_app_start_time(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'wallet:account0.customTokensLastUpdate\'")
        all = self.db_conn.fetchone()

        self.app_start_time = all[1]
        print(self.app_start_time)
        print(type(self.app_start_time))

        print("============================== 앱 시작 시간 끝 ============================== \n")


# ===================== CSV 출력
    def proc_csv(self, csv_conn):

        csv_conn.writerow("")
        csv_conn.writerow("")
        csv_conn.writerow(["========== Exodus Report =========="])


        result_colname = ['txid', 'date', 'amount', 'coinName', 'receive from or send to', 'wallet address']
       

        csv_conn.writerow(["wallet address Start"])
        csv_conn.writerow(['address'])
        csv_conn.writerow([self.address])

        csv_conn.writerow("")
        csv_conn.writerow(["transaction_list Start"])
        csv_conn.writerow(result_colname)

        result = []
        for val in self.dict_trans_list:
            result.clear()
            result.append(val.get('txid'))
            result.append(val.get('date'))
            result.append(val.get('amount'))
            result.append(val.get('coinName'))
            result.append(val.get('from_sent'))
            result.append(val.get('to'))
     
            csv_conn.writerow(result)

        csv_conn.writerow("")
        csv_conn.writerow(["app_ins_time Start"])
        csv_conn.writerow(['app_ins_time'])
        csv_conn.writerow([self.app_ins_time])

        csv_conn.writerow("")
        csv_conn.writerow(["app_start_time Start"])
        str = self.app_start_time
        csv_conn.writerow(['app_start_time'])
        csv_conn.writerow([time.asctime(time.localtime(float(str[:10] + "." + str[10:])))])

# ================== Exodus 끝 ==========================================

