# Data-Structures
-------------------
* [Singly Linked List](https://codefellows.github.io/sea-python-401d7/lectures/linked_list.html)
* [Doubly Linked List](https://codefellows.github.io/sea-python-401d7/lectures/double_linked_list.html)
* [Stack](https://codefellows.github.io/sea-python-401d7/lectures/stack.html)
* [Queue](https://codefellows.github.io/sea-python-401d7/lectures/queue.html)

## Singly Linked List (SLL)
A Singly Linked List is the containing/parent element to a collection on Nodes. The SLL flows in one direction with a head in the front of the list and with a tail pointing to None.

[H][Node] -> [Node] -> [Node][T] -> None
### SLL - Methods
-------------------
#### __init__
* *__init__()* Instaniates the new SLL.
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

## Doubly Linked List (DLL)
Much like a SLL, the only difference is that the DLL can traverse the list both ways.

[H][Node] <- -> [Node] <- -> [Node][T] <- -> None

### DLL - Methods
-------------------

#### __init__
* *__init__()* Instaniates a the DLL.
* Time Complexity = O(1)

#### __len__
* *__len__()* replaces the default Python  len() function and returns the lenth of the DLL using a counter.

#### Push
* *push()* adds a new node to the front/head of the DLL.
* Time Complexity = O(1)

#### Append
* *append()* adds a new node to the end/tail side of the DLL.
* Time Complexity = O(1)

#### Pop
* *pop()* removes a node from the front of the DLL and returns the value
* Time Complexity = 0(1)

#### Shift
* *shift()* removes a node from the end/tail of the DLL and returns the value.
* Time Complexity = 0(1)

#### Remove
* *remove()* will look for a given Node value and remove it from a SLL.
* Time Complexity = 0(1)

#### Display
* *display()* Will return a unicode string representing the list as if it were a Python tuple literal.
* Time Complexity = 0(1)
## Stack
A stack has a First In Last Out(FILO) priority order. 
### Stack - Methods
-------------------
We inherited all the methods from Singly Linked List. The only difference is that we were more explicit with our *pop()* method to work for the stack. In case the stack is empty, the method raises an *IndexError*.

#### __init__
* *__init__()* will instaniate the Stack.
#### Push
* *push()* method pushes a new Node into a stack. This stack uses FILO, which is First In Last Out.
* Time Complexity  = O(1)

#### Pop
* *pop()* method removes a new Node off the top of the stack. This stack uses FILO, which is First In Last Out.
* Time Complexity = O(1)

## Queue
A Queue utilizes the First In First Out (FIFO) priority order. An easy way to think of this is like waiting in line. The first person in line for at fair will be the first person on the ride.

### Queue - Methods
---------------------

#### __init__
* *__init__()* Instantiates a new Queue.

#### __len__
* *__len__()*  replaces the default Python  len() function and returns the the length of the Queue using a counter.

#### Length
* *length()* uses a counter to count the length of the Queue.

#### Enqueue
* *enqueue()* adds a node to the head of the queue. If a node is present it seats it behind it.
* Time Complexity = 0(1)

#### Dequeue
* *dequeue()* removes a node from the head of the queue. If a node isn't present it will return an *IndexError()* and message.
* Time Complexity = 0(1)

#### Peek
* *peek()* will display the value of a node without removing it from the Queue.
* Time Complexity = 0(1)