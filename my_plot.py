# -*- coding:utf-8 -*-
# Author:              Qi Wang, Tongji Univ. <wangqi14@tongji.edu.cn>  
# Established at:      2023/3/8 9:42     
# Modified at:         2023/3/8 9:42                               
# Project:

from matplotlib import pyplot as plt
import numpy as np

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

    def plot_single(self, is_show: bool):
        """
            plot in a single diagram
        :param is_show:
        :return:
        """
        fig, ax = plt.subplots(1, 1, figsize=(6, 3), dpi=300, bbox_inches='tight')
        for line in self.line_array:
            ax.plot(line.x, line.y, label=line.y_name)
        # axes.set(xlim=(0, 50), ylim=(-2, 6))
        ax.set_xlabel('x_label')
        ax.set_ylabel('y_label')
        ax.set_title('sigle')

        # ax.axis('tight')
        ax.legend()

        # plt.xlabel('x_label')
        # plt.ylabel('y_label')
        # plt.xlim([0, 50])
        # plt.ylim([-2, 10])

        plt.savefig('name_save_fig', bbox_inches='tight')
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
    x = np.arange(0, 50, 0.01)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sqrt(x)
    L1 = Line(x, y1, 'time', 'curve1')
    L2 = Line(x, y2, 'time', 'curve2')
    L3 = Line(x, y3, 'time', 'curve3')
    L = [L1, L2, L3]

    sine_export = Export2D(L)
    sine_export.plot_single(is_show=True)
