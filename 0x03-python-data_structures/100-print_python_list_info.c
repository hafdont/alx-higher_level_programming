#include <Python.h>
#include <listobject.h>
#include <stdio.h>

/**
* print_python_list_info - prints some basic info about pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p) 
{
	PyListObject *list;
	Py_ssize_t size, i;

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size if the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
