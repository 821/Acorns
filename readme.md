## 項目說明
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

#### 大漢和辭典
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw2ucs.txt
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw-word.txt

#### 漢語大詞典
https://github.com/cjkvi/cjkvi-dict/blob/master/hydcd-word.txt
剝離出了紙本部分的詞彙。由於源文件使用了大量的日本漢字，而且舊字型也不符合漢大詞的習慣，所以用自己寫的一個列表「漢大詞用字」來把用字修正爲與紙本儘量統一的狀態。

#### 康煕字典
https://github.com/cjkvi/cjkvi-dict/blob/master/kx2ucs.txt
頁碼對應最爲通用的同文書局版，含備攷和補遺。
根據新版 Unicode 修正了「鐕」、「呈」、「况」和「㤺」。「GKX-1595.80」根據原書改作「㠼」。
大抵帶星號的是某個字頭下的「古文」。
個別拆字不是很好，比如 1123.33 ，作「⿳⿲⿷匚一⿱古八𠆢？」（那個問號不知道是幹嘛），不如作「⿳⿶𦥑古八⿱人女」。還有 111.30 ，應該是「⿳巛𠔿⿵冂厶」。
「柵の形が微妙に違う」改作「⿰木𠕁」。
1602.022 誤作「𣨂」，改爲「⿱𢀸廾」。

#### 開放康煕字典
https://github.com/ksanaforge/kangxizidian/
臺灣人王志攀點校的康煕字典，底本也是同文版。
該文件喜歡自作聰明，將不倫不類的臺灣現行標準強加於康煕字典之上。還有很多細節誤，比如 775 頁第 23 字，當作「𤷒」，該文件作「痺」。
現在把一堆 xml 文件合倂成一個，並去掉多餘信息。細緻修理結果則會作他途。

#### 漢語大字典 第二版
http://bbs.unispim.com/forum.php?mod=redirect&goto=findpost&ptid=31606&pid=121595
retrieve date: 2015/06/30

#### 漢語大字典+中文大辭典+故訓匯纂
http://bbs.xueleku.com/forum.php?mod=viewthread&tid=369962
漢語大字典+中文大辭典+故訓匯纂聯合，提取其 data-sorted.js 。

#### 異體字字典
https://github.com/cjkvi/cjkvi-dict/blob/master/twedu-dict.txt

#### 四庫大辭典
在百度雲網盤上看到的一個 mdx ，基於李學勤版四庫大辭典。
源文件錯誤非常多，隨手修正了約一百條。

## 其他

#### 漢大詞用字
一個爲 EverEdit 服務的腳本，可以批量替換。

#### 廣韻全字表
http://www.pkucn.com/viewthread.php?tid=175767