import statist_games
import go_easy
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

def print_space():
    label_space = []
    str00 = "                                                                                                        " \
            "                                                                                                          "
    for i in range(8):
        label_space.append(Label(root, text=str00))
        label_space[i].grid(row=9+i, column=1, columnspan=8, sticky='w')

def print_p_mixed(strtgs):
    p_mixed = np.zeros(int(n_s.get()))
    i = []
    str1 = ''
    for strtg in strtgs:
        i.append(strtg)
    for k in range(len(i)):
        for j in range(len(p_mixed)):
            if j == i[k] - 1:
                p_mixed[j] = 1 / len(i)

    for i in range(len(p_mixed)):
        if (i == len(p_mixed) - 1):
            str1 += str(p_mixed[i])
        else:
            str1 += str(p_mixed[i]) + ', '

    label_space = ttk.Label(root, text=" ").grid(row=15, column=1)
    label_answer = ttk.Label(root, text=str("p* = " + '(' + str1 + ')'), font='Helvetica 9 bold')
    label_answer.grid(row=16, column=1, columnspan=2, sticky='w')

def write_conclusion():
    global par, lambd, n, m
    lines_to_stay = []
    lines_to_delete = []
    label_general = []
    count = 0

    easy = go_easy.go_easy(lines_to_delete, n, m, calc_Matrix, par, lambd, p, lines_to_stay)
    if easy == 1:
        print_space()
        for j, l in enumerate(label_general):
            l.config(text=str(lines_to_stay[j]))
        label_general1 = ttk.Label(root, text="Рекомендованная(ые) стратегия(и): ", font='Helvetica 9 bold')
        label_general1.grid(row=14, column=1, columnspan=2, sticky='w')
        for strtg in lines_to_stay:
            label_general.append(Label(root, text=strtg))
            label_general[count].grid(row=14, column=count+3)
            count += 1
        print_p_mixed(lines_to_stay)
        return 1

    strtgs1 = statist_games.max_sr_V(calc_Matrix, p, par, n)
    strtgs2 = statist_games.Vald(calc_Matrix, par)
    strtgs3 = statist_games.min_R(calc_Matrix, n, m, par)
    strtgs4 = statist_games.Gurvic(calc_Matrix, lambd, par, n)
    strtgs = statist_games.general(calc_Matrix, p, par, n, m, lambd)

    label_max_sr_V = []
    label_Vald = []
    label_min_R = []
    label_Gurvic = []
    label_general = []

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    count = 0

    for j, l in enumerate(label_max_sr_V):
        l.config(text=str(strtgs1[j]))

    for j, l in enumerate(label_Vald):
        l.config(text=str(strtgs2[j]))

    for j, l in enumerate(label_min_R):
        l.config(text=str(strtgs3[j]))

    for j, l in enumerate(label_Gurvic):
        l.config(text=str(strtgs4[j]))

    for j, l in enumerate(label_general):
        l.config(text=str(strtgs[j]))

    label_max_sr_V1 = ttk.Label(root, text="Критерий максимального среднего выигрыша: ", font='Helvetica 9 bold')
    label_max_sr_V1.grid(row=10, column=1, columnspan=2, sticky='w')
    for strtg in strtgs1:
        label_max_sr_V.append(Label(root, text=strtg))
        label_max_sr_V[c1].grid(row=10, column=c1+3)
        c1 += 1
    label_space1 = ttk.Label(root, text="                                                                             ")
    label_space1.grid(row=10, column=c1 + 3, columnspan=6)

    label_Vald1 = ttk.Label(root, text="Критерий Вальда: ", font='Helvetica 9 bold')
    label_Vald1.grid(row=11, column=1, columnspan=2, sticky='w')
    for strtg in strtgs2:
        label_Vald.append(Label(root, text=strtg))
        label_Vald[c2].grid(row=11, column=c2+3)
        c2 += 1
    label_space2 = ttk.Label(root, text="                                                                             ")
    label_space2.grid(row=11, column=c2 + 3, columnspan=6)

    label_min_R1 = ttk.Label(root, text="Критерий минимального риска Сэвиджа: ", font='Helvetica 9 bold')
    label_min_R1.grid(row=12, column=1, columnspan=2, sticky='w')
    for strtg in strtgs3:
        label_min_R.append(Label(root, text=strtg))
        label_min_R[c3].grid(row=12, column=c3+3)
        c3 += 1
    label_space3 = ttk.Label(root, text="                                                                             ")
    label_space3.grid(row=12, column=c3 + 3, columnspan=6)

    label_Gurvic1 = ttk.Label(root, text="Критерий Гурвица: ", font='Helvetica 9 bold')
    label_Gurvic1.grid(row=13, column=1, columnspan=2, sticky='w')
    for strtg in strtgs4:
        label_Gurvic.append(Label(root, text=strtg))
        label_Gurvic[c4].grid(row=13, column=c4+3)
        c4 += 1
    label_space4 = ttk.Label(root, text="                                                                             ")
    label_space4.grid(row=13, column=c4+3, columnspan=6)


    label_general1 = ttk.Label(root, text="Итоговая(ые) рекомендованная(ые) стратегия(и): ", font='Helvetica 9 bold')
    label_general1.grid(row=14, column=1, columnspan=2, sticky='w')
    for strtg in strtgs:
        label_general.append(Label(root, text=strtg))
        label_general[count].grid(row=14, column=count+3)
        count += 1
    label_space5 = ttk.Label(root, text="                                                                             ")
    label_space5.grid(row=14, column=count+3, columnspan=6)

    print_p_mixed(strtgs)

# Собирает все значения с виджетов
def entered():
    global par, lambd, n, m
    calc_Matrix.clear()
    p.clear()
    n = int(n_s.get())
    m = int(m_s.get())
    i = 0
    for r in range(n):
        calc_Matrix.append([])
        for c in range(m):
            calc_Matrix[r].append(arr_ent[i].get())
            i += 1
    if (selected_ch.get() == 0):
        par = "max"
    else:
        par = "min"
    if (selected_p.get() == 0):
        for j in range(m):
            p.append((p_s[j].get()))
        if int(sum(p)) != 1:
            showerror(title="Ошибка", message="p введены неверно: вероятности в сумме должны давать 1.")
            p.clear()
            return 1
    else:
        for i in range(m):
            p.append(1 / m)
    lambd = (lambd_s.get())
    if lambd > 1 or lambd < 0:
        showerror(title="Ошибка", message="lambda введена неверно: вероятность не может быть больше 1 и меньше 0.")
        return 1

    write_conclusion()



# Создание фрейм, где заполняем двумерную матрицу и остальные параметры
def create_frame_matrix():
    frame = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=[8, 10])
    n = int(n_s.get())
    m = int(m_s.get())
    label2 = ttk.Label(frame, text="Введите матрицу", font='Helvetica 9 bold').grid(row=5, column=1, columnspan=2)
    for r in range(n):
        for c in range(m):
            arr_ent.append(DoubleVar(frame))
            (Entry(frame, textvariable=arr_ent[-1])).grid(row=7 + r, column=c + 1)
    win = 'Матрица выигрыша'
    lose = 'Матрица потерь'
    ch1_btn = ttk.Radiobutton(frame, text=win, variable=selected_ch, value=0).grid(row=8 + n, column=1)
    ch2_btn = ttk.Radiobutton(frame, text=lose, variable=selected_ch, value=1).grid(row=8 + n, column=2)
    ch_no_btn = ttk.Radiobutton(frame, text='p: ', variable=selected_p, value=0).grid(row=10 + n, column=1)
    for c in range(m_s.get()):
        p_s.append(DoubleVar(frame))
        p_ent = Entry(frame, textvariable=p_s[-1]).grid(row=10 + n, column=2 + c)
    ch_avto_btn = ttk.Radiobutton(frame, text='p avto', variable=selected_p, value=1).grid(row=11 + n, column=1)
    label_l = ttk.Label(frame, text="lambda: ").grid(row=12 + n, column=1)
    lambd_ent = Entry(frame, textvariable=lambd_s).grid(row=12 + n, column=2)
    btn = Button(frame, text="Ввод", command=entered).grid(row=13 + n, column=2)
    return frame


# # Создаем фрейм. Если фрейм уже есть, мы его перезаписываем (сперва удаляем с формы, потом уничтожаем в программе и очищаем в списке)
def create_Frame():
    n = int(n_s.get())
    m = int(m_s.get())
    if n < 2 or m < 2:
        showerror(title="Ошибка", message="Данный размер матрицы недопустим, минимальный размер 2х2.")
        return 1
    if (len(frames) > 0):
        for frame in frames:
            frame.grid_forget()
            frame.destroy()
        arr_ent.clear()
        p_s.clear()
        frames.clear()
        calc_Matrix.clear()
    frames.append(create_frame_matrix())
    frames[-1].grid(columnspan=4, rowspan=4)


# Создание основного окна
root = Tk()
root.title("Решение статистических игр")
root.geometry("720x720")

frames = []
calc_Matrix = []
p = []

# Вводные данные для создания двухмерной матрицы
label1 = ttk.Label(root, text="Выберите размер матрицы", font='Helvetica 9 bold').grid(row=1, column=1, columnspan=2)
n_lb = Label(root, text='Число строк: ').grid(row=2, column=1)
m_lb = Label(root, text='Число столбцов: ').grid(row=3, column=1)
n_s = IntVar()
m_s = IntVar()
arr_ent = []
p_s = []
lambd_s = DoubleVar()
selected_ch = IntVar()
selected_p = IntVar()
n_ent = Entry(root, textvariable=n_s).grid(row=2, column=2)
m_ent = Entry(root, textvariable=m_s).grid(row=3, column=2)
btnCreate = Button(root, text="Ввод", command=create_Frame).grid(row=4, column=2)

# Запускаем окно
root.mainloop()
