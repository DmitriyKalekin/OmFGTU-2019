# OmFGTU-2019
Dev practice

### Инструментарий
#### Git  
- регаемся на [https://github.com/]  
- ставим себе на машину git [https://git-scm.com/downloads] или [https://gitforwindows.org/]  
(инструкцию по установке можно прочитать тут: [https://www.atlassian.com/git/tutorials/install-git#windows])  
- запоминаем свой пароль менеджером паролей (винды или git)   
- обязательно прописываем **переменные окружения** - нас интересует **PATH** для вашего установленного git.exe [http://qaru.site/questions/220706/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screenshots]


#### BitBucket (Факультатив)  
- то же самое, что Git - только нужно иметь представление, как с ним работать  
- настройте SSH-ключи  
- регаемся на [https://bitbucket.org]  

#### Консоль  
- Cmder (Win) [https://cmder.net/]
- Far Manager [https://www.farmanager.com/download.php?l=ru]  
- либо запускайте в проводнике с правами администратора PowerShell или cmd [https://os-helper.ru/windows-10/kak-otkryt-komandnuyu-stroku-ot-imeni-administratora.html]  

#### IDE
- MS VisualStudio CE (много весит, не ставим пока) [https://visualstudio.microsoft.com/ru/vs/community/?rr=https%3A%2F%2Fwww.google.com%2F]  
- (C#) если пока лень ставить MS VS CE, рекомендую делать в онлайне [https://dotnetfiddle.net/] или [https://rextester.com/]  
- (Обязательно!) Нужна быстрая и лёгкая IDE для работы с Python, PHP и JS.   
Возьмём:   
* MS Visual Studio Code [https://code.visualstudio.com/] (Я предпочитаю MS VS Code)  
* или Atom [https://ide.atom.io/]  
* или Sublime Text [https://www.sublimetext.com/3]    

#### Trello 
- регистрируемся [https://trello.com/]  
- здесь мы будем отмечать прогресс по работам  


NDA    
Опрос о скиллах: js, jQuery, python, PHP, HTML+CSS, C#    
Виды работ, направления: CRM-Казарма, Selenium, MLM, hmq-edu, скрейперы, обработка данных, машинное обучение, чат-боты    
Что хочется изучать    
Трелло  
Колаб  

MySQL / Mongo  
Neo4j / OrientDB  




 





Ниже я заимствую отсюда:
[https://github.com/morgan1189/HSE-Programming/wiki/%D0%97%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D0%B5-01:-GIT-%D0%B8-%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE-%D1%81-Python]


### Занятие 01: GIT и знакомство с Python
План занятия
```
    Создаём репозиторий на github, создаём у себя локальную копию, создаём тестовый файл и отправляем его на github.
    Создаём на своём компьютере файл math.py и начинаем изучать питон.
    В конце занятия отправляем свой «конспект» в удалённый репозиторий.
```
### GIT

Два конспекта о том, как начать пользоваться гитом и гитхабом: [https://ancatmara.gitbooks.io/digital-literacy/chapter1.html]
[https://github.com/ElizavetaKuzmenko/Programming-and-computer-instruments/wiki/%D0%A1%D0%B5%D0%BC%D0%B8%D0%BD%D0%B0%D1%80-1:-GIT]

Полезные ресурсы:
Atlassian tutorials: [https://www.atlassian.com/git/tutorials]  
A Quick Introduction to Version Control with Git and GitHub [http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668]    
Git Book по-русски [https://git-scm.com/book/ru/v2]   

### Python

Обращайте внимание на версию питона! Мы пишем на Python 3.
### Установка Python

Для Windows: [https://www.python.org/downloads/] — простой (он же единственный) путь

Для Mac OS X: [https://www.python.org/downloads/] - простой путь
[http://docs.python-guide.org/en/latest/starting/install3/osx/] - более сложный путь, потребует знания английского языка и командной строки

Документация [https://docs.python.org/3/index.html]  
An Informal Introduction to Python [https://docs.python.org/3/tutorial/introduction.html]  
Python Tutor [http://pythontutor.ru/lessons/inout_and_arithmetic_operations/]  

После установки Python - нужно прописать переменную окружения PATH к интерпретатору, например, `C:\Program Files\Pyhon3.6\bin\`.
Теперь можно запускать ваш файл на выполнение (допустим, `math.py`) на выполнение из командной строки: `python math.py`

Предлагается поиграться с репозиторием git  
— клонировать себе (`git clone ...`)  
— сохранить изменения  (`git commit -am 'я сохранил'`)  
— скопировать себе изменения из интернета (`git pull origin master`)  
— залить свои локальные  изменения в интернет (в удалённый репозиторий `git push origin master`)  
— сделать `stash save` какого-нибудь файла (локальный конфиг)  
— создать ветку под задачу `git checkout -b novaya_vetka` и внести туда изменения.
— переключиться на ветку мастер `git checkout master`  
— слить изменения из новой ветки в мастер `git merge novaya_vetka`  


