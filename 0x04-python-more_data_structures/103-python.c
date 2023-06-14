#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - function to print basic info about python bytes
 * @p: pyboject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
char *str;
size_t size, i, len_bytes;


printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
str = PyBytes_AsString(p);
if (size + 1 >= 10)
len_bytes = 10;
else
len_bytes = size + 1;
printf("  size: %zu\n", size);
printf("  trying string: %s\n", str);
printf("  first %zu bytes: ", len_bytes);
for (i = 0; i < size; i++)
{
if (i <= len_bytes - 1)
{
printf("%02hhx", str[i]);
printf(" ");
}
}
if (size + 1 <= 10)
printf("%02hhx", str[i]);
printf("\n");
}

/**
 * print_python_list - function to print info about python list
 * @p: pyobject
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
size_t size, allocated, i;
const char *type;
PyListObject *item = (PyListObject *)(p);

size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zu\n", size);
printf("[*] Allocated = %zu\n", allocated);
for (i = 0; i < size; i++)
{
type = item->ob_item[i]->ob_type->tp_name;
printf("Element %zu: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(item->ob_item[i]);
}
}
