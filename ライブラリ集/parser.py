# -*- coding: utf-8 -*-
"""

"""
from mistune import markdown
with open("ライブラリ集.md", "r", encoding="utf-8_sig") as fp:
    lines = fp.readlines()
    
import pathlib

p = pathlib.Path("..")
path = p / "docs" / "html" / "ライブラリ集.html"
#%%
#with open("template.html", "r", encoding="utf-8") as fp:
#    content = "".join(fp.readlines()).format("".join((markdown(line) for line in lines)))
#with open(str(path), "w", encoding="utf-8") as fp:
#    fp.write(content)
    
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
style_sheet = """
p{
  margin: 0px;
}
"""
#%%
with open(str(p / "docs" / "template_library.html"), "r", encoding="utf-8_sig") as fp:
    content = "".join(fp.readlines()).format(style_sheet,
                     "".join((markdown(line) for line in lines)))
#%%
with open(str(path), "w", encoding="utf-8_sig") as fp:
    fp.write(content)