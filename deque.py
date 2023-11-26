class Deque:
    def __init__(self, max_size):
        self._elements = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_size

    def push_back(self, value):
        if not self.is_full():
            self._elements[self._tail] = value
            self._tail = (self._tail + 1) % self._max_size
            self._size += 1
        else:
            print('error')

    def push_front(self, value):
        if not self.is_full():
            self._head = (self._head - 1) % self._max_size
            self._elements[self._head] = value
            self._size += 1
        else:
            print('error')

    def pop_back(self):
        if not self.is_empty():
            x = self._elements[self._tail - 1]
            self._elements[self._tail - 1] = None
            self._tail = (self._tail - 1) % self._max_size
            self._size -= 1
            print(x)
        else:
            print('error')

    def pop_front(self):
        if not self.is_empty():
            x = self._elements[self._head]
            self._elements[self._head] = None
            self._head = (self._head + 1) % self._max_size
            self._size -= 1
            print(x)
        else:
            print('error')


def process_commands(commands):
    n = commands.pop(0)
    m = commands.pop(0)
    deque = Deque(m)

    for command in commands:
        if command.startswith('push_back'):
            _, value = command.split()
            deque.push_back(int(value))
        elif command.startswith('push_front'):
            _, value = command.split()
            deque.push_front(int(value))
        elif command == 'pop_front':
            deque.pop_front()
        elif command == 'pop_back':
            deque.pop_back()


if __name__ == '__main__':
    commands_list = [
        10,
        5,
        'push_front 1',
        'push_back 2',
        'pop_back',
        'pop_front',
        'pop_front',
        'push_front 3',
        'push_back 4',
        'pop_back',
        'pop_front'
    ]

    process_commands(commands_list)
