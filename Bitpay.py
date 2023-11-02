"""
Bitpay.py

author: ironmask

blog: https://ironmask.net
"""

import sqlite3
import json
import time



# ================== Bitpay 시작 ==========================================

class Bitpay:

    def __init__(self, db_conn):
        print("Hello, Now is " + time.ctime() + "\n")

        self.db_conn = db_conn

        self.privatekey = " "
        self.mnemonic_list = []
        self.app_ins_time = " "
        self.app_start_time = " "
        self.wallet_name = " "

# ===================== 개인키 
    def proc_privatekey(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'persist:WALLET\'")  
        all = self.db_conn.fetchone()

        str = ",".join(all)
       # print(str)


        
        idx_address_start = str.find("properties")

        str = str[idx_address_start:]
       # print(str)

        idx_address_start = str.find("{")
        idx_address_end = str.find(",\\\"methods")
        str = str[idx_address_start:idx_address_end]

        str = str.replace('\\', '')

        '''
        str = str.replace('\\', '')
        print(str)

        idx_address_start = str.find("{")
        str = str[idx_address_start:]
        print(str)
        '''

        json_str = json.loads(str)
        print(json_str.get('xPrivKey'))
        self.privatekey = json_str.get('xPrivKey')


        print("============================== 개인키 끝 ============================== \n")

# ===================== 니모닉
    def proc_mnemonic(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'persist:WALLET\'")  
        all = self.db_conn.fetchone()

        str = ",".join(all)
       # print(str)
        
        idx_address_start = str.find("properties")

        str = str[idx_address_start:]
       # print(str)

        idx_address_start = str.find("{")
        idx_address_end = str.find(",\\\"methods")
        str = str[idx_address_start:idx_address_end]

        str = str.replace('\\', '')

        json_str = json.loads(str)
     #   print(json_str)
        print(json_str.get('mnemonic'))

        self.mnemonic_list = json_str.get('mnemonic').split(' ')
      #  print(self.mnemonic_list[0])

        print("============================== 니모닉 끝 ============================== \n")


# ===================== 앱 설치 시간
    def proc_app_ins_time(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'persist:WALLET\'")
        all = self.db_conn.fetchone()

        str = ",".join(all)

        idx_address_start = str.find("{")
        str = str[idx_address_start:]
      #  print(str)
        
        json_str = json.loads(str)
        

        self.app_ins_time = json_str.get('createdOn')
        print(self.app_ins_time)
        print(type(self.app_ins_time))

        print("============================== 앱 설치 시간 끝 ============================== \n")

# ===================== 앱 시작 시간
    def proc_app_start_time(self):
        # xxxxx-events 로 끝나는 key 이름으로 진행...
    #    self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key=?;', [-6:0]\'events\'")

        # 마지막이 events로 끝나는 값 찾기
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key LIKE '%events'")
        all = self.db_conn.fetchone()

        str = ",".join(all)
    #    print(str)

        idx_address_start = str.find("{")
        str = str[idx_address_start:]

       # print(str)
        json_str = json.loads(str)

        self.app_start_time = json_str.get('events')[1].get('timestamp')
        print(self.app_start_time)



        print("============================== 앱 시작 시간 끝 ============================== \n")

# ===================== 지갑 이름
    def proc_wallet_name(self):
        self.db_conn.execute("SELECT * FROM catalystLocalStorage WHERE key = \'persist:WALLET\'")

        all = self.db_conn.fetchone()

        str = ",".join(all)
      #  print(type(str))

                
        idx_address_start = str.find("\"totalBalance")
        idx_address_end = str.find(",\\\"isReadOnly")
        str = str[idx_address_start:idx_address_end]
        
        str = str.replace('\\', '')

        str2 = '{' + str + '}'
   
      #  print(str2)
        # list 형태로 만든 후 인덱싱해서 해보려 했지만..
        # 왜인지는 모르겠지만.. '{' 가 있어야 json 형태로 만들 수 있기에...
        
        #str_list = str.split(',')
        #print(str_list[4])
        

        json_str = json.loads(str2)
      #  print(json_str)
      #  print(type(json_str))
      #  print(json_str.get('keyName'))

        # list 에서 쓸 수 있는 함수들 활용해볼까 했지만..
        #str.insert(0, '{')
        #str.append('}')

        self.wallet_name = json_str.get('keyName')
        print(self.wallet_name)
        print(type(self.wallet_name))


        print("============================== 지갑 이름 끝 ============================== \n")


# ===================== CSV 출력
    def proc_csv(self, csv_conn):

        csv_conn.writerow("")
        csv_conn.writerow("")
        csv_conn.writerow(["========== Bitpay Report =========="])

        csv_conn.writerow(["PrivateKey Start"])
        csv_conn.writerow(['PrivateKey'])
        csv_conn.writerow([self.privatekey])

        csv_conn.writerow("")
        csv_conn.writerow(["Mnemonic Start"])
        csv_conn.writerow(['Mnemonic'])
        csv_conn.writerow([self.mnemonic_list])

        csv_conn.writerow("")
        csv_conn.writerow(["app_ins_time Start"])
        csv_conn.writerow(['app_ins_time'])
        str = self.app_ins_time
        csv_conn.writerow([time.asctime(time.localtime(float(str[:10] + "." + str[10:])))])

        csv_conn.writerow("")
        csv_conn.writerow(["app_start_time Start"])
        csv_conn.writerow(['app_start_time'])
        csv_conn.writerow([self.app_start_time])

        csv_conn.writerow("")
        csv_conn.writerow(["wallet_name Start"])
        csv_conn.writerow(['wallet_name'])
        csv_conn.writerow([self.wallet_name])


# ================== Bitpay 끝 ==========================================

