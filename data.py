import pandas as pd

def get_target_data():
    # 1. 課程與目標知識
    dflist = list()
    dflist.extend(['先有目標才設計課程' for _ in range(5)])
    dflist.extend(['用能力指標訂教學目標' for _ in range(1)])
    dflist.extend(['依照學生特性訂定目標' for _ in range(8)])
    dflist.extend(['先設計課程再推回去符合的教學目標' for _ in range(1)])

    return pd.DataFrame({
        "col": dflist
        })

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

def get_scene_data():
    # 8-1. 課程情境氛圍營造
    dflist = list()
    dflist.extend(['課程初始引起動機' for _ in range(10)])
    dflist.extend(['營造與課程主題或教學目標相關的課程氛圍' for _ in range(8)])

    return pd.DataFrame({
        "col": dflist
        })

def get_motivation_data():
    # 8-2. 學生缺乏學習動機
    dflist = list()
    dflist.extend(['了解原因' for _ in range(10)])
    dflist.extend(['與導師或輔導老師討論思考因應方式' for _ in range(8)])
    dflist.extend(['調整及反思課程設計與教學方式' for _ in range(8)])

    return pd.DataFrame({
        "col": dflist
        })

def get_interrupt_data():
    # 8-3. 學生課堂干擾行為
    dflist = list()
    dflist.extend(['操作制約' for _ in range(7)])
    dflist.extend(['調整' for _ in range(10)])
    dflist.extend(['了解原因' for _ in range(10)])
    dflist.extend(['反思課程設計與教學方式' for _ in range(8)])
    dflist.extend(['與導師或輔導老師討論思考因應方式' for _ in range(8)])

    return pd.DataFrame({
        "col": dflist
        })

def get_alienated_data():
    # 8-4. 學生人際疏離行為
    dflist = list()
    dflist.extend(['彈性調整分組方式' for _ in range(7)])
    dflist.extend(['設計疏離行為的議題融入課程' for _ in range(10)])
    dflist.extend(['了解原因' for _ in range(10)])
    dflist.extend(['與導師或輔導老師討論思考因應方式' for _ in range(8)])

    return pd.DataFrame({
        "col": dflist
        })

def get_disappoint_data():
    # 8-5. 學生情緒失落
    dflist = list()
    dflist.extend(['了解學生情緒失落的原因' for _ in range(10)])
    dflist.extend(['設計情緒調節課程' for _ in range(6)])
    dflist.extend(['與導師或輔導老師討論思考因應方式' for _ in range(8)])

    return pd.DataFrame({
        "col": dflist
        })

def get_special_data():
    # 8-6. 特殊學生
    dflist = list()
    dflist.extend(['事先了解班級學生的狀況' for _ in range(10)])
    dflist.extend(['擬定相關教學策略' for _ in range(9)])
    dflist.extend(['與導師或輔導老師或特教老師進行討論' for _ in range(10)])
    dflist.extend(['設計相關課程' for _ in range(7)])
    dflist.extend(['教育班級其他學生與特殊生的相處方式' for _ in range(10)])

    return pd.DataFrame({
        "col": dflist
        })

def get_conflict_data():
    # 8-7. 學生課堂衝突行為
    dflist = list()
    dflist.extend(['立即制止並分開衝突雙方' for _ in range(10)])
    dflist.extend(['注意學生安全與受教權益' for _ in range(6)])
    dflist.extend(['依照班級狀況判斷處理方式' for _ in range(8)])
    dflist.extend(['了解衝突原因' for _ in range(10)])
    dflist.extend(['通知並與導師討論學生的衝突行為與處理方式' for _ in range(10)])

    return pd.DataFrame({
        "col": dflist
        })