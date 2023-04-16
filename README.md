# arhdata
## HomeWork_3
1. Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
2. Реализовать сортировку пузырьком для двухсвязного списка

## Seminar_3
* singlLinkedL - однисвязный список и методы работы с ним
* dualLinkedL - двусвязный список и методы работы с ним

## Seminar_2
## Сортировка пузырьком
Один из наиболее простых алгоритмов сортировки массива – пузырьковая
сортировка. Нагляднее всего работу этого алгоритма можно продемонстрировать в
вертикальном массиве – наиболее легкие элементы стремятся вверх, словно
пузырьки воздуха в жидкости.
Базовый алгоритм предполагает, что каждый элемент необходимо сравнить с
соседним и, если правый элемент меньше левого, то их меняют местами. Алгоритм
повторяется до тех пор, пока все элементы в массиве не выстроятся в нужном
порядке.

## Сортировка выбором
Так же очень простой алгоритм сортировки, который предполагает поиск
наименьшего (или наибольшего) значения правее от сравниваемого элемента. В
случае, если такой элемент найден – происходит перестановка с начальным
элементом.
Данный алгоритм очень похож на пузырьковую сортировку, за тем исключением,
что для его записи удобнее использовать не цикл while, а 2 циклов for, вложенные
друг в друга.

## Сортировка вставками
Так же, как нечто среднее, между сортировкой пузырьком и выбором, можно
выделить сортировку вставками. Принцип работы у нее точно такой же, как у
предыдущей, только после сравнения двух элементов мы не запоминаем индекс
наименьшего (наибольшего) из элементов, а сразу производим перестановку.

## Бинарный поиск 
тип поискового алгоритма, который последовательно
делит пополам заранее отсортированный массив данных, чтобы обнаружить
нужный элемент. Другие его названия — двоичный поиск, метод половинного
деления, дихотомия. Принцип работы алгоритма бинарного поиска. Основная
последовательность действий алгоритма выглядит так: Сортируем массив
данных. Делим его пополам и находим середину.

## Быстрая сортировка (quicksort)
Чаще всего, когда мы используем сортировку, уже реализованную в штатных
средствах языка программирования или библиотеки, под капотом мы встретим
именно быструю сортировку. Суть быстрой сортировки – разделить массив на 2
части таким образом, чтобы справа все числа были больше, чем слева, при этом их
порядок относительно друг друга не важен. Это позволит не сравнивать элементы
справа с элементами слева больше 1 раза, как раз для достижения их разделения
на 2 части. И далее этот же подход будет применяться для каждой из получившихся
частей, равно как предусматривает принцип «разделяй и властвуй». При этом, в
отличии от бинарного поиска, количество операций в момент разделения не
константное, а линейное – необходимо сравнить все элементы правой и левой
части с неким эталоном и при необходимо – поменять их местами. В данном
алгоритме такой элемент называется пивотом.

## Сортировка кучей (пирамидальная)
Особенность данной сортировки в использовании дополнительной структуры
данных называемой бинарной кучей (пирамидой).
Бинарная куча представляет из себя древовидную структуру, когда у каждого
объекта может быть до 2 детей. При этом строится из массива она предельно
просто – первый элемент массива является корнем, 2 и 3 его детьми, 4 и 5 детьми
элемента 2 и т.д. пока в массиве остаются элементы. 
Cложность O(n log n), как и у быстрой сортировки.




