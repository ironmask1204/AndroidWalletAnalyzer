"""
Tokenpocket.py

author: ironmask

blog: https://ironmask.net
"""


import sqlite3
import json
import time

# ================== Tokenpocket 시작 ==========================================

class Tokenpocket:

    def __init__(self, db_conn):
        print("Hello, Now is " + time.ctime() + "\n")

        self.db_conn = db_conn

        self.wallet_address = []


# ===================== 지갑 주소
    def proc_address(self):
        # DOGE로 끝나는 값에 대해서 조
        self.db_conn.execute("SELECT walletinfo FROM WalletTokenRef WHERE tokenKey LIKE '%DOGE'")

        
        # fetchone() 와 fetchall()의 차이는... 모두 찾아주냐 아니냐?.. 기존 함수도 검토가...
        all = self.db_conn.fetchall() 
        print(all)

        for val in all:
            str = ",".join(val)
            str = str[3:] # 앞 3자리는 ID_ 로 붙은 tag
            self.wallet_address.append(str)
        
            print(str)
            print('=========================================')
       


        print("============================== 지갑 주소 끝 ============================== \n")


# ===================== CSV 출력
    def proc_csv(self, csv_conn):

        csv_conn.writerow("")
        csv_conn.writerow("")
        csv_conn.writerow(["========== Token Pocket Report =========="])

        result_colname = ['address']
        
        csv_conn.writerow(["wallet address Start"])
        csv_conn.writerow(result_colname)

        for val in self.wallet_address:
            csv_conn.writerow([val])

        

# ================== Tokenpocket 끝 ==========================================

