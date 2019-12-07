
# coding: utf-8

# In[1]:


import os
from jinja2 import Template
import glob


# In[2]:


with open('notebook-template.html', 'r') as fp:
    template_html = fp.read()

template = Template(template_html)
target = os.path.join("docs", "html")


# In[8]:


def listofipynb():
    folders = [folder for folder in os.listdir() if os.path.isdir(folder) and not folder[0].startswith('.')]
    path_title_html = []
    for folder in folders:
        paths = glob.glob(f'{folder}/*.ipynb')
        path_title_html.extend([(path, path.split('/')[1].split('.')[0], path.replace('ipynb', 'html')) for path in paths])
    return path_title_html

def nb2html(path_nb, title):
    body = get_ipython().getoutput('jupyter nbconvert "$path_nb" --to html --template basic --stdout')
    print(body)
    element_html = '\n'.join(body[1:])
    html_rendered = template.render(body=element_html, title=title)
    return html_rendered


# In[9]:


for path_nb, title, path_html in listofipynb():
    with open(os.path.join(target, path_html), 'w') as fp:
        print(path_html)
        print(path_nb)
        fp.write(nb2html(path_nb, title))

