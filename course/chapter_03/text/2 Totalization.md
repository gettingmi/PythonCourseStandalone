### Подсчет накопительных сумм и произведений с использованием цикла `while`

В цикле `while` часто используются операции для подсчета накопительных сумм и произведений. Эти приёмы позволяют накапливать значения переменных при каждой итерации цикла и используются во многих задачах, таких как подсчет суммы чисел, произведения чисел и других последовательных операций.

#### Накопление суммы

Чтобы посчитать сумму нескольких чисел с помощью цикла `while`, необходимо:
1. Инициализировать переменную для накопления суммы значением `0`.
2. При каждой итерации цикла добавлять новое значение к этой переменной.

**Пример: Подсчет суммы чисел от 1 до 5**

```python
count = 1
total_sum = 0  # Начальная сумма

while count <= 5:
    total_sum += count  # Добавляем текущее значение count к общей сумме
    count += 1

print(f"Сумма чисел от 1 до 5: {total_sum}")
```

**Вывод:**

```terminal
Сумма чисел от 1 до 5: 15
```

**Объяснение:**
- В переменной `total_sum` накапливаются значения переменной `count` на каждой итерации, начиная с 1 и до 5. После завершения цикла в `total_sum` будет храниться сумма всех чисел от 1 до 5.

#### Накопление произведения

Аналогично сумме, для вычисления произведения чисел:
1. Инициализируем переменную для накопления произведения значением `1` (так как начальное значение для произведения — это единица).
2. При каждой итерации умножаем накопленное произведение на текущее значение.

**Пример: Подсчет произведения чисел от 1 до 5**

```python
count = 1
total_product = 1  # Начальное произведение

while count <= 5:
    total_product *= count  # Умножаем текущее значение count на накопленное произведение
    count += 1

print(f"Произведение чисел от 1 до 5: {total_product}")
```

**Вывод:**

```terminal
Произведение чисел от 1 до 5: 120
```

**Объяснение:**
- В переменной `total_product` накапливаются результаты умножения переменной `count` на каждом шаге. Начальное значение произведения — 1, а после каждой итерации переменная увеличивается. В результате программа выводит произведение чисел от 1 до 5.

#### Пример: Сумма четных чисел

Мы можем модифицировать цикл для накопления суммы только четных чисел. Пример подсчета суммы четных чисел от 1 до 10:

```python
count = 1
even_sum = 0

while count <= 10:
    if count % 2 == 0:  # Проверка на четное число
        even_sum += count
    count += 1

print(f"Сумма четных чисел от 1 до 10: {even_sum}")
```

**Вывод:**

```terminal
Сумма четных чисел от 1 до 10: 30
```

#### Заключение

Использование накопительных сумм и произведений в циклах — это один из базовых и полезных приёмов при решении задач, связанных с последовательной обработкой данных. Переменные для накопления (суммы или произведения) и их изменение на каждом шаге позволяют легко решать задачи, такие как подсчёт итоговых результатов по множеству значений.