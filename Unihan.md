原數據普遍是給 Unicode 碼，現在把碼轉好，存成 utf-8 格式。
官網對數據有[說明](http://www.unicode.org/reports/tr38/)。
近期 Unihan 經常飆版本號，比較沒意思，所以這裏更新要看心情。

#### 廣韻
從 Unihan_DictionaryIndices.txt 裏提取 kSBGY 的行，也就是宋本廣韻頁碼及頁內位置。

#### 漢語大字典
有兩種，都是漢語大字典的第一版。數據源是中硏院。
不帶 IRG 的數據，有時一字多個頁碼。
讀音條目是 Readings 裏面的。

#### 康煕字典
有兩種，都是同文書局的頁碼。
不帶 IRG 的字數非常少。帶 IRG 的纔比較完整。

#### 大漢和辭典
又一版本的大漢和辭典字頭。

#### 諸橋
kMorohashi 數據。

#### 現漢1983
現漢 1983 版的頁碼和讀音。

#### 唐音擬
kTang 數據。

#### 主要音
kMandarin 數據。

#### 四角
衹有 GBK 的字。

#### 異體
kSemanticVariant 數據。收錄得不算多，但有出處也不錯。