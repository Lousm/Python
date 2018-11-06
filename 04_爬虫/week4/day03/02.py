from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt

background = plt.imread(r't2.jpg')

f = open(r'弹幕.txt', 'r', encoding='utf-8').read()

wordclouds = WordCloud(
    background_color='black',  # 默认黑色
    mask=background,
    font_path=r'C:\Windows\Fonts\STHUPO.TTF',
    width=1000,
    height=500,
    # margin=2
).generate(f)

plt.imshow(wordclouds)
plt.axis('off')
plt.show()
