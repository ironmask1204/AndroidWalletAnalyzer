"""
MainLogic.py.py

author: ironmask

blog: https://ironmask.net
"""

import sqlite3
import csv
import time
import Exodus
import Bitkeep
import Bitpay
import Tokenpocket
import Enjin
import Defi

class MainLogic:

    # def __init__(self, exodusFilePath, bitgetFilePath, bitpayFilePath, tokenpocketFilePath, enjinFilePath, defiFilePath):
    def __init__(self, FilePathList, checkList):
        print("Hello, Now is " + time.ctime() + "\n")

        self.exodusFilePath = FilePathList[0]
        self.bitgetFilePath = FilePathList[1]
        self.bitpayFilePath = FilePathList[2]
        self.tokenpocketFilePath = FilePathList[3]
        self.enjinFilePath = FilePathList[4]
        self.defiFilePath = FilePathList[5]

        self.checkList = checkList
        
        print(self.exodusFilePath)
        print(self.bitgetFilePath)
        print(self.bitpayFilePath)
        print(self.tokenpocketFilePath)
        print(self.enjinFilePath)
        print(self.defiFilePath)


    def start(self):

        # ===========================  Exodus Start =================================================

        if(self.exodusFilePath != ' ' and self.checkList[0] != 0):
            conn = sqlite3.connect(self.exodusFilePath)

            c = conn.cursor()

            exodus = Exodus.Exodus(c)
            exodus.proc_address()
            exodus.proc_transaction()
            exodus.proc_app_ins_time()
            exodus.proc_app_start_time()


            print(exodus.address)
            print(exodus.dict_trans_list[0])
            print(exodus.app_ins_time)
            print(exodus.app_start_time)

            #print(float(exodus.app_start_time + ".0000000"))
            str = exodus.app_start_time
            print(float(str[:10] + "." + str[10:]))

            print(time.asctime(time.localtime(float(str[:10] + "." + str[10:]))))


            c.close()
            conn.close()

        # ===========================  Exodus End =================================================


        # ===========================  Bitkeep Start =================================================

     #   conn = sqlite3.connect('bitkeep_09_25.db')
        if(self.bitgetFilePath != ' ' and self.checkList[1] != 0):
            conn = sqlite3.connect(self.bitgetFilePath)

            c = conn.cursor()

            bitkeep = Bitkeep.Bitkeep(c)
            bitkeep.proc_address()
            bitkeep.proc_transaction()
            bitkeep.proc_app_ins_time()
            bitkeep.proc_wallet_name()

            str = bitkeep.app_ins_time

            print('앱 설치 시간 - 유닉스타임 변환')
            print(time.asctime(time.localtime(str)))


            c.close()
            conn.close()


        # ===========================  Bitkeep End =================================================


        # ===========================  Bitpay Start =================================================

        #conn = sqlite3.connect('RKStorage_bitpay_10_05')
        if(self.bitpayFilePath != ' ' and self.checkList[2] != 0):
            conn = sqlite3.connect(self.bitpayFilePath)

            c = conn.cursor()

            bitpay = Bitpay.Bitpay(c)
            bitpay.proc_privatekey()
            bitpay.proc_mnemonic()
            bitpay.proc_app_ins_time()
            bitpay.proc_app_start_time()
            bitpay.proc_wallet_name()

            str = bitpay.app_ins_time
            print(float(str[:10] + "." + str[10:]))

            print(time.asctime(time.localtime(float(str[:10] + "." + str[10:]))))

            c.close()
            conn.close()


        # ===========================  Bitpay End =================================================


        # ===========================  Token Pocket Start =================================================

        # conn = sqlite3.connect('tp_db_common_tokenpocket_10_05')
        if(self.tokenpocketFilePath != ' ' and self.checkList[3] != 0):
            conn = sqlite3.connect(self.tokenpocketFilePath)

            c = conn.cursor()

            tokenpocket = Tokenpocket.Tokenpocket(c)
            tokenpocket.proc_address()


            c.close()
            conn.close()


        # ===========================  Token Pocket End ================================


        # ===========================  Enjin Wallet Start =================================================

        #conn = sqlite3.connect('2_enjin_10_05')
        if(self.enjinFilePath != ' ' and self.checkList[4] != 0):
            conn = sqlite3.connect(self.enjinFilePath)

            c = conn.cursor()

            enjin = Enjin.Enjin(c)
            enjin.proc_transaction()

            print(enjin.dict_trans_list)
            print(enjin.dict_trans_list[0].get('time'))

            c.close()
            conn.close()


        # ===========================  Enjin Wallet End ======================================


        # ===========================  DeFi Wallet Start =================================================

        #conn = sqlite3.connect('crypto_wallet_defi_10_05.db')
        if(self.defiFilePath != ' ' and self.checkList[5] != 0):
            conn = sqlite3.connect(self.defiFilePath)
            
            c = conn.cursor()

            defi = Defi.Defi(c)
            defi.proc_transaction()
            defi.proc_wallet_name()

            c.close()
            conn.close()


        # ===========================  DeFi Wallet End ================================


        #============== CSV 보고서 ㄲㄲㄲ ===================================

     #   csv_filepath = self.outputDir + "/" + "artifact_result.csv"
        
        with open("artifact_result.csv", 'w', newline='') as f:

            writer = csv.writer(f)   
            #writer.writerows(result)
            writer.writerow(["Android Wallet Analyzer - CSV File Report"])

            if(self.exodusFilePath != ' ' and self.checkList[0] != 0):
                exodus.proc_csv(writer)
            if(self.bitgetFilePath != ' ' and self.checkList[1] != 0):
                bitkeep.proc_csv(writer)
            if(self.bitpayFilePath != ' ' and self.checkList[2] != 0):
                bitpay.proc_csv(writer)
            if(self.tokenpocketFilePath != ' ' and self.checkList[3] != 0):
                tokenpocket.proc_csv(writer)
            if(self.enjinFilePath != ' ' and self.checkList[4] != 0):
                enjin.proc_csv(writer)
            if(self.defiFilePath != ' ' and self.checkList[5] != 0):
                defi.proc_csv(writer)

