# SKT Big Data Hub에서 제공하는 <배달 업종 이용 현황 분석> api 호출하기
# https://www.bigdatahub.co.kr/product/view.do?pid=1001785

import requests
import json
import pandas as pand

URL1 = 'https://api.bigdatahub.co.kr/v1/datahub/datasets/search.json?pid=1001814'
URL3 = '&TDCAccessKey='  # key 추가 필요

result = []


def get_data():
    try:
        for i in range(1, 3000):
            # page - default value 1, max value 3000 / count - default value 10, max value 300
            URL2 = '&$page=%d&$count=%d' % (i, 300)
            URL = URL1 + URL2 + URL3
            # print(URL)

            source_code = requests.get(URL)
            plain_text = source_code.text
            mydatas = json.loads(plain_text)
            # print(mydatas)

            for j in range(1, 300):
                result_sub = []
                result_sub.append(mydatas['entry'][j]['일자'])
                result_sub.append(mydatas['entry'][j]['읍면동'])
                result_sub.append(mydatas['entry'][j]['업종'])
                result_sub.append(mydatas['entry'][j]['시간대'])
                result_sub.append(mydatas['entry'][j]['통화건수'])
                result.append(result_sub)
        print('크롤링완료')
        return result

    except Exception as err:
        print(err)
        print("URL is error")


def dataframe_sorting():
    get_data()
    data = pand.DataFrame(result, columns=("일자", "읍면동", "업종", "시간대", "통화건수"))
    print(data)
    print(len(data))


if __name__ == "__main__":
    dataframe_sorting()
