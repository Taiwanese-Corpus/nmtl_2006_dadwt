# 台語文數位典藏資料庫

## 介紹
本資料是國史館收集的臺語文資料，目前在網路上有兩個網站。這兩個網站大部份的內容相同，不過可能文章會有小小的不一樣，可以比較著看
* 國史館網站：<http://xdcm.nmtl.gov.tw/dadwt/pbk.asp>
* 楊允言老師網站：<http://ip194097.ntcu.edu.tw/nmtl/dadwt/pbk.asp>

## 資料夾說明
本資料庫包含臺語漢羅及全羅對應的語料，以下依處理方式說明

### 原始文字檔
此資料夾的資料是台文館計劃ê文本, 是 plain text。
* `kp`表示劇本
* `ks`表示歌詩
* `sb`表示散文
* `ss`表示小說。
* `pbk.xls`是目錄
* `pbk_校對.xls`是校對後的`pbk.xls`

#### 勘誤
原本的資料有一些缺失，以下整理看到的部份。不過這勘誤是很久以前做的，可能不是很完整
* `資料路徑`
  * 勘誤說明
* `kp/K/1957/KP.1957.Ng5 Hoai5-un.Seng3-kek8 te7 1 chip8_04.tbk.txt`
  * 後壁減一字「完」
* `sb/K/1959/SB.1959.Bo5 chu3-beng5.Kim-ku3 E5 Kou3-su7_05.tbk.txt`
  * 5/24～5/30的內容無去矣
    * 佮<http://ip194097.ntcu.edu.tw/nmtl/DADWT/thak.asp?id=873>仝款，減幾仔段
  * 我去掠網站TTS的網址補的
    * 會當參考<http://xdcm.nmtl.gov.tw/dadwt/thak.asp?id=873>
* `sb/J/1940/SB.1941.Ko Kim-seng.Ko Tek-chiong e5 Sio2-toan7.tbk.txt`
  * 應該下佇1941年的資料夾
* `pbk.xls`
  * 有2169篇，目錄干焦2163篇
  * 改的是`pbk_校對.xls`

### 段落對齊
本資料夾的資料是`原始文字檔`經過上面的勘誤處理後，把漢羅和全羅的段落先對齊，再一句一句對齊。對齊後仍有誠萬句漢羅和全羅無法對齊。

裡面的檔案是`sql`檔，裡面有四個`sql table`：
* `原始段落資料`
  * `原始文字檔`匯入的結果
* `改過段落資料`
  * 人工從`原始段落資料`改成一段對齊一段
* `原始逝資料`
  * 用程式把`改過段落資料`轉成一句一句
* `改過逝資料`
  * 人工從`原始逝資料`改成一句對齊一句

當初是使用`postgres`，不過`mysql`應該也能匯入

### 電腦用文本格式
此資料夾是把`改過逝資料`的文本全部整理出來，含標題、作者
* 臺語文數位典藏漢羅文.txt
```
白 話 字 e5 利 益
葉 牧 師
廈 門 e5 牧 師 ， 冬 顯 理 舊 年 有 出 一 個 論 請 漳 泉 台 灣 各 教 會 e5 人 來 做 ： 題 目 就 是 「 白 話 字 e5 利 益 」 。 後 來 有 接 著 九 人 e5 論 ； 就 請 馬 醫 生 ， 甘 牧 師 kap4 伊 鬥 看 ， 評 取 懸 低 ； 第 一 名 賞 銀 五 個 ， 第 二 名 賞 銀 三 個 ， 第 三 名 賞 銀 兩 個 ， 第 四 名 賞 銀 一 個 。 評 了 取 ： - - -
1 . 葉 牧 師 ， tua3 ti7 小 溪 。
2 . 劉 茂 清 ， 台 灣 府 城 。
3 . 李 插 來 ， 鼓 浪 嶼 。
4 . 黃 德 善 ， 廈 門 。
```
* 臺語文數位典藏全羅文.txt
```
peh8-ue7-ji7 e5 li7-ik4
iap8 bok8-su1
e7-mng5 e5 bok8-su1 , tong1 hian2-li2 ku7-ni5 u7 tshut4 tsit8-e5 lun7 tshiann2 tsiang1-tsuan5 tai5-uan5 kok4 kau3-hue7 e5 lang5 lai5 tso3 : te5-bak8 tsiu7-si7 “ peh8-ue7-ji7 e5 li7-ik4 ” . au7-lai5 u7 tsih4-tioh8 kau2 lang5 e5 lun7 ; tsiu7 tshiann2 ma2 i1-sing1 , kam1 bok8-su1 kap4 i1 tau3-khuann3 , phing5 tshu2 kuan5-ke7 ; te7-it4 mia5 siunn2 gin5 goo7-e5 , te7 ji7 mia5 siunn2 gin5 sann1-e5 , te7 sann1 mia5 siunn2 gin5 nng7-e5 , te7 si3 mia5 siunn2 gin5 tsit8-e5 . phing5-liau2 tshu2 : - - -
1 . iap8 bok8-su1 , tua3 ti7 sio2-khe1 .
2 . lau5 boo7-tshing1 , tai5-uan5-hu2-siann5 .
3 . li2 tshah4-lai5 , koo2-long7-su7 .
4 . ng5 tik4-sian7 , e7-mng5 .
```

### 分詞格式
這資料夾的語料是在[翻譯研究](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3)使用[臺灣言語工具](https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_kang1-ku7)，經過程式處理過的。若要使用，可以參考臺灣言語工具的[解析文件](http://sih4sing5hong5.github.io/tai5-uan5_gian5-gi2_kang1-ku7/%E5%9F%BA%E6%9C%AC%E5%85%83%E7%B4%A0.html#)：
* `臺語文數位典藏一對一.txt`
  * 用臺灣言語工具裡`拆文分析器`將能對齊的漢羅和全羅合併，若無法對齊，則使用全羅。
  * 詳細流程請參考[程式](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3/blob/master/%E8%B3%87%E6%96%99%E8%99%95%E7%90%86/%E6%95%B8%E4%BD%8D%E5%85%B8%E8%97%8F%E4%B8%80%E5%B0%8D%E4%B8%80.py)
```
白-話-字｜peh8-ue7-ji7 e5 利-益｜li7-ik4
葉｜iap8 牧-師｜bok8-su1
e7-門｜-mng5 e5 牧-師｜bok8-su1 ，｜,
冬｜tong1 顯-理｜hian2-li2 舊-年｜ku7-ni5 有｜u7 出｜tshut4 一-e5｜tsit8- 論｜lun7 請｜tshiann2 漳-泉｜tsiang1-tsuan5 台-灣｜tai5-uan5 各｜kok4 教-會｜kau3-hue7 e5 人｜lang5 來｜lai5 做｜tso3 ：｜: 題-目｜te5-bak8 就-是｜tsiu7-si7 「｜“ 白-話-字｜peh8-ue7-ji7 e5 利-益｜li7-ik4 」｜” 。｜.
後-來｜au7-lai5 有｜u7 接-著｜tsih4-tioh8 九｜kau2 人｜lang5 e5 論｜lun7 ；｜; 就｜tsiu7 請｜tshiann2 馬｜ma2 醫-生｜i1-sing1 ，｜,
甘｜kam1 牧-師｜bok8-su1 kap4 伊｜i1 鬥-看｜tau3-khuann3 ，｜,
評｜phing5 取｜tshu2 懸-低｜kuan5-ke7 ；｜; 第-一｜te7-it4 名｜mia5 賞｜siunn2 銀｜gin5 五-e5｜goo7- ，｜,
第｜te7 二｜ji7 名｜mia5 賞｜siunn2 銀｜gin5 三-e5｜sann1- ，｜,
第｜te7 三｜sann1 名｜mia5 賞｜siunn2 銀｜gin5 兩-e5｜nng7- ，｜,
第｜te7 四｜si3 名｜mia5 賞｜siunn2 銀｜gin5 一-e5｜tsit8- 。｜.
```
* `01.典藏校對有例句.txt`
  * 用「教育部閩南話常用詞辭典」和「臺華新聞語料庫」的漢字音標對應，根據語言模型將`臺語文數位典藏一對一.txt`補最適當的漢字
  * 詳細流程請參考[程式](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3/blob/master/%E6%A0%A1%E5%B0%8D/%E4%BA%92%E7%9B%B8%E8%A8%93%E7%B7%B4%E6%9C%89%E4%BE%8B%E5%8F%A5.py)
```
白-話-字｜peh8-ue7-ji7 的｜e5 利-益｜li7-ik4
葉｜iap8 牧-師｜bok8-su1
廈-門｜e7-mng5 的｜e5 牧-師｜bok8-su1 ，｜,
冬｜tong1 顯-理｜hian2-li2 舊-年｜ku7-ni5 有｜u7 出｜tshut4 一-个｜tsit8-e5 論｜lun7 請｜tshiann2 漳-泉｜tsiang1-tsuan5 台-灣｜tai5-uan5 各｜kok4 教-會｜kau3-hue7 的｜e5 人｜lang5 來｜lai5 做｜tso3 ：｜: 題-目｜te5-bak8 就-是｜tsiu7-si7 「｜“ 白-話-字｜peh8-ue7-ji7 的｜e5 利-益｜li7-ik4 」｜” 。｜.
後-來｜au7-lai5 有｜u7 接-著｜tsih4-tioh8 九｜kau2 人｜lang5 的｜e5 論｜lun7 ；｜; 就｜tsiu7 請｜tshiann2 馬｜ma2 醫-生｜i1-sing1 ，｜,
甘｜kam1 牧-師｜bok8-su1 佮｜kap4 伊｜i1 鬥-看｜tau3-khuann3 ，｜,
評｜phing5 取｜tshu2 懸-低｜kuan5-ke7 ；｜; 第-一｜te7-it4 名｜mia5 賞｜siunn2 銀｜gin5 五-个｜goo7-e5 ，｜,
第｜te7 二｜ji7 名｜mia5 賞｜siunn2 銀｜gin5 三-个｜sann1-e5 ，｜,
第｜te7 三｜sann1 名｜mia5 賞｜siunn2 銀｜gin5 兩-个｜nng7-e5 ，｜,
第｜te7 四｜si3 名｜mia5 賞｜siunn2 銀｜gin5 一-个｜tsit8-e5 。｜.
```

## 產生臺灣言語資料yaml格式
自`01.典藏校對有例句.txt`轉做yaml格式
```
virtualenv --python python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install tai5-uan5_gian5-gi2_kang1-ku7 pyyaml
python 程式/轉做臺灣言語資料庫yaml格式.py
npm i && npm run deploy
```
就會使掠[yaml](https://taiwanese-corpus.github.io/nmtl_dadwt/台語文數位典藏資料庫.yaml)矣
  