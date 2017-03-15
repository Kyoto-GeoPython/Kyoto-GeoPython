# -*- coding: utf-8 -*-

"""
実行すると、ipynbをhtmlに変換し、それらをpublic内にフォルダ構造を再現して保存する。
"""

import os

target = "public"
try:
    os.mkdir(target)
except FileExistsError:
    pass


for folder in os.listdir():
    if os.path.isdir(folder) and folder[0] != ".":
        for file in os.listdir(folder):
            if file[-6:] == ".ipynb":
                path_output = os.path.join(target, folder)
                try:
                    os.mkdir(path_output)
                except FileExistsError:
                    pass
                path_html = os.path.join(target, path_output, file)
                line = 'jupyter nbconvert --to html "{}" --output-dir="{}"'.format(os.path.join(folder, file),path_output)
#                print(line)
                os.system(line)
                print("creating html from {} to {}".format(os.path.join(folder, file),
                                  path_output))