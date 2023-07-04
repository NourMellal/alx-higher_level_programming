#include "lists.h"

listint_t *ReverseList(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *curr;

	curr = *head;
	while (curr)
	{
		next = curr->next; //next hrab
		curr->next = prev; // 9leb lflow dyal list
		prev = curr; // prev yzid lgodam
		curr = next; // cuurent yl7g lnext
	}
	*head = prev;
	return (prev);
}

int is_palindrome(listint_t **head) {

	listint_t *mid, *rev, *tmp;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return 1;

	tmp = *head;

	while (tmp)
	{
		tmp = tmp->next;
		size++;
	}
	tmp = *head;

	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return 0;

	tmp = tmp->next->next;
	rev = ReverseList(&tmp);
	print_listint(*head);
	printf("====================\n");
	mid = rev;
	tmp = *head;
	while (rev)
	{
		if (rev->n != tmp->n)
			return 0;

		tmp = tmp->next;
		rev = rev->next;
	}

	ReverseList(&mid);
	return 1;

}

