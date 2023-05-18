import numpy as np

def ShowMatrix(A):
    for i in A:
        print(i)
    print()

def easer(first,second,m,par,lines_to_delete,fir,sec):  #сравнение 2х строк
    list_true = []
    reference_list = []
    reference2_list = []
    for i in range(m): #cоздаём эталонный список итога сравнения состоящий либо из 0, либо из 1
        reference_list.append(0)
        reference2_list.append(1)
    for i in range(m):
        if first[i] > second[i]: #ОН ДОБАВЛЯЕТСЯ 2 РАЗА ЕСЛИ ТУТ = -> решили проблему измением размера эталонного списка
            list_true.append(0)
        if first[i] < second[i]:
            list_true.append(1)
        if first[i] == second[i]:
            reference_list.pop(0)
            reference2_list.pop(0)
    if list_true == reference_list:
        if par == "max":
            lines_to_delete.append(sec)
        if par == "min":
            lines_to_delete.append(fir)
    if list_true == reference2_list:
        if par == "max":
            lines_to_delete.append(fir)
        if par == "min":
            lines_to_delete.append(sec)
    list_true = []
    return lines_to_delete #лист с номерами строк, которые можно удалить, но они повторяются

def go_easy(lines_to_delete, n, m, A, par, lambd, p, lines_to_stay):
    print('###########################################################################################################')
    print('----------------------Исходные данные----------------------')
    print('Исходная матрица: ')
    ShowMatrix(A)
    print('Количество строк: ', n)
    print('Количество столбцов: ', m)
    if par == 'max':
        print('Матрица выигрыша.')
    else:
        print('Матрица потерь.')
    print('Вероятности: ', p)
    print('lambda: ', lambd)
    print('----------------------Начало алгоритма----------------------')
    f=0
    for fir in range (n-1,0,-1): #сопоставляем все строки со всеми
        first = A[fir]
        for sec in range (n-2-f,-1,-1):
            second = A[sec]
            easer(first, second, m, par,lines_to_delete,fir,sec)
        f += 1

    lines_to_delete = list(set(lines_to_delete)) #убираем одинаковые номера строк

    #удаляем строки из матрицы
    if lines_to_delete != []:

        A_new = np.array([lines_to_delete])
        for elem in A_new:
            A = np.delete(A, elem, 0)
        lines_to_delete1 = []
        for i in range(len(lines_to_delete)):
            lines_to_delete1.append(lines_to_delete[i] + 1)

        for i in range(n):
            if lines_to_delete.count(i) == 0:
                lines_to_stay.append(i+1)

        if len(lines_to_delete) > (n-2):
            print('Осталась всего одна строка. Наилучшая стратегия найдена упрощением: ')
            ShowMatrix(A)
            print("Номер cтроки: ")
            print(lines_to_stay)
            return 1
        else:
            print("______________")
            print("Матрица после упрощения:")
            ShowMatrix(A)
            print("_____________")
            print("Номера удаленных строк:")
            print(lines_to_delete1)
            print("_____________")
    else:
        print("_____________")
        print("Матрицу нельзя упростить.")
        print("_____________")