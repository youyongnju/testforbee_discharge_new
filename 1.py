#导入tkinter模块并创建别名tk

import tkinter as tk

class App:

    def __init__(self, root):

       #设置标题

        root.title("打招呼测试")

       #创建一个框架，然后在里面添加一个Button组件

       #框架的作用一般是在复杂的布局中起到将组件分组的作用

        frame = tk.Frame(root)

        #pack()自动调节组件自身尺寸

        frame.pack()

         #创建一个按钮组件，fg是foreground（前景色）

        self.hi_there = tk.Button(frame, text="打招呼", fg="blue", command=self.say_hi)

        #左对齐

        self.hi_there.pack(side=tk.LEFT)



    def say_hi(self):
        print("您刚才通过点击打招呼触发了我:大家好，我是badao！")

#创建一个toplevel的根窗口，并把它作为参数实例化app对象

root = tk.Tk()
app = App(root)

#开始主事件循环

root.mainloop()