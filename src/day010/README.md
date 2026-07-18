**Что уже должно быть известно:** Lists, dict, set, функции.
**Цель занятия:** Освоить ссылки, mutability, shallow copy, `is` vs `==`, mutable default argument.
**Источники:**
- **Теория/курс:** [Python data model](https://docs.python.org/3/reference/datamodel.html)
- **Документация:** [copy module](https://docs.python.org/3/library/copy.html)

**Блок 1 — Python 60 мин: ссылки, shallow/deep copy, `is`/`==`, mutable defaults.**
- [ ] Показать aliasing: `b=a`; изменить b; проверить a.
- [ ] Сравнить `a[:]`, `list(a)`, `copy.copy`, `copy.deepcopy` на вложенном списке.
- [ ] Проверить `is` и `==` на двух списках с одинаковым содержимым.
- [ ] Воспроизвести mutable default argument; исправить через `None`.

**Блок 2 — Practice 60 мин: эксперименты и исправление типичных ошибок.**
- [ ] Исправить 5 фрагментов с aliasing/shared rows.
- [ ] Написать `append_item(item, items=None)` и тесты.
- [ ] Создать корректную матрицу 3x3 и доказать отсутствие shared rows.

**Артефакт дня:** `day10/mutability.py`, `day10/pitfalls.md`
**Критерий завершения:** Можешь предсказать вывод всех примеров и объяснить каждое исправление.
