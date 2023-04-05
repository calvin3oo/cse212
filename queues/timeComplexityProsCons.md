[Home](../README.md)

# Queue Time Complexity and Pros/Cons
## Time Complexity

| Operation           | Big O Notation |
|---------------------|----------------|
| Insert item (Back)  | O(1)           |
| Remove item (Front) | O(1)           |
| x Contains n        | O(n)           |
| Get Length          | O(n)           |

*This is for a Queue implimentation using a linked list.*

## Pros/Cons
Pros:
* Fast with removing and adding items

Cons:
* Limited to First in First out
* Need to loop through entire Queue to find if item is contained in queue

## Use Case Examples:
1. I want to store a list of functions to run whenever the CPU has bandwidth (callback queue)
2. I want to store a waitlist of newly married couples wanting to get an apartment contract

**Previous Page:** [Queue Introduction](./introduction.md)

**Current:** Queue Time Complexity and Pros/Cons 

**Next Page:** [Queue Examples](./examples.md)
