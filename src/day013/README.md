**Что уже должно быть известно:** Lists, sorting, complexity, collections.
**Цель занятия:** Освоить `heapq` и `bisect` на базовом уровне, без продвинутых heap-задач.
**Источники:**
- **Теория/курс:** [heapq](https://docs.python.org/3/library/heapq.html)
- **Документация:** [bisect](https://docs.python.org/3/library/bisect.html)

**Блок 1 — Python 55 мин: min/max heap, `bisect_left/right`, complexity.**
- [ ] Создать min-heap через `heapify`; выполнить push/pop.
- [ ] Смоделировать max-heap через отрицательные числа.
- [ ] Применить `bisect_left`, `bisect_right`, `insort`; записать результаты на массиве с дубликатами.
- [ ] Записать complexity операций.

**Блок 2 — Practice 65 мин: три небольших упражнения.**
- [ ] Найти 3 наименьших элемента потока через heap размера 3.
- [ ] Объединить два маленьких sorted списка вручную и сравнить с `heapq.merge`.
- [ ] Найти insertion position через bisect и через собственный linear scan.

**Артефакт дня:** `day13/heap_bisect.py`, `day13/notes.md`
**Критерий завершения:** Min/max heap и bisect работают на тестах; complexity названа верно.
