#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
import math

win_width = 1400
win_height = 1200

# ウィンドウを作る
root = tk.Tk()
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# geometry("(windowの横)✕(windowの縦)+(x方向へ平行移動)+(y方向へ平行移動)")
root.geometry(str(win_width) + "x" + str(win_height)
              + "+" + str(int(screen_width/2 - win_width/2))
              + "+" + str(int(screen_height/2 - win_height/2)))

#root.geometry("1400x1200")

# Canvasを作る
canvas = tk.Canvas(root, width=1400, height=1200, bg="white")
canvas.place(x=0, y=0)
# Label部品を作る
label = tk.Label(root, text="・・・認識停止・・・", bg="white", font=("",40))
label.place(x=350,y=600)
tk.Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()