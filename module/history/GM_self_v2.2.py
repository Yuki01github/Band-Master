"""
Returns scatter graph of given (x,y) coordinates
"""

from matplotlib import markers
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    # file_path = input("input file path >>>"
    file_path = r".\graph\data.csv"
    df = pd.read_csv(file_path, encoding='utf-8', header=0, index_col=None)
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
    colors = ['b', 'r', 'o', 'y']
    markers = ['o', 'x', 'v', '^']
    sizes = [20, 20, 20, 20]
    lr = [0, 0, 0, 0]
    graph_making(src, dst, title, legends, colors, ranges, markers,
                 sizes, reg_range, lr, xlabel, ylabel)


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
                 sizes, reg_range, lr, xlabel='x',  ylabel='y'):
    file_path = src
    df = pd.read_csv(file_path, encoding='utf-8', header=0, index_col=None)

    # L = len(df.columns) - 1
    L = len(df.columns) // 2

    name = []
    for i in range(L):
        name.append(f'x{i}')
        name.append(f'y{i}')
    df.columns = name

    # tick bar : in
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # plt.rcParams['font.family'] = 'Times New Roman'

    fig = plt.figure(dpi=80, figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')

    # ----style-----
    # edgecolors = ['r', 'g', 'b']
    # facecolors=['None', 'None','None']
    z_orders = [0, 1, 2, 3]
    # x_legends = 'x'

    for i in range(L):
        plt.scatter(df.iloc[:, 2*i], df.iloc[:, 2*i+1], label=legends[i], s=sizes[i],
                    color=colors[i], marker=markers[i], zorder=z_orders[i])

    plt.title(title)
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend()
    if ranges[0] != 0:
        plt.xlim(ranges[0][0], ranges[0][1])
    if ranges[1] != 0:
        plt.ylim(ranges[1][0], ranges[1][1])
    # plt.tight_layout()
    # plt.xticks(np.arange(-4.0, 5.0, 2.0))  # under, upper, step
    # plt.yticks(np.arange(400, 900, 100))

    # -----regression curve-----
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
        x = np.linspace(reg_range[j][0], reg_range[j][1])
        reg_curve = np.poly1d([reg_params[j][1], reg_params[j][0]])
        plt.plot(x, reg_curve(x), linestyle='dashed',
                 color=reg_colors[j], linewidth='0.7')

    # ----save as image----
    format = 'png'
    file_name = os.path.splitext(os.path.basename(file_path))[0] + f'.{format}'
    save_file = dst

    plt.savefig(rf'{save_file}\{file_name}',
                bbox_inches="tight", pad_inches=0.05, format=format, dpi=300)

    plt.show()
    plt.close()


if __name__ == '__main__':

    main()
