from tkinter import *


def main():
    splash_func()


def splash_func():

    splash_root = Tk()
    splash_root.overrideredirect(1)  # スプラッシュ画面のタイトルバー非表示
    ww = splash_root.winfo_screenwidth()  # モニターの横幅取得
    wh = splash_root.winfo_screenheight()  # モニターの縦幅取得
    splash_root.geometry("400x157+"+str((ww-400)//2)+"+" +
                         str((wh-157)//2))  # モニターの中央に画面を表示

    photo = PhotoImage(
        file=r".\module\figure\Bandmaster_logo.gif")  # 表示させたい画像ファイル指定
    canvas = Canvas(bg='#25292e', width=400, height=157)  # 画像のサイズに合わせて幅と高さ調整
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=photo, anchor=NW)

    splash_root.after(3000, lambda: splash_root.destroy())

    mainloop()


if __name__ == '__main__':
    main()
