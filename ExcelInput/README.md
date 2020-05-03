# ExcelInput
- テンプレートのExcelファイルの内容を出力ファイルへ転写
- 定型の入力をまとめて行うことができる
- テンプレートと同じアドレス($A$1など)のセル値をコピーする
- 値のみで書式のコピーは行わない

## 【前提】
- pythonのxlwingsライブラリが必要となる
    ```
    conda install xlwings
    ```

## 【利用方法】
- テンプレートと出力ファイル指定する
- 書き込みを別ファイルにする場合は3番目で指定することも可
    - 省略すれば出力ファイル=書き込みファイルとなる
```
> python main.py [テンプレートExcel] [出力Excel] (書き込みExcel)
```