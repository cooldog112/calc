import tkinter as tk
import tkinter.font as tkFont
#생성
window = tk.Tk()
window.title('계산기 프로그램')
window.geometry('360x540+200+200')
window.resizable(False, False)

fontStyle = tkFont.Font(family='malgun gothic', size=30)


b7 = tk.Button(window, text='7', width =3, height=1, font=fontStyle)
b8 = tk.Button(window, text='8', width =3, height=1, font=fontStyle)
b9 = tk.Button(window, text='9', width =3, height=1, font=fontStyle)
div = tk.Button(window, text='/', width =3, height=1, font=fontStyle)
b4 = tk.Button(window, text='4', width =3, height=1, font=fontStyle)
b5 = tk.Button(window, text='5', width =3, height=1, font=fontStyle)
b6 = tk.Button(window, text='6', width =3, height=1, font=fontStyle)
mul = tk.Button(window, text='*', width =3, height=1, font=fontStyle)
b1 = tk.Button(window, text='1', width =3, height=1, font=fontStyle)
b2 = tk.Button(window, text='2', width =3, height=1, font=fontStyle)
b3 = tk.Button(window, text='3', width =3, height=1, font=fontStyle)
minus = tk.Button(window, text='-', width =3, height=1, font=fontStyle)
b0 = tk.Button(window, text='0', width =3, height=1, font=fontStyle)
result = tk.Button(window, text='=', width =3, height=1, font=fontStyle)
plus = tk.Button(window, text='+', width =3, height=1, font=fontStyle)


b7.grid(row=2, column=0, padx=5)
b8.grid(row=2, column=1, padx=5)
b9.grid(row=2, column=2, padx=5)
div.grid(row=2, column=3, padx=5)
b4.grid(row=3, column=0, padx=5)
b5.grid(row=3, column=1, padx=5)
b6.grid(row=3, column=2, padx=5)
mul.grid(row=3, column=3, padx=5)
b1.grid(row=4, column=0, padx=5)
b2.grid(row=4, column=1, padx=5)
b3.grid(row=4, column=2, padx=5)
minus.grid(row=4, column=3, padx=5)
b0.grid(row=5, column=0, padx=5)
result.grid(row=5, column=2, padx=5)
plus.grid(row=5, column=3, padx=5)


window.mainloop()