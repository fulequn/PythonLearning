#GovRptWordCloudv1.py
import jieba
import wordcloud

#代开文件
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
#读取信息
t = f.read()
f.close()
ls = jieba.lcut(t)
#解析
txt = " ".join(ls)
#设置图片格式
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc",
    max_words = 15
    )
w.generate(txt)
w.to_file("grwordcloud.png")


