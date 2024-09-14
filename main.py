import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter 窗口")
frame = ttk.Frame(root)
frame.grid(column=2, row=2, columnspan=10)
times = 0


def click():
    global times
    times += 1
    print("点击按钮 {times} 次".format(times=times))

def enter(a):
    global message
    print("输入了一个字符串：{str}".format(str=entry.get()))
    message.config(text=entry.get())

# 创建主窗口
# 创建标签并添加到窗口
label = tk.Label(root, text=" Tkinter字符")
label.grid(column=0, row=0)
button = tk.Button(root, text="点我", command=click, fg="green", bg="red")
button.grid(column=0, row=1)
message = tk.Message(root, text=" ")
message.grid(column=2, row=0)
entry = tk.Entry(root, fg="green")
entry.grid(column=2, row=1)
entry.bind("<Return>", enter)
# 运行主循环
root.mainloop()
