Created on Wed Oct 13 15:57:33 2021
Nama Adilla Pramudya Rajasa
Nim : 064002100018
@author: Adilla Pramudya Rajasa
"""
print("====================")
print('Tugas Algoritma :)')
print("====================")



judul = str(input('Masukkan judul puisi: '))
filename = (('%s.txt')%(judul)) 
f = open(filename,'w')
f.write(judul)
f.write('\n\n')
print (('File %s dibuat!')%(filename))

for i in range(100): 
    print()


print('Ketik "exit" untuk keluar!')    
print (judul,'\n')

baris = True
nomor = 0 
while baris == True:
    nomor += 1; num = str(nomor) 
    penomoran = str(('%s  ')%(num))
    isi = str(input(penomoran)) 
    if isi == 'exit': 
        print('\nDisimpan. Terimakasih!')
        baris = False
    else:
        f.write(isi) 
        f.write('\n')
f.close() 
