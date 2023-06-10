#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindromeRec - recursively check if linked list palindrome
 * @head: head of linked list
 * @tail: tail of linked list
 * 
 * Return: 1 on success, 0 on failure
 */

int is_palindromeRec(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if ((*head)->n == tail->n && is_palindromeRec(head, tail->next))
	{
		(*head) = (*head)->next;
		return (1);
	}
		return (0);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: head of linked list
 * 
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (1);
	else
		return (is_palindromeRec(head, *head));
}
