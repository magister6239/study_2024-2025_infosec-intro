---
## Front matter
title: "Лабораторная работа № 14"
subtitle: "Операционные системы"
author: "Перегудов Александр Вадимович"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  Options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc Options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---


# Цель работы

Изучить основы программирования в оболочке ОС UNIX. Научится писать более
сложные командные файлы с использованием логических управляющих конструкций
и циклов.

# Задание

# Теоретическое введение

Здесь описываются теоретические аспекты, связанные с выполнением работы.

Например, в табл. [-@tbl:std-dir] приведено краткое описание стандартных каталогов Unix.

: Описание некоторых каталогов файловой системы GNU Linux {#tbl:std-dir}

| Имя каталога | Описание каталога                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------------|
| `/`          | Корневая директория, содержащая всю файловую                                                                               |
| `/bin `      | Основные системные утилиты, необходимые как в однопользовательском режиме, так и при обычной работе всем пользователям     |
| `/etc`       | Общесистемные конфигурационные файлы и файлы конфигурации установленных программ                                           |
| `/home`      | Содержит домашние директории пользователей, которые, в свою очередь, содержат персональные настройки и данные пользователя |
| `/media`     | Точки монтирования для сменных носителей                                                                                   |
| `/root`      | Домашняя директория пользователя  `root`                                                                                   |
| `/tmp`       | Временные файлы                                                                                                            |
| `/usr`       | Вторичная иерархия для данных пользователя                                                                                 |

Более подробно про Unix см. в [@tanenbaum_book_modern-os_ru; @robbins_book_bash_en; @zarrelli_book_mastering-bash_en; @newham_book_learning-bash_en].

# Выполнение лабораторной работы

Создал файл task1.sh, проверил его наличие и открыл его в nano (рис. [-@fig:001]).

![Файл task1.sh](image/1.PNG){#fig:001 width=70%}

Написал скрипт (рис. [-@fig:100]).

![Скрипт](image/code1.PNG){#fig:100 width=70%}

Запустил скрипт task1.sh в одном (1) виртуальном терминале в фоновом режиме, перенаправив его вывод в другой (0) (рис. [-@fig:002]).

![Результат](image/2.PNG){#fig:002 width=70%}

Запустил скрипт task1.sh в фоновом режиме несколько раз (рис. [-@fig:003]).

![Результат](image/3.PNG){#fig:003 width=70%}

Переместился в директорию /usr/share/man/man1 и проверил её содержимое (рис. [-@fig:004], [-@fig:005]).

![Переход в директорию /usr/share/man/man1](image/4.PNG){#fig:004 width=70%}

![Часть архивов в директории /usr/share/man/man1](image/5.PNG){#fig:005 width=70%}

Создал файл task2.sh, проверил его наличие и открыл его в nano (рис. [-@fig:006]).

![Файл task2.sh](image/6.PNG){#fig:006 width=70%}

Написал скрипт (рис. [-@fig:200]).

![Скрипт](image/code2.PNG){#fig:200 width=70%}

Запустил скрипт task2.sh с аргументом "ls" (рис. [-@fig:007], [-@fig:008]).

![Запуск](image/7.PNG){#fig:007 width=70%}

![Результат](image/8.PNG){#fig:008 width=70%}

Запустил скрипт task2.sh с неправильными аргументами несколько раз (рис. [-@fig:009]).

![Запуск и результат](image/9.PNG){#fig:009 width=70%}

Создал файл task3.sh, проверил его наличие и открыл его в nano (рис. [-@fig:010]).

![Файл task3.sh](image/10.PNG){#fig:010 width=70%}

Написал скрипт (рис. [-@fig:300]).

![Скрипт](image/code3.PNG){#fig:300 width=70%}

Запустил скрипт task2.sh с некоторыми аргументами несколько раз (рис. [-@fig:011]).

![Запуск и результат](image/11.PNG){#fig:011 width=70%}

# Выводы

Были изучены основы программирования в оболочке ОС UNIX/Linux. Было освоено написание более сложных командных файлов с использованием логических управляющих конструкций и циклов.

# Список литературы{.unnumbered}

::: {#refs}
:::
