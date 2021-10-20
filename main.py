# -*- coding: utf-8 -*-
import re
import pandas as pd
import matplotlib.pyplot as plt
import data
import numpy as np
import collections
import seaborn as sns
from PIL import Image
from wordcloud import WordCloud
from matplotlib.font_manager import FontProperties
myfont=FontProperties(fname=r'C:\Windows\Fonts\msjh.ttc',size=14)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

def wc(d, figname):
    mask = np.array(Image.open("cloud.png"))
    word_counts = collections.Counter(d.values.tolist())

    wc = WordCloud(
            width=800,
            height=400,
            background_color = "white",
            max_words = 200,
            mask=mask,
            contour_width=2,
            contour_color='steelblue',
            collocations = False,
            font_path ="/System/Library/Fonts/STHeiti Medium.ttc"
    ).generate_from_frequencies(word_counts)

    plt.imshow(wc)
    plt.axis("off")
    wc.to_file(f"report/{figname}.jpg")

def catbarplot(d, title):
    stick_name = [i for i in pd.unique(d['col'])]

    plt.figure(figsize=(10,8))
    sns.countplot(x='col', data=d, palette="flare")
    plt.xticks(range(len(stick_name)) ,[re.sub("(.{10})", "\\1\n", label, 0, re.DOTALL) for label in stick_name])
    plt.title(title)
    plt.tight_layout()
    # plt.show()
    plt.savefig(f'./report/{title}.jpg')
    plt.close()
    

def main():
    coaching = data.get_coaching_data()
    home = data.get_home_data()
    scout = data.get_scout_data()

    # 2. 學科內容知識
    wc(coaching['coaching'], "學科內容知識＿輔導科")
    wc(home['home'], "學科內容知識＿家政科")
    wc(scout['scout'], "學科內容知識＿童軍科")

    # 3. 教學策略知識
    d = data.get_strategy_data()
    wc(d['col'], "教學策略知識")

    # 4. 教學表徵知識
    d = data.get_know_data()
    wc(d['col'], "教學表徵知識")

    # 5. 對學生學習理解的知識
    d = data.get_studentlearn_data()
    wc(d['col'], "對學生學習理解的知識")

    # 6. 評量知識
    d = data.get_exam_data()
    wc(d['col'], "評量知識")

    # 7. 媒體知識
    d = data.get_media_data()
    wc(d['col'], "媒體知識")

def barplot():
    # 8.情景知識
    d8 = data.get_scene_data()
    catbarplot(d8, "課程情境氛圍營造")

    d8 = data.get_motivation_data()
    catbarplot(d8, "學生缺乏學習動機")

    d8 = data.get_interrupt_data()
    catbarplot(d8, "學生課堂干擾行為")

    d8 = data.get_alienated_data()
    catbarplot(d8, "學生人際疏離行為")

    d8 = data.get_disappoint_data()
    catbarplot(d8, "學生情緒失落")

    d8 = data.get_special_data()
    catbarplot(d8, "特殊學生")

    d8 = data.get_conflict_data()
    catbarplot(d8, "學生課堂衝突行為")

if __name__ == "__main__":
    # main()
    barplot()
