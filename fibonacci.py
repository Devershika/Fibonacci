#include <stdio.h>

// Function to print Fibonacci series
void fibonacci(int n) {
    int a = 0, b = 1, next;


    for (int i = 0; i < n; i++) {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
}

int main() {
    int n;

    printf("Enter number of terms: ");
    scanf("%d", &n);
 
    printf("This is the required fibonacci series")
    fibonacci(n);

    return 0;
}
