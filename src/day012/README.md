**Что уже должно быть известно:** Dict/set/list и их complexity.
**Цель занятия:** Освоить `Counter`, `defaultdict`, `deque` — только инструменты с высокой interview-отдачей.
**Источники:**
- **Теория/курс:** [collections documentation](https://docs.python.org/3/library/collections.html)
- **Документация:** [Python data structures](https://docs.python.org/3/tutorial/datastructures.html)

**Блок 1 — Python 55 мин: три высокоокупаемых инструмента `collections`.**
- [ ] Переписать frequency map через `Counter`.
- [ ] Построить grouping через `defaultdict(list)`.
- [ ] Реализовать FIFO queue через `deque`; применить append/popleft.
- [ ] Сравнить обычный dict и defaultdict в adjacency-list skeleton.

**Блок 2 — Practice 65 мин: Group Anagrams, queue и moving average.**
- [ ] Решить Group Anagrams через `defaultdict(list)`: [задача](https://leetcode.com/problems/group-anagrams/).
- [ ] Реализовать moving average последних k значений через deque.
- [ ] Переписать один старый код с collections, сохранив читаемость.

**Артефакт дня:** `day12/collections_examples.py`, `day12/group_anagrams.py`
**Критерий завершения:** Можешь без документации выбрать Counter/defaultdict/deque для трёх сценариев.
