from threading import Thread
import time
import random
from Queue import Queue

queue = Queue(10)

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced", num
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print "Consumed", num
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()

"""
Explanation

In place of list, we are using a Queue instance(hereafter queue).
queue has a Condition and that condition has its lock. You don’t need to bother about Condition and Lock if you use Queue.
Producer uses put available on queue to insert data in the queue.
put() has the logic to acquire the lock before inserting data in queue.
lso put() checks whether the queue is full. If yes, then it calls wait() internally and so producer starts waiting.
Consumer uses get.
get() acquires the lock before removing data from queue.
get() checks if the queue is empty. If yes, it puts consumer in waiting state.
get() and put() has proper logic for notify() too. Why don’t you check the source code for Queue now?

"""
