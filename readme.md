## 注意
本項目使用 GPL v3 協議。改編者請注意開源並使用相同協議。
本人輕度執行 Apache 關於文檔的標準，卽，對修改的內容做出說明。索引的修正多記錄在 https://github.com/821/Acorns 中，此處主要記錄圖片的處理。

## 說明
Acorns 是個素材收集庫。這些素材的主要服務對象是製作輸入法和電子辭書。
愛收集的人常被戲稱爲「松鼠症患者」，而二次元松鼠最喜歡收集的莫過於橡實。這項目的名字就這麼出現了。
基礎 retrieve date: 2015/06/22 。有不一樣的會再說明。
這個項目最早放在 Google Code ，後來用了一段時間 Google Sites ，現在還是覺得 Github 比較安心。

## 字

#### ids
https://github.com/cjkvi/cjkvi-ids/blob/master/ids.txt
http://kanji-database.sourceforge.net/ids/ids.html
漢字拆解成部分，比如「明」拆成「日月」。
問題很多，暫不整理。
又，「[零時字引](https://github.com/g0v/z0y/)」就是用了這份材料。

#### 部件檢索
http://blog.xuite.net/fg_wang/twblog/309627490
原爲 mdx ，通過 JavaScript 實現查詢，轉爲 tsv 。
事實上也吸收了 ids.txt 的成果。

#### 四角號碼
http://bbs.unispim.com/forum.php?mod=viewthread&tid=31674
原爲 chm 文件，轉爲 tsv 。

#### 筆順
https://github.com/rime/brise/blob/master/preset/stroke.dict.yaml
114954 條數據，但是錯誤太多——漢字的筆順，中臺敎育部都搞錯很多。
修正「成」字相關筆順。「必」「忄」「火」「右」「有」等工作量太大，改不完。

#### 臺灣讀音
https://github.com/lukhnos/openvanilla/blob/master/DataTables/bpmf-ext.cin
97968 條臺灣單字讀音數據。
同項目還有行列、大易之類臺灣輸入法的碼表，然並卵。

#### cns2py
https://github.com/cjkvi/cjkvi-data/blob/master/cns2py.txt
90933 個漢字的臺灣讀音。

#### 古籍字頻統計
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=972697
原爲 Excel 文件，轉爲 tsv 。

## 索引

#### 說文解字圖像查閱
http://www.byscrj.com/jmm/shuowen/dcd.js
retrieve date: 2015/08/20
各項依次爲字頭，詁林正編，詁林補遺，詁林補編，詁林後編外編，通訓定聲，祁嶲藻繫傳，述古堂繫傳，段注，連筠簃義證，崇文義證，句讀，宋本，藤花榭，汲古閣，孫星衍，陳昌治。
在線查閱：http://www.byscrj.com/jmm/shuowen/find.html

#### 洪武正韻
https://github.com/BYVoid/ytenx/blob/11dfc4bbfcb27857826efffc8463b0362af87b04/ytenx/tcenghyonhtsen/data/Dzih.txt
保留字頭、頁碼、韻部、聲調、反切，流水號和拉丁化之類就不要了。

#### 康煕字典
https://github.com/cjkvi/cjkvi-dict/blob/master/kx2ucs.txt
頁碼對應最爲通用的同文書局版，含備攷和補遺。
根據新版 Unicode 修正了「鐕」、「呈」、「况」和「㤺」。「GKX-1595.80」根據原書改作「㠼」，「KX0391.023」據原書改作「𦣽」。
大抵帶星號的是某個字頭下的「古文」。
個別拆字不是很好，比如 1123.33 ，作「⿳⿲⿷匚一⿱古八𠆢？」（那個問號不知道是幹嘛），不如作「⿳⿶𦥑古八⿱人女」。還有 111.30 ，應該是「⿳巛𠔿⿵冂厶」。
「柵の形が微妙に違う」改作「⿰木𠕁」。
1602.022 誤作「𣨂」，改爲「⿱𢀸廾」。

#### 大漢和辭典 字
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw2ucs.txt
Unicode 碼轉成字了。

#### 大漢和辭典 詞
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw-word.txt
原書「眾」的寫法，「亻」不蓋「人」。而且使用比較混亂，時而「衆」，時而「眾」。
錯誤較多，比如「奉諱」和「奉義」之間有兩個詞，本表僅一。又如「丟招」誤作「丟昭」，屬於同音字誤錄。還有三千多字顯示爲「■」，改正是個大工程。

#### 漢語大詞典 紙本 詞
https://github.com/cjkvi/cjkvi-dict/blob/master/hydcd-word.txt
剝離出了紙本部分的詞彙。由於源文件使用了大量的日本漢字，而且舊字形也不符合漢大詞的習慣，所以用自己寫的一個列表「漢大詞用字」來把用字修正爲與紙本儘量統一的狀態。然而漢語大詞典的用字特別強調新字形，其實也常常不符合繁體使用習慣（反而常符合微軟某繁體輸入法），比如用「录」不用「彔」（綠、剝、碌、淥等亦然），用「兑」不用「兌」（說、悅、脫、銳、閱等亦然），用「争」不用「爭」（靜、淨、猙、掙、崢、睜、箏亦然），用「真」不用「眞」（愼、塡、鎭、顚、巓、瑱等亦然），，用「册」不用「冊」（刪、姍、柵等亦然），用「吴」不用「吳」（娛、悞等亦然），用「吕」不用「呂」（侶、宮、等亦然），用「奂」不用「奐」（喚、換、瘓、煥、渙等亦然），用「」不用「強」（繈、襁等亦然），用「内」不用「內」（吶等亦然），用「黄」不用「黃」（橫等亦然），用「户」不用「戶」，用「虚」不用「虛」（噓等亦然），用「彦」不用「彥」（顏等亦然），用「産」不用「產」，用「遥」不用「遙」，用「摇」不用「搖」，用「謡」不用「謠」，用「瑶」不用「瑤」，用「熙」不用「煕」，用「没」不用「沒」，用「别」不用「別」，用「丢」不用「丟」，用「温」不用「溫」。但「爲」系列用的卻是舊字形。這些問題將在進一步處理中糾正，但不放在本文件。
漢語大詞典本身有很多奇怪的地方，比如把「示」的新舊字形當作截然不同的字做獨立解釋。而「示」的舊字形沒有獨立的編碼，所以本文件將二者合倂。「焭」分別入火、几二部，「缹」分別入「火」、「缶」二部，就不改了。
表中數百字使用頁碼或獨立號碼表示，現在全部改正。對於 Unicode 沒有的字，則使用拆字法。
表中不少錯誤，比如「嗥噦」，原書找不到。「矇瞍」出現兩次，查原書，發現後一個應該是「矇𥈟」，「轗𨎺」和「轗𨎹」、「蹴踏」和「蹴蹹」、「霶𩃰」和「霶𩃱」、「韭菹」和「韭葅」、「𪒱𪑠」和「𪒱𪒡」也誤作同一個。「𠌯昧」誤作「儷昧」、「𠵯喇」誤作「咶喇」、「喫詬」誤作「吃詬」、「⿰口渤」誤作「哱」、「𡃆楞嗆啷」誤作「噌楞嗆啷」、「𡸚嶭」誤作「嶘嶭」、「㕓闠」誤作「廛闠」、「椔翳」誤作「椔翳」、「凼肥」誤作「氹肥」、「撆缺」誤作「撇缺」、「鳧趨雀躍」誤作「島趨雀躍」、「鳧雛」誤作「島雛」。更神奇的還有「甯」誤作「寧」、「床」誤作「牀」、「箒」誤作「帚」、「穅」誤作「糠」、「𧃳」誤作「褻」、「韈」誤作「襪」、「蟑螂」的「螂」都打錯。均改正。

#### 漢語大詞典 光碟 字
http://bbs.gxsd.com.cn/forum.php?mod=redirect&goto=findpost&ptid=974990&pid=4330027
衹有大五碼所收字。

#### 漢語大字典 第二版
http://bbs.unispim.com/forum.php?mod=redirect&goto=findpost&ptid=31606&pid=121595
retrieve date: 2015/06/30

#### 漢語大字典+中文大辭典+故訓匯纂
http://bbs.xueleku.com/forum.php?mod=viewthread&tid=369962
漢語大字典+中文大辭典+故訓匯纂聯合，提取其 data-sorted.js 。

#### 異體字字典
https://github.com/cjkvi/cjkvi-dict/blob/master/twedu-dict.txt
這個文件可以檢索到五萬多個字，收錄時去掉了 twedu- 這個無用前綴。
另外這個文件竟然有一些官網沒有的字，可能是原來有，但被刪除了。

#### 異體字字典2
https://github.com/kcwu/moedict-variants/blob/master/list.txt
說明見其 [Wiki Page](https://github.com/kcwu/moedict-variants/wiki) 。
我把文件中的 /variants/tmp/ 和 .png 去掉了。
跟日本人做的文件相比，多了圖片地址。然而異體字字典原本是 Big5 的，向 Unicode 的推進過程不完善，很多 Unicode 已經有的字在日本版有了，但本文件跟官網一樣，衹能直接檢索到兩萬字。異體字字典官網對 Unicode 也是有意識的，很多圖片的地址實際上就是 Unicode 編碼。
有些不連續的號，比如 A00270-018 和 A00270-022 ，並不是顯示沒有這個字的，而是衹有字頭沒有釋義。兩個文件都沒有收錄。
此處順便吐槽一下異體字字典，修到第五版還不能直接檢索，第六版可以檢索了，又無聊把圖片的 link 全部改掉。比如原本一個字的字號是 B00001 ，那麼他的正字通的圖片名稱就是 B0000137.jpg ，其中 37 是第 37 部辭書的意思。現在是把所有的字的圖片編在一起，比如這張圖片之前有 12345 張圖片，那他就是 12346.png 。

#### 四庫大辭典
在百度雲網盤上看到的一個 mdx ，基於李學勤版四庫大辭典。
源文件錯誤非常多，隨手修正了約一百條。

#### 中國道敎大辭典
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=954856

#### 中華道教大辭典
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=954856

## 全文

#### 說文解字注
https://github.com/cjkvi/cjkvi-dict/blob/master/swjz.xml
有很多字是問號，是個草稿的草稿。

#### 說文解字綜合檢索
http://www.byscrj.com/jmm/shuowen/dcd1.js
retrieve date: 2015/08/20
各項目依次爲：字號，卷第，部首，北師篆，華師篆，字頭，反切音，解說，拼音，注音。
在線查閱：http://www.byscrj.com/jmm/shuowen/find_all.html

#### 開放康煕字典
https://github.com/ksanaforge/kangxizidian/
臺灣人王志攀點校的康煕字典，底本也是同文版。
該文件喜歡自作聰明，將不倫不類的臺灣現行標準強加於康煕字典之上。還有很多細節誤，比如 775 頁第 23 字，當作「𤷒」，該文件作「痺」。
現在把一堆 xml 文件合倂成一個，並去掉多餘信息。細緻修理結果則會作他途。

## 其他

#### 漢大詞用字
一個爲 EverEdit 服務的腳本，可以批量替換。

#### 廣韻全字表
http://www.pkucn.com/viewthread.php?tid=175767