
#include <stdio.h>


int mod(int a, int p) {
return (a % p + p) % p;
}
int modular_inverse(int a, int p) {
    int t[2] = {0,1};
    int remainder = p;
    int newremainder = mod(a, p);

    while (newremainder != 0) {
        int quotient = remainder / newremainder;
        int temp;

        temp = t[0];
        t[0] = t[1];
        t[1] = temp - quotient * t[1];

        temp = remainder;
        remainder = newremainder;
        newremainder = temp - quotient * newremainder;
    }

    if (remainder > 1) return -1;
    return mod(t[0], p);
}

void add_elliptic_curve(int a, int A[2], int B[2], int p, int R[2]) {
    int x1 = A[0];
    int y1 = A[1];
    int x2 = B[0];
    int y2 = B[1];
int slope;
    if ((x1 == x2 && y1 == mod(-y2, p))){
        R[0] = 0;
        R[1] = 0;
        return;
    }
if (x1 == x2 && y1 == y2) {
        slope = mod((3 * x1 * x1 + a) * modular_inverse(2 * y1, p), p);
    } 
    else {

        slope = mod((y2 - y1) * modular_inverse(x2 - x1, p), p);
    }
    
    int x3 = mod(slope * slope - x1 - x2, p);
    int y3 = mod(-slope * (x3 - x1) - y1, p);

    R[0] = x3;
    R[1] = y3;
}
void multiply_elliptic_curve(int a, int P[2], int k, int p) {
    short first_loop = 1;//true
    int result[2] = {0, 0};   
    int temp[2] = {P[0], P[1]};

    while (k > 0) {
    if (k%2) {
            if (first_loop) {
            result[0] = temp[0];
                result[1] = temp[1];
                first_loop = 0;//false
            } 
            else {
            add_elliptic_curve(a, result, temp, p, result);
            }
        }
        add_elliptic_curve(a, temp, temp, p, temp);
        k >>= 1;
    }
    P[0] = result[0];
    P[1] = result[1];
}

int main() {
    //finds the order of all 4 values
    int store[2] = {6,2};
    int P1[2] = {store[0], store[1]};
    int P2[2] = {0, 1};
    int P3[2] = {5, 6};
    int P4[2] = {3, 3}; 
    int count = 0;
    while(1){
    int P1[2] = {store[0], store[1]};
    count++;
    multiply_elliptic_curve(3, P1, count, 7);
    //printf("%d, %d\n", P1[0], P1[1]);
    if (P1[0] == 0 && P1[1] ==0){
        printf("ord P1 = %d\n", count);
        break;
    }
    }
    count = 0;
        while(1){
    int P1[2] = {P2[0], P2[1]};
    count++;
    multiply_elliptic_curve(3, P1, count, 7);
    //printf("%d, %d\n", P1[0], P1[1]);
    if (P1[0] == 0 && P1[1] ==0){
        printf("ord P2 = %d\n", count);
        break;
    }
    }
    count = 0;
        while(1){
    int P1[2] = {P3[0], P3[1]};
    count++;
    multiply_elliptic_curve(3, P1, count, 7);
   // printf("%d, %d\n", P1[0], P1[1]);
    if (P1[0] == 0 && P1[1] ==0){
        printf("ord P3 = %d\n", count);
        break;
    }
    }
    count = 0;
        while(1){
    int P1[2] = {P4[0], P4[1]};
    count++;
    multiply_elliptic_curve(3, P1, count, 7);
   // printf("%d, %d\n", P1[0], P1[1]);
    if (P1[0] == 0 && P1[1] ==0){
        printf("ord P4 = %d\n", count);
        break;
    }
    }
    count = 0;
    return 0;
}
