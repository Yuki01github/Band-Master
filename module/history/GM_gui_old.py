from tkinter.constants import COMMAND
import module.GM_self as GM
import tkinter as tk


def main():
    root = tk.Tk()
    app = Application(master=root)

    # img = tk.PhotoImage(
    #     file=r".\module\figure\windmill.gif")
    # bg = tk.Label(root, image=img)
    # bg.grid()

    app.mainloop()

    # root = tk.Tk()
    # root.title(u"Graph Maker v2.0")
    # root.geometry("400x300")

    # static1 = tk.Label(text=u'test')
    # static1.pack()

    # Path_EB = tk.Entry(width=10)
    # Path_EB.insert(tk.END, "default")
    # Path_EB.pack()
    # value = Path_EB.get()

    # Run_Button = tk.Button(text=u'button', width=10)
    # Run_Button.bind("<Button-1>", run_func(Path_EB))
    # Run_Button.pack()

    # root.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Graph Maker v2.0")
        self.master.geometry("500x500")

        label0 = tk.Label(self.master, text="パラメータ")

        label1 = tk.Label(self.master, text="系列1")
        label1_1 = tk.Label(self.master, text="凡例1")
        label1_2 = tk.Label(self.master, text='範囲1')
        label1_3 = tk.Label(self.master, text="回帰範囲")
        label1_4 = tk.Label(self.master, text="~")
        label1_5 = tk.Label(self.master, text="y軸範囲")
        label1_6 = tk.Label(self.master, text="~")
        label1_7 = tk.Label(self.master, text='~')

        label2 = tk.Label(self.master, text="系列2")
        label2_1 = tk.Label(self.master, text="凡例2")
        label2_2 = tk.Label(self.master, text='範囲2')
        label2_3 = tk.Label(self.master, text="回帰範囲")
        label2_4 = tk.Label(self.master, text="~")
        label2_5 = tk.Label(self.master, text="y軸範囲")
        label2_6 = tk.Label(self.master, text="~")
        label1_7 = tk.Label(self.master, text='~')

        label3 = tk.Label(self.master, text="系列3")
        label3_1 = tk.Label(self.master, text="凡例3")
        label3_2 = tk.Label(self.master, text='範囲3')
        label3_3 = tk.Label(self.master, text="回帰範囲")
        label3_4 = tk.Label(self.master, text="~")
        label3_5 = tk.Label(self.master, text="y軸範囲")
        label3_6 = tk.Label(self.master, text="~")
        label1_7 = tk.Label(self.master, text='~')

        label4 = tk.Label(self.master, text="系列4")
        label4_1 = tk.Label(self.master, text="凡例4")
        label4_2 = tk.Label(self.master, text='範囲4')
        label4_3 = tk.Label(self.master, text="回帰範囲")
        label4_4 = tk.Label(self.master, text="~")
        label4_5 = tk.Label(self.master, text="y軸範囲")
        label4_6 = tk.Label(self.master, text="~")
        label1_7 = tk.Label(self.master, text='~')

        label_xaxis = tk.Label(self.master, text="x軸ラベル")
        label_yaxis = tk.Label(self.master, text="y軸ラベル")
        label_title = tk.Label(self.master, text="グラフタイトル")
        label_input = tk.Label(self.master, text="ソース")
        label_output = tk.Label(self.master, text="保存先")

        self.entry1_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_1.insert(tk.END, "\it{V_{1}}")
        self.entry1_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry1_7 = tk.Entry(self.master, justify=tk.LEFT)

        self.entry2_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_1.insert(tk.END, "\it{V_{2}}")
        self.entry2_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry2_7 = tk.Entry(self.master, justify=tk.LEFT)

        self.entry3_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_1.insert(tk.END, "\it{V_{3}}")
        self.entry3_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry3_7 = tk.Entry(self.master, justify=tk.LEFT)

        self.entry4_1 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_1.insert(tk.END, "\it{V_{4}}")
        self.entry4_2 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_3 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_4 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_5 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_6 = tk.Entry(self.master, justify=tk.LEFT)
        self.entry4_7 = tk.Entry(self.master, justify=tk.LEFT)

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

        button_run = tk.Button(self.master, text="RUN",
                               width=8, command=self.gm_func)
        button_quit = tk.Button(self.master, text="Quit",
                                width=8, command=self.master.destroy)

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

        label2.grid(row=4, column=1, columnspan=7)
        label2_1.grid(row=5, column=1)
        self.entry2_1.grid(row=5, column=2)
        label2_2.grid(row=5, column=3)
        self.entry2_2.grid(row=5, column=4)
        label2_3.grid(row=6, column=1)
        self.entry2_3.grid(row=6, column=2)
        label2_4.grid(row=6, column=3)
        self.entry2_5.grid(row=6, column=4)
        label2_5.grid(row=7, column=1)
        self.entry2_6.grid(row=7, column=2)
        label2_6.grid(row=7, column=3)
        self.entry2_4.grid(row=7, column=4)

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

        label_xaxis.grid(row=12, column=1)
        self.entry_xaxis.grid(row=12, column=2, columnspan=5)
        label_yaxis.grid(row=13, column=1)
        self.entry_yaxis.grid(row=13, column=2, columnspan=5)
        label_title.grid(row=14, column=1)
        self.entry_title.grid(row=14, column=2, columnspan=5)
        label_input.grid(row=15, column=1)
        self.entry_input.grid(row=15, column=2, columnspan=5)
        label_output.grid(row=16, column=1)
        self.entry_output.grid(row=16, column=2, columnspan=5)
        button_run.grid(row=17, column=1, columnspan=5)
        button_quit.grid(row=0, column=6, columnspan=5)

    def gm_func(self):
        legends = []
        xlabel = self.entry_xaxis.get()
        ylabel = self.entry_yaxis.get()
        title = self.entry_title.get()
        src = self.entry_input.get()
        dst = self.entry_output.get()

        legends.append(self.entry1_1.get())
        legends.append(self.entry2_1.get())
        legends.append(self.entry3_1.get())
        legends.append(self.entry4_1.get())
        GM.graph_making(src, dst, title, legends, xlabel, ylabel)


if __name__ == '__main__':
    main()
