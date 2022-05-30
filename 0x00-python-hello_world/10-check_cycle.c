#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list
 * Return: a integer.
 */
int check_cycle(listint_t *list)
{
	listint_t *les = list;
	listint_t *pes = list;

	while (les && pes && les->next)
	{
		pes = pes->next;
		les = les->next->next;
		if (pes == les)
			return (1);
	}
	return (0);
}
