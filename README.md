# loveplanet
* Тестовое задание на бэкенд-разработчика. Приложение для знакомств(соотв. нормальной, настоящей регистрации нет)
 
 `git clone https://github.com/hed0xakep/lovaplanet.git`

 `python manage.py runserver`
 
 ## Логика работы приложения
`api/clients/create/` - эндпоинт дя регистрации. Тело запроса:
```
{
'firstname': 'Иван',
'lastname': 'Иванов',
'email': 'ex@ex.com',
'gender': 'm',
'avatar': __file__,
'password': 'pass123'
}
```
`api/clients/<id>/match/` - эндпоинт лайка юзера. Если лайки совпадут, то выведется почта участника.
