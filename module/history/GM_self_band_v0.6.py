"""
Returns scatter graph of given (x,y) coordinates
"""

from email import header
from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
from tkinter.font import Font
from numpy import poly1d, linspace, exp, sqrt
from pandas import read_csv, read_clipboard
from os.path import basename, splitext
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import interpolate, optimize
import pyperclip


def main():
    # file_path = input("input file path >>>"
    # file_path = ".\\graph\\data.csv"
    file_path = r"C:\Users\rinko\software\GM_app_band\graph\data.csv"
    # df = read_csv(file_path, encoding='utf-8', header=0, index_col=None)
    df = read_clipboard(header=0, index_col=None)
    # L = len(df.columns) - 1
    L = len(df.columns) // 2

    src = file_path
    dst = r"."
    title = "タイトル"
    xlabel = '入力電圧 $\it{V_{1}}$ / $\mathsf{V}$'
    ylabel = '入力端子間電圧 $\it{V_{+} - V_{-}}$ / $\mathsf{μV}$'
    ranges = [[-10, 10], [-17, 17]]
    reg_range = [[-2.5, 2.5], [-1.5, 1.5]]
    legends = [f'y{i+1}' for i in range(L)]
    colors = ['b', 'r', 'g', 'y']
    markers = ['o', 'x', 'v', '^']
    sizes = [20, 20, 20, 20]
    lr = [0, 0, 0, 0]
    legendf = 1
    gridf = 1
    g_type = 1
    figwidth, figheight = 8, 6
    linef = 0
    lcf = 1
    graph_making(src, dst, title,  legends, colors, ranges, markers, sizes,
                 reg_range, lr, legendf, gridf, linef, lcf, g_type, figwidth, figheight, xlabel,  ylabel)


def regression(df, L, reg_range):
    reg_params = []
    model = LinearRegression()
    for j in range(L):
        label = df.columns[2*j]
        s, f = reg_range[j]
        data = df[(df[label] >= s) & (df[label] <= f)]
        x = data.iloc[:, 2*j].values.reshape(-1, 1)
        y = data.iloc[:, 2*j+1].values.reshape(-1, 1)
        model.fit(x, y)
        a, b = float(model.intercept_), float(model.coef_)
        reg_params.append([a, b])
    print(f'(intercept, coef) \n=\n {reg_params}')
    return reg_params


def graph_making(src, dst, title,  legends, colors, ranges, markers,
                 sizes, reg_range, lr, legendf=1, gridf=1, linef=1, lcf=1, g_type="None", figwidth=8, figheight=6, xlabel='x',  ylabel='y'):
    minorticksf = 1
    flag_vline = linef
    flag_leaky = lcf
    file_path = src
    font_size = 15
    # df = read_csv(file_path, encoding='utf-8', header=0, index_col=None)
    df = read_clipboard(header=0, index_col=None)
    # L = len(df.columns) - 1
    L = len(df.columns) // 2
    print(df, "\n", L)
    name = []
    for i in range(L):
        name.append(f'x{i}')
        name.append(f'y{i}')
    print(name)
    df.columns = name

    # tick bar : in
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family'] = "DejaVu Serif"
    plt.rcParams['font.size'] = font_size

    # plt.rcParams['font.family'] = 'Times New Roman'

    fig = plt.figure(dpi=80, figsize=(figwidth, figheight))
    # fig = plt.figure(dpi=80, figsize=(9, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')

    # ----plot-----
    # edgecolors = ['r', 'g', 'b']
    # facecolors=['None', 'None','None']
    z_orders = [i for i in range(L)]
    # x_legends = 'x'

    facecolors = ['None'] * L
    symbol_filled = [',', 'o', 'v', '^', '<', '>',
                     '8', 's', 'p', '*', 'h', 'H', 'D', 'd']
    symbol_unfilled = ['1', '2', '3', '4', '+', 'x', '|', '-']
    for i in range(L):
        if markers[i] in symbol_unfilled:
            facecolors[i] = colors[i]

    # ---------
    for i in range(L):
        ax.scatter(df.iloc[:, 2*i], df.iloc[:, 2*i+1],
                   marker=markers[i], c=colors[i], s=sizes[i])
    # ---------

    for i in range(L):
        # if g_type:
        #     ax.plot(df.iloc[:, 2*i], df.iloc[:, 2*i+1], markersize=sizes[i]//4,
        #             c=colors[i], linestyle='dashed', marker=markers[i],  zorder=z_orders[i])
        # else:
        ax.scatter(df.iloc[:, 2*i], df.iloc[:, 2*i+1],
                   marker=markers[i], c=colors[i], s=sizes[i])
        ax.scatter([], [], label=legends[i], s=20,
                   color=colors[i], marker=markers[i])
    ax.set_title(title)
    ax.set_xlabel(xlabel, fontsize=font_size)
    ax.set_ylabel(ylabel, fontsize=font_size)
    # ax.set_major_formatter(ScalarFormatter(useMathText=True))

    # -----regression curve-----
    reg_params = []
    if 1 in lr:
        reg_colors = colors
        for i in range(L):
            try:
                reg_range[i] = [float(reg_range[i][0]), float(reg_range[i][1])]
            except ValueError:
                reg_range[i] = [min(df.iloc[:, 2*i]), max(df.iloc[:, 2*i])]
        reg_params = regression(df, L, reg_range)

        for j in range(L):
            if lr[j] == 0:
                continue
            x = linspace(reg_range[j][0], reg_range[j][1])
            reg_curve = poly1d([reg_params[j][1], reg_params[j][0]])
            ax.plot(x, reg_curve(x),  linestyle='dashed',
                    color=reg_colors[j], linewidth='0.7')

    if minorticksf:
        ax.minorticks_on()
    if legendf:
        ax.legend()
    if gridf:
        ax.grid()
    # ax.tight_layout()
    # ax.xticks(np.arange(-4.0, 5.0, 2.0))  # under, upper, step
    # ax.yticks(np.arange(400, 900, 100))

    if g_type == "hex":
        # ------------------
        if flag_leaky:
            x_lightline_left = linspace(0, 2, 1000)
            x_lightline_right = linspace(3, 3+sqrt(3), 1000)
            x_lightline_center = linspace(2, 3, 1000)
            y1_ll = x_lightline_left/3
            y1_lr = -(x_lightline_right-3-sqrt(3))/3
            hyperbolic_func = \
                lambda x: sqrt(x**2-6*x+12)/3
            yc = hyperbolic_func(x_lightline_center)
            # yc = -(2-sqrt(3))*x_lightline_center/3+(6-2*sqrt(3))/3
            y2_ll = 1
            y2_lr = 1
            ax.fill_between(x_lightline_left, y1_ll, y2_ll,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_right, y1_lr, y2_lr,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_center, yc, y2_lr,
                            facecolor='gray', alpha=0.5)
        ax.set_xlim(0, 3+sqrt(3))
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 2, 3, 3+sqrt(3)])
        ax.set_xticklabels(
            ["$\mathsf{\Gamma}$", "$\mathsf{K}$", "$\mathsf{M}$", "$\mathsf{\Gamma}$"])
        if flag_vline == 1:
            ax.vlines(x=2, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=3, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
    # ------------------
    elif g_type == "hext(KGK)":
        # if flag_leaky:
        #     x_lightline_left = linspace(0, 2, 1000)
        #     x_lightline_right = linspace(3, 3+sqrt(3), 1000)
        #     x_lightline_center = linspace(2, 3, 1000)
        #     y1_ll = x_lightline_left/3
        #     y1_lr = -(x_lightline_right-3-sqrt(3))/3
        #     hyperbolic_func = \
        #         lambda x: sqrt(x**2-6*x+12)/3
        #     yc = hyperbolic_func(x_lightline_center)
        #     # yc = -(2-sqrt(3))*x_lightline_center/3+(6-2*sqrt(3))/3
        #     y2_ll = 1
        #     y2_lr = 1
        #     ax.fill_between(x_lightline_left, y1_ll, y2_ll,
        #                     facecolor='gray', alpha=0.5)
        #     ax.fill_between(x_lightline_right, y1_lr, y2_lr,
        #                     facecolor='gray', alpha=0.5)
        #     ax.fill_between(x_lightline_center, yc, y2_lr,
        #                     facecolor='gray', alpha=0.5)
        ax.set_xlim(0, 3+sqrt(3))
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 2, 3, 3+sqrt(3)])
        ax.set_xticklabels(
            ["$\mathsf{K}$", "$\mathsf{\Gamma_{m}}$", "$\mathsf{M_{m}}$", "$\mathsf{K}$"])
        if flag_vline == 1:
            ax.vlines(x=2, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=3, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
    # ------------------
    elif g_type == "hext(GKG)":
        # if flag_leaky:
        #     x_lightline_left = linspace(0, 2, 1000)
        #     x_lightline_right = linspace(3, 3+sqrt(3), 1000)
        #     x_lightline_center = linspace(2, 3, 1000)
        #     y1_ll = x_lightline_left/3
        #     y1_lr = -(x_lightline_right-3-sqrt(3))/3
        #     hyperbolic_func = \
        #         lambda x: sqrt(x**2-6*x+12)/3
        #     yc = hyperbolic_func(x_lightline_center)
        #     # yc = -(2-sqrt(3))*x_lightline_center/3+(6-2*sqrt(3))/3
        #     y2_ll = 1
        #     y2_lr = 1
        #     ax.fill_between(x_lightline_left, y1_ll, y2_ll,
        #                     facecolor='gray', alpha=0.5)
        #     ax.fill_between(x_lightline_right, y1_lr, y2_lr,
        #                     facecolor='gray', alpha=0.5)
        #     ax.fill_between(x_lightline_center, yc, y2_lr,
        #                     facecolor='gray', alpha=0.5)
        ax.set_xlim(0, 3+sqrt(3))
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 2, 3, 4,  6])
        ax.set_xticklabels(
            ["$\mathsf{\Gamma_{m}}$", "$\mathsf{K_{1}}$", "$\mathsf{M_{m}}$", "$\mathsf{K_{2}}$", "$\mathsf{\Gamma_{m}}$"])
        if flag_vline == 1:
            ax.vlines(x=2, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=3, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=4, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=6, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
    # ------------------
    elif g_type == "sq":
        if flag_leaky:
            x_lightline_left = linspace(0, 1, 1000)
            x_lightline_right = linspace(2, 2+sqrt(2), 1000)
            x_lightline_center = linspace(1, 2, 1000)
            y1_ll = x_lightline_left/2
            y1_lr = -(x_lightline_right-2-sqrt(2))/2
            hyperbolic_func = \
                lambda x: sqrt(x**2-2*x+2)/2
            yc = hyperbolic_func(x_lightline_center)
            y2_ll = 1
            y2_lr = 1
            ax.fill_between(x_lightline_left, y1_ll, y2_ll,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_right, y1_lr, y2_lr,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_center, yc, y2_lr,
                            facecolor='gray', alpha=0.5)
        ax.set_xlim(0, 2+sqrt(2))
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 1, 2, 2+sqrt(2)])
        ax.set_xticklabels(
            ["$\mathsf{\Gamma}$", "$\mathsf{X}$", "$\mathsf{M}$", "$\mathsf{\Gamma}$"], fontsize=font_size*1.3)
        if flag_vline == 1:
            ax.vlines(x=1, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=2, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
    # ------------------
    elif g_type == "sqt":
        if flag_leaky:
            x_lightline_left = linspace(0, 1, 1000)
            x_lightline_right = linspace(2, 2+sqrt(2), 1000)
            x_lightline_center = linspace(1, 2, 1000)
            y1_ll = x_lightline_left/2
            y1_lr = -(x_lightline_right-2-sqrt(2))/2
            hyperbolic_func = \
                lambda x: sqrt(x**2-2*x+2)/2
            yc = hyperbolic_func(x_lightline_center)
            y2_ll = 1
            y2_lr = 1
            ax.fill_between(x_lightline_left, y1_ll, y2_ll,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_right, y1_lr, y2_lr,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_center, yc, y2_lr,
                            facecolor='gray', alpha=0.5)
        ax.set_xlim(0, 2+sqrt(2))
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 1, 2, 2+sqrt(2)])
        ax.set_xticklabels(
            ["$\mathsf{\Gamma_{m}}$", "$\mathsf{X_{m}}$", "$\mathsf{M_{m}}$", "$\mathsf{\Gamma_{m}}$"], fontsize=font_size*1.3)
        if flag_vline == 1:
            ax.vlines(x=1, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
            ax.vlines(x=2, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
    # ------------------
    elif g_type == "1D":
        if flag_leaky:
            x_lightline_left = linspace(0, 1, 1000)
            x_lightline_right = linspace(1, 2, 1000)
            y1_ll = x_lightline_left/2
            y1_lr = -(x_lightline_right)/2+1
            y2_ll = 1
            y2_lr = 1
            ax.fill_between(x_lightline_left, y1_ll, y2_ll,
                            facecolor='gray', alpha=0.5)
            ax.fill_between(x_lightline_right, y1_lr, y2_lr,
                            facecolor='gray', alpha=0.5)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 1, 2])
        ax.set_xticklabels(
            ["$\mathsf{\Gamma}$", "$\mathsf{X}$",  "$\mathsf{\Gamma}$"])
        if flag_vline == 1:
            ax.vlines(x=1, ymin=0, ymax=1, colors='black',
                      linestyles='dashed', zorder=-0.1)
    if ranges[0] != 0:
        ax.set_xlim(ranges[0][0], ranges[0][1])
    if ranges[1] != 0:
        ax.set_ylim(ranges[1][0], ranges[1][1])
    print("save")
    # ----save as image----
    format = 'png'
    file_name = splitext(basename(file_path))[0] + f'.{format}'
    save_file = dst

    fig.savefig(rf'{save_file}\{file_name}',
                bbox_inches="tight", pad_inches=0.05, format=format, dpi=300)

    if __name__ == '__main__':
        plt.show(block=True)
    else:
        plt.show(block=False)

    plt.close()
    return reg_params


if __name__ == '__main__':

    main()
