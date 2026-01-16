;implementing a basic hill cipher mod 257 via matrix multiplication in intel 8086 assembly(WARNING, THIS PROGRAM DOES NOT PRINT THE ANSWER, I SUGGEST USING emu8086 TO VIEW ANSWER IN MEMORY IF RUNNNING THIS CODE)
;This program also does not compute the determinant to ensure a valid key since it only computes mod a prime
twod equ 1
threed equ 3 
include "emu8086.inc"
org 100h      
;loading the key and plaintext into 2 registers 
lea di, key
lea si, plaintxt
;nested loop which acts something like
;    for(int i = 0; i<LENGTH; i++){
;        for(int j = 0; j<LENGTH; j++){
;            Answer[i]= (Answer[i]+ Plaintext[j]*Key[i][j])%257;
;        }}
lea dx, answer
mov ch, 255
For1:
inc ch
mov cl, 255
For2:
mov ax, 0
inc cl
mov al, threed
mul ch
mov bx, ax
add bl, cl
mov al,[bx+di]
mov bx, 0
mov bl, cl
mul [si+bx]
mov bx, dx
add bl, ch
add bl, ch
add [bx], ax
mov ax, [bx]
;doing mod 257
cmp ax, 0
je eqzero
mov bx, 257
xor dx, dx
div bx
lea bx, answer
add bl, ch
add bl, ch
eqzero:
mov [bx], dx
lea dx, answer


cmp cl, 2
jne For2 
cmp ch, 2
jne For1

ret

key db 11,8,9,3,7,23,21,4,12   
plaintxt db 9,20,22  
answer dw 0,0,0




