from nptdms import TdmsFile
import os, sys, shutil
import pandas as pd

print('请输入文件路径')
source_dir: str = sys.stdin.readline().strip()

def get_metadata_info(tdms_file_path: str):
    # 这里主要是避免不清楚 group_name和channel_name导致无法提取数据，建议前期先跑这个函数来输出对应的信息
    tdms_file = TdmsFile.read(tdms_file_path)
    for group in tdms_file.groups():
        group_name = group.name
        for channel in group.channels():
            channel_name = channel.name
            properties = channel.properties
            data = channel[:]
            print('group_name', group_name,'channel_name',  channel_name,'len', len(data))

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
                else:
                    excel_data[f'{group_name}-{channel_name}'] = data
        if not os.path.exists(output_path[:output_path.rfind('/')]):
            os.makedirs(output_path[:output_path.rfind('/')])
        excel_data.to_excel(output_path, index=None)

def cover_dir_to_excel(dir_path: str, output_dir_path:str):
    print(f'开始转换文件夹: {dir_path}')
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.tdms'):
            tdms_path = os.path.join(dir_path + '/' + file_name)
            output_path = output_dir_path + '/' + file_name.replace('tdms', 'xlsx')
            conver_to_excel(tdms_path, output_path)
            print(f'{file_name} 转换完成')

output_path = source_dir + '/output'

if not os.path.exists(output_path):
    os.makedirs(output_path)
else:
    shutil.rmtree(output_path)
    os.makedirs(output_path)
    
def dfs(search_path: str):
    cover_dir_to_excel(search_path, output_path + search_path.replace(source_dir, ''))
    for file_name in os.listdir(search_path):
        file_path = os.path.join(search_path + '/' + file_name)
        if os.path.isdir(file_path):
            if file_name[0] != '.':
                dfs(file_path)

dfs(source_dir)        
            


        
