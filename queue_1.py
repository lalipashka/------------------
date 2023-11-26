Queue = []
QueueStart = 0

def push(val):
    """
    Функция для добавления элемента в очередь.
    """
    Queue.append(val)

def top():
    """
    Функция для получения элемента из начала очереди без удаления.
    """
    if QueueStart < len(Queue):
        return Queue[QueueStart]
    else:
        print("Queue is empty.")
        return None

def pop():
    """
    Функция для удаления и возврата элемента из начала очереди.
    """
    global QueueStart
    result = Queue[QueueStart] 
    QueueStart += 1
    if QueueStart > len(Queue) / 2:
        Queue[:QueueStart] = []
        QueueStart = 0
    return result

def size():
    """
    Функция для получения текущего размера очереди.
    """
    return len(Queue) - QueueStart

def isempty():
    """
    Функция для проверки, пуста ли очередь.
    """
    return QueueStart >= len(Queue)

def clear():
    """
    Функция для очистки очереди.
    """
    global QueueStart
    QueueStart = 0
    Queue[:] = []

# Пример использования
push(1)
push(2)
push(3)

print("Queue:", Queue)  # Вывод: Queue: [1, 2, 3]

popped_value = pop()
print("Popped value:", popped_value)  # Вывод: Popped value: 1

print("Updated Queue:", Queue)  # Вывод: Updated Queue: [2, 3]

print("Top element:", top())  # Вывод: Top element: 2

print("Queue size:", size())  # Вывод: Queue size: 2

print("Is Queue empty?", isempty())  # Вывод: Is Queue empty? False

clear()

print("Cleared Queue:", Queue)  # Вывод: Cleared Queue: []
