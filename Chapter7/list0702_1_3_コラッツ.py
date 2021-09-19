import tkinter

def click_btn_del():
    text.delete("1.0","end-1c")

def click_btn_get():
    txt= int(entry.get())
    button1["text"] = "結果を出力"

    def kora(N):
        count: int = 0
        maxN = 0
        while N != 1:
            if N % 2 == 0:
                N = N // 2
                count += 1
            else:
                N = 3 * N + 1
                count += 1
            if maxN < N:
                maxN = N

        return (count, maxN)
    text.delete("1.0", "end-1c") #前の結果を消す
    text.insert("1.0","計算回数は" + str(kora(txt)[0]) +"　最大値は"+str(kora(txt)[1])) #コラッツ予想の計算回数と最大値を出力


root = tkinter.Tk()
root.title("コラッツ予想")
root.geometry("400x200")
entry = tkinter.Entry(width =20)
entry.place(x=0,y=0)
button1 = tkinter.Button(text = "結果",command=click_btn_get)
button1.pack()
button2 = tkinter.Button(text = "ここ押すと消えるよ",command=click_btn_del)
button2.pack()
text = tkinter.Text()
text.pack()
root.mainloop()