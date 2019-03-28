#!/usr/local/bin/python3.7

import os
import re
import string

def find_all_class():
    
    for root, _, files in os.walk(path):
        for file_name in files:
            if os.path.splitext(file_name)[1] in filter_file_names:
                file_real_name = os.path.splitext(file_name)[0]
                file_path = os.path.join(root, file_real_name)
                all_class_dict[file_real_name] = file_path

def find_unused_class():
    
    pattern = '(?<=").*?(?=")'
    
    #匹配尖括号中的e内容 pattern1 = '(?<=<).*?(?=>)'
    for root, _, files in os.walk(path):
        for file_name in files:
            if os.path.splitext(file_name)[1] in filter_file_names:
                file_path = os.path.join(root, file_name)
                try:
                    file = open(file_path, 'r')
                    file_content = file.read()
                    result = re.findall(r'%s'%(pattern), file_content)
                    #print(file_name)
                    for result_name in result:
                        if result_name is not file_name:
                            file_real_name = os.path.splitext(file_name)[0]
                            if file_real_name in all_class_dict:
                                del all_class_dict[file_real_name]
                                print('已删除使用的类%s'%(file_real_name))
                finally:
                    file.close()


if __name__ == '__main__':
    
    path = os.getcwd()
    path = '/Users/edz/Desktop/JXEDT'
    all_class_dict = dict()
    filter_file_names = ['.m', '.h', '.xib','.mm', '.pch', 'storyboard']
    print ('当前的工作目录为%s'%(path))
    find_all_class()
    find_unused_class()
    
    for key in all_class_dict.keys():
        print('key = {}'.format(key))

