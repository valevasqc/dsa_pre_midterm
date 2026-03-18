#include <stdio.h>

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    int i; 

    printf("Counter i is in address: %p\n", (void*) &i); 

    for (i = 0; i < 5; i++) 
    {
        printf("Element %d is in address: %p\n", arr[i], (void*) &arr[i]);
    }
}
