**Что уже должно быть известно:** Дни 1–4: базовые типы, условия, циклы.
**Цель занятия:** Освоить функции: `def`, параметры, `return`, локальные переменные; без `*args`, decorators и сложной типизации.
**Источники:**
- **Теория/курс:** [CS50P Functions](https://cs50.harvard.edu/python/notes/0/)
- **Документация:** [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

**Блок 1 — Python 60 мин: `def`, параметры, `return`, локальные переменные.**
- [ ] Написать `add(a,b)`, `is_even(n)`, `celsius_to_fahrenheit(c)`, `monthly_payment(...)`.
- [ ] Для каждой функции записать 2–4 примера вход→выход.
- [ ] Показать разницу между `print` и `return`.
- [ ] Разбить ипотечный калькулятор на `read_inputs`, `validate`, `calculate`, `format_result`; `read_inputs` пока может быть без тестов.

**Блок 2 — Practice 60 мин: декомпозиция и чистые функции с `assert`.**
- [ ] Функция `max_of_three(a,b,c)` без `max`.
- [ ] Функция `count_digits(n)`.
- [ ] Функция `is_prime(n)`.
- [ ] Добавить к чистым функциям минимум 10 `assert`-проверок.

- **Артефакт дня:** `day05/functions.py`, `day05/mortgage_refactored.py`, `day05/tests.py`
- **Критерий завершения:** Чистые функции возвращают значения и проверяются через `assert`; ипотечная формула изолирована от ввода/вывода.
