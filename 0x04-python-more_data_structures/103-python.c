#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int py; /* py = size */
	int n;
	char *check_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &check_str, &py);

	printf("  size: %li\n", py);
	printf("  trying string: %s\n", check_str);
	if (py < 10)
		printf("  first %li bytes:", py + 1);
	else
		printf("  first 10 bytes:");
	for (n = 0; n <= py && n < 10; n++)
		printf(" %02hhx", check_str[n]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int n;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (n = 0; n < size; n++)
        {
                type = (list->ob_item[n])->ob_type->tp_name;
		printf("Element %i: %s\n", n, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[n]);
        }
}
