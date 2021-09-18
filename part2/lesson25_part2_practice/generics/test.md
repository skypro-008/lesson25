1. `GET destination/` работает
2.  Отдается список всех Destination, но только поля `id, name`
3. Вьшка-класс и наследуется от ListView


1. `GET destination/<int:id>/` работает
2. Возвращается запись с переданным id
3. Возвращаются только поля `id, name, visa_id, covid_status`
4. По несуществующему id возвращается 404
5. Вьшка-класс и наследуется от DetailView
