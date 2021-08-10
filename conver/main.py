import argparse
import os
import shutil
import sys

import pandas as pd
from nptdms import TdmsFile

APP_DESC = """
这是一个简单好用的tdms格式转换为xlsx的工具.
"""
# print(APP_DESC)

if len(sys.argv) == 1:
    sys.argv.append('--help')
parser = argparse.ArgumentParser()
# parser.add_argument('-v', '--verbose', default=0, help="print more debuging information")
parser.add_argument('-s', '--store', help="保存输出的文件到指定位置")
parser.add_argument('path', metavar='Path', nargs='+', help="tdms文件/文件夹路径")
args = parser.parse_args()

source_dir: str = str(args.path[0]).strip()

if os.path.isdir(source_dir):
    output_path = source_dir + '/output'
else:
    output_path = source_dir

if args.store is not None:
    output_path = str(args.store).strip()


def get_metadata_info(tdms_file_path: str):
    # 这里主要是避免不清楚 group_name和channel_name导致无法提取数据，建议前期先跑这个函数来输出对应的信息
    tdms_file = TdmsFile.read(tdms_file_path)
    for group in tdms_file.groups():
        group_name = group.name
        for channel in group.channels():
            channel_name = channel.name
            properties = channel.properties
            data = channel[:]
            print('group_name', group_name, 'channel_name', channel_name, 'len', len(data))


def conver_to_excel(tdms_file_path: str, output_path: str):
    tdms_file = TdmsFile.read(tdms_file_path)
    excel_data = None
    for group in tdms_file.groups():
        group_name = group.name
        for channel in group.channels():
            channel_name = channel.name
            properties = channel.properties
            data = channel[:]
            if len(data) > 0:
                if excel_data is None:
                    excel_data = pd.DataFrame(data, columns=[f'{group_name}-{channel_name}'])
                # else:
                #   excel_data[f'{group_name}-{channel_name}'] = data
        if not os.path.exists(output_path[:output_path.rfind('/')]):
            os.makedirs(output_path[:output_path.rfind('/')])
        excel_data.to_excel(output_path, index=None)


def cover_dir_to_excel(dir_path: str, output_dir_path: str):
    print(f'开始转换文件夹: {dir_path}')
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.tdms'):
            tdms_path = os.path.join(dir_path + '/' + file_name)
            output_path = output_dir_path + '/' + file_name.replace('.tdms', '.xlsx')
            conver_to_excel(tdms_path, output_path)
            print(f'{file_name} 转换完成')


def dfs(search_path: str):
    cover_dir_to_excel(search_path, output_path + search_path.replace(source_dir, ''))
    for file_name in os.listdir(search_path):
        file_path = os.path.join(search_path + '/' + file_name)
        if os.path.isdir(file_path):
            if file_name[0] != '.':
                dfs(file_path)


def main():
    if not os.path.exists(source_dir):
        print('目标路径不存在')

    if os.path.isdir(source_dir):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        else:
            shutil.rmtree(output_path)
            os.makedirs(output_path)

        dfs(source_dir)
    else:
        conver_to_excel(source_dir, source_dir.replace('.tdms', '.xlsx'))


if __name__ == '__main__':
    main()
