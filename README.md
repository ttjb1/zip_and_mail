# zip_and_mail
## Инструкция по эксплуатации

### Использование:

*zip_and_mail.py [-f <output_file_name>] [-t <file_type>] [-a] [-e <path/to/email/config/file>]  </path/to/folder/you/want/to/zip>*

Перед началом работы необходимо выдать права на запуск файла zip_and_mail.py  

>  _chmod +x zip_and_mail.py_

**!!! Для корректной работы решения необходимо использовать полный путь до директории, которую планируем архивировать !!!**


### Общая информация

#### Варианты работы решения:


- Архив создается в той директории, которую планируем архивировать  
- Возможность указать имя архива (-f <имя_файла.zip>). По умолчанию (если параметр -f отсутствует) имя архива будет <YYYYMMDD-HHmmss.zip>  
- Возможность архивирования всех файлов заданного типа в указанной директории (-t <extention>). По умолчанию (если параметр -t отсутствует) будет заархивирована вся директория включая субдиректории. Если указан тип файла, отсутствующий в указанной директории, будет выведено сообщение о том, что файлы такого типа отсутствуют в директории   
- Возможность архивирования директории с абсолютным путем (если указан флаг -a). По умолчанию (если флаг -a не указан) архивирование выполняется без абсолютного пути   
- Возможность отправки полученного файла по Email (-e </path/to/config/file>). По умолчанию (если параметр -e не указан) функция отправки архива по Email отключена    

#### Конфигурационный файл для отправки архива по Email:

- Конфигурационный файл в формате JSON  
- Описание параметров файла конфигурации:
  
  "MESSAGE_BODY": "" -- Тело сообщения
  
  "EMAIL_SUBJECT": "" -- Тема письма
  
  "EMAIL_FROM": "" -- От кого
  
  "EMAIL_TO": "" -- Кому (есть возможность указать несколько адресов через запятую)
  
  "SMTP_SERVER": "" -- SMTP сервер, через который осуществляется отправка
  
  "SMTP_PORT": "" -- Порт SMTP сервера, через который осуществляется отправка
  
  "SMTP_USERNAME": "" -- Имя пользователя
  
  "SMTP_PASSWORD": "" -- Пароль (необходимо использовать "пароль приложения")  
  


#### Тест кейсы
- Для облегчения проверки в поставке присутствует файл demo_files.zip, содержащий тестовую дироекторию с файлами разного типа и субдиректорями.


#### Примеры использования:
- *zip_and_mail.py </path/to/folder/you/want/to/zip>*  
  
  Результат:
  
  В директории </path/to/folder/you/want/to/zip> создан файл <YYYYMMDD-HHmmss.zip>, содержищий всю директорию (включая субдиректории)

- *zip_and_mail.py -f <filename.zip> </path/to/folder/you/want/to/zip>*  
  
  Результат:
  
  В директории </path/to/folder/you/want/to/zip> создан файл <filename.zip>, содержищий всю директорию (включая субдиректории)

- *zip_and_mail.py -f <filename.zip> -t <txt> </path/to/folder/you/want/to/zip>*  
  
  Результат:
  
  В директории </path/to/folder/you/want/to/zip> создан файл <filename.zip>, содержищий файлы с расширением .txt из указанной директории
 
- *zip_and_mail.py -f <filename.zip> -t <txt> -a </path/to/folder/you/want/to/zip>*  
  
  Результат:
  
  В директории </path/to/folder/you/want/to/zip> создан файл <filename.zip>, содержищий файлы с расширением .txt из указанной директории. Архив содержит абсолютный путь к файлам
 
 - *zip_and_mail.py -f <filename.zip> -t <txt> -a -c </path/to/config/file> </path/to/folder/you/want/to/zip>*  
  
    Результат:
  
    В директории </path/to/folder/you/want/to/zip> создан файл <filename.zip>, содержищий файлы с расширением .txt из указанной директории. Архив содержит   абсолютный путь к файлам. Архив будет отправлен по Email в соответствии с параметрами, указанными в конфигурационном файле
