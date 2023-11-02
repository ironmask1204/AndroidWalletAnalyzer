"""
AndroidWalletAnalyzer.py

author: ironmask

blog: https://ironmask.net
"""

from tkinter import *       
from tkinter import filedialog
import os 
from pathlib import Path
import webbrowser
import MainLogic

def openweb():
    url = "https://ironmask.net"
    webbrowser.open(url,new=1)

def main():
    window = Tk()                                               # 창 생성
    window.geometry("500x820")                                  # 창 크기설정
    window.title("AndroidWalletAnalyzer by ironmask")           # 창 제목
    window.option_add("*Font","맑은고딕 12")                    # 폰트
    window.resizable(False, False)                              # x, y 창 크기 고정

#=================================================================================

    # exodus 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_exodus():
        window.exodusFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        exodusFileLabel.configure(text = window.exodusFilePath)

    # 전체 레이블
    exodusLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    exodusLabel.pack(pady=5)


    # 파일 열기 버튼
    button = Button(exodusLabel, text="Exodus db 파일 열기", command=fileOpenDialog_exodus, width=30, bg='yellow')
    button.pack(pady=5)


    # Exodus 파일 경로 표시
    exodusFileLabel = Label(exodusLabel, text="Exodus db 파일", width=40, height=3, fg="red", relief="solid")
    #label.grid(column=0, row=0)
    exodusFileLabel.pack(pady=5)  
#=================================================================================    
    
    # Bitget_Wallet 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Bitget_Wallet():
        window.bitgetFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        bitgetFileLabel.configure(text = window.bitgetFilePath)

    # 전체 레이블
    bitgetLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    bitgetLabel.pack(pady=5)

    # 파일 열기 버튼
    button = Button(bitgetLabel, text="Bitget_Wallet db 파일 열기", command=fileOpenDialog_Bitget_Wallet, width=30, bg='yellow')
    button.pack(pady=5)

    # Bitget_Wallet 파일 경로 표시
    bitgetFileLabel = Label(bitgetLabel, text="Bitget_Wallet db 파일", width=40, height=3, fg="red", relief="solid")
    bitgetFileLabel.pack(pady=5)
#=================================================================================
    
    # Bitpay 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Bitpay():
        window.bitpayFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        bitpayFileLabel.configure(text = window.bitpayFilePath)

    # 전체 레이블
    bitpayLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    bitpayLabel.pack(pady=5)

    # 파일 열기 버튼
    button = Button(bitpayLabel, text="Bitpay db 파일 열기", command=fileOpenDialog_Bitpay, width=30, bg='yellow')
    button.pack(pady=5)

    # Bitpay 파일 경로 표시
    bitpayFileLabel = Label(bitpayLabel, text="Bitpay db 파일", width=40, height=3, fg="red", relief="solid")
    bitpayFileLabel.pack(pady=5)
#=================================================================================
    
    # TokenPocket 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_TokenPocket():
        window.tokenpocketFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        tokenpocketFileLabel.configure(text = window.tokenpocketFilePath)

    # 전체 레이블
    tokenpocketLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    tokenpocketLabel.pack(pady=5)

    # 파일 열기 버튼
    button = Button(tokenpocketLabel, text="TokenPocket db 파일 열기", command=fileOpenDialog_TokenPocket, width=30, bg='yellow')
    button.pack(pady=5)

    # TokenPocket 파일 경로 표시
    tokenpocketFileLabel = Label(tokenpocketLabel, text="TokenPocket db 파일", width=40, height=3, fg="red", relief="solid")
    tokenpocketFileLabel.pack(pady=5)
#=================================================================================
    
    # Enjin_Wallet 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Enjin_Wallet():
        window.enjinFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        enjinFileLabel.configure(text = window.enjinFilePath)

    # 전체 레이블
    enjinLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    enjinLabel.pack(pady=5)

    # 파일 열기 버튼
    button = Button(enjinLabel, text="Enjin_Wallet db 파일 열기", command=fileOpenDialog_Enjin_Wallet, width=30, bg='yellow')
    button.pack(pady=5)

    # Bitget_Wallet 파일 경로 표시
    enjinFileLabel = Label(enjinLabel, text="Enjin_Wallet db 파일", width=40, height=3, fg="red", relief="solid")
    enjinFileLabel.pack(pady=5)
#=================================================================================
    
    # DeFi_Wallet 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Defi_Wallet():
        window.defiFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        defiFileLabel.configure(text = window.defiFilePath)

    # 전체 레이블
    defiLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    defiLabel.pack(pady=5)

    # 파일 열기 버튼
    button = Button(defiLabel, text="DeFi_Wallet db 파일 열기", command=fileOpenDialog_Defi_Wallet, width=30, bg='yellow')
    button.pack(pady=5)

    # Bitget_Wallet 파일 경로 표시
    defiFileLabel = Label(defiLabel, text="DeFi_Wallet db 파일", width=40, height=3, fg="red", relief="solid")
    defiFileLabel.pack(pady=5)
#=================================================================================    

    # 분석 시작버튼 클릭
  #  main = main()
    def btnpress():                            # 함수 btnpress() 정의
   
        print('button press')

        # 00. 결과 label 초기화
        resultlabel.configure(text = "분석 결과")

        # 0. db파일들 및 csv 파일 저장 위치 설정
        exodusFilePath = window.exodusFilePath
        bitgetFilePath = window.bitgetFilePath
        bitpayFilePath = window.bitpayFilePath
        tokenpocketFilePath = window.tokenpocketFilePath
        enjinFilePath = window.enjinFilePath
        defiFilePath = window.defiFilePath

        # 1. 메인로직 함수 호출
        mainlogic = MainLogic.MainLogic(exodusFilePath, bitgetFilePath, bitpayFilePath, tokenpocketFilePath, enjinFilePath, defiFilePath)
        mainlogic.start()

        # 2. 결과 출력
        resultlabel.configure(text = "분석 완료")


    # 분석 및 CSV 추출 시작 버튼
    btn = Button(window)                       # window라는 창에 버튼 생성
    btn.config(text= "분석 시작")              # 버튼 내용 
    btn.config(width=30)                       # 버튼 크기
    btn.config(command=btnpress)               # 버튼 함수 호출
    btn.config(bg='orange')
    btn.pack(pady=10)                          # 버튼 배치

    # 분석 결과 (성공) 출력
    resultlabel = Label(window, text = '분석 결과', height=1)
    resultlabel.pack(pady=5)

    # 블로그 홈페이지 바로가기 버튼
    openWebButton = Button(window, text = "ironmask 블로그 바로가기",command=openweb)
    openWebButton.pack(side=BOTTOM, pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
