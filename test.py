import jieba


def v1():
    list_v = []
    for i in final_array:
        weight = 0
        for j in res_array:
            if i == j:
                weight += 1
        list_v.append(weight)
    print(list_v)
    return list_v


def v2():
    list_v = []
    for i in final_array:
        weight = 0
        for j in words:
            if i == j:
                weight += 1
        list_v.append(weight)
    print(list_v)
    return list_v


def cos(v_1, v_2):
    sum_v = 0
    len_v1 = 0
    len_v2 = 0
    for i in range(len(v_1)):
        sum_v += v_1[i] * v_2[i]
    for j in range(len(v_1)):
        len_v1 += v_1[j] ** 2
    for z in range(len(v_2)):
        len_v2 += v_2[z] ** 2
    cos_ = sum_v / ((len_v1 ** 0.5) * (len_v2 ** 0.5))
    print(cos_)


stop_array = [',']
# jieba.load_userdict('di.txt')
res = jieba.cut("无审批监管平台统一代码", cut_all=False)
res_array = [word for word in res if word not in stop_array]
res_no_repeat_array = list(set(res_array))
print(res_no_repeat_array)
list_di = []
with open("di.txt", encoding='utf-8') as file_di:
    for line in file_di:
        list_di.append(line.split(" ")[0])
print(list_di)
# words = ('在线平台', '代码', '项目')
words = tuple(list_di)
final_array = list(set(words + tuple(res_array)))
print(final_array)
words_weight = (1, 2, 3, 4)
sentence = ''
cos(v1(), v2())
