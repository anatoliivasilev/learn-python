**Что уже должно быть известно:** Python collections и Big-O на базовом уровне.
**Цель занятия:** Выучить complexity основных операций list/dict/set/string и сортировки.
**Источники:**
- **Теория/курс:** [Python Time Complexity wiki](https://wiki.python.org/moin/TimeComplexity)
- **Документация:** [Sorting HOWTO](https://docs.python.org/3/howto/sorting.html)

**Блок 1 — Theory 60 мин: Big-O основных операций list/dict/set/string/sort.**
- [ ] Составить таблицу complexity: list index/append/insert/pop(0)/membership; dict/set lookup; sort; slicing.
- [ ] Для 15 коротких фрагментов определить time/space complexity.
- [ ] Проверить `list.pop(0)` против `deque.popleft` на концептуальном уровне.

**Блок 2 — Practice 60 мин: анализ фрагментов и оптимизация одного решения.**
- [ ] Переписать один O(n²) duplicate search через set до O(n).
- [ ] Сравнить Two Sum brute force и Hash Map.
- [ ] Объяснить, почему slicing создаёт новый объект и требует O(k) памяти.

**Артефакт дня:** `day11/complexity.md`, `day11/complexity_exercises.py`
**Критерий завершения:** Не менее 13/15 оценок верны; complexity Two Sum и list operations объясняется без заметок.
