import module.GM_self as GM
from module.GM_config import config_writing, config_reading
import tkinter as tk
from tkinter import ttk
import os
import sys
from tkinter import Variable, filedialog
from module.splash import splash_func
from module.open_csv_module import open_csv_func, create_csv_func, open_help_func
from PIL import ImageTk, Image
import configparser


def main():

    splash_func()
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.config = config_reading()
        self.root_width = 890
        self.root_height = 500
        self.master.title("Band Master v0.5")
        self.master.geometry(f"{self.root_width}x{self.root_height}+0+0")
        # self.master.iconbitmap('.\\module\\figure\\gm_icon.ico')
        self.background()
        self.arrangement()
        self.create_menu()
        self.graph_canvas()
        self.create_statusbar()
        self.shortcut()

    def graph_canvas(self):
        # ----グラフ描画キャンバスの設定----
        self.canvas_width = 450
        self.canvas_height = 350
        self.canvas = tk.Canvas(
            self.master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(row=1, column=8, rowspan=16)

    def background(self):
        # ----背景の設定----
        self.img = Image.open(rf".\module\figure\cloud.gif").resize(
            (self.root_width, self.root_height))
        self.photo = ImageTk.PhotoImage(
            self.img, width=self.root_width, height=self.root_height, master=self.master)
        self.bg = tk.Label(self.master, image=self.photo)
        self.bg.place(x=0, y=0)

    def create_menu(self):
        # メニュ-バーの設定
        menu_bar = tk.Menu(self, bg='grey')

        file_menu = tk.Menu(menu_bar, tearoff=tk.OFF)
        menu_bar.add_cascade(
            label="ファイル(F)", menu=file_menu, accelerator='Alt+F')
        file_menu.add_command(
            label="ソース", command=self.source_file_path, accelerator="Alt+S")
        file_menu.add_command(
            label="保存先", command=self.dst_dir_path, accelerator="Alt+D")
        file_menu.add_separator()
        file_menu.add_command(
            label="開く", command=self.open_func, accelerator="Alt+O")
        file_menu.add_command(
            label="csvの新規作成", command=create_csv_func, accelerator="Alt+N")
        file_menu.add_separator()
        file_menu.add_command(label="終了",  command=self.master.destroy)
        help_menu = tk.Menu(menu_bar, tearoff=tk.OFF)
        menu_bar.add_cascade(label="ヘルプ(H)", menu=help_menu)
        help_menu.add_command(
            label="ヘルプ", command=self.open_help, accelerator="Ctrl+H")
        help_menu.add_separator()
        # menu_bar.bind_all("", self.menu_open_click)
        self.master.config(menu=menu_bar)

    def source_file_path(self, event=None):
        # ファイルメニューの設定
        self.var_status.set(" ステータス : データファイル選択中...")
        file_name = filedialog.askopenfilename(initialdir=os.getcwd())
        if file_name != '':
            self.entry_input.delete(first=0, last=tk.END)
            self.entry_input.insert(index=0, string=file_name)
        self.var_status.set(" ステータス : 待機中")

    def dst_dir_path(self):
        self.var_status.set(" ステータス : 保存フォルダ選択中...")
        directory_name = filedialog.askdirectory(initialdir=os.getcwd())
        if directory_name != '':
            self.entry_output.delete(first=0, last=tk.END)
            self.entry_output.insert(index=0, string=directory_name)
        self.var_status.set(" ステータス : 待機中")

    def open_func(self):
        self.var_status.set(" ステータス : ファイル選択中...")
        file_name = filedialog.askopenfilename(initialdir=os.getcwd())
        if file_name != '':
            open_csv_func(file_name)
        self.var_status.set(" ステータス : 待機中")

    def open_help(self):
        # ヘルプメニューの設定
        open_help_func()

    def create_statusbar(self):
        self.var_status = tk.StringVar()
        self.var_status.set(" ステータス : 待機")
        self.statusbar = tk.Label(
            self.master, textvariable=self.var_status, width=130, anchor=tk.W)
        self.statusbar.grid(
            row=20, column=0, columnspan=self.root_width, pady=23)

    def shortcut(self):
        self.master.bind(sequence='<Alt-q>', func=sys.exit)
        self.master.bind(sequence='<Alt-r>',
                         func=lambda f1: self.gm_func())
        self.master.bind(sequence='<Control-h>',
                         func=lambda f2: self.open_help())
        self.master.bind(sequence='<Alt-s>',
                         func=lambda f3: self.source_file_path())
        self.master.bind(sequence='<Alt-d>',
                         func=lambda f4: self.dst_dir_path())
        self.master.bind(sequence='<Alt-n>', func=lambda f5: create_csv_func())
        self.master.bind(sequence='<Alt-o>', func=lambda f6: self.open_func())

    def arrangement(self):
        # ----ラベルの設定----
        self.var_intercept = []
        self.var_coefficient = []
        for i in range(4):
            self.var_intercept.append(tk.StringVar())
            self.var_intercept[i].set("a0: ")
            self.var_coefficient.append(tk.StringVar())
            self.var_coefficient[i].set("a1: ")

        label0 = tk.Label(self.master, text="パラメータ")

        label1 = tk.Label(self.master, text="系列1",
                          font=("Meiryo", "10", "normal"))
        label1_1 = tk.Label(self.master, text="凡例1", width=7)
        label1_2 = tk.Label(self.master, text='色', width=1)
        label1_3 = tk.Label(self.master, text="回帰範囲", width=7)
        label1_4 = tk.Label(self.master, text="~", width=1)
        label1_5 = tk.Label(self.master, text="シンボル", width=7)
        label1_6 = tk.Label(self.master, text="サイズ")

        label2 = tk.Label(self.master, text="系列2",
                          font=("meiryo", "10", "normal"))
        label2_1 = tk.Label(self.master, text="凡例2", width=7)
        label2_2 = tk.Label(self.master, text='色', width=1)
        label2_3 = tk.Label(self.master, text="回帰範囲", width=7)
        label2_4 = tk.Label(self.master, text="~", width=1)
        label2_5 = tk.Label(self.master, text="シンボル", width=7)
        label2_6 = tk.Label(self.master, text="サイズ")

        label3 = tk.Label(self.master, text="系列3",
                          font=("meiryo", "10", "normal"))
        label3_1 = tk.Label(self.master, text="凡例3", width=7)
        label3_2 = tk.Label(self.master, text='色', width=1)
        label3_3 = tk.Label(self.master, text="回帰範囲", width=7)
        label3_4 = tk.Label(self.master, text="~", width=1)
        label3_5 = tk.Label(self.master, text="シンボル", width=7)
        label3_6 = tk.Label(self.master, text="サイズ")

        label4 = tk.Label(self.master, text="系列4",
                          font=("meiryo", "10", "normal"))
        label4_1 = tk.Label(self.master, text="凡例4", width=7)
        label4_2 = tk.Label(self.master, text='色', width=1)
        label4_3 = tk.Label(self.master, text="回帰範囲", width=7)
        label4_4 = tk.Label(self.master, text="~", width=1)
        label4_5 = tk.Label(self.master, text="シンボル", width=7)
        label4_6 = tk.Label(self.master, text="サイズ")

        label_graph = tk.Label(self.master, text="プレビュー",
                               font=("MSゴシック", "10", "normal"))
        label_xrange1 = tk.Label(self.master, text='x軸範囲', width=7)
        label_xrange2 = tk.Label(self.master, text='~', width=1)
        label_yrange1 = tk.Label(self.master, text='y軸範囲', width=7)
        label_yrange2 = tk.Label(self.master, text='~', width=1)
        label_xaxis = tk.Label(self.master, text="x軸ラベル", width=7)
        label_yaxis = tk.Label(self.master, text="y軸ラベル", width=7)
        label_title = tk.Label(self.master, text="グラフタイトル")
        # label_input = tk.Label(self.master, text="ソース", width=7)
        label_output = tk.Label(self.master, text="保存先", width=7)
        label_gtype = tk.Label(self.master, text="構造", width=3)
        label_gsize = tk.Label(self.master, text="比率", width=3)

        self.label_intercept = [tk.Label(self.master, textvariable=self.var_intercept[i],
                                         justify=tk.LEFT) for i in range(4)]
        self.label_coefficient = [tk.Label(self.master, textvariable=self.var_coefficient[i],
                                           justify=tk.LEFT) for i in range(4)]

        # -----エントリーボックスの設定-----
        self.entry1_1 = ttk.Entry(self.master, justify=tk.LEFT)  # width =20
        self.entry1_2 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry1_3 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry1_4 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry1_5 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry1_6 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry1_7 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry1_1.insert(tk.END, self.config.get('values', 'legend1'))
        # self.entry1_2.insert(tk.END, "b")
        # self.entry1_5.insert(tk.END, "o")
        self.entry1_6.insert(tk.END, 20)

        self.entry2_1 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_2 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_3 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_4 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_5 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_6 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_7 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry2_1.insert(tk.END, self.config.get('values', 'legend2'))
        # self.entry2_2.insert(tk.END, "r")
        # self.entry2_5.insert(tk.END, "x")
        self.entry2_6.insert(tk.END, 20)

        self.entry3_1 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_2 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_3 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_4 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_5 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_6 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_7 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry3_1.insert(tk.END, self.config.get('values', 'legend3'))
        # self.entry3_2.insert(tk.END, "g")
        # self.entry3_5.insert(tk.END, "v")
        self.entry3_6.insert(tk.END, 20)

        self.entry4_1 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_2 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_3 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_4 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_5 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_6 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_7 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry4_1.insert(tk.END, "$\it{V_{4}}$")
        self.entry4_2.insert(tk.END, "y")
        self.entry4_5.insert(tk.END, "^")
        self.entry4_6.insert(tk.END, 20)

        self.entry_xaxis = ttk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_xaxis.insert(tk.END, self.config.get('values', 'xlabel'))

        self.entry_yaxis = ttk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_yaxis.insert(
            tk.END, self.config.get('values', 'ylabel'))

        self.entry_xrange1 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry_xrange1.insert(tk.END, self.config.get('values', 'xmin'))
        self.entry_xrange2 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry_xrange2.insert(tk.END, self.config.get('values', 'xmax'))
        self.entry_yrange1 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry_yrange1.insert(tk.END, self.config.get('values', 'ymin'))
        self.entry_yrange2 = ttk.Entry(self.master, justify=tk.LEFT)
        self.entry_yrange2.insert(tk.END, self.config.get('values', 'ymax'))
        self.entry_title = ttk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_title.insert(tk.END, self.config.get('values', 'title'))

        self.var_input = tk.StringVar()
        self.entry_input = ttk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_input.insert(
            tk.END, self.config.get('path', 'src'))

        self.entry_output = ttk.Entry(self.master, justify=tk.LEFT, width=55)
        self.entry_output.insert(
            tk.END, self.config.get('path', 'dst'))
        self.label_lat_const = tk.Label(self.master, text="格子定数〔m〕", width=10)
        self.entry_lat_const = ttk.Entry(
            self.master, justify=tk.LEFT, width=7)
        self.entry_lat_const.insert(tk.END, 600e-9)

        # ------ボタンの設定-----
        self.button_run = ttk.Button(self.master, text="RUN",
                                     width=8, command=self.gm_func)
        self.button_quit = ttk.Button(self.master, text="Quit",
                                      width=8, command=self.master.destroy)

        # -----チェックボックスの設定------
        self.bln_lr = [tk.BooleanVar() for i in range(4)]
        self.chk_lr = [tk.Checkbutton(self.master, variable=self.bln_lr[i],
                                      text='線形回帰', height=1) for i in range(4)]
        self.bln_xrange, self.bln_yrange = tk.BooleanVar(), tk.BooleanVar()
        self.chk_xrange = tk.Checkbutton(self.master, variable=self.bln_xrange)
        self.chk_yrange = tk.Checkbutton(self.master, variable=self.bln_yrange)
        self.bln_gridflag = tk.BooleanVar()
        if self.config.get("values", "gridf") == 'True':
            self.bln_gridflag.set(True)
        self.chk_gridflag = ttk.Checkbutton(
            self.master, variable=self.bln_gridflag, text="グリッド線")

        self.bln_legendflag = tk.BooleanVar()
        if self.config.get("values", "legendf") == 'True':
            self.bln_legendflag.set(True)
        self.chk_legendflag = ttk.Checkbutton(
            self.master, variable=self.bln_legendflag, text="凡例の表示")
        self.bln_line = tk.BooleanVar()
        if self.config.get("values", "flag_line") == 'True':
            self.bln_legendflag.set(True)
        self.chk_line = ttk.Checkbutton(
            self.master, variable=self.bln_line, text="点線の表示")
        self.bln_lightcone = tk.BooleanVar()
        if self.config.get("values", "flag_leaky") == 'True':
            self.bln_legendflag.set(True)
        self.chk_lightcone = ttk.Checkbutton(
            self.master, variable=self.bln_lightcone, text="Leaky領域")
        self.bln_norm = tk.BooleanVar()
        self.bln_norm.set(True)
        self.chk_norm = ttk.Checkbutton(
            self.master, variable=self.bln_norm, text="正規化")
        self.bln_src = tk.BooleanVar()
        if self.config.get("values", "srf") == 'True':
            self.bln_src.set(True)
        self.chk_src = ttk.Checkbutton(
            self.master, variable=self.bln_src, text="ソース")

        self.gtype = tk.StringVar()
        self.gtype_menu = ttk.Combobox(
            self.master, textvariable=self.gtype,  values=("None", "hex", "hext(KGK)", "hext(GKG)", "sq", "sqt", "1D"), width=9)
        self.gtype_menu.set(self.config.get('values', 'gtype'))
        # if self.config.get("values", "gtype") == 'True':
        #     self.bln_gtype.set(True)
        # self.chk_gtype = tk.Checkbutton(
        #     self.master, text="Leaky領域表示", variable=self.gtype)
        self.gsize = tk.StringVar()
        self.gsize_menu = ttk.Combobox(
            self.master, textvariable=self.gsize,  values=("8x6", "9x10", "8x10", "7x10", "6x10", "5x10"), width=9)
        self.gsize_menu.set("8x6")
        # ---comboboxの定義
        self.color = [tk.StringVar() for i in range(4)]
        self.symbol = [tk.StringVar() for i in range(4)]
        self.color_menu1_2 = ttk.Combobox(
            self.master, textvariable=self.color[0], values=("r", "g", "b"), width=17)
        self.symbol_menu1_5 = ttk.Combobox(
            self.master, textvariable=self.symbol[0], values=("o", "v", "x", "."), width=17)
        self.color_menu2_2 = ttk.Combobox(
            self.master, textvariable=self.color[1], values=("r", "g", "b"), width=17)
        self.symbol_menu2_5 = ttk.Combobox(
            self.master, textvariable=self.symbol[1], values=("o", "v", "x", "."), width=17)
        self.color_menu3_2 = ttk.Combobox(
            self.master, textvariable=self.color[2],  values=("r", "g", "b"), width=17)
        self.symbol_menu3_5 = ttk.Combobox(
            self.master, textvariable=self.symbol[2],  values=("o", "v", "x", "."), width=17)

        self.color_menu1_2.current(0)
        self.color_menu2_2.current(1)
        self.color_menu3_2.current(2)
        self.symbol_menu1_5.current(0)
        self.symbol_menu2_5.current(1)
        self.symbol_menu3_5.current(2)
        # ------ラベルの配置------
        # label0.grid(row=0, column=0, rowspan=15)

        label1.grid(row=0, column=1, columnspan=6)
        label1_1.grid(row=1, column=1)
        self.entry1_1.grid(row=1, column=2)
        label1_2.grid(row=1, column=3)
        self.color_menu1_2.grid(row=1, column=4)
        self.label_intercept[0].grid(row=1, column=5)
        label1_3.grid(row=2, column=1)
        self.entry1_3.grid(row=2, column=2)
        label1_4.grid(row=2, column=3)
        self.entry1_4.grid(row=2, column=4)
        self.label_coefficient[0].grid(row=2, column=5)
        label1_5.grid(row=3, column=1)
        self.symbol_menu1_5.grid(row=3, column=2)
        label1_6.grid(row=3, column=3)
        self.entry1_6.grid(row=3, column=4)
        self.chk_lr[0].grid(row=3, column=5)

        label2.grid(row=4, column=1, columnspan=5)
        label2_1.grid(row=5, column=1)
        self.entry2_1.grid(row=5, column=2)
        label2_2.grid(row=5, column=3)
        self.color_menu2_2.grid(row=5, column=4)
        self.label_intercept[1].grid(row=5, column=5)
        label2_3.grid(row=6, column=1)
        self.entry2_3.grid(row=6, column=2)
        label2_4.grid(row=6, column=3)
        self.entry2_4.grid(row=6, column=4)
        self.label_coefficient[1].grid(row=6, column=5)
        label2_5.grid(row=7, column=1)
        self.symbol_menu2_5.grid(row=7, column=2)
        label2_6.grid(row=7, column=3)
        self.entry2_6.grid(row=7, column=4)
        self.chk_lr[1].grid(row=7, column=5)

        label3.grid(row=8, column=1, columnspan=5)
        label3_1.grid(row=9, column=1)
        self.entry3_1.grid(row=9, column=2)
        label3_2.grid(row=9, column=3)
        self.color_menu3_2.grid(row=9, column=4)
        self.label_intercept[2].grid(row=9, column=5)
        label3_3.grid(row=10, column=1)
        self.entry3_3.grid(row=10, column=2)
        label3_4.grid(row=10, column=3)
        self.entry3_4.grid(row=10, column=4)
        self.label_coefficient[2].grid(row=10, column=5)
        label3_5.grid(row=11, column=1)
        self.symbol_menu3_5.grid(row=11, column=2)
        label3_6.grid(row=11, column=3)
        self.entry3_6.grid(row=11, column=4)
        self.chk_lr[2].grid(row=11, column=5)

        label_graph.grid(row=0, column=8, sticky=tk.S)
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
        self.chk_gridflag.grid(row=17, column=8, sticky=tk.W)
        self.chk_legendflag.grid(row=18, column=8, sticky=tk.W)
        self.gtype_menu.place(x="11.2cm", y="11.5cm")
        label_gtype.place(x="13.3cm", y="11.5cm")
        label_gsize.place(x="14.5cm", y="11.5cm")
        self.gsize_menu.place(x="15.2cm", y="11.5cm")
        self.chk_line.place(x="13.5cm", y="10.38cm")
        self.chk_lightcone.place(x="13.5cm", y="10.9cm")
        self.chk_norm.place(x="15.7 cm", y="10.38cm")
        self.label_lat_const.place(x="17.3cm", y="10.38cm")
        self.entry_lat_const.place(x="19.3 cm", y="10.38cm")
        label_title.grid(row=16, column=1)
        self.entry_title.grid(row=16, column=2, columnspan=5)
        self.chk_src.grid(row=17, column=1)
        self.entry_input.grid(row=17, column=2, columnspan=5)
        label_output.grid(row=18, column=1)
        self.entry_output.grid(row=18, column=2, columnspan=5)
        self.button_run.grid(row=19, column=1, columnspan=5)
        self.button_quit.grid(row=0, column=5, columnspan=3)

    def image_reading(self, src, dst, format='png'):
        file_name = os.path.splitext(os.path.basename(src))[0] + f'.{format}'
        img_path = rf'{dst}\{file_name}'
        img = Image.open(img_path)
        resized_size = (self.canvas_width, self.canvas_height)
        if self.canvas_width/img.width < self.canvas_height/img.height:
            resized_size = (self.canvas_width, round(
                img.height*self.canvas_width/img.width))
        else:
            resized_size = (round(img.width*self.canvas_height /
                            img.height), self.canvas_height)
        resized_img = img.resize(resized_size)
        self.graph = ImageTk.PhotoImage(
            resized_img, width=self.canvas_width, height=self.canvas_height, master=self.master)
        self.canvas.create_image(self.canvas_width//2,
                                 self.canvas_height//2, image=self.graph)

    def gm_func(self):
        self.var_status.set(" ステータス : 描画中...")
        try:
            config_writing(self)
            src = self.entry_input.get()
            dst = self.entry_output.get()
            xlabel = self.entry_xaxis.get()
            ylabel = self.entry_yaxis.get()
            title = self.entry_title.get()
            legends = [item.get() for item in [self.entry1_1,
                                               self.entry2_1, self.entry3_1, self.entry4_1]]
            colors = [item.get() for item in self.color]

            ranges = [[], []]
            if self.bln_xrange.get():
                ranges[0] = [float(item.get())
                             for item in [self.entry_xrange1, self.entry_xrange2]]
            else:
                ranges[0] = 0
            if self.bln_yrange.get():
                ranges[1] = [float(item.get())
                             for item in [self.entry_yrange1, self.entry_yrange2]]
            else:
                ranges[1] = 0
            markers = [item.get() for item in self.symbol]
            sizes = [float(item.get()) for item in [self.entry1_6,
                                                    self.entry2_6, self.entry3_6, self.entry4_6]]
            reg_range = [[item[0].get(), item[1].get()] for item in [[self.entry1_3, self.entry1_4], [self.entry2_3,
                                                                                                      self.entry2_4], [self.entry3_3, self.entry3_4], [self.entry4_3, self.entry4_4]]]
            lat_const = float(self.entry_lat_const.get())

            srf = int(self.bln_src.get())
            lr = [int(self.bln_lr[i].get()) for i in range(4)]
            legendf = int(self.bln_legendflag.get())

            gridf = int(self.bln_gridflag.get())
            normf = int(self.bln_norm.get())
            g_type = self.gtype.get()
            strings = self.gsize.get()
            idx = strings.find("x")
            figwidth, figheight = int(strings[:idx]), int(strings[idx+1:])
            linef = int(self.bln_line.get())
            lcf = int(self.bln_lightcone.get())

            reg_params = GM.graph_making(src, dst, title, legends, colors, ranges,
                                         markers, sizes,  reg_range, srf, lr, legendf, gridf, linef, lcf, normf, g_type, figwidth, figheight, xlabel, ylabel, lat_const)

            for i in range(4):
                if lr[i]:
                    self.var_intercept[i].set(f"a0: {reg_params[i][0]:.3e}")
                    self.var_coefficient[i].set(f"a1: {reg_params[i][1]:.3e}")
                else:
                    continue
            self.image_reading(src, dst)
            self.var_status.set(" ステータス : 描画完了")
        except:
            self.var_status.set(" ステータス : 描画エラー")


if __name__ == '__main__':
    main()
