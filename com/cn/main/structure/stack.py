# coding=utf-8
# 栈的实现

class Stack():

    def __init__(st,size):
        st.stack=[];
        st.size=size;
        st.top=-1;

    def push(st,content):
        if st.Full():
            print "Stack is Full!"
        else:
            st.stack.append(content)
            st.top=st.top+1

    def out(st):
        if st.Empty():
            print "Stack is Empty!"
        else:
            st.top=st.top-1

    def Full(st):
        if  st.top==st.size:
            return True
        else:
            return False

    def Empty(st):
        if st.top==-1:
            return True
        else:
            return False

    def getTop(st):
        if st.Empty():
            print "Stack is Empty!"
        else:
            return st.stack[st.top]

bs = Stack(5)
bs.push("1")
bs.push("2")
bs.push("3")
bs.push("4")
bs.push("5")
print bs.getTop()
bs.out()
print bs.getTop()