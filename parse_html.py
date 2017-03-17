# -*- coding: utf-8 -*-
"""
index.htmlを生成するスクリプト。

"""

import os
from os.path import join
from mistune import markdown

dir_htmls = join("docs", "html")
path_index = join("docs", "index.html")
path_template = join("docs", "template.html")

#res = markdown("# KyotoGeoPython ホームページへようこそ")
res = ""

for folder in os.listdir(dir_htmls):
    if os.path.isdir(folder):
        res += markdown("## {}".format(folder))
        for file in os.listdir(join(dir_htmls, folder)):
            if file[-5:] == ".html":
                name = file[:-5]
                res += markdown("[{}]({})".format(name, join("html", folder, file)))
        
        
with open(path_template, "r", encoding="utf-8") as fp:
    template = "".join(fp.readlines())
with open(path_index, "w", encoding="utf-8") as fp:
    fp.write(template.format(res))
print(res)