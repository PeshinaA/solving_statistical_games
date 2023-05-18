import numpy as np

def ShowMatrix(x):
    for i in x:
        print(i)
    print()

def min_el(x,tp):
    min_ = []
    if tp == 'str':
        min_ = np.full(len(x), np.inf)
        for i in range(len(x)):
            for j in range(len(x[0])):
                if x[i][j] < min_[i]:
                    min_[i] = x[i][j]
    elif tp == 'column':
        min_ = np.full(len(x[0]), np.inf)
        for i in range(len(x[0])):
            for j in range(len(x)):
                if x[j][i] < min_[i]:
                    min_[i] = x[j][i]
    return min_

def max_el(x,tp):
    if tp == 'str':
        max_ = np.full(len(x), -1 * np.inf)
        for i in range(len(x)):
            for j in range(len(x[0])):
                if x[i][j] > max_[i]:
                    max_[i] = x[i][j]
    elif tp == 'column':
        max_ = np.full(len(x[0]), -1 * np.inf)
        for i in range(len(x[0])):
            for j in range(len(x)):
                if x[j][i] > max_[i]:
                    max_[i] = x[j][i]
    return max_

def max_sr_V(x,p, par,n):

    print('----------------------Критерий макс среднего выигрыша----------------------')

    alf = np.zeros((n), dtype=float)
    strtg = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            alf[i] = alf[i] + x[i][j]*p[j]
        print('А', i + 1, '=', alf[i])

    if par == 'min':
        m = min(alf)
        for i in range(len(alf)):
            if alf[i] == m:
                strtg.append(i + 1)
                print('min: ', alf[i])
    elif par == 'max':
        m = max(alf)
        for i in range(len(alf)):
            if alf[i] == m:
                strtg.append(i + 1)
                print('max: ', alf[i])

    print('Рекомендуется выбрать стратегию(и): ',strtg)
    return strtg

def Vald(x,par):

    print('----------------------Критерий Вальда----------------------')

    strtg = []
    if par =='min':
        m = max_el(x, 'str')
        print('max: ', m)
        for i in range(len(m)):
            if m[i] == min(m):
                strtg.append(i + 1)
                print('min: ', m[i])
    elif par =='max':
        m = min_el(x, 'str')
        print('min: ', m)
        for i in range(len(m)):
            if m[i] == max(m):
                strtg.append(i + 1)
                print('max: ', m[i])
    print('Рекомендуется выбрать стратегию(и): ',strtg)
    return strtg

def min_R(x,n,m,par):

    print('----------------------Критерий минимального риска Сэвиджа----------------------')

    strtg = []
    m_1 = []
    R = np.zeros((n, m), dtype=float)
    if par == 'min':
        m_1 = min_el(x,'column')
        print('min: ', m_1)
        for i in range(len(x)):
            for j in range(len(x[0])):
                R[i][j] = abs(x[i][j] - m_1[j])
    elif par == 'max':
        m_1 = max_el(x, 'column')
        print('max: ', m_1)
        for i in range(len(x)):
            for j in range(len(x[0])):
                R[i][j] = abs(x[i][j] - m_1[j])

    print('Матрица рисков: ')
    ShowMatrix(R)
    max_elem = max_el(R, 'str')
    print('max: ', max_elem)
    m_2 = min(max_elem)
    for i in range(len(max_elem)):
        if max_elem[i] == m_2:
            strtg.append(i+1)
            print('min: ', max_elem[i])
    print('Рекомендуется выбрать стратегию(и): ',strtg)
    return strtg

def Gurvic(x,lambd,par,n):

    print('----------------------Критерий Гурвица----------------------')

    alf = np.zeros((n), dtype=float)
    mx_el = max_el(x, 'str')
    mn_el = min_el(x, 'str')
    m = 0
    strtg = []
    if par == 'min':
        for i in range(len(alf)):
            alf[i] = lambd*mx_el[i] + (1-lambd)*mn_el[i]
            print('alf', i+1, ' = ', alf[i])
        m = min(alf)
        print('min: ', m)
    elif par == 'max':
        for i in range(len(alf)):
            alf[i] = lambd*mn_el[i] + (1-lambd)*mx_el[i]
            print('alf', i+1, ' = ', alf[i])
        m = max(alf)
        print('max: ', m)
    for i in range(len(alf)):
        if alf[i] == m:
            strtg.append(i+1)

    print('Рекомендуется выбрать стратегию(и): ',strtg)
    return strtg

def get_key(value_count, value):
    answer = []
    for k, v in value_count.items():
        if v == value:
            answer.append(k)
    print('----------------------')
    print("Итоговая(ые) рекомендованная(ые) стратегия(и): ", answer)
    print('###########################################################################################################')
    return answer

def general(A, p, par, n, m, lambd):
    strtgs1 = max_sr_V(A, p, par, n)
    strtgs2 = Vald(A, par)
    strtgs3 = min_R(A, n, m, par)
    strtgs4 = Gurvic(A, lambd, par, n)

    itog = strtgs1 + strtgs2 + strtgs3 + strtgs4

    list_key = list(set(itog))

    list_value = []
    for i in range(len(list_key)):
        list_value.append(itog.count(i + 1))

    value_count = {}
    for i in range(len(list_key)):
        value_count[list_key[i]] = list_value[i]

    max_of_list = max(list_value)

    return get_key(value_count, max_of_list)



