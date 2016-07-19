import csv
from os import walk
from os.path import join, dirname, abspath, basename
from itertools import chain

import yaml
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def 轉yaml(語料檔案):
    全部資料 = []
    with open(語料檔案) as 檔:
        for 一逝 in 檔.readlines():
            句物件 = 拆文分析器.分詞句物件(一逝.strip())
            全部資料.append({
                '文本資料': 句物件.看型(),
                '屬性': {'音標': 句物件.看音()}
            })
    return 全部資料

if __name__ == '__main__':
    資料 = {
        '來源': {'名': '台語文數位典藏資料庫'},
        '版權': '會使公開',
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作年': '2006',
        '著作所在地': '臺灣',
    }
    專案目錄 = dirname(dirname(abspath(__file__)))
    資料['下層'] = 轉yaml(join(專案目錄, '分詞格式', '01.典藏校對有例句.txt'))
    with open('台語文數位典藏資料庫.yaml', 'w') as 檔案:
        yaml.dump(資料, 檔案, default_flow_style=False, allow_unicode=True)
