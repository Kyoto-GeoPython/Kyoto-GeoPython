
# coding: utf-8

from jinja2 import Template
import subprocess


def render_ipynb(src_path, title, template_path):
    body = get_nb_html(src_path)

    if template_path is not None:
        with open(template_path, 'r') as fp:
            template_html = fp.read()
        template = Template(template_html)
        body = template.render(body=body, title=title)

    return body


def get_nb_html(path_nb):
    cmd = ['jupyter', 'nbconvert', path_nb,
           '--to', 'html', '--template', 'basic', '--stdout']
    proc = subprocess.run(cmd, capture_output=True, encoding='utf-8')
    return proc.stdout


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--template', metavar='T', type=str,
                        help='template file to use for rendering')
    parser.add_argument('src', metavar='src', type=str,
                        help='source ipynb file to render')
    parser.add_argument('-o', metavar='output', type=str,
                        default='a.html', help='output html file')
    parser.add_argument('--title', metavar='title', type=str,
                        default='', help='title for header')
    args = parser.parse_args()

    template_path = args.template
    src_path = args.src
    output_path = args.o
    title = args.title

    body = render_ipynb(src_path, title, template_path)
    with open(output_path, 'w') as fp:
        fp.write(body)
