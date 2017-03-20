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


style_sheet = """hr {
  -moz-border-bottom-colors: none;
  -moz-border-image: none;
  -moz-border-left-colors: none;
  -moz-border-right-colors: none;
  -moz-border-top-colors: none;
  border-color: #EEEEEE -moz-use-text-color #FFFFFF;
  border-style: solid none;
  border-width: 1px 0;
  margin: 18px 0;
}
"""
res = ""

for folder in os.listdir(dir_htmls):
    if os.path.isdir(folder) and folder in ["基礎編", "応用編"]: 
        reses = dict(basic="", other="")
        res += markdown("## {}".format(folder))
        
        for file in os.listdir(join(dir_htmls, folder)):
            if file[-5:] == ".html":
                name = file[:-5]
                if file.startswith("Pythonの基礎"):
                    key = "basic"
                else:
                    key = "other"
                reses[key] += markdown("[{}]({})".format(name, join("html", folder, file)))
        
        res += reses["basic"] + reses["other"]
        res += markdown("***")
        
# リンク集を生成する
s_links = ""
for file in sorted(os.listdir("リンク集")):
    with open(join("リンク集", file), "r", encoding="utf-8_sig") as fp:
        for line in fp.readlines():
            s_links += markdown(line)

with open(join("docs", "template_Links.html"), "r", encoding="utf-8") as fp:
    html_links = "".join(fp.readlines()).format(style_sheet, s_links)
with open(join("docs", "html", "Links.html"), "w", encoding="utf-8") as fp:
    fp.write(html_links)
    

res += markdown("## その他")
# リンク集へのリンクを追加
# ライブラリ集へのリンクを追加
res += markdown("[ライブラリ集]({})".format(join("html", "ライブラリ集.html")))
res += markdown("[リンク集]({})".format(join("html", "Links.html")))

        
with open(path_template, "r", encoding="utf-8") as fp:
    template = "".join(fp.readlines())
with open(path_index, "w", encoding="utf-8") as fp:
    fp.write(template.format(style_sheet, res))
print(res)
