"""
Enjin.py

author: ironmask

blog: https://ironmask.net
"""

import sqlite3
import json
import time

# ================== Enjin 시작 ==========================================

class Enjin:

    def __init__(self, db_conn):
        print("Hello, Now is " + time.ctime() + "\n")

        self.db_conn = db_conn
        
        self.dict_trans_list = []
        
# ===================== 거래내역
    def proc_transaction(self):



        # 테이블 리스트 확인
        table_check_query = "SELECT name FROM sqlite_master WHERE type='table'" # AND name='mytable'"
        self.db_conn.execute(table_check_query)  
        table_list = self.db_conn.fetchall()

        

        print(table_list)
        print(type(table_list))

        for val in table_list:

            # dictionary 항목 정의 
            dict = {'time':' ', 'coinname':' ', 'contactname':' ', 'to':' '}

            
           # table_check_query = "PRAGMA table_info('%s')" %(str_table)
            str_table = ",".join(val)
        #    print(str_table)

            # 테이블 내 컬럼 값들 확인
            self.db_conn.execute("PRAGMA table_info('%s')" %(str_table))
            col_list = self.db_conn.fetchall()
        #    print(col_list)

            # col_list 값은 list 형태로 1차원 배열 마다 컬럼의 특성 등 여러  값이 들어가고, 2차원 배열 내 2번째 인덱스가 colum 값임
            if(col_list[0][1] == 'a' and col_list[1][1] == 'n' and col_list[2][1] == 'nn' and col_list[3][1] == 'f' and col_list[4][1] == 'd'):
                self.db_conn.execute("SELECT * FROM '%s'" %(str_table))  
                all = self.db_conn.fetchone()

                print(val)
                print(all)

                str = all[4]
                print(time.asctime(time.localtime(str)))


                dict['time'] = time.asctime(time.localtime(str))
                dict['coinname'] = all[1]
                dict['contactname'] = all[2]
                dict['to'] = all[0]

                self.dict_trans_list.append(dict)
                

        print("============================== 거래 내역 끝 ============================== \n")

# ===================== CSV 출력
    def proc_csv(self, csv_conn):

        csv_conn.writerow("")
        csv_conn.writerow("")
        csv_conn.writerow(["========== Enjin Wallet Report =========="])
        result_colname = ['date', 'coinname', 'contactname', 'to']

        csv_conn.writerow(["transaction_list Start"])
        csv_conn.writerow(result_colname)

        result = []   
        for val in self.dict_trans_list:
            result.clear()            
            result.append(val.get('time'))
            result.append(val.get('coinname'))
            result.append(val.get('contactname'))
            result.append(val.get('to'))
     
            csv_conn.writerow(result)
        

# ================== Enjin 끝 ==========================================

