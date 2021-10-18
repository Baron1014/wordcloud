# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud



def get_subjects_data():
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

def main():
    data = get_subjects_data()

    wc = WordCloud(
            width=800,
            height=400,
            font_path ="/System/Library/Fonts/STHeiti Medium.ttc"
    ).generate(' '.join(data['coaching']))

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
