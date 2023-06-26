#include <Python.h>

/**
 * print_python_float - print float value
 * @p: pyobject
 *
 * Return: Void
 */

void print_python_float(PyObject *p)
{
PyFloatObject *pfo = (PyFloatObject *)(p);
float value;

setbuf(stdout, NULL);
value = pfo->ob_fval;
printf("[.] float object info\n");
if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
printf("  value: %2.2f\n", value);
}

/**
 * print_python_bytes - function to print basic info about python bytes
 * @p: pyboject
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
size_t size, i, len_bytes;
PyBytesObject *pbo = (PyBytesObject *)(p);

setbuf(stdout, NULL);
printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
if (size + 1 >= 10)
len_bytes = 10;
else
len_bytes = size + 1;
printf("  size: %zu\n", size);
printf("  trying string: %s\n", pbo->ob_sval);
printf("  first %zu bytes: ", len_bytes);
for (i = 0; i < size; i++)
{
if (i <= len_bytes - 1)
{
printf("%02hhx", pbo->ob_sval[i]);
printf(" ");
}
}
if (size + 1 <= 10)
printf("%02hhx", pbo->ob_sval[i]);
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

size = PyList_GET_SIZE(p);
allocated = ((PyListObject *)p)->allocated;
setbuf(stdout, NULL);
printf("[*] Python list info\n");
if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}
printf("[*] Size of the Python List = %zu\n", size);
printf("[*] Allocated = %zu\n", allocated);
for (i = 0; i < size; i++)
{
type = item->ob_item[i]->ob_type->tp_name;
printf("Element %zu: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(item->ob_item[i]);
if (strcmp(type, "float") == 0)
print_python_float(item->ob_item[i]);
}
}
