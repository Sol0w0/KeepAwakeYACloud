# KeepAwakeYACloud
Программа для пинга и включения прерываемой VPS на Yandex Cloud
## Гайд
Для работы нужен Python и библиотеки requests и json.
- В код нужно вставить идентификатор вашей машины и ваш OAuth-токен. После этого вставьте значения в соответсующие поля и запустите скрипт.
- Скрипт проверяет состояние машины каждые 10 минут. Время можно поменять в функции main().
## Получение OAuth токена
- Перейдите по ссылке https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb и войдите в ваш аккаунт Яндекс. Вы получите свой OAuth-токен.
- Токен действует 1 год, после этого придется обновлять его.
## Материалы
- Документация об OAuth-токен: https://yandex.cloud/ru/docs/iam/concepts/authorization/oauth-token
- Документация о методах для машины на Yandex Cloud: https://yandex.cloud/ru/docs/compute/api-ref/Instance/
- Документация о аутентификации при использовании API: https://yandex.cloud/ru/docs/compute/api-ref/authentication
