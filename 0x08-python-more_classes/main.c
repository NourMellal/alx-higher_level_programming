#include <stdio.h>
int actual_sqr_root(int n, int i);

int _sqrt_recursion(int n)
{
	if (n < 0)
		return (-1);
	return actual_sqr_root(n, 0);

}

int actual_sqr_root(int n, int i)
{
	if (i * i > n)
		return -1;
	if (i * i == n)
		return (i);
	return actual_sqr_root(n, i + 1);
}


int main(void)
{
    int r;

    r = _sqrt_recursion(1);
    printf("%d\n", r);
    r = _sqrt_recursion(1024);
    printf("%d\n", r);
    r = _sqrt_recursion(16);
    printf("%d\n", r);
    r = _sqrt_recursion(17);
    printf("%d\n", r);
    r = _sqrt_recursion(25);
    printf("%d\n", r);
    r = _sqrt_recursion(-1);
    printf("%d\n", r);
    return (0);
}