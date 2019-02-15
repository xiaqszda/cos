import jieba
import config
import jieba.posseg as pseg


def doit():

    # sentences = ["已核实，该项目实际发生", "总投资已经调概", "工程概算偏低，利息费用高",
    # "县财政资金到位大于到位的情况说明： 调概后工程总概算为37928万元，未列入工程总概算的投入还有利息等8400万元，因发改局文件还未下发，计划总投资没更改，所以县财政资金到位大于计划的"]  # 句子列表
    sentences = []
    # stop_words = [",", "，", "：", " ", "    ", "‘", "“", "’", "”", "。", "、", ".", "'", ";", "\n"]  # 不参与的词语标点
    stop_words = []
    word_lib_path = config.word_lib_path
    sentences_path = config.sentences_path
    stop_path = config.stop_path
    words = []  # 库中词
    words_rate = []  # 库中词频

    # terms = jieba.cut(sentence)
    # current_terms = [word for word in terms if word not in stop_words]  #参与比对的词
    current_terms = []

    def insert(word):
        if word in words:
            word_index = [index for index, value in enumerate(words) if value == word][0]  # 找到的词在库中下标
            words_rate[word_index] += 1
        else:
            words.append(word)
            words_rate.append(1)

    sentences_file = open(sentences_path, "r", encoding="utf-8")
    # print(sentences_file.read().split("\n"))
    sentences += sentences_file.read().split("\n")
    sentences_file.close()

    stop_file = open(stop_path, "r", encoding="utf-8")
    stop_words += stop_file.read().split("\n")
    stop_file.close()

    stop_flag = ["u", "x", "p", "c", "e", "w", "o", "q", ]

    for s in sentences:
        # terms = jieba.cut(s)
        a = pseg.cut(s)
        # for i in a:
        #     print(i.word, "---", i.flag)
        terms = [word.word for word in a if word.flag[0] not in stop_flag]
        current_terms += [word for word in terms if word not in stop_words]  # 参与比对的词

    for t in current_terms:
        insert(t)

    # print(words)
    # print(words_rate)
    lib_file = open(word_lib_path, "w", encoding="utf-8")
    for i in range(len(words)):
        if words[i].isdigit() or words[i].isspace() or "." in words[i]\
                or words_rate[i] < 3:
            continue
        lib_file.write(words[i] + " " + str(words_rate[i]))
        lib_file.write("\n")
    lib_file.close()


doit()