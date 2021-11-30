def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selection(A):    
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j     
        A[i], A[min_idx] = A[min_idx], A[i]
        
while True:
    ops = input('Sudahkah anda punya file (data.txt) yang mau diurutkan?(y/n)\n>> ')
    if ops == 'y':
        try:
            file = open('data.txt','r')
        except:
            input('Tidak ditemukan file (data.txt)!\nPRESS ENTER')
        else:
            p1 = file.write()
            p1 = p1.split(',')
            p1 = [int(i) for i in p1]
            metod2 = False
            res = True
    elif ops == 'n':
        metod2 = True
        break
    else:
        input('Saya tidak mengerti\nPRESS ENTER!')
        
if metod2 == True:
    print('\n\nKetik rangkaian angka, dan ENTER saja untuk menyudahi!')
    p1 = []
    while True:
        p = input('\n>> ')
        if p == '':
            res = True
            break
        else:
            p1.append(int(p))

print(f'\nList yang dihimpun: {p1}')
while res == True:
    ops = input('\nMau diurutkan dengan metode apa?\na. Bubble Sort\nb. Insertion Sort\nc. Selection Sort\n\n>> ')
    if ops == 'a':
        bubble(p1)
        break
    elif ops == 'b':
        insertion(p1)
        break
    elif ops == 'c':
        selection(p1)
        break
    else:
        input('\nSaya tidak mengerti!\nPRESS ENTER')
print(f'List setelah diurutkan: {p1}')
