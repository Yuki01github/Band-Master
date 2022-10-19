# グラフ描画用GUIアプリケーション

建て増し方式で拡張してしまったため、グラフの系列を3つまでしか追加できない。

- グラフの色・シンボル・サイズ
- タイトル、軸ラベル
- 凡例・グリッド線の表示/非表示
- 散布図/折れ線図
- 線形回帰<br>
などのフォーマットを設定可能.

# 手順

### 1. 可視化するデータの選択

- ツールバーの「ソース」から可視化するcsvデータを選択
  (「ソース」のテキストボックスに直接フルパスを入力してもよい)
- データのフォーマットは以下に示す通り。

例:<br>
	x1	,y1	,x2	,y2 <br>
	-10,	16.5397,-10	,15
	...

### 2. ツールバーの保存先から保存するフォルダを指定

### 3. チェックボックスで線形回帰の有無を設定

- 必要に応じて回帰範囲を与える(デフォルトは全データ)。

### 4. タイトルやシンボル、サイズ、色などを設定

- 色は基本的に単語の頭文字で指定(e.g. <span style="color:red;">赤</span>→r, <span style="color:purple;">紫</span>→p)
- シンボルにはアルファベットや記号を指定可能。
- 軸ラベルやタイトルについては、`$\it{f}$` のように記述することで、TeX記法によるレンダリングが行われる.(詳細は[公式リファレンス](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html))

### 5. `RUN`でグラフをpng形式で保存

- プレビューウィンドウで結果を確認できる。

### 6. `QUIT`でアプリを終了

- 次回起動時に一部プロット設定が引き継がれる。

# その他
- ./module/figureの各種画像は同名のファイルで差し替え可能.

# Author
* Yuki Ishii
* Keio University
* rinkobu@keio.jp

# License
This application is under [MIT license](https://opensource.org/licenses/mit-license.php)
