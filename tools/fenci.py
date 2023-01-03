# fenci.py
import jieba
import jieba.posseg as psg
import jieba.analyse


# 创建停用词list
def stopwordslist(file):
    stopwords = [line.strip() for line in open(file, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence, fileStopWords, type=0):
    if type == 0:  # 普通分词结果
        sentence_seged = jieba.cut(sentence.strip())
    elif type == 1:  # 带词性标注的分词结果
        sentence_seged = psg.cut(sentence.strip())
    stopwords = stopwordslist(fileStopWords)  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        word = str(word)
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# fenci.py
# 分词（type=0则普通分词，type=1则带词性标注）
def fenci(fileIn, fileOut, fileStopWords, type=0):
    # 读入需要分词的文件
    inputs = open(fileIn, 'r', encoding='utf-8')
    # 输出分词结果
    outputs = open(fileOut, 'w', encoding='utf-8')
    for line in inputs:
        line_seg = seg_sentence(line, fileStopWords, type)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()


# fenci.py
# 基于TF-IDF算法抽取关键词
def get_tags(fileIn, fileOut):
    # 输入与输出文件目录
    inputs = open(fileIn, 'r', encoding='utf-8')
    outputs = open(fileOut, 'w', encoding='utf-8')
    lines = inputs.read()

    outputs.write('前20个关键词：\n')
    line_seg = jieba.analyse.extract_tags(lines, topK=20, withWeight=True, allowPOS=())
    for tag in line_seg:
        outputs.write(tag[0] + '；')

    outputs.write('\n\n前10个关键词-形容词:\n')
    line_seg = jieba.analyse.extract_tags(lines, topK=10, withWeight=False, allowPOS=(['a']))
    for tag in line_seg:
        outputs.write(str(tag) + '；')

    outputs.write('\n\n前10个关键词-名词:\n')
    line_seg = jieba.analyse.extract_tags(lines, topK=10, withWeight=False, allowPOS=(['n']))
    for tag in line_seg:
        outputs.write(str(tag) + '；')

    outputs.write('\n\n前10个关键词-动词:\n')
    line_seg = jieba.analyse.extract_tags(lines, topK=10, withWeight=False, allowPOS=(['v']))
    for tag in line_seg:
        outputs.write(str(tag) + '；')

    outputs.close()
    inputs.close()
