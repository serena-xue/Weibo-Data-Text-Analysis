# LDA.py
from gensim.models import LdaModel
from gensim.corpora import Dictionary


def LDA(fileIn, fileOut):
    # 读取数据
    train = []
    fp = open(fileIn, 'r',encoding='utf8')
    for line in fp:
        line = line.split()
        train.append([w for w in line])

    dictionary = Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]
    sum = 3  # 主题个数
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=sum,passes=20)

    # 输出主题以及各主题关键词
    outputs = open(fileOut, 'w', encoding='utf-8')
    for topic in lda.print_topics(num_words = 5):
        outputs.write(str(topic[0]) + ':\n')
        listOfTerms = topic[1].split('+')
        for term in listOfTerms:
            listItems = term.split('*')
            outputs.write('  ' + listItems[1].strip(' ') + '(' + listItems[0].strip(' ') + ')\n')
        outputs.write('\n')
