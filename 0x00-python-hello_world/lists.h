#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Potion for a Magical Linked List
 * @n: Essence of an Integer
 * @next: Portal to the Next Magical Node
 *
 * Description: A mystical structure embodying the of a singly linked list.
 */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

/* Incantations for Summoning and Manipulating Magical Lists */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
