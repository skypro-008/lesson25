1. `GET destination/` работает
2.  Отдается список всех Destination, но только поля `id, name`


1. `POST destination/` работает 
2. Создается новая запись в Destination 
3. Сохраняются поля `name, visa_id, covid_status`, остальные поля не сохраняются
4. Возвращаются только поля `id, name, visa_id, covid_status`


1. `GET destination/<int:id>/` работает
2. Возвращается запись с переданным id
3. Возвращаются только поля `id, name, visa_id, covid_status`
4. По несуществующему id возвращается 404


1. `PATCH destination/<int:id>/` работает 
2. Обновляется запись по переданному id
3. Сохраняются поля `name, visa_id, covid_status`, остальные поля не сохраняются
4. Возвращаются только поля `id, name, visa_id, covid_status`
5. По несуществующему id возвращается 404


1. `DELETE destination/<int:id>/` работает
2. Удаляется запись по указанному id
3. По несуществующему id возвращается 200