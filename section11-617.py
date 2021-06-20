# csv 파일 읽기 쓰기
# csv:  MIME - text/csv

import csv

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 딜리미터 옵션
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)


# 딕셔너리로 변환

with open('./resource/sample2.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter="|")
    print(type(reader))
    print(dir(reader))

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------------------')


# csv 파일 쓰기 - 한줄씩

w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

with open('./resource/sample3.csv','w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# csv 파일 쓰기 - 한번에
with open('./resource/sample4.csv','w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# 엑셀파일 처리 xls, xlsx
# # xlre, openpyxl, pandas 설치 필요

# import pandas as pd


# # 옵션들이 있다
# # sheetname - 특정 시트의 이름 또는 숫자 지정하여 불러오기
# # header - 몇번째열을 헤더로 지정할지
# # skiprow - 몇번째 행을 스킵하고 가져오지 않을지


# xlsx = pd.read_excel('./resource/sample.xlsx')
# # 데이터 확인
# print(xlsx.head())
# print(xlsx.tail())
# print(xlsx.shape) # 행, 열 확인


# # 엑셀 or csv로 쓰기
# xlsx.to_excel('./resource/result.xlsx', index=False)
# xlsx.to_csv('./resource/result.csv', index=False)