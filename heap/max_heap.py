class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        head = self.storage[0]
        if len(self.storage) > 1:
            self.storage[0] = self.storage.pop()
            self._sift_down(0)
            return head
        else:
            return self.storage.pop()

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return

        parentIx = (index - 1) // 2
        if self.storage[index] <= self.storage[parentIx]:
            return
        else:
            self._swap(index, parentIx)
            self._bubble_up(parentIx)

    def _swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _max_index(self, i, j):
        if j not in range(len(self.storage)):
            return i
        return i if self.storage[i] > self.storage[j] else j

    def _sift_down(self, index):
        left_ix = index * 2 + 1
        if left_ix not in range(len(self.storage)):
            return
        max_child_ix = self._max_index(left_ix, left_ix + 1)
        if self.storage[max_child_ix] <= self.storage[index]:
            return
        else:
            self._swap(index, max_child_ix)
            self._sift_down(max_child_ix)
