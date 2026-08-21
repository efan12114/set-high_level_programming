#include "hash_tables.h"

/**
 * shash_table_create - Creates a sorted hash table.
 * @size: Size of the array.
 *
 * Return: Pointer to sorted hash table, or NULL on failure.
 */
shash_table_t *shash_table_create(unsigned long int size)
{
	shash_table_t *ht;
	unsigned long int i;

	if (size == 0)
		return (NULL);

	ht = malloc(sizeof(shash_table_t));
	if (ht == NULL)
		return (NULL);

	ht->size = size;
	ht->array = calloc(size, sizeof(shash_node_t *));
	if (ht->array == NULL)
	{
		free(ht);
		return (NULL);
	}
	for (i = 0; i < size; i++)
		ht->array[i] = NULL;

	ht->shead = NULL;
	ht->stail = NULL;

	return (ht);
}

/**
 * insert_sorted - Inserts node into sorted doubly linked list.
 * @ht: Pointer to sorted hash table.
 * @node: Node to insert.
 */
static void insert_sorted(shash_table_t *ht, shash_node_t *node)
{
	shash_node_t *tmp;

	if (ht->shead == NULL)
	{
		node->sprev = NULL;
		node->snext = NULL;
		ht->shead = node;
		ht->stail = node;
		return;
	}

	if (strcmp(node->key, ht->shead->key) < 0)
	{
		node->sprev = NULL;
		node->snext = ht->shead;
		ht->shead->sprev = node;
		ht->shead = node;
		return;
	}

	tmp = ht->shead;
	while (tmp->snext && strcmp(node->key, tmp->snext->key) >= 0)
		tmp = tmp->snext;

	node->snext = tmp->snext;
	node->sprev = tmp;
	if (tmp->snext == NULL)
		ht->stail = node;
	else
		tmp->snext->sprev = node;
	tmp->snext = node;
}

/**
 * shash_table_set - Adds or updates element in sorted hash table.
 * @ht: Sorted hash table pointer.
 * @key: Key string.
 * @value: Value associated with key.
 *
 * Return: 1 on success, 0 otherwise.
 */
int shash_table_set(shash_table_t *ht, const char *key, const char *value)
{
	shash_node_t *node, *tmp;
	char *value_copy, *key_copy;
	unsigned long int index;

	if (ht == NULL || key == NULL || *key == '\0' || value == NULL)
		return (0);

	value_copy = strdup(value);
	if (value_copy == NULL)
		return (0);

	index = key_index((const unsigned char *)key, ht->size);
	tmp = ht->array[index];
	while (tmp)
	{
		if (strcmp(tmp->key, key) == 0)
		{
			free(tmp->value);
			tmp->value = value_copy;
			return (1);
		}
		tmp = tmp->next;
	}

	key_copy = strdup(key);
	if (key_copy == NULL)
	{
		free(value_copy);
		return (0);
	}

	node = malloc(sizeof(shash_node_t));
	if (node == NULL)
	{
		free(key_copy);
		free(value_copy);
		return (0);
	}

	node->key = key_copy;
	node->value = value_copy;
	node->next = ht->array[index];
	ht->array[index] = node;

	insert_sorted(ht, node);

	return (1);
}

/**
 * shash_table_get - Retrieves value associated with key in sorted ht.
 * @ht: Sorted hash table pointer.
 * @key: Key string.
 *
 * Return: Associated value, or NULL if not found.
 */
char *shash_table_get(const shash_table_t *ht, const char *key)
{
	shash_node_t *node;
	unsigned long int index;

	if (ht == NULL || key == NULL || *key == '\0')
		return (NULL);

	index = key_index((const unsigned char *)key, ht->size);
	if (index >= ht->size)
		return (NULL);

	node = ht->array[index];
	while (node && strcmp(node->key, key) != 0)
		node = node->next;

	return ((node == NULL) ? NULL : node->value);
}

/**
 * shash_table_print - Prints sorted hash table in order.
 * @ht: Sorted hash table pointer.
 */
void shash_table_print(const shash_table_t *ht)
{
	shash_node_t *node;
	unsigned char flag = 0;

	if (ht == NULL)
		return;

	printf("{");
	node = ht->shead;
	while (node)
	{
		if (flag == 1)
			printf(", ");
		printf("'%s': '%s'", node->key, node->value);
		flag = 1;
		node = node->snext;
	}
	printf("}\n");
}

/**
 * shash_table_print_rev - Prints sorted hash table in reverse order.
 * @ht: Sorted hash table pointer.
 */
void shash_table_print_rev(const shash_table_t *ht)
{
	shash_node_t *node;
	unsigned char flag = 0;

	if (ht == NULL)
		return;

	printf("{");
	node = ht->stail;
	while (node)
	{
		if (flag == 1)
			printf(", ");
		printf("'%s': '%s'", node->key, node->value);
		flag = 1;
		node = node->sprev;
	}
	printf("}\n");
}

/**
 * shash_table_delete - Deletes a sorted hash table.
 * @ht: Sorted hash table pointer.
 */
void shash_table_delete(shash_table_t *ht)
{
	shash_node_t *node, *tmp;

	if (ht == NULL)
		return;

	node = ht->shead;
	while (node)
	{
		tmp = node->snext;
		free(node->key);
		free(node->value);
		free(node);
		node = tmp;
	}
	free(ht->array);
	free(ht);
}
