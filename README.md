pylab
====

python環境を少し便利にするため、お決まりの処理などをライブラリとして用意しておく。


Preparation
---

./libの中身任意の場所に置き、以下のいずれかの方法でpathを設定する。

### PYTHONPATH に追加する
- linux

```sh
# bash系
export PYTHONPATH='</your/lib/path>'

# csh系
setenv PYTHONPATH '</your/lib/path>'

# '</your/lib/path>:</other/path>' など、: で区切って複数のpathを登録することができる
```


- windows  
システムの詳細設定 > 環境変数 から設定


Usage
---

### グラフ描画ツール
- xy散布図
- 折れ線

### 実行ログとかファイル整理などするツール
他者のツールを使ったとき、実行ログが残らないとか、出力ファイルの階層が深いとか、痒い所を整理できるようなラッパー。
人間がよそ様のツールを実行しファイル整理などを行うのを、subprocessを使ってやってしまおうという発想。
カスタムする部分もあると思うので、そのベースになるものを作っておく。
例えば、あるプログラムを実行した後に、指定したフォルダに新しくできたファイルのリストを返すとか。
そのあとリストから必要なファイルを特定して必要な処理をすればいい。

###


description
---


Licence
---

<!-- [MIT](https://github.com/shka86/foo/blob/master/LICENCE) -->

Author
---

[shka86](https://github.com/shka86)
