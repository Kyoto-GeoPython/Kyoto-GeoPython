# Kyoto-GeoPython

Kyoto-GeoPython の HP を管理するための GitHub repository です。

https://kyotogeopython.zawawahoge.com/ で公開されています。

# 開発者用

## 準備

- Python を実行できる環境を用意する
- パッケージ管理＆仮想環境構築用に [Poetry](https://python-poetry.org/docs/) をインストールしておく

```
$ poetry install
```

を実行すると、必要な依存関係が全て入る。

`.venv` という仮想環境が生成され、これを使って開発を行う。

## ipynb → 　HTML への変換

```
$ make convert
```

## ローカルサーバの起動

```
$ make start
```


ブラウザで `http://localhost:8080` を開く。

## Jupyter Notebook の起動

```
$ make jupyter
```
