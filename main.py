# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import data
import numpy as np
import collections
from PIL import Image
from wordcloud import WordCloud

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

if __name__ == "__main__":
    main()
