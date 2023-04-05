[Home](../README.md)

# Linked List Time Complexity and Pros/Cons
## Time Complexity

| Operation                            | Big O Notation |
|--------------------------------------|----------------|
| Insert/Remove item (Back or Front)   | O(1)           |
| Insert/Remove item (Middle)          | O(n)           |
| x Contains n                         | O(n)           |
| Get Length                           | O(n)           |


## Pros/Cons
Pros:
* Fast with removing and adding items at beginning or end of list

Cons:
* Fast with getting length of Linked List
* slow with removing and adding items in the middle of the list
* Need to loop through entire Queue to find if item is contained in queue

## Use Case Examples:
1. Implimenting a Queue/Stack
2. Building a playlist where there are a lot of songs. We can easily retrieve only part of the playlist, and we can easily go to the next song in the list from the current song.

**Previous Page:** [Linked List Introduction](./introduction.md)

**Current:** Linked List Time Complexity and Pros/Cons 

**Next Page:** [Linked List Examples](./examples.md)
