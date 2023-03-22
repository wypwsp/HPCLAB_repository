# -*- coding:utf-8 -*-
# Author:              Qi Wang, Tongji Univ. <wangqi14@tongji.edu.cn>
# Established at:      2021/11/1 14:57
# Modified at:         2022/5/2 12:21-
# Project:

import pandas as pd


def rpt_reader(fp, header=1, index_col=None, delim_whitespace=True):
    """
    returns:
    data_df: pandas dataframe of the rpt files
    usually, column 1: time, column 2~... acceleration/velocity/displacement
    used for Abaqus 6.22 .rpt report files
    
    data_df.values
    """
    data_df = pd.read_table(fp, header=header, index_col=index_col, delim_whitespace=delim_whitespace)
    return data_df


def csv_reader(fp, header, index_col, drop_labels, delimiter=',', low_memory=False):
    """

    :return:
    """
    data_df = pd.read_table(fp, header=header, index_col=index_col, delimiter=delimiter, low_memory=low_memory)
    data_df = data_df.drop(labels=drop_labels)
    # data_df.dropna(axis=0, how='any', inplace=True)
    return data_df
