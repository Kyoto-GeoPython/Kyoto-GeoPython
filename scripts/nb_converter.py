# coding: utf-8

from jinja2 import Template
import os
import glob
import asyncio


async def convert_nb_with_template(template: Template,
                                   path_nb: str, out_dir: str):
    cmd = ['jupyter', 'nbconvert', f'"{path_nb}"',
           '--to', 'html', '--template', 'basic', '--stdout']
    
    print(f'[My nbconvert] {" ".join(cmd)}')
    proc = await asyncio.create_subprocess_shell(
        " ".join(cmd),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    print(f'[My nbconvert] {path_nb}')
    print(f'[My nbconvert] {proc.stderr}')

    stdout, stderr = await proc.communicate()
    print(stderr.decode('utf-8'))
    body = stdout.decode('utf-8')

    title = path_nb.split('/')[-1].replace('.ipynb', '')
    rendered = template.render(body=body, title=title)
    path_html = path_nb.replace('.ipynb', '.html')
    path_html = path_html.replace('src/', '')
    path_html = os.path.join(out_dir, path_html)
    with open(path_html, 'w') as fp:
        fp.write(rendered)


async def async_hello(cmd: str):
    print("async start ", cmd)
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print("stdout ", stdout)
    print("stderr ", stderr)


async def main():
    with open('template/notebook-template.html', 'r') as fp:
        template_html = fp.read()

    template = Template(template_html)

    out_dir = 'docs/html'

    tasks: list(asyncio.Task) = []
    for path_nb in glob.glob('src/*/*.ipynb'):
        task = asyncio.create_task(
            convert_nb_with_template(template, path_nb, out_dir),
        )
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':

    asyncio.run(main())
