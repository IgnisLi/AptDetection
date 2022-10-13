from typing import List
import pandas
import pandas.core.frame


def read_with_pandas(csv_file_path: str) -> pandas.DataFrame:
    '''使用pandas读取csv并返回

    :param csv_file_path: csv文件目录
    :return: csv内容（第一行为列名称）
    '''
    csv_content: pandas.DataFrame = pandas.read_csv(csv_file_path)
    return csv_content


def drop_the_column_with_the_specified_name(csv_content: pandas.DataFrame, column_name: List) -> pandas.DataFrame:
    '''丢弃指定名称的列

    :param csv_content: csv内容（第一行为列名称）
    :return: 已丢弃指定列后的csv内容
    '''
    existing_column_name: List = []
    # 遍历查找
    for each_column_name in column_name:
        if each_column_name in csv_content.columns:
            existing_column_name.append(each_column_name)
    # 丢弃
    droped_csv_content: pandas.DataFrame = csv_content.drop(columns=existing_column_name)
    return droped_csv_content