class maxHeap:
    def __init__(self):
        self.heap = []
        
    def percolateUp(self, i):
        if i == 0:
            return 
        if self.heap[i] > self.heap[(i-1)//2]:
            swap = self.heap[i]
            self.heap[i] = self.heap[(i-1)//2]
            self.heap[(i-1)//2] = swap
            self.percolateUp((i-1)//2)
        
    def percolateDown(self, i):
        childIndex = 2*i + 1
        if childIndex >= len(self.heap):
            return
        
        maxValue = self.heap[i]
        maxIndex = i
        
        for j in range(min(2, len(self.heap)-childIndex)):
            if self.heap[j + childIndex] > self.heap[maxIndex]:
                maxValue = self.heap[j + childIndex]
                maxIndex = j + childIndex
                
        if maxIndex == i:
            return
        swap = self.heap[i]
        self.heap[i] = self.heap[maxIndex]
        self.heap[maxIndex] = swap
        self.percolateDown(maxIndex)
        
    def insert(self, val):
        self.heap.append(val)
        self.percolateUp(len(self.heap)-1)
        
    def heapify(self):
        for i in range(len(self.heap)//2 - 1)[::-1]:
            self.percolateDown(i)
            
    def pop(self):
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.percolateDown(0)
        return root