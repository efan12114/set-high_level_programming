#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint_end(listint_t **head, const int n);
void print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif /* LISTS_H */
