# 台語文數位典藏資料庫

## 介紹
國史館網站：<http://xdcm.nmtl.gov.tw/dadwt/pbk.asp>
楊允言老師網站：<http://ip194097.ntcu.edu.tw/nmtl/dadwt/pbk.asp>

## 資料說明
本資料庫包含臺語漢羅及全羅對應的語料，以下依處理方式說明

### 原始文字檔
台文館計劃ê文本, 是 plain text。
kp 表示劇本， ks表示歌詩， sb表示散文，ss表示小說。

#### 勘誤
這勘誤是很久以前做的，可能不是很完整
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
把漢羅和全羅的段落先對齊，再一句一句對齊。對齊後仍有誠萬句漢羅和全羅無法對齊。

當初是使用`postgres`，不過`mysql`應該也能匯入
裡面有四個`sql table`：
* 原始段落資料
  * 原始文字檔匯入的結果
* 改過段落資料
  * 人工從`原始段落資料`改成一段對齊一段
* 原始逝資料
  * 用程式把`改過段落資料`轉成一句一句
* 改過逝資料
  * 人工從`原始逝資料`改成一句對齊一句

### 電腦用文本格式
此資料夾是把`改過逝資料`的文本全部整理出來，含標題、作者
* 臺語文數位典藏漢羅文.txt
* 臺語文數位典藏全羅文.txt

### 分詞格式
這資料夾的語料是在[翻譯研究](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3)使用[臺灣言語工具](https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_kang1-ku7)，經過程式處理過的，
* 臺語文數位典藏一對一.txt
  * 用臺灣言語工具裡`拆文分析器`將能對齊的漢羅和全羅合併，若無法對齊，則使用全羅。
  * 詳細流程請參考[程式](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3/blob/master/%E8%B3%87%E6%96%99%E8%99%95%E7%90%86/%E6%95%B8%E4%BD%8D%E5%85%B8%E8%97%8F%E4%B8%80%E5%B0%8D%E4%B8%80.py)
* 01.典藏校對有例句.txt
  * 用「教育部閩南話常用詞辭典」和「臺華新聞語料庫」的漢字音標對應，根據語言模型將`臺語文數位典藏一對一.txt`補最適當的漢字
  * 詳細流程請參考[程式](https://github.com/sih4sing5hong5/huan1-ik8_gian2-kiu3/blob/master/%E6%A0%A1%E5%B0%8D/%E4%BA%92%E7%9B%B8%E8%A8%93%E7%B7%B4%E6%9C%89%E4%BE%8B%E5%8F%A5.py)
