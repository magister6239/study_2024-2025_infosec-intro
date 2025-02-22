---
## Front matter
title: "Лабораторная работа № 10"
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

Познакомиться с операционной системой Linux. Получить практические навыки работы с редактором vi, установленным по умолчанию практически во всех дистрибутивах.

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

Создал директорию (рис. [-@fig:001]).

![Команда mkdir](image/1.PNG){#fig:001 width=70%}

Перешёл в созданную директорию (рис. [-@fig:002]).

![Команды](image/2.PNG){#fig:002 width=70%}

Вызвал vi и создал файл hello.sh (рис. [-@fig:003], [-@fig:004]).

![Команда](image/3.PNG){#fig:003 width=70%}

![Редактор vi](image/4.PNG){#fig:004 width=70%}

Перешёл в режим вставки и ввёл текст (рис. [-@fig:005]).

![Введённый текст](image/5.PNG){#fig:005 width=70%}

Перешёл в режим последней строки, сохранил изменения и вышел из редактора (рис. [-@fig:006]).

![Команда wq](image/6.PNG){#fig:006 width=70%}

Проверил содержимое файла hello.sh (рис. [-@fig:007]).

![Команда cat](image/7.PNG){#fig:007 width=70%}

Сделал файл hello.sh исполняемым (рис. [-@fig:008]).

![Команда chmod](image/8.PNG){#fig:008 width=70%}

Открыл файл hello.sh в редакторе vi (рис. [-@fig:009], [-@fig:010]).

![Команда](image/9.PNG){#fig:009 width=70%}

![Редактор vi и содержимое файла hello.sh](image/10.PNG){#fig:010 width=70%}

Изменил слово HELL на HELLO (рис. [-@fig:011]).

![Изменённый текст](image/11.PNG){#fig:011 width=70%}

Изменил слово LOCAL на local (рис. [-@fig:012]).

![Изменённый текст](image/12.PNG){#fig:012 width=70%}

Скопировал строку с текстом "echo $HELLO" и вставил эту строку после последней строки (рис. [-@fig:013]).

![Изменённый текст](image/13.PNG){#fig:013 width=70%}

Удалил последнюю строку (рис. [-@fig:014]).

![Изменённый текст](image/14.PNG){#fig:014 width=70%}

Отменил удаление строки нажав клавишу u (рис. [-@fig:015]).

![Изменённый текст](image/15.PNG){#fig:015 width=70%}

Перешёл в режим последней строки, сохранил изменения и вышел из редактора (рис. [-@fig:016]).

![Команда wq](image/16.PNG){#fig:016 width=70%}

Проверил содержимое файла hello.sh (рис. [-@fig:017]).

![Команда cat](image/17.PNG){#fig:017 width=70%}

# Выводы

Были получены практические навыки работы с редактором vi.

# Список литературы{.unnumbered}

::: {#refs}
:::
