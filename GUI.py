import tkinter as tk  # 使用Tkinter前需要先导入
import CMW500_measure
import sharedata
import time




if __name__=='__main__':
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('自动测试系统_____________author:Youyong')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('800x600+500+250')  # 这里的乘是小x+500 +400 定义窗口弹出时的默认展示位置

    # 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
    t = tk.Text(window, height=30)
    t.pack()

    def insert_end(content):  # 在文本框内容最后接着插入输入内容
        t.insert('end', content)

    b1 = tk.Button(window, text='开始测试', width=20, height=4, command=CMW500_measure.measure())
    b1.place(x=320, y=420)
    #b1.config(state= 'disabled')


    # 第8步，主窗口循环显示
    window.mainloop()
