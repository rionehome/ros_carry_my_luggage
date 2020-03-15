#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
import math

# ウィンドウを作る
root = tk.Tk()
root.update_idletasks()
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# geometry("(windowの横)✕(windowの縦)+(x方向へ平行移動)+(y方向へ平行移動)")
root.geometry(str(win_width) + "x" + str(win_height)
              + "+" + str(int(screen_width/2 - win_width/2))
              + "+" + str(int(screen_height/2 - win_height/2)))

#root.geometry("1600x1200")

# Canvasを作る
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="white")
canvas.place(x=0, y=0)

# Label部品を作る
label = tk.Label(root, text="・・・認識停止・・・", bg="white", font=("",40))
label.place(x=root.winfo_screenwidth()/2-350,y=root.winfo_screenheight()/2)
tk.Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()