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

#### 古籍字頻統計
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=972697
原爲 Excel 文件，轉爲 tsv 。

## 索引

#### 大漢和辭典
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw2ucs.txt
https://github.com/cjkvi/cjkvi-dict/blob/master/dkw-word.txt

#### 康煕字典
https://github.com/cjkvi/cjkvi-dict/blob/master/kx2ucs.txt
根據新版 Unicode 修正了「况」和「㤺」。

#### 漢語大字典 第二版
http://bbs.gxsd.com.cn/forum.php?mod=viewthread&tid=899628 20140415 版
原爲 Excel 文件，純文字表格轉爲 tsv 。

#### 三大辭書
http://bbs.xueleku.com/forum.php?mod=viewthread&tid=369962
漢語大字典+中文大辭典+故訓匯纂聯合，提取其 data-sorted.js 。