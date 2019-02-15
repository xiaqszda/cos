import jieba
import util.util as util
import config


class Analysis:
    wrong_words = []
    correct_words = []
    correct_rates = []

    def __init__(self):
        wrong_path = config.wrong_path
        # wrong_file = open(wrong_path, "r", encoding="utf-8")
        # self.wrong_words += wrong_file.read().split("\n")
        # wrong_file.close()
        with open(wrong_path, "r", encoding="utf-8") as wrong_file:
            self.wrong_words += wrong_file.read().split("\n")
        correct_path = config.word_lib_path
        # correct_file = open(correct_path, "r", encoding="utf-8")
        # content = correct_file.read()
        with open(correct_path, "r", encoding="utf-8") as correct_file:
            content = correct_file.read()
        for i in content.split("\n"):
            c = i.split(" ")
            if c[0] == "":
                continue
            self.correct_words.append(c[0])
            self.correct_rates.append(int(c[1]))

    def once(self, sentence):
        # print(self.wrong_words)
        # print(self.correct_words)
        # print(self.correct_rates)

        current_terms = []  # 分词结果
        terms = jieba.cut(sentence)
        current_terms += [word for word in terms if word not in self.wrong_words]
        term = []  # 最终分词结果
        term_rate = []
        for i in current_terms:
            if i in term:
                term_rate[[index for index, value in enumerate(term) if value == i][0]] += 1
            else:
                if i.isdigit() or i.isspace() or "." in i:
                    continue
                term.append(i)
                term_rate.append(1)
        correct_term = [""] * len(term)
        correct_term_rate = [0] * len(term_rate)
        # print(term)
        for i in range(len(term)):
            index = [index for index, value in enumerate(self.correct_words) if value == term[i]]
            if len(index) == 0:
                continue
            else:
                index = index[0]
            #     print("序号", index)
            # print("是是是", correct_term)
            # print("库", self.correct_words)
            # print(i)
            correct_term[i] = self.correct_words[index]
            correct_term_rate[i] = self.correct_rates[index]

        if len(correct_term) == 0:
            print("正确率", 0)
            return 0
        else:
            # cos_v = util.cos(correct_term_rate, term_rate)
            print(correct_term)
            print(term)
            math = util.Algorithm(correct_term_rate, term_rate)
            cos_v = math.cos()
            print("正确率", cos_v)
            return cos_v
        

