import tkinter as tk
from tkinter import *
from tkinter import ttk # thrmr of tk
from tkinter import messagebox
import tkinter as tk

# สร้างหน้าต่าง tkinter
window = Tk()
window.title("Calculator")
window.geometry("600x500")
#สร้าง Label
L1 = Label(window,text = 'โปรแกรมคำนวนผลิต',font=('Angsana New',30),fg='green').pack()

L2 = Label(window,text = 'เลขที่ใบงานผลิต',font=('Angsana New',14),fg='green')
L2.place(x=50,y=100)

L3 = Label(window,text = 'ความยาวของหลังคา',font=('Angsana New',14),fg='green')
L3.place(x=50,y=150)

L4 = Label(window,text = 'จำนวน',font=('Angsana New',14),fg='green')
L4.place(x=50,y=200)

L5 = Label(window,text = 'เมตร',font=('Angsana New',14),fg='green')
L5.place(x=300,y=150)

L6 = Label(window,text = 'แผ่น',font=('Angsana New',14),fg='green')
L6.place(x=300,y=200)

L7 = Label(window,text = 'พื้นที่',font=('Angsana New',14),fg='green')
L7.place(x=50,y=400)

L8 = Label(window,text = 'ตารางเมตร',font=('Angsana New',14),fg='green')
L8.place(x=300,y=400)

# สร้าง entry 4 ช่อง
entry1 = Entry(window, width=10)
entry1.place(x=200,y=100)

entry2 = Entry(window, width=10)
entry2.place(x=200,y=150)

entry3 = Entry(window, width=10)
entry3.place(x=200,y=200)

entry4 = Entry(window, width=10)
entry4.place(x=200,y=400)

# สร้างปุ่มคำนวน
calculate_button = tk.Button(window, text="Calculate")

def calculate():
    num1 = entry1.get()
    num2 = float(entry2.get())
    num3 = float(entry3.get())
    S1 = str(num1)
    area = num2 * num3 * 0.85
    mat = area*2
    print("SO : ",str(S1))
    print("Area:", area,"sq.m")
    print("Material used:", mat,"kg")
    entry4.delete(0,tk.END)
    entry4.insert(0,area)
calculate_button.config(command=calculate)
calculate_button.place(x=200,y=300)
   
window.mainloop()

#กด ESC ปลดลูบเพื่อทำงานต่อไป

# ask a yes/no question
response = messagebox.askquestion("Order", "ต้องการจัดเป็นคิวผลิต")

# check the response
if response == "yes":
    print("รับจองคิวผลิต")
    response1 = messagebox.showinfo("","รับจองคิวผลิต")
else:
    print("เลื่อนการผลิตของออเดอร์")          


