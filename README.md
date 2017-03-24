# Kyoto-GeoPython

とりあえずのホームページが出来ました

詳細はCHANGELOG.mdを参照してください。

[https://kyoto-geopython.github.io/Kyoto-GeoPython/](https://kyoto-geopython.github.io/Kyoto-GeoPython/)

#### ipynb、リンク集の変更をホームページに反映させるためには

1. ipynb_html_converter.py（docs/htmlフォルダ下にipynbファイルに対応するhtmlを生成する）
1. parse_html.py（docs/html以下のファイルをもとにindex.htmlを生成する）

#### リンク集の書き方（多分conflictしないはず。。。）
1. リンク集以下のマークダウンファイルを開く
1. 「###」でリンク先のタイトルを[]でくくってそのURLを()で書く  
1. 数行説明を書く
1. 最後は「***」だけを書いた行を追加（ボーダーラインになる）
1. 確認は「parse_html.py」の実行後のdocs/html/Links.htmlで出来る