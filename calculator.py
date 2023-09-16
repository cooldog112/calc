import tkinter as tk
import tkinter.font as tkFont
#생성
window = tk.Tk()

fontStyle = tkFont.Font(family='malgun gothic', size=20)
fontStyle_number = tkFont.Font(family='malgun gothic', size=20)


window.title("계산기")
window.geometry('400x640+300+300')
window.resizable(False, False)

label = tk.Label(window,
                 text='계산기 프로그램',
                 width=20,
                 height=2,
                 fg="red",
                 relief='solid',
                 font = fontStyle
                 )
cnt_label = tk.Label(window, text='0', font = fontStyle_number)
cnt = 0
#함수 정의
def countUP():
    global cnt
    cnt += 1
    cnt_label.config(text=str(cnt))
def countDown():
    global cnt
    cnt -= 1
    cnt_label.config(text=str(cnt))
btn1 = tk.Button(window, text = '+',
                 overrelief='solid',
                 width=10,
                 command=countUP)
btn2 = tk.Button(window, text = '-',
                 overrelief='solid',
                 width=10,
                 command=countDown)
#배치
label.pack()
cnt_label.pack()
btn1.pack()
btn2.pack()
#윈도우가 종료될 까지 계속 실행
window.mainloop()