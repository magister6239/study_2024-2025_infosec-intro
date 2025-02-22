---
## Front matter
title: "Лабораторная работа № 11"
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

Познакомиться с операционной системой Linux. Получить практические навыки работы с редактором Emacs.

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

Вызвал Emacs (рис. [-@fig:001], [-@fig:002]).

![Команда emacs](image/1.PNG){#fig:001 width=70%}

![Emacs](image/2.PNG){#fig:002 width=70%}

Создал файл lab07.sh с помощью Emacs (рис. [-@fig:003]).

![Название файла](image/3.PNG){#fig:003 width=70%}

Ввёл текст в созданный файл (рис. [-@fig:004]).

![Текст](image/4.PNG){#fig:004 width=70%}

Сохранил файл lab07.sh (рис. [-@fig:005]).

![Сохранение](image/5.PNG){#fig:005 width=70%}

Вырезал первую строку и вставил её в конец файла (рис. [-@fig:006]).

![Изменённый текст](image/6.PNG){#fig:006 width=70%}

Скопировал функцию hello и вставил её в конец файла (рис. [-@fig:007]).

![Изменённый текст](image/7.PNG){#fig:007 width=70%}

Удалил первое определение функции hello (рис. [-@fig:008]).

![Изменённый текст](image/8.PNG){#fig:008 width=70%}

Отменил последнюю команду (рис. [-@fig:009]).

![Изменённый текст](image/9.PNG){#fig:009 width=70%}

Вывел список активных буферов на экран (рис. [-@fig:010]).

![Окно активных буферов](image/10.PNG){#fig:010 width=70%}

Переместился в окно со списком буферов (рис. [-@fig:011]).

![Перемещение между окнами](image/11.PNG){#fig:011 width=70%}

Переключился на буфер появляющийся при запуске Emacs (рис. [-@fig:012]).

![Стартовый буфер](image/12.PNG){#fig:012 width=70%}

Закрыл буфер (рис. [-@fig:013]).

![Результат](image/13.PNG){#fig:013 width=70%}

Переключился на предыдущий буфер без вывода списка буферов на экран (рис. [-@fig:014], [-@fig:015]).

![Строка для ввода названия буфера](image/14.PNG){#fig:014 width=70%}

![Стартовый буфер](image/15.PNG){#fig:015 width=70%}

Поделил фрейм на 4 части (рис. [-@fig:016]).

![4 фрейма](image/16.PNG){#fig:016 width=70%}

В каждом фрейме написал произвольный текст (рис. [-@fig:017]).

![Текст в 4 фреймах](image/17.PNG){#fig:017 width=70%}

Переключился в режим поиска (рис. [-@fig:018]).

![Режим поиска](image/18.PNG){#fig:018 width=70%}

Нашёл все слова "echo" (рис. [-@fig:019]).

![Совпадения](image/19.PNG){#fig:019 width=70%}

Переключился на одно из найденных слов (рис. [-@fig:020]).

![Переход к совпадению](image/20.PNG){#fig:020 width=70%}

Переключился в режим поиска и замены (рис. [-@fig:021]).

![Режим поиска и замены](image/21.PNG){#fig:021 width=70%}

Заменил слова HELL= на HELLO= (рис. [-@fig:022], [-@fig:023]).

![Замена](image/22.PNG){#fig:022 width=70%}

![Совпадения](image/23.PNG){#fig:023 width=70%}

Подтвердил свой выбор (рис. [-@fig:024]).

![Изменённый текст](image/24.PNG){#fig:024 width=70%}

Переключился в альтернативный режим поиска (рис. [-@fig:025]).

![Альтернативный режим поиска](image/25.PNG){#fig:025 width=70%}

Ввёл слово "echo" (рис. [-@fig:026]).

![Введёное слово "echo"](image/26.PNG){#fig:026 width=70%}

Нашёл все слова "echo" и вывел строки в которых они находятся в новый фрейм (рис. [-@fig:027]).

![Результат поиска слова "echo"](image/27.PNG){#fig:027 width=70%}

# Выводы

Были получены практические навыки работы с редактором Emacs.

# Список литературы{.unnumbered}

::: {#refs}
:::
