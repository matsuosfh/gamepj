import tkinter

#移動
key =""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

mx = 1
my = 1

def main_proc():
    global mx,my
    if key =="Up" and maze[my-1][mx] == 0:
        my -= 1
    if key =="Down" and maze[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx += 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        canvas.create_rectangle(mx*80,my*80,mx*80+79,my*80+79,fill="pink",width=0)
    canvas.delete("MYCHR")
    #canvas.coords("MYCHR", mx * 80 + 40, my * 80 + 40)
    canvas.create_image(mx*80+40,my*80+40,image=img,tag="MYCHR") #+40は座標が画像の中心にするため
    root.after(300,main_proc)


root = tkinter.Tk()
root.title("迷路内を移動する")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

#迷路の表示
canvas = tkinter.Canvas(width=800,height=560,bg="white")
canvas.pack()
maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80,y*80,x*80+79,y*80+79,fill="skyblue",width=0)


img = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40,my*80+40,image=img,tag="MYCHR")
main_proc()

root.mainloop()