
# coding: utf-8

# In[1]:


import os
from jinja2 import Template
import glob
import subprocess
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

with open('notebook-template.html', 'r') as fp:
    template_html = fp.read()
template = Template(template_html)

target = 'docs/html'

# In[]


def write_body(path, body):
    with open(path, 'w') as fp:
        fp.write(body)


def path_nb_to_html(path_nb):
    return os.path.join(target, path_nb.replace('.ipynb', '.html'))


def find_nb():
    return glob.glob('*/*.ipynb')


def nbconvert_stdout(path_nb):
    cmd = ['jupyter', 'nbconvert', path_nb,
           '--to', 'html', '--template', 'basic', '--stdout']
    logger.debug(f'[My nbconvert] {" ".join(cmd)}')
    proc = subprocess.run(cmd, capture_output=True, encoding='utf-8')
    logger.debug(f'[My nbconvert] {path_nb}')
    logger.debug(f'[My nbconvert] {proc.stderr}')
    return proc.stdout


def extract_title(path_nb):
    return path_nb.split('/')[-1].replace('.ipynb', '')


def render(element, title):
    return template.render(body=element, title=title)


for path_nb in find_nb():
    element = nbconvert_stdout(path_nb)
    title = extract_title(path_nb)
    rendered = render(element, title)
    path_html = path_nb_to_html(path_nb)
    write_body(path_html, rendered)
