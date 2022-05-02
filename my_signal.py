# -*- coding:utf-8 -*-
# Author:              Qi Wang, Tongji Univ. <wangqi14@tongji.edu.cn>
# Established at:      2021/11/1 14:57
# Modified at:         2022/5/2 12:21
# Project:

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import signal
from scipy import linalg
from scipy.fftpack import fft
from scipy.signal import butter, lfilter
import matplotlib
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def my_dft(time, motion):
    """
    :param time: numpy.ndarray
    :param motion: numpy.ndarray
    :return: dictionary
    0 frequency_array
    1 amplitude_array
    2 magnitude_array
    3 complex_array
    4 phase_array
    5 powers_as_msa_array
    6 dB_array

    references:
    1. OriginLab help files and scipy references
    2. scipy.fftpack.fft
    z: complex ndarray
    with the elements:
    [y(0),y(1),..,y(n/2),y(1-n/2),...,y(-1)]        if n is even
    [y(0),y(1),..,y((n-1)/2),y(-(n-1)/2),...,y(-1)]  if n is odd
    where:
    y(j) = sum[k=0..n-1] x[k] * exp(-sqrt(-1)*j*k* 2*pi/n), j = 0..n-1
    """
    dt = time[1] - time[0]
    z = fft(motion)
    n = len(z)
    t_n = int(n / 2) + 1
    # frequency x-axis
    # TODO check the following equations
    frequency_array = np.linspace(0, int(n / 2) / (dt * n), t_n)
    # amplitude 振幅
    amplitude_array = 2 * np.abs(z)[0: t_n] / n
    # magnitude of z 复数的幅值
    magnitude_array = np.abs(z)[0: t_n]
    # z: complex array
    complex_array = z[0: t_n]
    # phase of z
    # phase = arc-tangent(Im/Re)
    phase_array = np.arctan(np.imag(complex_array) / np.real(complex_array))
    # powers as MSA from origin LAB
    powers_as_msa_array = np.sqrt(1/2) * amplitude_array
    # dB from origin LAB
    dB_array = 20 * np.log(amplitude_array)
    return {'frequency':frequency_array,
           'amplitude':amplitude_array,
           'magnitude':magnitude_array,
           'complex':complex_array,
           'phase':phase_array,
           'powers':powers_as_msa_array,
           'dB':dB_array}



def my_butter_lowpass_filter(data, cutoff=60, fs=200, order=4):
    """
    https://blog.csdn.net/kkkxiong1/article/details/84941992
    :param data:
    :param cutoff:
    :param fs:
    :param order:
    :return:
    """
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y


def my_hanning(freq, amp, bandwidth):
    """
    :param freq: array 频率序列
    :param amp: array 傅里叶幅值序列
    :param bandwidth: 带宽 单位为频率
    :return: 通过窗函数后的幅值
    """
    fs = 1. / (freq[1] - freq[0])
    # N取奇数
    N = int(2 * np.floor(bandwidth * fs / 2) + 1)
    # 注意！修改以下窗函数#######
    window = np.hanning(N)
    # ########################
    amp_filtered = []
    for i in range(len(amp)):
        n = int((N - 1) / 2)
        # 分三段讨论
        if i < n:
            amp_window = np.dot(window[n - i: N], amp[0: i + n + 1]) / np.sum(window[n - i: N])
        elif i >= len(amp) - n:
            amp_window = np.dot(window[0: n + len(amp) - i], amp[i - n: len(amp)]) / np.sum(window[0: n + len(amp) - i])
        else:
            amp_window = np.dot(window, amp[i - n: i + n + 1]) / np.sum(window)
        amp_filtered.append(amp_window)
    return amp_filtered

def plot_3d(X, Y, Z):
    """
    :param X: ndarray
    :param Y: ndarray
    :param Z: ndarray
    :return: return None
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Make data.
    X, Y = np.meshgrid(X, Y)
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, linewidth=0, cmap=cm.coolwarm, antialiased=False)
    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(11))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.06f'))
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=1, aspect=10)
    plt.show()
    return None