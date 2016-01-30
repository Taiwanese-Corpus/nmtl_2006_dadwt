# 台語文數位典藏資料庫

國史館網站：<http://xdcm.nmtl.gov.tw/dadwt/pbk.asp>
楊允言老師網站：<http://ip194097.ntcu.edu.tw/nmtl/dadwt/pbk.asp>

## 資料說明

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
