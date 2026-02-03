import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        if not self.heap:
            return "Queue Empty"
        return heapq.heappop(self.heap)

    def display(self):
        return sorted(self.heap)

pq = PriorityQueue()
pq.push(30)
pq.push(10)
pq.push(20)
pq.pop()
print(pq.display())