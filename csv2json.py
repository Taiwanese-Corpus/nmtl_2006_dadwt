from csv import DictReader
import csv
import json


def tsuliau():
    with open('/tmp/nmtl.csv') as tong:
        for phinn in DictReader(tong):
            phinn['資料'] = list(zip(
                phinn['漢羅文'].split('\n'), phinn['全羅文'].split('\n')
            ))
            for na in ['漢羅文', '全羅文', '漢羅逝', '全羅逝', ]:
                phinn.pop(na)
            yield phinn


csv.field_size_limit(1000000)
with open('nmtl.json', 'w') as tong:
    json.dump(
        list(tsuliau()), tong,
        ensure_ascii=False,
        indent=2, sort_keys=True
    )
