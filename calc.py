import tkinter as tk
import tkinter.font as tkFont
#생성
window = tk.Tk()
window.title('계산기 프로그램')
window.geometry('450x540+200+200')
window.resizable(False, False)

def 입력하기(temp):
    input.insert(len(input.get()), temp)
def 계산하기():
    output.delete(0, len(output.get()))
    #1. input entry 에 있는 값을 가져옵니다.
    t = input.get()
    #2. 연산
    t = eval(t)
    #3. 연산결과를 output에 반영
    output.insert(0, t)

fontStyle = tkFont.Font(family='malgun gothic', size=30)
input = tk.Entry(window, font=fontStyle, justify='right')
output = tk.Entry(window, font=fontStyle, justify='right')
# input.bind("<Return>", 계산하기)
input.grid(row=0, column=0, columnspan=4)
output.grid(row=1, column=0, columnspan=4)
btn_width = 4
b7 = tk.Button(window, text='7', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('7'))
b8 = tk.Button(window, text='8', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('8'))
b9 = tk.Button(window, text='9', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('9'))
div = tk.Button(window, text='/', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('/'))
b4 = tk.Button(window, text='4', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('4'))
b5 = tk.Button(window, text='5', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('5'))
b6 = tk.Button(window, text='6', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('6'))
mul = tk.Button(window, text='*', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('*'))
b1 = tk.Button(window, text='1', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('1'))
b2 = tk.Button(window, text='2', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('2'))
b3 = tk.Button(window, text='3', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('3'))
minus = tk.Button(window, text='-', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('-'))
b0 = tk.Button(window, text='0', width =9, height=1, font=fontStyle, command= lambda: 입력하기('0'))
result = tk.Button(window, text='=', width =btn_width, height=1, font=fontStyle, command=계산하기)
plus = tk.Button(window, text='+', width =btn_width, height=1, font=fontStyle, command=lambda: 입력하기('+'))


b7.grid(row=2, column=0, padx=5, pady=3)
b8.grid(row=2, column=1, padx=5, pady=3)
b9.grid(row=2, column=2, padx=5, pady=3)
div.grid(row=2, column=3, padx=5, pady=3)
b4.grid(row=3, column=0, padx=5, pady=3)
b5.grid(row=3, column=1, padx=5, pady=3)
b6.grid(row=3, column=2, padx=5, pady=3)
mul.grid(row=3, column=3, padx=5, pady=3)
b1.grid(row=4, column=0, padx=5, pady=3)
b2.grid(row=4, column=1, padx=5, pady=3)
b3.grid(row=4, column=2, padx=5, pady=3)
minus.grid(row=4, column=3, padx=5, pady=3)
b0.grid(row=5, column=0, padx=5, columnspan=2, pady=3)
result.grid(row=5, column=2, padx=5, pady=3)
plus.grid(row=5, column=3, padx=5, pady=3)


window.mainloop()