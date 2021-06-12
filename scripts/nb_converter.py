# coding: utf-8

from jinja2 import Template
import os
import glob
import asyncio

filename_title_map = {
    "src/基礎編/Pythonの基礎1.ipynb": {
        "title": "Pythonの基礎（１）",
    },
    "src/基礎編/Pythonの基礎2.ipynb": {
        "title": "Pythonの基礎（２）",
    },
    "src/基礎編/Matplotlib.ipynb": {
        "title": "Matplotlib"
    },
    "src/基礎編/Numpyの基礎（１）導入.ipynb": {
        "title": "Numpyの基礎（１）導入"
    },
    "src/基礎編/Numpyの基礎（２）生成関数.ipynb": {
        "title": "Numpyの基礎（２）生成関数"
    },
    "src/基礎編/Numpyの基礎（３）ufunc.ipynb": {
        "title": "Numpyの基礎（３）配列に関数を作用させる"
    },
    "src/基礎編/Numpyの基礎（４）データ型.ipynb": {
        "title": "Numpyの基礎（４）データ型（C,Fortranとの比較）"
    },
    "src/基礎編/Numpyの基礎（５）要素の参照.ipynb": {
        "title": "Numpyの基礎（５）要素の取り出し方"
    },
    "src/基礎編/Numpyの基礎（６）ブロードキャスト.ipynb": {
        "title": "Numpyの基礎（６）ブロードキャスト"
    },
    "src/基礎編/Numpyの基礎（７）便利なライブラリ群.ipynb": {
        "title": "Numpyの基礎（７）線形代数やフーリエ変換"
    },
    "src/基礎編/Numpyの基礎（８）ファイル入出力.ipynb": {
        "title": "Numpyの基礎（８）様々な形式に対応したファイル入出力"
    },
    "src/基礎編/ファイル読み込み.ipynb": {
        "title": "ファイル読み込み"
    },
    "src/基礎編/文字列操作（１）str.format.ipynb": {
        "title": "文字列操作（１）数値を文字列にフォーマットする"
    },
    "src/基礎編/文字列操作（２）strやファイル読み込み.ipynb": {
        "title": "文字列操作（２）文字列に関数を適用する"
    },
    "src/基礎編/読みやすいPythonコードを書こう.ipynb": {
        "title": "読みやすいPythonコードを書こう"
    },

    "src/応用編/Animation.ipynb": {
        "title": "Animation"
    },
    "src/応用編/Fortran, C言語 との連携.ipynb": {
        "title": "Fortran, C言語 との連携"
    },
    "src/応用編/Pandas―データ分析（１）Series.ipynb": {
        "title": "Pandas ― データ分析（１）時系列などをうまく扱えるようにする"
    },
    "src/応用編/Pandas―データ分析（２）DataFrame.ipynb": {
        "title": "Pandas ― データ分析（２）複数の列を持った表形式でデータを格納する"
    },
    "src/応用編/Pandas―データ分析（３）GroupBy.ipynb": {
        "title": "Pandas ― データ分析（３）データを分割し、個別に集計する"
    },
    "src/応用編/Pandas―データ分析（４）ファイル入出力.ipynb": {
        "title": "Pandas ― データ分析（４）高度なファイル入出力"
    },
    "src/応用編/Pandas―データ分析（５）応用：都道府県別人口推移.ipynb": {
        "title": "Pandas ― データ分析（５）応用：都道府県別人口推移"
    },
    "src/応用編/Seaborn ― matplotlib をより美しく、使いやすく.ipynb": {
        "title": "Seaborn ― matplotlib をより美しく、使いやすく"
    },
    "src/応用編/shやBashの代わりにPythonを使う.ipynb": {
        "title": "shやBashの代わりにPythonを使う"
    },
    "src/応用編/SymPyー代数演算（１）使い方.ipynb": {
        "title": "SymPy ― 代数演算（１）文字を文字のまま計算する"
    },
    "src/応用編/SymPyー代数演算（２）応用：二重振り子.ipynb": {
        "title": "SymPy ― 代数演算（２）応用：ラグランジアンから運動方程式を求めて二重振り子を解く"
    },

    "src/スライド/1日目スライド.ipynb": {
        "title": "1日目スライド"
    },

    "src/基礎編/Numpyを使う際の注意点.ipynb": {
        "title": "Numpyを使う際の注意点"
    },
    "src/基礎編/numpy（基礎編）.ipynb": {
        "title": "Numpy（基礎編）"
    },
    "src/応用編/SymPyー代数演算.ipynb": {
        "title": "SymPyー代数演算"
    },
    "src/応用編/Pandas　―　データ分析.ipynb": {
        "title": "Pandas　―　データ分析"
    },
}

async def convert_nb_with_template(template: Template,
                                   path_nb: str, title: str, out_dir: str):
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
        if path_nb not in filename_title_map:
            print(path_nb)
            raise FileNotFoundError

        if "title" not in filename_title_map[path_nb]:
            raise Exception(f"title key not found: {path_nb}")

        title = filename_title_map[path_nb]["title"]
        task = asyncio.create_task(
            convert_nb_with_template(template, path_nb, title, out_dir),
        )
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':

    asyncio.run(main())
