# coding=utf-8
# 队列的实现


class Queue():
    def __init__(qu,size):
        qu.queue=[];
        qu.size=size;
        qu.head=-1;
        qu.tail=-1;

    def Empty(qu):
        if qu.head==qu.tail:
            return True
        else:
            return False

    def Full(qu):
        if qu.tail-qu.head+1==qu.size:
            return True
        else:
            return False

    def enQueue(qu,content):
        if qu.Full():
            print "Queue is Full!"
        else:
            qu.queue.append(content)
            qu.tail = qu.tail+1

    def outQueue(qu):
        if qu.Empty():
            print "Queue is Empty!"
        else:
            qu.head=qu.head+1

    def clearQueue(qu):
        qu.head=qu.tail



f = Queue(5)

f.enQueue("123")
f.enQueue("234")
f.enQueue("345")
f.enQueue("456")
f.enQueue("567")
f.clearQueue()
print f.Empty()
print f.head
f.enQueue("123")
f.enQueue("234")
f.enQueue("345")
f.enQueue("456")
f.enQueue("567")
f.outQueue()
print f.tail
