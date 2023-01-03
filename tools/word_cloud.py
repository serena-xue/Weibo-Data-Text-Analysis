# word_cloud.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def word_cloud(path, fileIn, figName, png_name):
    text = open(fileIn, "r", encoding='utf8').read()
    font_path = '‪C:\Windows\Fonts\simhei.ttf'

    # 设置词云
    wc = WordCloud(background_color='white', width=500, height=350, max_font_size=80,
                   min_font_size=4, mode='RGBA', font_path=font_path, colormap='Set2')

    wc.generate(text)

    myword = wc.generate(text)  # 生成词云

    # 展示词云图
    plt.figure(figName)
    plt.imshow(myword)
    plt.axis('off')
    plt.savefig(path + png_name + '.png')
    plt.show()