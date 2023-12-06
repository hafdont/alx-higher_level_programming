#include "lists.h"

/**
 * check_cycle - Checks if a single linked list has a cycle
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, ! is there is a cycle.
 */

int check_cycle(listint_t *list)
{
listint_t *slow = list, *fast = list;

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
{
return (1);
}
}
return (0);
}
