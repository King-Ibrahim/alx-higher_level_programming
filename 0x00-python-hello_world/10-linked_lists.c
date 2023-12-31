#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint -This function prints
 * all elements of a listint_t list
 * @h: the pointer to head of list
 * Return: returns the number of nodes
 *
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int nodes;
	/* number of nodes */
	current = h;
	nodes = 0;
	while (current != NULL)
	{
		printf("%i\n", current->nodes);
		current = current->next;
		nodes++;
	}
	return (nodes);
}

/**
 * add_nodeint - This function adds a new node at
 * the beginning of a listint_t list
 * @head: the pointer to a pointer of the start of the list
 * @n: the integer to be included in node
 * Return: returns the address of a new element
 *  returns NULL if it fails
 *
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * free_listint - This function frees a listint_t list
 * @head: the pointer to the list to be freed
 * Return: returns void
 *
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
