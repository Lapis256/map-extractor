# map-extractor
指定したワールドのマップデータを全て出力するツールです。

## 導入
### 依存関係
Python 3.8 以上

### インストール
```
pip install git+https://github.com/Lapis256/map-extractor.git
```

## 使い方
実行場所に指定したワールドにあるマップデータを出力します。
```
map_extractor <ワールドのディレクトリ>
```

--output オプションで出力先のディレクトリを指定可能です。
```
map_extractor <ワールドのディレクトリ> --output <出力先のディレクトリ>
```
-o とする事も可能です。
```
map_extractor <ワールドのディレクトリ> -o <出力先のディレクトリ>
```
