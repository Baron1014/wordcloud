import pandas as pd

def get_coaching_data():
    # 輔導科
    coaching = list()
    coaching.extend(['職涯課程' for _ in range(5)])
    coaching.extend(['情緒管理' for _ in range(4)])
    coaching.extend(['壓力調適' for _ in range(4)])
    coaching.extend(['性別議題' for _ in range(5)])
    coaching.extend(['心理測驗' for _ in range(5)])
    coaching.extend(['輔導知能' for _ in range(6)])
    coaching.extend(['家人溝通' for _ in range(2)])
    coaching.extend(['小組榮譽' for _ in range(6)])
    coaching.extend(['合科教學能力' for _ in range(5)])

    return pd.DataFrame({
        "coaching":coaching
        })

def get_scout_data():
    # 童軍
    scout = list()
    scout.extend(['野外求生' for _ in range(2)])
    scout.extend(['環境保育' for _ in range(2)])
    scout.extend(['野外炊事' for _ in range(2)])
    scout.extend(['繩結' for _ in range(2)])
    scout.extend(['小組榮譽' for _ in range(2)])
    scout.extend(['合科教學能力' for _ in range(5)])

    return pd.DataFrame({
        "scout": scout
        })

def get_home_data():
    # 家政
    home = list()
    home.extend(['食物學' for _ in range(1)])
    home.extend(['營養學' for _ in range(1)])
    home.extend(['食物製備' for _ in range(1)])
    home.extend(['烹飪' for _ in range(1)])
    home.extend(['外食注意事項' for _ in range(1)])
    home.extend(['色彩學' for _ in range(1)])
    home.extend(['服裝搭配' for _ in range(1)])
    home.extend(['家人溝通' for _ in range(1)])
    home.extend(['合科教學能力' for _ in range(5)])

    return pd.DataFrame({
        "home": home
        })

def get_strategy_data():
    # 3. 教學策略知識
    dflist = list()
    dflist.extend(['活動' for _ in range(10)])
    dflist.extend(['討論' for _ in range(10)])
    dflist.extend(['講授課程' for _ in range(10)])
    dflist.extend(['團隊合作' for _ in range(10)])
    dflist.extend(['實作' for _ in range(8)])
    dflist.extend(['遊戲' for _ in range(10)])
    dflist.extend(['合作學習' for _ in range(10)])
    dflist.extend(['口頭發表' for _ in range(10)])

    return pd.DataFrame({
        "col": dflist
        })

def get_know_data():
    # 4. 教學表徵知識
    dflist = list()
    dflist.extend(['舉例' for _ in range(10)])
    dflist.extend(['提問' for _ in range(10)])
    dflist.extend(['產婆法' for _ in range(1)])
    dflist.extend(['心理測驗' for _ in range(4)])
    dflist.extend(['運用媒材進行課程' for _ in range(10)])

    return pd.DataFrame({
        "col": dflist
        })

def get_studentlearn_data():
    # 5. 對學生學習理解知識
    dflist = list()
    dflist.extend(['理解學生的先備知識' for _ in range(10)])
    dflist.extend(['了解學生的差異性' for _ in range(6)])
    dflist.extend(['從課程中與課後互動觀察學生的學習狀況' for _ in range(8)])
    dflist.extend(['透過A卡或B卡的資料了解學生背景' for _ in range(4)])

    return pd.DataFrame({
        "col": dflist
        })

def get_exam_data():
    # 6. 評量知識
    dflist = list()
    dflist.extend(['多元評量方式' for _ in range(10)])
    dflist.extend(['標準本位評量方式' for _ in range(5)])
    dflist.extend(['課前進行評量規準的擬定' for _ in range(6)])

    return pd.DataFrame({
        "col": dflist
        })

def get_media_data():
    # 7. 媒體知識
    dflist = list()
    dflist.extend(['蒐集及篩選相關媒材' for _ in range(10)])
    dflist.extend(['將媒材融入教案設計與課程' for _ in range(10)])
    dflist.extend(['適時與適當的使用媒材' for _ in range(7)])

    return pd.DataFrame({
        "col": dflist
        })
