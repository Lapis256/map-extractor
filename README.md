# map-extractor
指定したワールドのマップデータを全て出力するツールです。Bedrock Edition限定です。

## 導入
### インストール
[Releases](https://github.com/Lapis256/map-extractor/releases) から v2.0.0 以降の実行ファイルをダウンロードして、パスを通します。

cargo をインストール済みの場合は以下のコマンドでインストール可能です。
```
cargo install --git https://github.com/Lapis256/map-extractor
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
