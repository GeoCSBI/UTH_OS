class pyQueue:

    def __init__(self):

        self.queue = []

    def enqueue(self, item):

        self.queue.insert(0, item)
        print "Item: " + '\33[1m' + str(item) + '\33[0m' + " enqueued."

    def dequeue(self):

        out = self.queue.pop()
        print "Item: " + '\33[1m' + str(out) + '\33[0m' + " dequeued."

        return out

    def size(self):

        queueLenght = len(self.queue)
        print "Queue's lenght is: " + '\33[1m' + str(queueLenght) + '\33[1m' + " ."
        return queueLenght

    def queueToString(self):
        for i in range(self.size()):
            print(self.queue[i])