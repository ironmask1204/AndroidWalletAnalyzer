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
    window.geometry("500x900")                                  # 창 크기설정
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

    # 부분 레이블
    exodusLabel2 = Label(exodusLabel, width=50, height=5, fg="red", relief="solid")
    exodusLabel2.pack(pady=5)

    # 파일 열기 버튼
    button1 = Button(exodusLabel2, text="Open Exodus db file", command=fileOpenDialog_exodus, width=30, bg='yellow', state='disabled')
    button1.pack(pady=5, side=LEFT)

    def chk1proc():
        if(var1.get()==1):
            button1.config(state='active')
        else:
            button1.config(state='disabled')

    # check box
    var1 = IntVar()
    c1 = Checkbutton(exodusLabel2, text='', variable=var1, command=chk1proc)
    c1.pack(side=RIGHT)


    # Exodus 파일 경로 표시
    exodusFileLabel = Label(exodusLabel, text="Exodus db file", width=40, height=3, fg="red", relief="solid")
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

    # 부분 레이블
    bitgetLabel2 = Label(bitgetLabel, width=50, height=5, fg="red", relief="solid")
    bitgetLabel2.pack(pady=5)

    # 파일 열기 버튼
    button2 = Button(bitgetLabel2, text="Open Bitget_Wallet db file", command=fileOpenDialog_Bitget_Wallet, width=30, bg='yellow', state='disabled')
    button2.pack(pady=5, side=LEFT)

    def chk2proc():
        if(var2.get()==1):
            button2.config(state='active')
        else:
            button2.config(state='disabled')    

    # check box
    var2 = IntVar()
    c2 = Checkbutton(bitgetLabel2, text='', variable=var2, command=chk2proc)
    c2.pack(side=RIGHT)


    # Bitget_Wallet 파일 경로 표시
    bitgetFileLabel = Label(bitgetLabel, text="Bitget_Wallet db file", width=40, height=3, fg="red", relief="solid")
    bitgetFileLabel.pack(pady=5)

#=================================================================================
    
    # Bitpay 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Bitpay():
        window.bitpayFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        bitpayFileLabel.configure(text = window.bitpayFilePath)

    # 전체 레이블
    bitpayLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    bitpayLabel.pack(pady=5)

    # 부분 레이블
    bitpayLabel2 = Label(bitpayLabel, width=50, height=5, fg="red", relief="solid")
    bitpayLabel2.pack(pady=5)

    # 파일 열기 버튼
    button3 = Button(bitpayLabel2, text="Open Bitpay db file", command=fileOpenDialog_Bitpay, width=30, bg='yellow', state='disabled')
    button3.pack(pady=5, side=LEFT)

    def chk3proc():
        if(var3.get()==1):
            button3.config(state='active')
        else:
            button3.config(state='disabled')   
    
    # check box
    var3 = IntVar()
    c3 = Checkbutton(bitpayLabel2, text='', variable=var3, command=chk3proc)
    c3.pack(side=RIGHT)    

    # Bitpay 파일 경로 표시
    bitpayFileLabel = Label(bitpayLabel, text="Bitpay db file", width=40, height=3, fg="red", relief="solid")
    bitpayFileLabel.pack(pady=5)
#=================================================================================
    
    # TokenPocket 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_TokenPocket():
        window.tokenpocketFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        tokenpocketFileLabel.configure(text = window.tokenpocketFilePath)

    # 전체 레이블
    tokenpocketLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    tokenpocketLabel.pack(pady=5)

    # 부분 레이블
    tokenpocketLabel2 = Label(tokenpocketLabel, width=50, height=5, fg="red", relief="solid")
    tokenpocketLabel2.pack(pady=5)

    # 파일 열기 버튼
    button4 = Button(tokenpocketLabel2, text="Open TokenPocket db file", command=fileOpenDialog_TokenPocket, width=30, bg='yellow', state='disabled')
    button4.pack(pady=5, side=LEFT)

    def chk4proc():
        if(var4.get()==1):
            button4.config(state='active')
        else:
            button4.config(state='disabled')   
    
    # check box
    var4 = IntVar()
    c4 = Checkbutton(tokenpocketLabel2, text='', variable=var4, command=chk4proc)
    c4.pack(side=RIGHT)   

    # TokenPocket 파일 경로 표시
    tokenpocketFileLabel = Label(tokenpocketLabel, text="TokenPocket db file", width=40, height=3, fg="red", relief="solid")
    tokenpocketFileLabel.pack(pady=5)
#=================================================================================
    
    # Enjin_Wallet 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Enjin_Wallet():
        window.enjinFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        enjinFileLabel.configure(text = window.enjinFilePath)

    # 전체 레이블
    enjinLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    enjinLabel.pack(pady=5)

    # 부분 레이블
    enjinLabel2 = Label(enjinLabel, width=50, height=5, fg="red", relief="solid")
    enjinLabel2.pack(pady=5)      

    # 파일 열기 버튼
    button5 = Button(enjinLabel2, text="Open Enjin_Wallet db file", command=fileOpenDialog_Enjin_Wallet, width=30, bg='yellow', state='disabled')
    button5.pack(pady=5, side=LEFT)

    def chk5proc():
        if(var5.get()==1):
            button5.config(state='active')
        else:
            button5.config(state='disabled')   
    
    # check box
    var5 = IntVar()
    c5 = Checkbutton(enjinLabel2, text='', variable=var5, command=chk5proc)
    c5.pack(side=RIGHT)  

    # Enjin_Wallet 파일 경로 표시
    enjinFileLabel = Label(enjinLabel, text="Enjin_Wallet db file", width=40, height=3, fg="red", relief="solid")
    enjinFileLabel.pack(pady=5)
#=================================================================================
    
    # DeFi_Wallet 파일 열기 버튼 클릭시 호출
    def fileOpenDialog_Defi_Wallet():
        window.defiFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        defiFileLabel.configure(text = window.defiFilePath)

    # 전체 레이블
    defiLabel = Label(window, width=50, height=10, fg="red", relief="solid")
    defiLabel.pack(pady=5)

    # 부분 레이블
    defiLabel2 = Label(defiLabel, width=50, height=5, fg="red", relief="solid")
    defiLabel2.pack(pady=5)

    # 파일 열기 버튼
    button6 = Button(defiLabel2, text="Open DeFi_Wallet db file", command=fileOpenDialog_Defi_Wallet, width=30, bg='yellow', state='disabled')
    button6.pack(pady=5, side=LEFT)

    def chk6proc():
        if(var6.get()==1):
            button6.config(state='active')
        else:
            button6.config(state='disabled')   

    # check box
    var6 = IntVar()
    c6 = Checkbutton(defiLabel2, text='', variable=var6, command=chk6proc)
    c6.pack(side=RIGHT)        
    
    # DeFi_Wallet 파일 경로 표시
    defiFileLabel = Label(defiLabel, text="DeFi_Wallet db file", width=40, height=3, fg="red", relief="solid")
    defiFileLabel.pack(pady=5)
#=================================================================================    


# 분석 시작버튼 클릭
    def btnpress():                            # 함수 btnpress() 정의
   
        print('button press')

        # 000. path 초기화
       # window.exodusFilePath = ' '
       # window.bitgetFilePath = ' '
       # window.bitpayFilePath = ' '
       # window.tokenpocketFilePath = ' '
       # window.enjinFilePath = ' '
       # window.defiFilePath = ' '

        exodusFilePath = ' '
        bitgetFilePath = ' '
        bitpayFilePath = ' '
        tokenpocketFilePath = ' '
        enjinFilePath = ' '
        defiFilePath = ' '
                
     #   resultlabel = Label(window, text = 'Analysis Reuslt', height=1)
     #   resultlabel.pack(pady=5)

        # 0. 앱 선택 checkbox check값 추출
        checkList = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()]
        
        print(var1.get())
        # 0. db파일들 경로 설정
        if(checkList[0]==1):
            exodusFilePath = window.exodusFilePath
        if(checkList[1]==1):            
            bitgetFilePath = window.bitgetFilePath
        if(checkList[2]==1):            
            bitpayFilePath = window.bitpayFilePath
        if(checkList[3]==1):
            tokenpocketFilePath = window.tokenpocketFilePath
        if(checkList[4]==1):
            enjinFilePath = window.enjinFilePath
        if(checkList[5]==1):
            defiFilePath = window.defiFilePath

        FilePathList = [exodusFilePath, bitgetFilePath, bitpayFilePath, tokenpocketFilePath, enjinFilePath, defiFilePath]
        print(FilePathList[5])


        # 1. 메인로직 함수 호출
        mainlogic = MainLogic.MainLogic(FilePathList, checkList)
        mainlogic.start()

        # 2. 결과 출력
        resultlabel.configure(text = "Analysis Complete")

        # 3. reset 버튼 누르기 전에는 비활성화
        btn.config(state='disabled')


    # 분석 및 CSV 추출 시작 버튼
    btn = Button(window)                       # window라는 창에 버튼 생성
    btn.config(text= "Start to Analyze")              # 버튼 내용 
    btn.config(width=30)                       # 버튼 크기
    btn.config(command=btnpress)               # 버튼 함수 호출
    btn.config(bg='orange')
    btn.pack(pady=10)                          # 버튼 배치


    # 분석 결과 (성공) 출력
    resultlabel = Label(window, text = 'Analysis Reuslt', height=1)
    resultlabel.pack(pady=5)

    # 분석 초기화 버튼 클릭
    def reset_btnpress():                            # 함수 btnpress() 정의
        print('button press')
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)

        button1.config(state='disabled')
        button2.config(state='disabled')
        button3.config(state='disabled')
        button4.config(state='disabled')
        button5.config(state='disabled')
        button6.config(state='disabled')

        # 결과 label 초기화
        resultlabel.configure(text = 'Analysis Reuslt')

        # 분석 시작 버튼 활성화
        btn.config(state='active')
        

    # 분석 초기화 버튼
    reset_btn = Button(window)                       # window라는 창에 버튼 생성
    reset_btn.config(text= "Reset")              # 버튼 내용 
    reset_btn.config(width=10)                       # 버튼 크기
    reset_btn.config(command=reset_btnpress)               # 버튼 함수 호출
    reset_btn.config(bg='green')
    reset_btn.pack(pady=10, side=BOTTOM)                          # 버튼 배치

    # 블로그 홈페이지 바로가기 버튼
#    openWebButton = Button(window, text = "Visit to ironmask blog",command=openweb)
#    openWebButton.pack(side=BOTTOM, pady=5)

    window.mainloop()




if __name__ == "__main__":
    main()



