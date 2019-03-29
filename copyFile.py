#!/usr/local/bin/python3.7

import os
import shutil

find_path = ''
filter_file_names = ['.m', '.h', '.xib','.mm', '.pch', 'storyboard']
new_path = ''

def find_all_class():
    
    for root, _, files in os.walk(path):
        for file_name in files:
            if os.path.splitext(file_name)[1] in filter_file_names:
                file_real_name = os.path.splitext(file_name)[0]
                file_path = os.path.join(root, file_real_name)
                shutil.copyfile(file_path, new_path)

if __name__ == '__main__':

    find_all_class()


