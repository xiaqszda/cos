import analysis
import datetime
import train.train as train
import jieba.posseg as posseg
import jieba


def analyze():
    analy = analysis.Analysis()
    with open("model/sample.txt", "r", encoding="utf-8") as sample_file:
        sample = sample_file.read().split("\n")
    res_set = []
    for sentence in sample:
        res = analy.once(sentence)
        res_set.append(sentence + "~~~" + str(res))
    # res_file = open("model/res.txt", "w", encoding="utf-8")
    with open("model/res.txt", "w", encoding="utf-8") as res_file:
        for r in res_set:
            res_file.write(r)
            res_file.write("\n")
    # res_file.close()


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    # train.doit()

    # analysis = analysis.Analysis()
    # result = analysis.once("核对核对无误")
    # print(result)

    # analyze()

    # a = posseg.cut("核实付款哈菲尼克斯第六届!!!,?http://sadsad", )
    # for i in a:
    #     print(i.word, "---", i.flag)

    a = posseg.cut("部分固定资产折旧已提完，不再计提折旧")
    for i in a:
        print(i.word,"---", i.flag)
    end_time = datetime.datetime.now()
    print("运行共花费时间", end_time - start_time)


