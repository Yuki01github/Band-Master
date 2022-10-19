import module.GM_self as GM
import tkinter as tk
from module.splash import splash_func
from PIL import ImageTk


def main():

    splash_func()
    root = tk.Tk()
    app = Application(master=root)
    # background = tk.PhotoImage(
    #     file=r".\module\figure\windmill.gif")
    # bg = tk.Canvas(root, width=500, height=500)
    # bg.grid(0, 0)

    app.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Graph Maker v2.0")
        self.master.geometry("600x600")

        label0 = tk.Label(self.master, text="パラメータ")

        label1 = tk.Label(self.master, text="系列1")
        label1_1 = tk.Label(self.master, text="凡例1")
        label1_2 = tk.Label(self.master, text='色')
        label1_3 = tk.Label(self.master, text="回帰範囲")
        label1_4 = tk.Label(self.master, text="~")
        label1_5 = tk.Label(self.master, text="シンボル")
        label1_6 = tk.Label(self.master, text="サイズ")
        label1_7 = tk.Label(self.master, text='近似直線')

        label2 = tk.Label(self.master, text="系列2")
        label2_1 = tk.Label(self.master, text="凡例2")
        label2_2 = tk.Label(self.master, text='色')
        label2_3 = tk.Label(self.master, text="回帰範囲")
        label2_4 = tk.Label(self.master, text="~")
        label2_5 = tk.Label(self.master, text="シンボル")
        label2_6 = tk.Label(self.master, text="サイズ")
        label1_7 = tk.Label(self.master, text='近似直線')

        label3 = tk.Label(self.master, text="系列3")
        label3_1 = tk.Label(self.master, text="凡例3")
        label3_2 = tk.Label(self.master, text='色')
        label3_3 = tk.Label(self.master, text="回帰範囲")
        label3_4 = tk.Label(self.master, text="~")
        label3_5 = tk.Label(self.master, text="シンボル")
        label3_6 = tk.Label(self.master, text="サイズ")
        label1_7 = tk.Label(self.master, text='近似直線')

        label4 = tk.Label(self.master, text="系列4")
        label4_1 = tk.Label(self.master, text="凡例4")
        label4_2 = tk.Label(self.master, text='色')
        label4_3 = tk.Label(self.master, text="回帰範囲")
        label4_4 = tk.Label(self.master, text="~")
        label4_5 = tk.Label(self.master, text="シンボル")
        label4_6 = tk.Label(self.master, text="サイズ")
        label1_7 = tk.Label(self.master, text='近似直線')

        label_xrange1 = tk.Label(self.master, text='x軸範囲')
        label_xrange2 = tk.Label(self.master, text='~')
        label_yrange1 = tk.Label(self.master, text='y軸範囲')
        label_yrange2 = tk.Label(self.master, text='~')
        label_xaxis = tk.Label(self.master, text="x軸ラベル")
        label_yaxis = tk.Label(self.master, text="y軸ラベル")
        label_title = tk.Label(self.master, text="グラフタイトル")
        label_input = tk.Label(self.master, text="ソース")
        label_output = tk.Label(self.master, text="保存先")

        self.entry1_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_7 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_1.insert(tk.END, "$\it{V_{1}}$")
        self.entry1_2.insert(tk.END, "b")
        self.entry1_5.insert(tk.END, "o")
        self.entry1_6.insert(tk.END, 20)

        self.entry2_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_7 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_1.insert(tk.END, "$\it{V_{2}}$")
        self.entry2_2.insert(tk.END, "r")
        self.entry2_5.insert(tk.END, "x")
        self.entry2_6.insert(tk.END, 20)

        self.entry3_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_7 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_1.insert(tk.END, "$\it{V_{3}}$")
        self.entry3_2.insert(tk.END, "o")
        self.entry3_5.insert(tk.END, "v")
        self.entry3_6.insert(tk.END, 20)

        self.entry4_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_7 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_1.insert(tk.END, "$\it{V_{4}}$")
        self.entry4_2.insert(tk.END, "y")
        self.entry4_5.insert(tk.END, "^")
        self.entry4_6.insert(tk.END, 20)

        self.entry_xrange1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry_xrange2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry_yrange1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry_yrange2 = tk.Entry(self.master, justify=tk.LEFT)

        self.entry_xaxis = tk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_xaxis.insert(tk.END, "入力電圧 $\it{V_{1}}$ / $\mathsf{V}$")

        self.entry_yaxis = tk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_yaxis.insert(
            tk.END, "差動電圧 $\it{V_{+} - V_{-}}$ / $\mathsf{μV}$")

        self.entry_title = tk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_title.insert(tk.END, "タイトル")

        self.entry_input = tk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_input.insert(
            tk.END, r".\graph\data.csv")
        src = self.entry_input.get()

        self.entry_output = tk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_output.insert(
            tk.END, r".")

        self.button_run = tk.Button(self.master, text="RUN",
                                    width=8, command=self.gm_func)
        self.button_quit = tk.Button(self.master, text="Quit",
                                     width=8, command=self.master.destroy)

        self.bln_xrange, self.bln_yrange = tk.BooleanVar(), tk.BooleanVar()
        self.chk_xrange = tk.Checkbutton(self.master, variable=self.bln_xrange)
        self.chk_yrange = tk.Checkbutton(self.master, variable=self.bln_yrange)

        self.bln_lr = [tk.BooleanVar() for i in range(4)]
        self.chk_lr = [tk.Checkbutton(self.master, variable=self.bln_lr[i],
                                      text='線形回帰') for i in range(4)]

        label0.grid(row=0, column=0, rowspan=15)

        label1.grid(row=0, column=1, columnspan=7)
        label1_1.grid(row=1, column=1)
        self.entry1_1.grid(row=1, column=2)
        label1_2.grid(row=1, column=3)
        self.entry1_2.grid(row=1, column=4)
        label1_3.grid(row=2, column=1)
        self.entry1_3.grid(row=2, column=2)
        label1_4.grid(row=2, column=3)
        self.entry1_4.grid(row=2, column=4)
        label1_5.grid(row=3, column=1)
        self.entry1_5.grid(row=3, column=2)
        label1_6.grid(row=3, column=3)
        self.entry1_6.grid(row=3, column=4)
        self.chk_lr[0].grid(row=3, column=5)

        label2.grid(row=4, column=1, columnspan=7)
        label2_1.grid(row=5, column=1)
        self.entry2_1.grid(row=5, column=2)
        label2_2.grid(row=5, column=3)
        self.entry2_2.grid(row=5, column=4)
        label2_3.grid(row=6, column=1)
        self.entry2_3.grid(row=6, column=2)
        label2_4.grid(row=6, column=3)
        self.entry2_4.grid(row=6, column=4)
        label2_5.grid(row=7, column=1)
        self.entry2_5.grid(row=7, column=2)
        label2_6.grid(row=7, column=3)
        self.entry2_6.grid(row=7, column=4)
        self.chk_lr[1].grid(row=7, column=5)

        label3.grid(row=8, column=1, columnspan=7)
        label3_1.grid(row=9, column=1)
        self.entry3_1.grid(row=9, column=2)
        label3_2.grid(row=9, column=3)
        self.entry3_2.grid(row=9, column=4)
        label3_3.grid(row=10, column=1)
        self.entry3_3.grid(row=10, column=2)
        label3_4.grid(row=10, column=3)
        self.entry3_4.grid(row=10, column=4)
        label3_5.grid(row=11, column=1)
        self.entry3_5.grid(row=11, column=2)
        label3_6.grid(row=11, column=3)
        self.entry3_6.grid(row=11, column=4)
        self.chk_lr[2].grid(row=11, column=5)

        label_xaxis.grid(row=12, column=1)
        self.entry_xaxis.grid(row=12, column=2, columnspan=5)
        label_yaxis.grid(row=13, column=1)
        self.entry_yaxis.grid(row=13, column=2, columnspan=5)
        label_xrange1.grid(row=14, column=1)
        self.entry_xrange1.grid(row=14, column=2)
        label_xrange2.grid(row=14, column=3)
        self.entry_xrange2.grid(row=14, column=4)
        self.chk_xrange.grid(row=14, column=5)
        label_yrange1.grid(row=15, column=1)
        self.entry_yrange1.grid(row=15, column=2)
        label_yrange2.grid(row=15, column=3)
        self.entry_yrange2.grid(row=15, column=4)
        self.chk_yrange.grid(row=15, column=5)
        label_title.grid(row=16, column=1)
        self.entry_title.grid(row=16, column=2, columnspan=5)
        label_input.grid(row=17, column=1)
        self.entry_input.grid(row=17, column=2, columnspan=5)
        label_output.grid(row=18, column=1)
        self.entry_output.grid(row=18, column=2, columnspan=5)
        self.button_run.grid(row=19, column=1, columnspan=5)
        self.button_quit.grid(row=0, column=5, columnspan=3)

    def gm_func(self):
        legends = []
        reg_range = []
        ranges = [[], []]
        lr = []
        colors = []
        markers = []
        sizes = []

        xlabel = self.entry_xaxis.get()
        ylabel = self.entry_yaxis.get()
        title = self.entry_title.get()
        src = self.entry_input.get()
        dst = self.entry_output.get()

        legends.append(self.entry1_1.get())
        legends.append(self.entry2_1.get())
        legends.append(self.entry3_1.get())
        legends.append(self.entry4_1.get())

        colors.append(self.entry1_2.get())
        colors.append(self.entry2_2.get())
        colors.append(self.entry3_2.get())
        colors.append(self.entry4_2.get())

        reg_range.append([self.entry1_3.get(), self.entry1_4.get()])
        reg_range.append([self.entry2_3.get(), self.entry2_4.get()])
        reg_range.append([self.entry3_3.get(), self.entry3_4.get()])
        reg_range.append([self.entry4_3.get(), self.entry4_4.get()])

        markers.append(self.entry1_5.get())
        markers.append(self.entry2_5.get())
        markers.append(self.entry3_5.get())
        markers.append(self.entry4_5.get())

        sizes.append(float(self.entry1_6.get()))
        sizes.append(float(self.entry2_6.get()))
        sizes.append(float(self.entry3_6.get()))
        sizes.append(float(self.entry4_6.get()))

        if self.bln_xrange.get():
            ranges[0].append(float(self.entry_xrange1.get()))
            ranges[0].append(float(self.entry_xrange2.get()))
        else:
            ranges[0] = 0

        if self.bln_yrange.get():
            ranges[1].append(float(self.entry_yrange1.get()))
            ranges[1].append(float(self.entry_yrange2.get()))
        else:
            ranges[1] = 0

        for i in range(4):
            lr.append(int(self.bln_lr[i].get()))

        GM.graph_making(src, dst, title, legends, colors, ranges,
                        markers, sizes,  reg_range, lr,  xlabel, ylabel)


if __name__ == '__main__':
    main()
