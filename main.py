from Node import *

stack = Stack(5000)

stack.push_v(100)
stack.push_v(300)
stack.push_v(500)

stack.print_stack()

stack.pop()
stack.pop()

stack.print_stack()
