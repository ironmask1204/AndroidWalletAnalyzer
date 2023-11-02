"""
Defi.py

author: ironmask

blog: https://ironmask.net
"""


import sqlite3
import json
import time

# ================== Defi 시작 ==========================================

class Defi:

    def __init__(self, db_conn):
        print("Hello, Now is " + time.ctime() + "\n")

        self.db_conn = db_conn

        self.wallet_name = " "
        self.dict_trans_list = []
        
# ===================== 거래내역
    def proc_transaction(self):     
        
        self.db_conn.execute("SELECT hash FROM tb_transaction WHERE symbol = \'DOGE\'")
        all = self.db_conn.fetchone()

        # json dict 구조 {}는 dict 이고, []는  list 인 것을 주의!!
        for val in all:
            dict = {'txid':' ', 'time':' ', 'direction':' ', 'to':' ', 'from':' '}

            self.db_conn.execute("SELECT hash FROM tb_transaction WHERE symbol = \'DOGE\'")
            val = self.db_conn.fetchone()
            str = ",".join(val)
            dict['txid'] = str

            self.db_conn.execute("SELECT date FROM tb_transaction WHERE symbol = \'DOGE\'")
            val = self.db_conn.fetchone()
            str = ",".join(val)
            dict['time'] = str

            self.db_conn.execute("SELECT type FROM tb_transaction WHERE symbol = \'DOGE\'")
            val = self.db_conn.fetchone()
            str = ",".join(val)
            dict['direction'] = str

            self.db_conn.execute("SELECT to_address FROM tb_transaction WHERE symbol = \'DOGE\'")
            val = self.db_conn.fetchone()
            str = ",".join(val)
            dict['to'] = str

            self.db_conn.execute("SELECT from_address FROM tb_transaction WHERE symbol = \'DOGE\'")
            val = self.db_conn.fetchone()
            str = ",".join(val)
            dict['from'] = str
            

            self.dict_trans_list.append(dict)
            print(dict)
            print('=========================================')
        

        print("============================== 거래 내역 끝 ============================== \n")
        

# ===================== 지갑 이름
    def proc_wallet_name(self):
        self.db_conn.execute("SELECT wallet_name FROM tb_transaction WHERE symbol = \'DOGE\'")

        all = self.db_conn.fetchone()

        str = ",".join(all)
        self.wallet_name = str
        

        print(self.wallet_name)
        print(type(self.wallet_name))


        print("============================== 지갑 이름 끝 ============================== \n")


# ===================== CSV 출력
    def proc_csv(self, csv_conn):

        csv_conn.writerow("")
        csv_conn.writerow("")
        csv_conn.writerow(["========== DeFi Wallet Report =========="])

        result_colname = ['txid', 'date', 'direction', 'to', 'from']


        csv_conn.writerow(["transaction_list Start"])
        csv_conn.writerow(result_colname)

        result = []
        for val in self.dict_trans_list:
            result.clear()
            result.append(val.get('txid'))
            result.append(val.get('time'))
            result.append(val.get('direction'))
            result.append(val.get('to'))
            result.append(val.get('from'))
            
            csv_conn.writerow(result)

        csv_conn.writerow("")
        csv_conn.writerow(["wallet name Start"])
        csv_conn.writerow([self.wallet_name])


# ================== Defi 끝 ==========================================

