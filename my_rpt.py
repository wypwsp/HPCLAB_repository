import pandas as pd
#edited by wang

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


def csv_reader(fp, header, index_col, drop_lables, delimiter=',', low_memory=False):
    """

    :return:
    """
    data_df = pd.read_table(fp, header=2, index_col=None, delimiter=',', low_memory=False)
    data_df = data_df.drop(labels=drop_lables)
    return data_df
