from tkinter import *
from tkinter import ttk # thrmr of tk
from tkinter import messagebox
############### CSV ########################
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='')as file:
        fw = csv.writer(file) #fw= file writer
        fw.writerow(datalist) # datalist= ['pen,'pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='')as file:
        fr = csv.reader(file) #fr= file reader
        data = list(fr)
    return data
#######################################

GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('Record Program') # name of program
GUI.geometry('900x400') # ขนาด


#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)
L1 = Label(GUI,text = 'โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
###########

def Button2():
    text = 'ตอนนี้มีเงิน 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) # กระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#B2.place(x=50,y=200)

#B0 = Button(GUI,text='เงินมีอยู่กี่บาท')
#B0.pack()

###########
def Button3():
    text = 'Python 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB2 = Frame(GUI) # กระดาน
FB2.place(x=100,y=180)
B3 = ttk.Button(FB2,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

############## SECTION RIGHT
LF1 = ttk.Labelframe(GUI,text= 'กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=400,y=50)

v_data= StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable= v_data,font=('Angsana New',25))
E1.pack(padx=10,pady=20)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] #เวลา,ข้อมูลในการกรอก
    writecsv(text) # บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยูในช่องกรอก



B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)

GUI.mainloop()

