## 注意
本項目使用 GPL v3 協議。改編者請注意開源並使用相同協議。
本人輕度執行 Apache 關於文檔的標準，卽，對修改的內容做出說明。索引的修正多記錄在 https://github.com/821/Acorns 中，此處主要記錄圖片的處理。

## 說明
Acorns 是個素材收集庫。這些素材的主要服務對象是製作輸入法和電子辭書。
愛收集的人常被戲稱爲「松鼠症患者」，而松鼠最喜歡收集的莫過於橡實。這項目的名字就這麼出現了。
基礎 retrieve date: 2015/06/22 。有不一樣的會再說明。
這個項目最早放在 Google Code ，後來用了一段時間 Google Sites ，現在還是覺得 Github 較安心。

## 字

### ids
https://github.com/cjkvi/cjkvi-ids/blob/master/ids.txt
http://kanji-database.sourceforge.net/ids/ids.html
漢字拆解成部分，比如「明」拆成「日月」。
問題很多，暫不整理。
又，「[零時字引](https://github.com/g0v/z0y/)」就是用了這份材料。

### 部件檢索
http://blog.xuite.net/fg_wang/twblog/309627490
原爲 mdx ，通過 JavaScript 實現查詢，轉爲 tsv 。
事實上也吸收了 ids.txt 的成果。

### 四角號碼
http://bbs.unispim.com/forum.php?mod=viewthread&tid=31674
原爲 chm 文件，轉爲 tsv 。

### 筆順
https://github.com/rime/brise/blob/master/preset/stroke.dict.yaml
114954 條數據，但是錯誤太多——漢字的筆順，中臺敎育部都搞錯很多。
修正「成」字相關筆順。「必」「忄」「火」「右」「有」等工作量太大，改不完。

### 臺灣讀音
https://github.com/lukhnos/openvanilla/blob/master/DataTables/bpmf-ext.cin
97968 條臺灣單字讀音數據。
同項目還有行列、大易之類臺灣輸入法的碼表，然並卵。

### cns2py
https://github.com/cjkvi/cjkvi-data/blob/master/cns2py.txt
90933 個漢字的臺灣讀音。

### 古籍字頻統計
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=972697
原爲 Excel 文件，轉爲 tsv 。

## 索引

### 說文解字圖像查閱
http://www.byscrj.com/jmm/shuowen/dcd.js
retrieve date: 2015/08/20
各項依次爲字頭，詁林正編，詁林補遺，詁林補編，詁林後編外編，通訓定聲，祁嶲藻繫傳，述古堂繫傳，段注，連筠簃義證，崇文義證，句讀，宋本，藤花榭，汲古閣，孫星衍，陳昌治。
在線查閱：http://www.byscrj.com/jmm/shuowen/find.html

### 說文解字詁林+古文字詁林+說文通訓定聲
http://bbs.xueleku.com/forum.php?mod=viewthread&tid=399185
從 Excel 轉成了 txt 。各項依次爲部首、字頭、說文解字詁林正編頁碼、說文解字詁林補遺頁碼、說文解字詁林補編頁碼、古文字詁林冊數、古文字詁林頁碼、說文通訓定聲頁碼。
說文解字詁林頁碼依中華書局 1988 版，雲南 2006 版頁碼可用此公式換算：(X-976)/4+244。本表不含無後編（說文逸字）文字及頁碼，補遺沒有的字也會被打上頁碼。
古文字詁林第十一冊未錄入頁碼。
說文通訓定聲頁碼依 1983 版武漢古籍版。

### 洪武正韻
https://github.com/BYVoid/ytenx/blob/11dfc4bbfcb27857826efffc8463b0362af87b04/ytenx/tcenghyonhtsen/data/Dzih.txt
保留字頭、頁碼、韻部、聲調、反切，流水號和拉丁化之類就不要了。

### 康煕字典
https://github.com/cjkvi/cjkvi-dict/blob/master/kx2ucs.txt
頁碼對應最爲通用的同文書局版，含備攷和補遺。
根據新版 Unicode 修正了「鐕」、「呈」、「况」和「㤺」。「GKX-1595.80」根據原書改作「㠼」，「KX0391.023」據原書改作「𦣽」。
大抵帶星號的是某個字頭下的「古文」。
個別拆字不是很好，比如 1123.33 ，作「⿳⿲⿷匚一⿱古八𠆢？」（那個問號不知道是幹嘛），不如作「⿳⿶𦥑古八⿱人女」。還有 111.30 ，應該是「⿳巛𠔿⿵冂厶」。
「柵の形が微妙に違う」改作「⿰木𠕁」。
1602.022 誤作「𣨂」，改爲「⿱𢀸廾」。
1595.072 至 KX1595.082 順序錯誤，已修正。

### 經籍䉵詁
http://www.byscrj.com/jmm/Classic/data-sorted.js
轉成 utf-8 ，做了一些細微的修正，比如構字法、批量遺漏的字符。
在線查閱： http://www.byscrj.com/jmm/Classic/search.html

### 大漢和辭典 字
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw2ucs.txt
Unicode 碼轉成字了。

### 大漢和辭典 詞
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw-word.txt
原書「眾」的寫法，「亻」不蓋「人」。而且使用比較混亂，時而「衆」，時而「眾」。
錯誤較多，比如「奉諱」和「奉義」之間有兩個詞，本表僅一。又如「丟招」誤作「丟昭」，屬於同音字誤錄。還有三千多字顯示爲「■」，改正是個大工程。

### 國語字典（趙元任等）
http://pdawiki.com/forum/forum.php?mod=viewthread&tid=14227
retrieve date: 2015/10/07
拆包、用 EmEditor 按頁碼重排。

### 經傳釋詞札記
http://pdawiki.com/forum/forum.php?mod=viewthread&tid=14155
retrive date: 2015/09/21
原爲 mdx ，現轉成 txt 。順序用編輯器隨便排了一下。

### 王力古漢語字典
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=730553
原程序無法批量導出，用的格式也很詭異，所以用 AHK 逐筆提取成 txt ，提取時維持了原有的順序。之後用 Python 寫了個腳本來添加每一頁的字序，受限於源文件，錯誤很多。
王力古漢語字典的檢索還有 mdx 版，是經同源材料加工而成（完全繼承了本材料的錯誤，包括一些非常腦殘的獨特錯誤，故可判定爲同源材料），順序是錯亂的。本文件也有錯亂，但好一些，前面很小部分似乎校對過，順序是正確的，後面纔開始亂排。
刪去沒意義的集、畫，因王力不時在部首處加以解釋，故留部。
據原書修補了鬧、鬨、𩰓、緬、緘、鰍、帶、勢、黴、黲、纔、䋿、𧉅、𧍧、鑰、鋚、蕭、蘚、𧆌、虛、褻、襁、賒、𧦧、䩉、𨎌、呂、宮、閭、閶、吳、嘯、㘊、嚘、啑、蕆、藕、藼、陝、䤃、襗、肓、䏿、𪎭、痲、瘞、痬、壚、媼、嶪、憂、𢥘、坺、摲、𢶡、掔、攕、𢹲、攮、攣、哂、𪊨、麐、麌、雱、昴、䁝、晝、杠、㭒、搥、譥、賮、竇、餘、膞、䕓、𥹤、玂、禪、麈、哆、禠、譶、樁、庛、剌、蠯、鵃、䚢、𧕰、皃、𦢌、縳、罼、獆、麡、胄、𧏚、嘗、髺、疁、畼、晝、獎、娜、䣛、㝔、寠、歭、臝、嬴、褏、裏、㢮、彄、惲、𢝰、昡、眘、晙、皙、㬉、䁔、曈、禊、櫺、櫱、櫾、櫜、櫎、瀹、灈、𤄶、灟、為、溈、鳥、鳴、隝、鷦、鷙、鴂、鷥、鷫、䴠、雟、矕、矙、砯、𥛙、禜、禬、熲、豎、籪、籮、羅、簠、䈾、𩔞、𩅞、㷠、甡、觷、鴇、𪊍、賷、賺、賾、頤、闓、𨵦、闃、𤮘、䱍、䲔、蘤、璜、齷、齯、䬟、賢、驘、驪、驌、䮧、騺、驡、藚、荁、荆、姸、豣、筓、銒、鉶、幷、腁、逬、缾、餠、絣、蛢、輧、滋、荓、⿰氵茲、⿰𧾷幷、⿰幷色、⿰金幷、⿰𧾷幵、⿰氵幵、⿰石幵、⿱竹衛、⿱艹寗、⿰目𢿌、⿰⿱艹幵刂等字（多數是搞錯偏旁部首，用形近字，錄入者可能是用了非常不淸晰的掃描版來對照，也可能是在 OCR 的基礎上粗校而成）和部分排序，刪去多餘的字。

### 漢語大詞典 紙本 詞
https://github.com/cjkvi/cjkvi-dict/blob/master/hydcd-word.txt
剝離出了紙本部分的詞彙。由於源文件使用了大量的日本漢字，而且舊字形也不符合漢大詞的習慣，所以用自己寫的一個列表「漢大詞用字」來把用字修正爲與紙本儘量統一的狀態。
漢語大詞典本身有很多奇怪的地方，比如把「示」的新舊字形當作截然不同的字做獨立解釋。而「示」的舊字形沒有獨立的編碼，所以本文件將二者合倂。「焭」分別入火、几二部，「缹」分別入「火」、「缶」二部，就不改了。
表中數百字使用頁碼或獨立號碼表示，現在全部改正。對於 Unicode 沒有的字，則使用拆字法。
表中不少錯誤，比如「嗥噦」，原書找不到。「矇瞍」出現兩次，查原書，發現後一個應該是「矇𥈟」，「轗𨎺」和「轗𨎹」、「蹴踏」和「蹴蹹」、「霶𩃰」和「霶𩃱」、「韭菹」和「韭葅」、「𪒱𪑠」和「𪒱𪒡」也誤作同一個。「𠌯昧」誤作「儷昧」、「𠵯喇」誤作「咶喇」、「喫詬」誤作「吃詬」、「𠷺」誤作「哱」、「𡃆楞嗆啷」誤作「噌楞嗆啷」、「𡸚嶭」誤作「嶘嶭」、「㕓闠」誤作「廛闠」、「凼肥」誤作「氹肥」、「撆缺」誤作「撇缺」、「鳧趨雀躍」誤作「島趨雀躍」、「鳧雛」誤作「島雛」。更神奇的還有「甯」誤作「寧」、「床」誤作「牀」、「箒」誤作「帚」、「穅」誤作「糠」、「𧃳」誤作「褻」、「韈」誤作「襪」、「蟑螂」的「螂」都打錯。均改正。

### 漢語大詞典 紙本 字
基於紙本詞表和大五碼版字表等已有資源製作而成，缺字很多。

### 漢語大詞典 光碟 字
http://bbs.gxsd.com.cn/forum.php?mod=redirect&goto=findpost&ptid=974990&pid=4330027
衹有大五碼所收字。

### 漢語大字典 第二版
http://bbs.unispim.com/forum.php?mod=redirect&goto=findpost&ptid=31606&pid=121595
retrieve date: 2015/06/30

### 漢語大字典+中文大辭典+故訓匯纂
http://bbs.xueleku.com/forum.php?mod=viewthread&tid=369962
提取其 data-sorted.js 。

### 異體字字典
https://github.com/cjkvi/cjkvi-dict/blob/master/twedu-dict.txt
這個文件可以檢索到五萬多個字，收錄時去掉了 twedu- 這個無用前綴。
另外這個文件竟然有一些官網沒有的字，可能是原來有，但被刪除了。

### 異體字字典2
https://github.com/kcwu/moedict-variants/blob/master/list.txt
說明見其 [Wiki Page](https://github.com/kcwu/moedict-variants/wiki) 。
我把文件中的 /variants/tmp/ 和 .png 去掉了。
跟日本人做的文件相比，多了圖片地址。然而異體字字典原本是 Big5 的，向 Unicode 的推進過程不完善，很多 Unicode 已經有的字在日本版有了，但本文件跟官網一樣，衹能直接檢索到兩萬字。異體字字典官網對 Unicode 也是有意識的，很多圖片的地址實際上就是 Unicode 編碼。
有些不連續的號，比如 A00270-018 和 A00270-022 ，並不是顯示沒有這個字的，而是衹有字頭沒有釋義。兩個文件都沒有收錄。
此處順便吐槽一下異體字字典，修到第五版還不能直接檢索，第六版可以檢索了，又無聊把圖片的 link 全部改掉。比如原本一個字的字號是 B00001 ，那麼他的正字通的圖片名稱就是 B0000137.jpg ，其中 37 是第 37 部辭書的意思。現在是把所有的字的圖片編在一起，比如這張圖片之前有 12345 張圖片，那他就是 12346.png 。

### 現代漢語詞典 第六版
http://pdawiki.com/forum/forum.php?mod=viewthread&tid=13755
retrieve date: 2015/09/01
從 mdx 轉出來，用 EmEditor 自動排序。
收詞量不大，有心情再做 dsl 。

### 古文字通假字典
http://www.mebag.com/index/tongjia/List.asp
retrieve date: 2015/10/28
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。
有不少缺字和頁碼錯誤。

### 字源
http://www.mebag.com/index/tongjia/List.asp
retrieve date: 2015/10/28
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。
有不少缺字和頁碼錯誤。

### 中國隸書大字典（李志賢等）
http://www.mebag.com/index/shodoo/list.asp
retrieve date: 2015/10/31
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。

### 中國正書大字典（李志賢等）
http://www.mebag.com/index/shodoo/list.asp
retrieve date: 2015/11/01
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。

### 中國行書大字典（李志賢等）
http://www.mebag.com/index/shodoo/list.asp
retrieve date: 2015/11/02
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。

### 中國草書大字典（李志賢等）
http://www.mebag.com/index/shodoo/list.asp
retrieve date: 2015/11/02
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。

### 訂正六書通
http://www.mebag.com/index/shodoo/list.asp
retrieve date: 2015/11/03
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。

### 傳抄古文字編
http://www.mebag.com/index/shodoo/list.asp
retrieve date: 2015/11/03
Python 抓取所得，用 EmEditor 自動排序。點號後面是索引上的頁碼。

## 百科

### 四庫大辭典
在百度雲網盤上看到的一個 mdx ，基於李學勤版四庫大辭典。
源文件錯誤非常多，隨手修正約一百條，然後用 EmEditor 按頁碼排了順序——當然，和原書裏每一頁的順序有所不同。

### 中國哲學辭典（韋政通， 2009 ）
從超星的目錄裏提取的，順便添加了詞序。
詞條不多，但解釋很詳盡，六百多頁纔四百多詞。
附帶做了繁化版。

### 中國道敎大辭典
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=954856

### 中華道教大辭典
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=954856

### 本草綱目（劉衡如、劉山永校， 1998 ）
提取自 ssid: 10444286 的 pdg 所附 BookContents.dat 。補上了 GBK 編碼不兼容的字，拆分了有又名的詞條。
此書爲二校版，三校版也已出版。

## 全文

### 說文解字注
https://github.com/cjkvi/cjkvi-dict/blob/master/swjz.xml
有很多字是問號，是個草稿的草稿。

### 說文解字綜合檢索
http://www.byscrj.com/jmm/shuowen/dcd1.js
retrieve date: 2015/08/20
各項目依次爲：字號，卷第，部首，北師篆，華師篆，字頭，反切音，解說，拼音，注音。
在線查閱：http://www.byscrj.com/jmm/shuowen/find_all.html

### 開放康煕字典
https://github.com/ksanaforge/kangxizidian/
臺灣人王志攀點校的康煕字典，底本也是同文版。
該文件喜歡自作聰明，將不倫不類的臺灣現行標準強加於康煕字典之上。還有很多細節誤，比如 775 頁第 23 字，當作「𤷒」，該文件作「痺」。
現在把一堆 xml 文件合倂成一個，並去掉多餘信息。細緻修理結果則會作他途。

### 現代漢語詞典 第五版
http://bbs.unispim.com/forum.php?mod=viewthread&tid=31657

### 古漢語常用字字典
也是百度上找來的，本來打包成 dz 了，現拆出並去掉 [trn][/trn] 符號（因爲沒什麼用）。

### CC-CEDICT
http://cc-cedict.org/wiki/
釋義非常簡短的中英辭典，與其說是 dictionary ，不如說是 thesaurus 。對於漢語爲母語的英語學習者來說，是一部英文用詞相當地道的中翻英辭典。
另有 StarDict 格式版 http://simonwiles.net/files/cc-cedict/stardict-cc-cedict.tar.bz2 。

## 其他

### 漢大詞用字
一個爲 EverEdit 服務的腳本，可以批量替換。

### 廣韻全字表
http://www.pkucn.com/viewthread.php?tid=175767

### txt2dsl
顧名思義，製作 dsl 的懶人腳本，衹要根據情況塡寫一下數據就行了。

### addseq
顧名思義，給有頁碼無頁內詞序的索引添加詞序。