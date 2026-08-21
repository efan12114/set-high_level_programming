#include "hash_tables.h"

/**
 * key_index - Gives the index of a key.
 * @key: Key string.
 * @size: Size of the array of the hash table.
 *
 * Return: Index at which the key/value pair should be stored.
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	if (key == NULL || size == 0)
		return (0);

	return (hash_djb2(key) % size);
}
