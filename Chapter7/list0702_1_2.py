import tkinter

def click_btn_del():
    text.delete("1.0","end-1c")

def click_btn_get():
    txt= entry.get()
    button1["text"] = "次を入力してください"
    text.insert(tkinter.END, txt)

root = tkinter.Tk()
root.title("複数行のテキスト入力")
root.geometry("400x200")
entry = tkinter.Entry(width =20)
entry.place(x=0,y=0)
button1 = tkinter.Button(text = "メッセージ",command=click_btn_get)
button1.pack()
button2 = tkinter.Button(text = "ここ押すと消えるよ",command=click_btn_del)
button2.pack()
text = tkinter.Text()
text.pack()
root.mainloop()