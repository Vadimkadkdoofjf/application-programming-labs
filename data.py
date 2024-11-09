import cv2
import matplotlib.pyplot as plt
import pandas as pd

def create_dataframe(file:str) -> pd.DataFrame:
    """
    Making DataFrame
    :param file: name of csv file
    :return: DataFrame
    """
    data_frame = pd.read_csv(file)
    data_frame.columns=['re_path','abs_path']
    return data_frame

def add_columns(dataframe:pd.DataFrame)->None:
    """
    Adding Columns
    :param dataframe: DataFrame
    :return: None
    """
    images = [cv2.imread(img) for img in dataframe['abs_path']]
    dataframe['Height'] = [img.shape[0] if img is not None else 0  for img in images]
    dataframe['Width'] = [img.shape[1] if img is not None else 0  for img in images]
    dataframe['Channels'] = [img.shape[2] if img is not None else 0  for img in images]

def stat(dataframe:pd.DataFrame)-> pd.DataFrame:
    """
    Printing all stats
    :param dataframe: DataFrame
    :return: None
    """
    statistic = dataframe.loc[:, ('Height','Width','Channels')].describe()
    return statistic
def sort(dataframe: pd.DataFrame,max_h:int,max_w:int)->pd.DataFrame:
    """
    Sorting old dataframe and return new
    :param dataframe: old DataFrame
    :param max_h: max value of height
    :param max_w: max value of width
    :return: new DataFrame
    """
    new_data = dataframe[(dataframe['Height']<max_h)&(dataframe['Width']<max_w)]
    return new_data

def create_s_column(dataframe:pd.DataFrame)->None:
    """
    Making new column(Height*Width)
    :param dataframe: DataFrame
    :return: None
    """
    dataframe['S'] = dataframe['Height']*dataframe['Width']

def sort_s(dataframe:pd.DataFrame)->pd.DataFrame:
    """
    Sorting S columns
    :param dataframe: DataFrame
    :return: new DataFrame
    """
    new_data = dataframe.sort_values('S')
    return new_data

def hist(dataframe:pd.DataFrame)->None:
    plt.figure(figsize=(10,5))

    dataframe['S'].diff().hist()

    plt.title('гистограмма распределения площадей изображений')
    plt.xlabel('площадь')
    plt.ylabel('количество изображений')
    plt.show()