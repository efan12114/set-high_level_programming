#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;       /* Moves 1 step */
		fast = fast->next->next; /* Moves 2 steps */

		if (slow == fast) /* If they meet, there is a cycle */
			return (1);
	}

	return (0); /* If fast reaches the end, there is no cycle */
}
