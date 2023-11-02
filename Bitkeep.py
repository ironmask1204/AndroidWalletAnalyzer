"""
Bitkeep.py

author: ironmask

blog: https://ironmask.net
"""

import sqlite3
import json
import time

# ================== Bitkeep 시작 ==========================================

class Bitkeep:

    def __init__(self, db_conn):
        print("Hello, Now is " + time.ctime() + "\n")

        self.db_conn = db_conn

        self.address = " "
        self.dict_trans_list = []
        self.app_ins_time = " "
        self.wallet_name = " "

# =====================지갑주소
    def proc_address(self):
        self.db_conn.execute("SELECT address FROM my_coins WHERE chain = \'doge\'")  
        all = self.db_conn.fetchone()
       # print(all)
       # print(type(all))
  
        str = ",".join(all)
        print(str)
        print(type(str))

        self.address = str

        '''
        str.find("address")

        # "address":" 이후에 " 인덱스 찾기
        idx_address_start = str.find("address")+10
        idx_address_end = idx_address_start + str[str.find("address")+10:].find("\"")

        print(str[idx_address_start:idx_address_end])
        self.address = str[idx_address_start:idx_address_end]
        '''
        print("============================== 지갑 주소 끝 ============================== \n")

# ===================== 거래내역
    def proc_transaction(self):
        self.db_conn.execute("SELECT ext FROM my_coins WHERE chain = \'doge\'")
        all = self.db_conn.fetchone()

        str = ",".join(all)
       # print(str)

        json_str = json.loads(str)

        txs_str = json_str.get('txs')
        #print(txs_str)

        '''
        idx_address_start = str.find("[")

        str = str[idx_address_start:]
        json_str = json.loads(str)
         ''' 

        
        print(len(txs_str));
        

    # json dict 구조 {}는 dict 이고, []는  list 인 것을 주의!!
        for i in range(0, len(txs_str)):
            dict = {'txid':' ', 'time':' ', 'amount':' ', 'direction':' ', 'to':' '}
            
            dict['txid'] = txs_str[i].get('txid')
            dict['time'] = txs_str[i].get('time')
            dict['amount'] = txs_str[i].get('amount')
            dict['direction'] = txs_str[i].get('direction')
            dict['to'] = txs_str[i].get('to')

            self.dict_trans_list.append(dict)
            print(dict)
            print('=========================================')

      #  print(len(self.dict_trans_list))
      #  print(self.dict_trans_list[1])

        print("============================== 거래 내역 끝 ============================== \n")


# ===================== 앱 설치 시간
    def proc_app_ins_time(self):
        self.db_conn.execute("SELECT create_time FROM my_identities_log")
        all = self.db_conn.fetchone()

        print(all)
        print(type(all))

        str = all[0]

        print(str)
        print(type(str))

        self.app_ins_time = str

        print("============================== 앱 설치 시간 끝 ============================== \n")
       

# ===================== 지갑 이름
    def proc_wallet_name(self):
        self.db_conn.execute("SELECT name FROM my_identities")

        all = self.db_conn.fetchone()

        print(all)
        print(type(all))

        str = all[0]

        print(str)
        print(type(str))

        self.wallet_name = str

        print("============================== 지갑 이름 끝 ============================== \n")


# ===================== CSV 출력
    def proc_csv(self, csv_conn):

        csv_conn.writerow("")
        csv_conn.writerow("")
        csv_conn.writerow(["========== BitGet Wallet Report =========="])


        result_colname = ['txid', 'date', 'amount', 'direction', 'to']
       

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
            str = val.get('time')
            result.append(time.asctime(time.localtime(str)))
            result.append(val.get('amount'))
            result.append(val.get('direction'))
            result.append(val.get('to'))
     
            csv_conn.writerow(result)

        csv_conn.writerow("")
        csv_conn.writerow(["app_ins_time Start"])
        csv_conn.writerow(['app_ins_time'])
        str = self.app_ins_time
        csv_conn.writerow([time.asctime(time.localtime(str))])

        csv_conn.writerow("")
        csv_conn.writerow(["wallet_name Start"])
        csv_conn.writerow(['wallet_name'])
        csv_conn.writerow([self.wallet_name])

# ================== Bitkeep 끝 ==========================================

