# Програма для обчислення часу прання

Ця програма дозволяє користувачеві обрати режим прання, вказати температуру та швидкість обертів пральної машини. Вона розраховує час, необхідний для стирки, та відображає зворотний відлік до завершення стирки.

## Особливості
- Перетворення температури з різних одиниць (Цельсій, Кельвін, Фаренгейт).
- Розрахунок часу стирки в залежності від вибраного режиму та температури.
- Відлік часу до завершення стирки.

## Як користуватися
1. Запустіть програму.
2. Оберіть один з доступних режимів прання:
   - синтетика
   - бавовна
   - делікатна
   - швидке прання
   - полоскання
   - віджим
3. Введіть температуру у форматі (число + тип), наприклад:
   - `30C`
   - `300K`
   - `86F`
4. Введіть швидкість обертів пральної машини у числовому форматі (більше за 0).
5. Програма розрахує час прання і розпочне зворотний відлік.

## Залежності
Програма використовує стандартну бібліотеку `time`.

## Винятки
Програма обробляє помилки для:
- Невірного формату температури.
- Неправильно вказаного режиму прання.
- Швидкості обертів, яка повинна бути більшою за 0.

## Приклад використання
Оберіть режим прання: синтетика, бавовна, делікатна, швидке прання, полоскання, віджим: бавовна На якій температурі ви будете стирати (за форматом (число + тип, напр. '30C', '300K', '86F')?): 30C На якій швидкості ви будете стирати?: 1200 Стирка займе 97 секунд. Натисніть Enter, щоб розпочати стирку 00:01 ... 00:00 Стирка закінчилася. Натисніть Enter, щоб розпочати нову стирку

 

## Внесок
Будь ласка, відправляйте ваші ідеї та питання через [GitHub Issues](https://github.com/your-repo/issues).

## Ліцензія

Так якової ліцензії немає, але правила поширення є у LICENSE.md 

---

Дякуємо за використання програми! Сподіваємося, ви знайдете її корисною!

