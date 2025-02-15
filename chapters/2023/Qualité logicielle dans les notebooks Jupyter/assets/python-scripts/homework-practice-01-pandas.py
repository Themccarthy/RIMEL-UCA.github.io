#!/usr/bin/env python
# coding: utf-8

# ## Машинное обучение 1, ПМИ ФКН ВШЭ
# 
# ## Практическое домашнее задание 1
# 
# ### Общая информация
# 
# Дата выдачи: 09.09.2022
# 
# Мягкий дедлайн: 23:59MSK 22.09.2022
# 
# Жесткий дедлайн: 23:59MSK 29.09.2022

# ### О задании
# 
# Задание состоит из двух разделов, посвященных работе с табличными данными с помощью библиотеки pandas и визуализации с помощью matplotlib. В первом разделе вам предстоит выполнить базовые задания с помощью вышеуказанных библиотек, а во втором распределить студентов по курсам. Баллы даются за выполнение отдельных пунктов. Задачи в рамках одного раздела рекомендуется решать в том порядке, в котором они даны в задании.
# 
# Задание направлено на освоение jupyter notebook (будет использоваться в дальнейших заданиях), библиотек pandas и matplotlib.
# 
# ### Оценивание и штрафы
# Каждая из задач имеет определенную «стоимость» (указана в скобках около задачи). Максимально допустимая оценка за работу — 10 баллов.
# 
# Сдавать задание после жёсткого дедлайна нельзя. При выставлении неполного балла за задание в связи с наличием ошибок на усмотрение проверяющего предусмотрена возможность исправить работу на указанных в ответном письме условиях.
# 
# Задание выполняется самостоятельно. «Похожие» решения считаются плагиатом и все задействованные студенты (в том числе те, у кого списали) не могут получить за него больше 0 баллов (подробнее о плагиате см. на странице курса). Если вы нашли решение какого-то из заданий (или его часть) в открытом источнике, необходимо указать ссылку на этот источник (скорее всего вы будете не единственным, кто это нашел, поэтому чтобы исключить подозрение в плагиате, необходима ссылка на источник).
# 
# ### Формат сдачи
# Задания сдаются через систему Anytask. Инвайт можно получить у семинариста или ассистента. Присылать необходимо ноутбук с выполненным заданием. Сам ноутбук называйте в формате homework-practice-01-pandas-Username.ipynb, где Username — ваша фамилия.
# 
# Для удобства проверки самостоятельно посчитайте свою максимальную оценку (исходя из набора решенных задач) и укажите ниже.
# 
# Оценка: xx.

# ## 0. Введение

# Сейчас мы находимся в jupyter-ноутбуке (или ipython-ноутбуке). Это удобная среда для написания кода, проведения экспериментов, изучения данных, построения визуализаций и других нужд, не связанных с написанием production-кода. 
# 
# Ноутбук состоит из ячеек, каждая из которых может быть либо ячейкой с кодом, либо ячейкой с текстом размеченным и неразмеченным. Текст поддерживает markdown-разметку и формулы в Latex.
# 
# Для работы с содержимым ячейки используется *режим редактирования* (*Edit mode*, включается нажатием клавиши **Enter** после выбора ячейки), а для навигации между ячейками искользуется *командный режим* (*Command mode*, включается нажатием клавиши **Esc**). Тип ячейки можно задать в командном режиме либо с помощью горячих клавиш (**y** to code, **m** to markdown, **r** to edit raw text), либо в меню *Cell -> Cell type*. 
# 
# После заполнения ячейки нужно нажать *Shift + Enter*, эта команда обработает содержимое ячейки: проинтерпретирует код или сверстает размеченный текст.

# In[ ]:


# ячейка с кодом, при выполнении которой появится output
2 + 2

# Ячейка с неразмеченным текстом.

# Попробуйте создать свои ячейки, написать какой-нибудь код и текст какой-нибудь формулой.

# In[ ]:


# your code

# [Здесь](https://athena.brynmawr.edu/jupyter/hub/dblank/public/Jupyter%20Notebook%20Users%20Manual.ipynb) находится <s>не</s>большая заметка о используемом языке разметки Markdown. Он позволяет:
# 
# 0. Составлять упорядоченные списки
# 1. Выделять *текст* <s>при</s> **необходимости**
# 2. Добавлять [ссылки](http://imgs.xkcd.com/comics/the_universal_label.png)
# 
# 
# * Составлять неупорядоченные списки
# 
# Делать вставки с помощью LaTex:
#     
# $
# \left\{
# \begin{array}{ll}
# x = 16 \sin^3 (t) \\ 
# y = 13 \cos (t) - 5 \cos (2t) - 2 \cos (3t) - \cos (4t) \\
# t \in [0, 2 \pi]
# \end{array}
# \right.$

# А ещё можно вставлять картинки, или гифки, или что захотите:
# 
# <img src="https://media1.tenor.com/images/9b8fbe9214504bcf6c60fe4e4f7e114e/tenor.gif?itemid=5416416" style="width: 400px">

# ### Google Colab

# Что за колаб? 
# 
# **Google Colab (Colaboratory)** это **Jupyter Notebook + Cloud + Google Drive.**
# 
# Компания Google предоставляет возможность бесплатно запускать ноутбуки (предварительно загрузив их на свой гугл-диск) прямо в облаке. При этом вам не требуется установка никаких пакетов на свою машину, а работать можно прямиком из браузера. Вот ссылка:

# https://colab.research.google.com

# При использовании вы увидете много сходств с jupyter ноутбуком. Одним из преимуществ является доступность GPU, соответствующую опцию можно активировать в настройках сервиса. При желании вы сможете найти в интернете много туториалов по использованию или разобраться самостоятельно =)

# ## 1. Табличные данные и Pandas

# Pandas — удобная библиотека для работы с табличными данными в Python, если данных не слишком много и они помещаются в оперативную память вашего компьютера. Несмотря на неэффективность реализации и некоторые проблемы, библиотека стала стандартом в анализе данных.
# 
# Основной объект в pandas — это DataFrame, представляющий собой таблицу с именованными колонками различных типов, индексом (может быть многоуровневым). DataFrame можно создавать, считывая таблицу из файла или задавая вручную из других объектов.
# 
# В этой части потребуется выполнить несколько небольших заданий. Можно пойти двумя путями: сначала изучить материалы, а потом приступить к заданиям, или же разбираться "по ходу". Выбирайте сами.
# 
# Материалы:
# 1. [Pandas за 10 минут из официального руководства](http://pandas.pydata.org/pandas-docs/stable/10min.html)
# 2. [Документация](http://pandas.pydata.org/pandas-docs/stable/index.html) (стоит обращаться, если не понятно, как вызывать конкретный метод)
# 3. [Примеры использования функционала](http://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/pandas.ipynb)
# 
# Многие из заданий можно выполнить несколькими способами. Не существуют единственно верного, но попробуйте максимально задействовать арсенал pandas и ориентируйтесь на простоту и понятность вашего кода. Мы не будем подсказывать, что нужно использовать для решения конкретной задачи, попробуйте находить необходимый функционал сами (название метода чаще всего очевидно). В помощь вам документация, поиск и stackoverflow.

# In[ ]:


%pylab inline
import pandas as pd

# <span style="color:red">Перед выполнением задания необходимо ознакомиться с первым семинаром (seminars/sem01-pandas.ipynb) </span>.
# 
# Это поможет вам получить общее понимание происходяшего и успешнее справиться с заданием.
# 
# Также успешному выполнению способствует внимательное чтение текста задания от начала до конца.
# 
# Удачи!

# Скачаем подготовленные на семинаре данные:

# In[ ]:


!wget  -O 'end_seminar.xlsx' -q 'https://www.dropbox.com/s/f4rm8sjc3v99p0m/_end_seminar.xlsx?dl=0'

# Для пользователей Windows: скачайте файл самостоятельно и поместите его в папку с тетрадкой. Или попробуйте один из следующих вариантов:

# In[ ]:


# !powershell iwr -outf somefile https://somesite/somefile

# In[ ]:


# !pip install wget
# import wget 
# wget.download('https://dropbox.com/s/f4rm8sjc3v99p0m/_end_seminar.xlsx?dl=1', 'end_seminar.xlsx')

# ##### В первой части задания (до раздела "Распределение студентов по курсам") использование циклов запрещается и повлечет за собой снижение оценки. Использование <code>vectorize</code> и  <code>apply</code>, <code>apply_along_axis</code> крайне нежелательно.

# Для каждой задачи из этого раздела вы должны написать код для получения ответа, а также дать текстовый ответ, если он предполагается.
# 
# На некоторые вопросы вы можете получить путём пристального взгляда на таблицу, но это не будет засчитываться. Вы в любом случае должны получить ответ с помощью кода.

# #### 1. [0 баллов] Откройте файл с таблицей (не забудьте про её формат). Выведите последние 10 строк.
# 
# Посмотрите на данные и скажите, что они из себя представляют, сколько в таблице строк, какие столбцы? (на это не надо отвечать, просто подумайте об этом)

# In[ ]:


# your code

# #### 2. [0.5 балла] Есть ли в данных пропуски? В каких колонках? Сколько их в каждой из этих колонок?

# In[ ]:


# your code

# Заполните пропуски пустой строкой для строковых колонок и нулём для числовых (постарайтесь избежать перечисления названий всех столбцов).

# In[ ]:


# your code

# #### 3. [0.5 балла] Посмотрите повнимательнее на колонку 'is_first_time'. 
# 
# Есть ли в ней ответы "Нет"? Сколько их?
# 
# Если вы найдете повторные обращения студентов, оставьте только самую позднюю версию. В дальнейших заданиях используйте версию данных без повторов.
# 
# <i>Обращения со значением "Нет" в 'is_first_time' могут быть как повторными, так и первичными, поскольку поле заполняли сами студенты.</i>

# In[2]:


# your code

# #### 4. [0.5 балла] Ответьте на вопросы:
# 1. Сколько было заявок из групп 18-го года набора, а сколько из групп 17-го года?
# 2. Есть ли студенты с равными перцентилями (среди объединенных данных, ведь конкурс на каждый курс общий)?

# In[ ]:


# your code

# #### 5. [0.5 балла] Какие  blended-курсы для четверокурсников существуют? На какой blended-курс записалось наибольшее количество студентов? На каком из blended-курсов собрались студенты с самым высоким средним рейтингом (выведите этот курс и количество студентов на нем)? 

# In[ ]:


# your code

# #### 6. [1 балл] Выясните, есть ли студенты с абсолютно одинаковыми предпочтениями по всем курсам.
# 
# Для этого сформируйте таблицу, где для каждого возможного набора курсов посчитано количество студентов, выбравших такой набор, и оставьте только строки где это количество больше 1.
# 
# В данном случае набор курсов задается упорядоченным множеством ('fall_1', 'fall_2', 'fall_3', 'spring_1', 'spring_2', 'spring_3', 'blended'). Элемент blended будет нулевым для 3-го курса.

# In[ ]:


# your code

# #### 7. [0.5 балла] Найдите курсы по выбору, на которые записывались как студенты 18-го года набора, так и студенты 17-го года.

# In[ ]:


# your code

# Методом исключения найдите курсы, которые предлагались только студентам 18-го года и только студентам 17-го года.

# In[ ]:


# your code

# ### Визуализации и matplotlib

# При работе с данными часто неудобно делать какие-то выводы, если смотреть на таблицу и числа в частности, поэтому важно уметь визуализировать данные. Здесь будут описаны ключевые правила оформления графиков для **всех** домашних заданий.
# 
# У matplotlib, конечно же, есть [документация](https://matplotlib.org/users/index.html) с большим количеством [примеров](https://matplotlib.org/examples/), но для начала достаточно знать про несколько основных типов графиков:
# - plot — обычный поточечный график, которым можно изображать кривые или отдельные точки;
# - hist — гистограмма, показывающая распределение некоторой величины;
# - scatter — график, показывающий взаимосвязь двух величин;
# - bar — столбцовый график, показывающий взаимосвязь количественной величины от категориальной.
# 
# В этом задании вы попробуете построить один из них. Не забывайте про базовые принципы построения приличных графиков:
# - оси должны быть подписаны, причём не слишком мелко;
# - у графика должно быть название;
# - если изображено несколько графиков, то необходима поясняющая легенда;
# - все линии на графиках должны быть чётко видны (нет похожих цветов или цветов, сливающихся с фоном);
# - если отображена величина, имеющая очевидный диапазон значений (например, проценты могут быть от 0 до 100), то желательно масштабировать ось на весь диапазон значений (исключением является случай, когда вам необходимо показать малое отличие, которое незаметно в таких масштабах);
# - сетка на графике помогает оценить значения в точках на глаз, это обычно полезно, поэтому лучше ее отрисовывать;
# - если распределение на гистограмме имеет тяжёлые хвосты, лучше использовать логарифмическую шкалу.
# 
# Еще одна билиотека для визуализации: [seaborn](https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html) (обычно сокращается до sns). Это настройка над matplotlib, иногда удобнее и красивее делать визуализации через неё. 
# 
# **5 пунктов после которых ваши графики не будут прежними:**
# - для красивой картинки <code>%config InlineBackend.figure_format = 'retina'</code>
# - задаем размер (почти) всех графиков (можно выбрать другие значения) <code>plt.rcParams['figure.figsize'] = 8, 5</code>
# - размер шрифта подписей графиков <code>plt.rcParams['font.size'] = 12</code>
# - формат в котором сохраняется изображение <code>mpl.rcParams['savefig.format'] = 'pdf'</code>
# - sns – seaborn, добавляет решетку <code>sns.set_style('darkgrid')</code>
# 
# Добавьте эти функции в ячейку ниже. Каждый график все равно придется настраивать отдельно, но указанные строчки позволят значительно упростить процесс.  

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns

# your code

# #### 8. [0.5 балла] Постройте график средних рейтингов по дням получения ответов (bar plot).

# In[ ]:


# your code

# Сохраните график в формате pdf (так он останется векторизованным).

# In[ ]:


# your code

# ### 2. Распределение студентов по курсам.

# <span style="color:red">!!!ВНИМАТЕЛЬНО ИЗУЧИТЕ ТЕКСТ НИЖЕ!!!</span>.
# 
# <span style="color:orange">Если во время выполнения заданий у вас вознинут вопросы -- еще раз перечитайте текст целиком, скорее всего ответы уже содержатся в нем.</span>

# Теперь вам нужно распределить студентов по осенним курсам по выбору, учитывая их предпочтения.

# Алгоритм распределения студентов по курсам:
# 1. По умолчанию на каждой дисциплине по выбору у 3 и 4 курсов может учиться 1 группа (до 30 студентов). Исключения описаны ниже. На blended-дисциплинах для четверокурсников количество мест не ограничено.
# 2. Проводится первая волна отбора. Для каждой дисциплины формируется список тех, кто указал её первым приоритетом (если студент должен выбрать два курса по выбору, то для него дисциплины, которые он указал первым и вторым приоритетом, рассматриваются как дисциплины первого приоритета). Если желающих больше, чем мест, то выбирается топ по перцентилю рейтинга.
# 3. На дисциплинах, где остались места после первой волны, формируются списки тех, кто выбрал их вторым приоритетом и еще не прошел на необходимое количество курсов. Места заполняются лучшими по перцентилю рейтинга студентами. После этого проводится такая же процедура для дисциплин третьего приоритета.
# 4. Если студент не попал на необходимое количество курсов по итогам трёх волн, с ним связывается учебный офис и решает вопрос в индивидуальном порядке.

# Обращаем ваше внимание на следующие детали:
# - Конкурс на каждый курс общий для 3-го и 4-го курса
# 
# - По умолчанию студент выбирает один осенний и один весенний курс по выбору, а также четверокурсники выбирают один blended-курс. Студенты групп 17-го года специализаций МОП и ТИ выбирают по 2 осенних и 2 весенних курса по выбору, также студенты групп 18' специализации МИ выбирают 2 осенних курса. <i>Для студентов, которые выбирают 2 курса (например, осенних) первый приоритет — <code>fall_1</code> и <code>fall_2</code>, второй приоритет — <code>fall_3</code>. Такие студенты участвуют только в двух волнах отбора</i>.
# 
# - Студенты специализации МОП не могут выбрать весенним курсом по выбору Машинное обучение 2. **Если студент специализации МОП выбрал Машинное обучение 2, то его приоритеты сдвигаются.** Из-за совпадений первого и второго курса по выбору двигать приоритеты не надо.
# 
# - Blended-курсы не трогайте, по ним не надо распределять, на другие курсы они никак не влияют.
# 
# - Заведомо известно, что в процессе распределения не возникнет ситуации, когда на одно место претендуют студенты с одинаковым перцентилем.
# 
# - Постарайтесь воздержаться от использования циклов там, где это возможно. <i>Допустимо итерироваться по <b>курсам</b>, на которые проводится отбор, и по <b>волнам</b> отбора. Если вы придумаете, как обойтись и без этих циклов, то на усмотрение проверяющего могут быть добавлены бонусные баллы. <b>Дублирование кода не признается успешным избавлением от циклов</b></i>
# 
# - На выходе ожидается файл res_fall.csv с результатами распределения на осенние курсы по выбору. Файл должен быть следующего формата:
# 
#     * Три колонки: ID, course1, course2
#     
#     * Если студент не попал на курс, но должен был, то вместо названия курса в ячейке должна быть строка "???"
#     
#     * Если студент должен выбрать только один курс, то в колонке course2 для него должна стоять строка "-"
#     
#     * Если студент должен выбрать два курса по выбору, то порядок в колонках course1 и course2 не важен.
#     
#     * hint: для сохранения воспользуйтесь df.to_csv('solution.csv', index=None)
#     
# 
# Для работы вам могут понадобиться следующие данные:
# 
# - Результаты опроса (вы уже использовали этот файл в первой части задания, но на всякий случай ссылка: https://www.dropbox.com/s/f4rm8sjc3v99p0m/_end_seminar.xlsx?dl=0)
# 
# - Соответствие номеров групп специализациям:
# 
#     * 171, 172 - МОП; 173 - ТИ; 174 — АДИС; 175, 176 — РС; 177 — АПР
#     
#     * У студентов 18-го года номера групп соответствуют номерам до распределения по специализациям. Это означает, что по номеру группы 18* нельзя однозначно определить специализацию студента. При этом в рамках распределения важно знать информацию только о двух из них: МОП и МИ. Эти знание можно получить из колонок 'is_ml_student
# ' и 'is_mi' соответственно.
# 
# - Ограничения по количеству мест на курсах по выбору:
# 
#     * Осенние: везде 30 мест, кроме Statistical Learning Theory (60 мест), Высокопроизводительных вычислений (60 мест), Анализа неструктурированных данных ($\infty$ мест)
# 
#     * Весенние: везде 30 мест, кроме Обучения с подкреплением (60 мест), Анализа данных в бизнесе (60 мест).
# 
# 
# Кстати, убедитесь, что в данных больше нет пропусков и повторных записей.

# #### 0. Проверка
# 
# Для начала давайте убедимся, что вы успешно выполнили задания первой части и проверим ваши данные на наличие пропусков и повторов:

# In[ ]:


assert df.shape[0] == 347, 'В таблице остались повторы или потеряны данные'

assert df.isna().sum().sum() == 0, 'В таблице остались пропуски'

# Если вы не получили AssertionError, то можете продолжать.

# #### 1. [1 балл] Создайте новый признак, обозначающий, сколько осенних курсов должен выбрать студент
# 
# В этом вам может помочь информация о специализации и группе стундента.

# In[ ]:


# (￣^￣)ゞ

# Проверка:

# In[ ]:


col_name =     # insert your new column name as str

assert(df[df['id'] == '2662600c2c37e11e62f6ee0b88452f22'][col_name] == 2).all()
assert(df[df['id'] == 'd555d2805e1d93d4f023e57dc4c8f403'][col_name] == 2).all()
assert(df[df['id'] == '8fe79f84f36e3a5d2d6745621321302c'][col_name] == 1).all()
assert(df[df['id'] == 'e4caca755ee0bdd711e18fb8084958b5'][col_name] == 1).all()

# #### 2. [2 балла] Распределите студентов в соответствии с первым приоритетом

# In[ ]:


# (￣^￣)ゞ

# Здесь для проверки приведена таблица, в которой есть 2 дополнительные колонки:
#     
#     1) is_first_place - является ли студент лучшим по перцентили хотя бы на одном из курсов, куда он был зачислен 
#     (True / NaN)
#     
#     2) is_last_place  - является ли студент худшим по перцентили хотя бы на одном из курсов, куда он был зачислен (True / NaN)

# In[ ]:


!wget  -O '2_task_check.csv' -q 'https://www.dropbox.com/s/v8o2zzq3iz5gc9w/_2_task_check.csv?dl=0'
check_df = pd.read_csv('2_task_check.csv')

# После распределения студентов в соответствии с первым приоритетом добавьте в свой датафрейм аналогичные признаки и запустите проверку:

# In[ ]:


fir_col_name =       # insert name of your new column with is_first_place as str
last_col_name =      # insert name of your new column with is_last_place as str


assert((df[df[fir_col_name].isna() == False][['id']].sort_values('id').reset_index(drop=True)
        ==
        check_df[check_df['is_first_place'].isna() == False][['id']].sort_values('id').reset_index(drop=True)
       ).id.values).all()


assert((df[df[last_col_name].isna() == False][['id']].sort_values('id').reset_index(drop=True)
       == 
       check_df[check_df['is_last_place'].isna() == False][['id']].sort_values('id').reset_index(drop=True)
      ).id.values).all()

# #### 3. [3 балла] Проведите все три волны отбора студентов на курсы по выбору

# In[ ]:


# (￣^￣)ゞ

# **Отправьте свой файл res_fall.csv в контест (https://contest.yandex.ru/contest/40211/problems/A/) и прикрепите/укажите ниже ваш никнейм и ссылку на успешную посылку.**

# *Дисклеймер:*
# 
# Успешная посылка в контесте является **обязательным** условием получения полного балла за этот (и следующий) пункт. Если добиться успешной посылки не удастся, баллы будут выставляться на усмотрение проверяюшего. 
# 
# При этом ОК в контесте не гарантирует полный балл. Оценка всё равно может быть снижена в случае обнаружения неэффективностей или ошибок в коде. Если вы сдадите в AnyTask очевидно неработающий код или ноутбук без кода, но при этом в контест будет сдан корректный файл, то это будет расцениваться как плагиат.

# На всякий случай просим вас сдать вместе с ноутбуком файл res_fall.csv в anytask

# **Дополнительное задание. [2 бонусных балла] Распределите таким же образом студентов еще и на весенние курсы по выбору.**
# 
# Если ваш код был хорошо структурирован, то это не составит проблем. 
# 
# Если вы выполнили это задание, сдайте среди прочего файл res_spring.csv в таком же формате, как и res_fall.csv.

# In[ ]:


# (￣^'￣)ゞ

# **Отправьте свой файл res_spring.csv в контест (https://contest.yandex.ru/contest/40211/problems/B/) и прикрепите/укажите ниже ваш никнейм и ссылку на успешную посылку.**

# На всякий случай просим вас сдать вместе с ноутбуком файл res_spring.csv в anytask

# Вставьте картинку, описывающую ваш опыт выполнения этого задания:

# In[ ]:



