# -*- coding:utf-8 -*-
# Author:              Qi Wang, Tongji Univ. <wangqi14@tongji.edu.cn>  
# Established at:      2023/3/8 9:42     
# Modified at:         2023/3/8 9:42                               
# Project:

import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
import cmasher

# plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.sans-serif'] = 'Calibri'


class Line:
    """
        2D line definition
    """

    def __init__(self, x_array: 'np.ndarray|list', y_array: 'np.ndarray|list', x_name='', y_name=''):
        self.x = x_array
        self.y = y_array
        self.x_name = x_name
        self.y_name = y_name


class Curve:
    """
        3D curve definition
    """

    def __init__(self):
        pass


class Export2D:
    """
        2D plot library customization
    """

    def __init__(self, lines: 'list|Line'):
        self.line_array = lines
        if not hasattr(self.line_array, '__iter__'):
            self.line_array = [lines]

    def plot_single(self,
                    is_show: bool = True,
                    fig_save_name: str = None,
                    fig_save_format: tuple = ('svg', 'png'),

                    figsize: tuple = (6, 3),
                    dpi: int = 300,
                    fontsize: int = 16,

                    x_label: str = 'X-label',
                    y_label: str = 'Y-label',
                    title: str = None,
                    has_legend: bool = True,
                    xlim: tuple = None,
                    ylim: tuple = None,

                    line_property_grid: tuple = ('grey', '--', 0.3),
                    line_property_plot: tuple = ('--', 1.5, None, 0),
                    color: cm.colors = cm.Set2,
                    color_id: tuple = None,

                    fontsize_scaling_legend=1.2,
                    fontsize_scaling_ticks=1.2,
                    fig_layout='constrained',
                    x_label_style='italic',
                    y_label_style='italic',
                    title_style='italic',
                    tick_direction='in',
                    tick_axis='both',
                    grid_axis='both',
                    grid_which='major',
                    legend_loc='best',
                    legend_ncol=1,
                    legend_labelspacing=0.1,
                    legend_borderpad=0.2,
                    ):

        """
            plot in a single diagram
        :param fontsize_scaling_ticks:
        :param fontsize_scaling_legend:
        :param fig_layout:
        :param legend_borderpad:
        :param legend_loc:
        :param legend_labelspacing:
        :param legend_ncol:
        :param grid_which:
        :param tick_axis:
        :param grid_axis:
        :param tick_direction:
        :param title_style:
        :param y_label_style:
        :param x_label_style:
        :param color_id: color number in matplotlib.cm
                         for example: (127, 191, 255) for 3 lines in 256 colors bar
                         色阶图的调用索引
        :param color: cm.greys/ cm.Set2
        :param fontsize: basic fontsize
        :param has_legend: legend or not
        :param line_property_plot: one-dimensional(same), n-dimensional(different)
        :param fig_save_format:
        :param fig_save_name:
        :param line_property_grid:
        :param title:
        :param y_label: use $...$ for equations. e.g. r'$\alpha_i$ mm $\mathrm{abc}$'
        :param x_label:
        :param ylim:
        :param xlim:
        :param dpi:
        :param figsize:
        :param is_show:
        :return: None
        """

        # Colors: https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html
        color_map = color
        if not color_id:  # if color_id is not defined
            if type(color_map) == matplotlib.colors.ListedColormap:  # continuously, usually 256 colors
                color_id = np.arange(0, color_map.N, 1)
            else:  # separated, usually less than 10
                interval = int(color_map.N / (len(self.line_array) + 1))
                color_id = np.arange(interval, color_map.N - interval + 1, interval)

        # Line
        if type(line_property_plot[0]) is not tuple:  # Duplicate identical line_property_plot
            line_property_plot_temp = []
            [line_property_plot_temp.append(line_property_plot) for i in range(len(self.line_array))]
            line_property_plot = tuple(line_property_plot_temp)
        fig, ax = plt.subplots(1, 1, figsize=figsize, dpi=dpi, layout=fig_layout)
        for i, line in enumerate(self.line_array):
            ax.plot(line.x, line.y, label=line.y_name, color=color_map(color_id[i]),
                    linestyle=line_property_plot[i][0], linewidth=line_property_plot[i][1],
                    marker=line_property_plot[i][2], markersize=line_property_plot[i][3])

        # Axis
        ax.set(xlim=xlim, ylim=ylim)

        # Label
        ax.set_xlabel(x_label, fontstyle=x_label_style, fontsize=fontsize)
        ax.set_ylabel(y_label, fontstyle=y_label_style, fontsize=fontsize)

        # Ticks
        ax.tick_params(axis=tick_axis, direction=tick_direction, top=True, right=True,
                       labelsize=fontsize / fontsize_scaling_ticks)

        # title
        ax.set_title(title, fontstyle=title_style, fontsize=fontsize)

        # Grid
        if line_property_grid:
            ax.grid(visible=True, which=grid_which, axis=grid_axis, c=line_property_grid[0],
                    ls=line_property_grid[1], lw=line_property_grid[2])

        # Legend
        if has_legend:
            ax.legend(loc=legend_loc, fontsize=fontsize / fontsize_scaling_legend,
                      ncol=legend_ncol, labelspacing=legend_labelspacing, borderpad=legend_borderpad)

        # Save Figure
        for fmt in fig_save_format:
            plt.savefig(f'{fig_save_name}.{fmt}', format=fmt)

        # Show figure in IDE
        if is_show:
            plt.show(block=True)

    # def plot_multiple(self, is_show: bool):
    #     fig, axes = plt.subplots(len(sensors), 1, figsize=(16, 2 * len(acc_array)), dpi=300)
    #     if len(acc_array) > 1:
    #         for i in range(len(axes)):
    #             axes[i].plot(time_array, acc_array[i], label=f'{case}_{sensors[i]}')
    #             axes[i].legend()
    #     else:
    #         axes.plot(time_array, acc_array[0], label=f'{case}_{sensors[0]}')
    #         axes.legend()
    #     plt.show()
    #

    def export(self):
        pass


class Figure3D:
    """
        3D plot library customization
    """

    def __init__(self):
        pass


if __name__ == '__main__':
    print('start')
    x = np.arange(0, 50, 1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sqrt(x)
    L1 = Line(x, y1, 'time', 'curve1')
    L2 = Line(x, y2, 'time', 'curve2')
    L3 = Line(x, y3, 'time', 'curve3')
    L = [L1, L2, L3]

    sine_export = Export2D(L)
    sine_export.plot_single(is_show=True)
