#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
import math

win_width = 1400
win_height = 1200

# 円の座標
x = win_width/2
y = win_height/2
i = 0


def move():
    global x, y, i
    # 前の円を隠す
    canvas.create_oval(x - 50 - 300, y - 50, x + 50 - 300, y + 50, fill="white", width=0)

    i += 0.01
    x = x + 3*math.sin(i)
    y = y + 3*math.cos(i)
    # 新しい円を描く
    canvas.create_oval(x - 40 - 300, y - 40, x + 40 - 300, y + 40, fill="blue", width=0)
    # タイマーを作る
    root.after(3, move)




# ウィンドウを作る
root = tk.Tk()
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# geometry("(windowの横)✕(windowの縦)+(x方向へ平行移動)+(y方向へ平行移動)")
root.geometry(str(win_width) + "x" + str(win_height)
              + "+" + str(int(screen_width/2 - win_width/2))
              + "+" + str(int(screen_height/2 - win_height/2)))

#root.geometry("1600x1200")


# Label部品を作る


# Canvasを作る
canvas = tk.Canvas(root, width=1400, height=1200, bg="white")
canvas.place(x=0, y=0)

# タイマーを作る
root.after(3, move)
label = tk.Label(root, text="・・・認識中・・・", bg="white", font=("",20))
label.place(x=550,y=600)
tk.Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()