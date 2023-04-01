# custom_translate
日本語のテキストファイルを英語へ翻訳し、txtファイルを出力します  
  
## 目的
描いたイラストを公開する際、説明文等は日本語と英語を併記していますが私は英語がさっぱりです  
なので、今までは[Google Translate](https://translate.google.com)を頼っていましたが  
一部の単語を変換したい場合があったのでcustom_translateを作成しました  
大まかには下記の様な流れです
  
1. [googletrans](https://github.com/ssut/py-googletrans/blob/master/README.rst)を使い、翻訳したデータを取得する
2. 1に対して、自分にとって必要な置換を行う
3. 2を書き出す

## 注意
googletransには[制限](https://github.com/ssut/py-googletrans#note-on-library-usage)があります  
使用する際、ご自分の使用頻度や文量が制限に引っかかるかどうかご確認下さい  

## 確認した動作環境
- macOS Monterey 12.6.3
- python 3.9.6
- googletrans 3.1.0a0
    - 3.0.0では正常に動作しなかった為、3.1.0a0をインストール

## 実行方法
`python3 custom_translate.py example.txt`

### 例
example.txtの内容が下記だったとします  
日本語が読め、特定の作品に対しての理解が有る方には  
これで伝わると思います(伝わると思って下さい)  
  
```
私はアイマスの美希が好きです

美希のイラストを頻繁に描きますが
美希はもっと可愛く、もっと格好良い筈だ
という意識を常に心がけています
```
  
これをgoogletransで翻訳した場合  
下記の様になります  
  
```
I like Miki from Imus

I often draw illustrations of Miki
Miki should be prettier and prettier
I always keep in mind that
```
  
やりたい事が見えたと思います  
imusをなんとかしたいですね  
ですので、それを置換し出力します  
  
```
I like Miki from THE IDOLM@STER

I often draw illustrations of Miki
Miki should be prettier and prettier
I always keep in mind that
```
  
それっぽい結果が出力されました  
念の為、これを日本語へ翻訳してみます  
  
```
THE IDOLM@STERのミキが好きです

ミキのイラストをよく描きます
みきちゃんはもっともっと可愛くなるべき
私は常にそれを心に留めています
```
  
元の文に比べ、それなりに変わっていますが  
何となく言わんとする事はわかるか？感が満載の結果になりました  
ですが嘆いても仕方がありません、これが精一杯です  
英語が苦手な自分が悪い  

## 置換定義変更のやり方
custom_translate.pyに下記の様な部分があります  
簡単に言えば `imus` という文字(大文字小文字は気にしないで構いません)を `THE IDOLM@STER` へ変えますよという定義だとお考え下さい
  
```
replace_str_dic = {
    'imus': 'THE IDOLM@STER'
}
 ```

定義を追加/編集したい場合はこんな感じにします

```
replace_str_dic = {
    'idol master': 'THE IDOLM@STER',
    'mirishita': 'THE IDOLM@STER MILLION LIVE! THEATER DAYS'
}
 ```

## Licence
- `Googletrans` - [MIT](https://github.com/ssut/py-googletrans/blob/master/README.rst)
