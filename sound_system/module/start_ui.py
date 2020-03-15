import tkinter as tk
import time
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

# Canvasを作る
canvas = tk.Canvas(root, width=root.winfo_screenwidth(),
                         height=root.winfo_screenheight(), bg="white")
canvas.place(x=0, y=0)

# Label部品を作る
label = tk.Label(root, text="・・・認識中・・・", bg="white", font=("",20))
label.place(x=root.winfo_screenwidth()/2-150,y=root.winfo_screenheight()/2)
# Buttonを作る
tk.Button(root, text="Quit", command=root.destroy).pack()

# 変数
radius_circle = 40
radius_area = 300
x = win_width/2
y = win_height/2

# 図形

circle = canvas.create_oval(x - radius_circle - radius_area,
                            y - radius_circle,
                            x + radius_circle - radius_area,
                            y + radius_circle,
                            fill="blue", width=0)  # 円

i = 0
# 無限ループ
while True:
    canvas.coords(circle, x - radius_circle - radius_area, y - radius_circle, x + radius_circle - radius_area, y + radius_circle)
    i += 0.01
    x = x + 3*math.sin(i)
    y = y + 3*math.cos(i)
    time.sleep(0.002)  # 0.002秒ずつ更新
    root.update()  # ウインド画面を更新
