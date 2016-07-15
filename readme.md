## 注意
本項目使用 GPL v3 協議，改編者請注意開源並使用相同協議。本人輕度執行 Apache 關於文檔的標準，卽，對修改的內容做出說明，改編者如能指明所修改的內容則最善。

## 說明
Acorns 是個素材收集庫。這些素材的主要服務對象是製作輸入法和電子辭書，也收一些適合閒暇閱讀的文章。愛收集的人常被戲稱爲「松鼠症患者」，而松鼠最喜歡收集的莫過於橡實。這項目的名字就這麼出現了。  
基礎 retrieve date: 2015/06/22 。有不一樣的會再說明。
由於本說明太長，有礙本人觀瞻，故將不那麼感興趣的說明放在另幾個 md 文件中。

分類|內容
----|----
[字](#字)|字表、各種對漢字的編碼與拆分
[Unihan](#Unihan)|整理自 [Unihan](http://www.unicode.org/Public/UNIDATA/) 的數據
[索引](#索引)|辭書頁碼，粗分爲[古典類](#古典類)、[權威類](#權威類)、[字形類](#字形類)
[百科](#百科)|語辭的「百科分書」，而非「百科全書」
[全文](#全文)|書籍全文，主收[辭書](#辭書類)，重要[古籍](#一般古籍)也來者不拒
[其他](#其他)|雜物箱，腳本、不好歸類也不好處理的文件

## 字
見[字.md](字.md)。

## Unihan
見[Unihan.md](Unihan.md)。

## 索引

### 古典類

名稱|retrieved|說明|備註
----|----|----|----
[說文解字圖像查閱](http://www.byscrj.com/jmm/shuowen/dcd.js)|15/08/20|各爲字頭、詁林正編、補遺、補編、後編外編、通訓定聲、祁嶲藻繫傳、述古堂繫傳、段注、連筠簃義證、崇文義證、句讀、宋本、藤花榭、汲古閣、孫星衍、陳昌治|可[在線查閱](http://www.byscrj.com/jmm/shuowen/find.html)
[說文解字詁林+古文字詁林+說文通訓定聲](http://bbs.xueleku.com/forum.php?mod=viewthread&tid=399185)|15/06/22|各爲部首、字頭、正編、補遺、補編、古文字詁林冊、古文字詁林頁、武漢古籍 1983 版通訓定聲頁碼|說文詁林依中華書局版，無後編，補遺無字也排碼，雲南版用(X-976)/4+244查。古文字詁林缺十一冊
[洪武正韻](https://github.com/BYVoid/ytenx/blob/11dfc4bbfcb27857826efffc8463b0362af87b04/ytenx/tcenghyonhtsen/data/Dzih.txt)|15/06/22|保留字頭、頁碼、韻部、聲調、反切|流水號和拉丁化之類就不要了
[康煕字典](https://github.com/cjkvi/cjkvi-dict/blob/master/kx2ucs.txt)|16/07/11|頁碼對應同文書局版，含備攷和補遺。帶星號的通常是某個字頭下的「古文」|修正鐕、呈、况、㤺、㠼、𦣽、⿰木𠕁、⿱⿰歹巳廾、重排 1595.072 - 1595.082
[經籍䉵詁](http://www.byscrj.com/jmm/Classic/data-sorted.js)|15/06/22|轉 utf-8 ，做了些細微修正，比如構字法、批量遺漏的字符|可[在線查閱](http://www.byscrj.com/jmm/Classic/search.html)
[經傳釋詞札記](http://pdawiki.com/forum/forum.php?mod=viewthread&tid=14155)|15/09/21|編輯器隨便排序||

### 權威類

名稱|retrieved|說明|備註
----|----|----|----
[大漢和辭典 字](https://github.com/cjkvi/cjkvi-dict/blob/master/dkw2ucs.txt)|15/06/22|Unicode 碼轉成字了||
[大漢和辭典 詞](https://github.com/cjkvi/cjkvi-dict/blob/master/dkw-word.txt)|15/06/22|有三千多字顯示爲「■」。錯字多，還缺少量詞條|原書「眾」的寫法「亻」不蓋「人」，且時「衆」，時「眾」
[國語字典（趙元任等）](http://pdawiki.com/forum/forum.php?mod=viewthread&tid=14227)|15/10/07|拆包、用 EmEditor 按頁碼重排||
[王力古漢語字典](http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=730553)|15/06/22|AHK 逐筆提取，刪去集、畫，留部|原文件常錯偏旁部首或用形近字，修正見[後](#王力古漢語字典修正)
[漢語大詞典 紙本 詞](https://github.com/cjkvi/cjkvi-dict/blob/master/hydcd-word.txt)|15/06/22|原文件大量使用日本漢字、舊字形，不符原書，故據[列表](其他.md#漢大詞用字)調整。|表中數百字用頁碼或獨立號碼表示，現全部替換|其他個別錯誤見[後](#漢語大詞典修正)
漢語大詞典 紙本 字|15/06/22|基於紙本詞表和大五碼版字表等已有資源製作而成|缺字很多
[漢語大詞典 光碟 字](http://bbs.gxsd.com.cn/forum.php?mod=redirect&goto=findpost&ptid=974990&pid=4330027)|15/06/22||衹有大五碼所收字|
[漢語大字典 第二版](http://bbs.unispim.com/forum.php?mod=redirect&goto=findpost&ptid=31606&pid=121595)|15/06/30|||
[漢語大字典+中文大辭典+故訓匯纂](http://bbs.xueleku.com/forum.php?mod=viewthread&tid=369962)|15/06/22|提取其 data-sorted.js||
[現代漢語詞典 第六版](http://pdawiki.com/forum/forum.php?mod=viewthread&tid=13755)|15/09/01|用 EmEditor 自動排序||
[異體字字典](https://github.com/cjkvi/cjkvi-dict/blob/master/twedu-dict.txt)|15/06/22||有官網沒有的字，來源不詳
[異體字字典2](https://github.com/kcwu/moedict-variants/blob/master/list.txt)|15/06/22|詳見[Wiki Page](https://github.com/kcwu/moedict-variants/wiki)||

##### 王力古漢語字典修正
鬧、鬨、𩰓、緬、緘、鰍、帶、勢、黴、黲、纔、䋿、𧉅、𧍧、鑰、鋚、蕭、蘚、𧆌、虛、褻、襁、賒、𧦧、䩉、𨎌、呂、宮、閭、閶、吳、嘯、㘊、嚘、啑、蕆、藕、藼、陝、䤃、襗、肓、䏿、𪎭、痲、瘞、痬、壚、媼、嶪、憂、𢥘、坺、摲、𢶡、掔、攕、𢹲、攮、攣、哂、𪊨、麐、麌、雱、昴、䁝、晝、杠、㭒、搥、譥、賮、竇、餘、膞、䕓、𥹤、玂、禪、麈、哆、禠、譶、樁、庛、剌、蠯、鵃、䚢、𧕰、皃、𦢌、縳、罼、獆、麡、胄、𧏚、嘗、髺、疁、畼、晝、獎、娜、䣛、㝔、寠、歭、臝、嬴、褏、裏、㢮、彄、惲、𢝰、昡、眘、晙、皙、㬉、䁔、曈、禊、櫺、櫱、櫾、櫜、櫎、瀹、灈、𤄶、灟、為、溈、鳥、鳴、隝、鷦、鷙、鴂、鷥、鷫、䴠、雟、矕、矙、砯、𥛙、禜、禬、熲、豎、籪、籮、羅、簠、䈾、𩔞、𩅞、㷠、甡、觷、鴇、𪊍、賷、賺、賾、頤、闓、𨵦、闃、𤮘、䱍、䲔、蘤、璜、齷、齯、䬟、賢、驘、驪、驌、䮧、騺、驡、藚、荁、荆、姸、豣、筓、銒、鉶、幷、腁、逬、缾、餠、絣、蛢、輧、滋、荓、⿰氵茲、⿰𧾷幷、⿰幷色、⿰金幷、⿰𧾷幵、⿰氵幵、⿰石幵、⿱竹衛、⿱艹寗、⿰目𢿌、⿰⿱艹幵刂等字

##### 漢語大詞典修正
比如「嗥噦」原書找不到。「矇瞍」和「矇𥈟」、「轗𨎺」和「轗𨎹」、「蹴踏」和「蹴蹹」、「霶𩃰」和「霶𩃱」、「韭菹」和「韭葅」、「𪒱𪑠」和「𪒱𪒡」誤作同一個。「𠌯昧」誤作「儷昧」、「𠵯喇」誤作「咶喇」、「喫詬」誤作「吃詬」、「𠷺」誤作「哱」、「𡃆楞嗆啷」誤作「噌楞嗆啷」、「𡸚嶭」誤作「嶘嶭」、「㕓闠」誤作「廛闠」、「凼肥」誤作「氹肥」、「撆缺」誤作「撇缺」、「鳧趨雀躍」誤作「島趨雀躍」、「鳧雛」誤作「島雛」。更神奇的還有「甯」誤作「寧」、「床」誤作「牀」、「箒」誤作「帚」、「穅」誤作「糠」、「𧃳」誤作「褻」、「韈」誤作「襪」、「蟑螂」的「螂」都打錯。

### 字形類
見[字形類.md](字形類.md)。

## 百科

名稱|retrieved|說明|備註
----|----|----|----
四庫大辭典|15/06/22|百度盤上搜到的 mdx ，隨手修正約一百條|基於李學勤版，應是 OCR 的，錯誤非常多
中國哲學辭典|15/06/22|從超星提取，順便添加詞序和繁體化|韋政通， 2009
[中國道敎大辭典](http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=954856)|15/06/22|||
[中華道教大辭典](http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=954856)|15/06/22|||
本草綱目|15/06/22|提取自 ss: 10444286 ，補 GBK 編碼不兼容字，拆分有又名的詞條|劉衡如、劉山永校， 1998，新版已出

## 全文

### 辭書類

名稱|retrieved|說明|備註
----|----|----|----
[說文解字注](https://github.com/cjkvi/cjkvi-dict/blob/master/swjz.xml)|15/06/22|有很多字是問號||
[說文解字綜合檢索](http://www.byscrj.com/jmm/shuowen/dcd1.js)|15/08/20|各爲字號、卷第、部首、北師篆、華師篆、字頭、反切音、解說、拼音、注音|可[在線查閱](http://www.byscrj.com/jmm/shuowen/find_all.html)
[開放康煕字典](https://github.com/ksanaforge/kangxizidian/)|15/06/22|把一堆 xml 合倂成一個，去掉多餘信息|底本是同文版，將不倫不類的臺灣現行標準強加於康煕字典，還有很多細節誤
[現代漢語詞典 第五版](http://bbs.unispim.com/forum.php?mod=viewthread&tid=31657)|15/06/22|||
古漢語常用字字典|15/06/22|去掉 [trn][/trn] 符號（因爲沒什麼用）||
[CC-CEDICT](http://cc-cedict.org/wiki/)|15/06/22|釋義非常簡短的中英辭典，類似 thesaurus|另有 [StarDict](http://simonwiles.net/files/cc-cedict/stardict-cc-cedict.tar.bz2) 版

### 一般古籍

名稱|retrieved|說明|備註
----|----|----|----
[世說新語](https://zh.wikisource.org/wiki/%E4%B8%96%E8%AA%AA%E6%96%B0%E8%AA%9E/%E5%85%A8%E8%A6%BD)|16/07/04|改成了 TeX ，文字不修改||

## 其他
見[其他.md](其他.md)。