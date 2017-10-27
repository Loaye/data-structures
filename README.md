# Data-Structures
-------------------
* [Singly Linked List](https://codefellows.github.io/sea-python-401d7/lectures/linked_list.html)
* [Doubly Linked List](https://codefellows.github.io/sea-python-401d7/lectures/double_linked_list.html)
* [Stack](https://codefellows.github.io/sea-python-401d7/lectures/stack.html)
* [Queue](https://codefellows.github.io/sea-python-401d7/lectures/queue.html)

## Singly Linked List(SLL)
A Singly Linked List is the containing/parent element to a collection on Nodes. The SLL flows in one direction with a head in the front of the list and with a tail pointing to None.

[H][Random Node] -> [Random Node] -> [Random Node][T] -> None
### SLL - Methods
-------------------
#### __init__
* *__init__()* Instaniates a new node
* Time Complexity = O(1)

#### Push
* *push()* adds a new node to the front of the SLL
* Time Complexity = O(1)

#### Pop
* *pop()* removes a node from the front of the SLL and returns the value
* Time Complexity = 0(1)

#### Size
* *size()* implements a counter for when pushing and popping nodes. When called size returns the size of the SLL.
* Time Complexity = 0(1)

#### Search
* *search()* looks for a given Node value in a SLL, and returns that value.
* Time Complexity = 0(1)

#### Remove
* *remove()* will look for a given Node value and remove it from a SLL.
* Time Complexity = 0(1)

#### Display
* *display()* Will return a unicode string representing the list as if it were a Python tuple literal.
* Time Complexity = 0(1)
## Stack
A stack has a First In Last Out(FILO) order. 
### Stack - Methods
-------------------
We inherited all the methods from Singly Linked List. The only difference is that we were more explicit with our *pop()* method to work for the stack. In case the stack is empty, the method raises an *IndexError*.

#### Push
* *push()* method pushes a new Node into a stack. This stack uses FILO, which is First In Last Out.
* Time Complexity  = O(1)

#### Pop
* *pop()* method removes a new Node off the top of the stack. This stack uses FILO, which is First In Last Out.
* Time Complexity = O(1)