# map-extractor
指定したワールドのマップデータを全て出力するツールです。Bedrock Edition限定です。

## 導入
### 依存関係
Python 3.8 以上

### インストール
```
pip install git+https://github.com/Lapis256/map-extractor.git
```

## 使い方
指定したワールドのマップデータから作成された画像を全てを出力します。また、出力先はデフォルトでは実行指定しているディレクトリ直下に出力されます。
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
