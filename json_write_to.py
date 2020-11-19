import json
from datetime import datetime

# str = [{
#     "探索": ["2020-11-18", 0],
#     "圣迹": ["2020-11-18", 0],
#     "普h图": ["2020-11-18", 0],
#     "活动h图": ["2020-11-18", 0],
#     "露娜塔": ["2020-11-18", 0],
#     "工会战": ["2020-11-18", 0],
#     "穿装备": ["2020-11-18", 0],
#     "点赞": ["2020-11-18", 0],
#     "升rank": ["2020-11-18", 0],
#     "地下城": ["2020-11-18", 0],
#     "双场": ["2020-11-18", 0]
# }]

# str = [{
#     "主线": 1,
#     "竞技场": 1,
#     "地下城": 1,
#     "穿装备": 1,
#     "无料十连": 1,
#     "露娜塔": 1,
#     "活动": 1,
#     "会战": 1,
#     "时间": 1605779341.0,
#     "位置": "c:/"
# }]

# with open('settings.json','w') as file:
#     file.write(json.dumps(str,indent=2,ensure_ascii=False))

with open('settings.json','r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

#datetime.fromtimestamp(data[0]["时间"])

#datetime.now().timestamp() + 10
