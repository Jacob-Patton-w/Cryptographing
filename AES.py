#Jacob Patton 991726430
GF28 = 0x11B
S_BOX_C = 0x63
BIT_LENGTH=8
import math
def GF_multi(a,b):
    store= 0
    final = 0
    for i in range(1,BIT_LENGTH+1):
        if b ^ 2**(BIT_LENGTH-i)< b:
            store = a << (BIT_LENGTH-i)
            while store >= 256:
                store = store ^ GF28 << (math.floor(math.log2(store))- math.floor(math.log2(GF28)))#used to find number of bits needed to shift left 
            final = final ^ store
            
    return final
def GFinverse(x):
    s=[1,0]
    t=[0,1]
    
    prev_remainder = GF28
    remainder = x
    while True:
        final_devisor = 0
        devisor = 0
        while remainder >= x:
            devisor = math.floor(math.log2(prev_remainder))- math.floor(math.log2(x))
            shift = x << devisor#shift left however many bits it takes for it to be 9 bits long
            remainder = prev_remainder ^ shift
            final_devisor = final_devisor+2**devisor
            prev_remainder = remainder
        s[0],s[1] = s[1], s[0] ^ GF_multi(s[1],final_devisor)
        t[0],t[1] = t[1], t[0] ^ GF_multi(t[1],final_devisor)
        if remainder == 0:
            return t[0]
        else:
            prev_remainder = x
            x = remainder
def get_bit(number, index):
    return (number >> index) & 1            
def get_S_box(inv):
    
    final = 0
    for i in range(BIT_LENGTH):
        final =final +(get_bit(inv,(i)%BIT_LENGTH) + get_bit(inv,(i+4)%BIT_LENGTH) + get_bit(inv,(i+5)%BIT_LENGTH)+ get_bit(inv,(i+6)%BIT_LENGTH) + get_bit(inv,(i+7)%BIT_LENGTH) + get_bit(S_BOX_C,i))%2*2**i
    return final

def Row_Permutation(matrix):
    p = [0,1,2,3]
    ret_matrix = []
    for arr in matrix:
        arr[0],arr[1],arr[2],arr[3] = arr[p[0]],arr[p[1]],arr[p[2]],arr[p[3]]
        for i in range(4):
            p[i] = (p[i]+1)%4
        ret_matrix.append(arr)
    return ret_matrix
def AddandMulti(matrix):
    multi = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    ret_matrix = []
    buffer = [0,0,0,0]
    for b in range(4):
        for i in range(4):
                for c in range(4):
                    buffer[i] ^= GF_multi(matrix[c][b],multi[i][c])
        ret_matrix.append(buffer)
        buffer = [0,0,0,0]
    return ret_matrix
def Keyaddition(matrix, key):
    ret_matrix =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for b in range(4):
            ret_matrix[i][b] = matrix[i][b] ^ key[i][b]
    return ret_matrix
            
Question1 = [[0x54, 0x32, 0xFA, 0x41],
[0x77, 0xAB, 0x24, 0x37],
[0x05, 0xFF, 0xC2, 0xC3],
[0x1C, 0xE5, 0x36, 0x7A]]
print("Question 1, the resulting array of inverses(in decimal) is: \n[", end = "")
for arr in Question1:
    for item in arr:
        print(GFinverse(item), end = ", ")
print("]\nThe resulting array after finding the S-Box value for each item \n[", end = "")
for arr in Question1:
    for item in arr:
        print(get_S_box(GFinverse(item)), end = ", ")

Question2 = [[0x9B, 0xAC, 0x11, 0x22],
[0x85, 0x41, 0xFD, 0xAB],
[0x34, 0x09, 0x0C, 0xD3],
[0xA4, 0x1C, 0xD7, 0x88]]
print("]\nQuestion 2, Finding the ShiftRows: ")
print(Row_Permutation(Question2))
Question3 = [[0x7A, 0xE3, 0xAF, 0x04],
[0x63, 0xDC, 0x2D, 0x32],
[0x19, 0xF1, 0xAB, 0x4D],
[0x5F, 0x55, 0xE7, 0x49]]
print("Question 3, Finding the MixColumn values: ")
print(AddandMulti(Question3))
print("The x value is: ", AddandMulti(Question3)[1][1])
print("The y value is: ", AddandMulti(Question3)[2][2])
Question4 = [[0x9B, 0xAC, 0x11, 0x22],
[0x85, 0x41, 0xFD, 0xAB],
[0x34, 0x09, 0x0C, 0xD3],
[0xA4, 0x1C, 0xD7, 0x88]]
Question4key = [[0x54, 0x32, 0xFA, 0x41],
[0x77, 0xAB, 0x24, 0x37],
[0x05, 0xFF, 0xC2, 0xC3],
[0x1C, 0xE5, 0x36, 0x7A]]
print("Question 4, Finding the AddRoundKey values: ")
print(Keyaddition(Question4, Question4key))
print("The w value is: ", Keyaddition(Question4, Question4key)[0][3])
print("The x value is: ", Keyaddition(Question4, Question4key)[1][1])
print("The y value is: ", Keyaddition(Question4, Question4key)[2][2])
print("The z value is: ", Keyaddition(Question4, Question4key)[3][0])

print(GFinverse(0xC2))
print(GF_multi(55,0x42))