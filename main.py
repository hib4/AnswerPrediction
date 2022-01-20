import random
import time

ncases = 0
ncases_true = 0
classes = {}

# database
dbase_c = []
dbase_d = []

def guess(x):
    '''Guess by KNN (K-Nearest Neighbour)'''

    distance = []
    for d in dbase_d:
        # hitung kuadrat jarak euclid dan masukkan ke list
        distance.append((x - d) ** 2)

    if len(distance):
        # cari jarak minimal
        d_min = min(distance)
        idx = distance.index(d_min)
        # kembalikan kode kategorinya
        return dbase_c[idx]
    else:
        # kembalikan saja kategori pertama
        return list(classes)[0]

# ---- main program ----
print('Belajar Artificial Intelligence')
print('-------------------------------')
time.sleep(1.5)

# penjelasan
print('\nKomputer akan menampilkan angka random 1 s.d 100')
print('dan akan menduga angka tersebut masuk kategori apa.')
print('Tugas user adalah mengkoreksi dugaan yang salah.')
print('Bedasarkan koreksian tsb, komputer akan belajar')
time.sleep(1.5)

print('\nInput label untuk kategori yang akan dibuat,')
print('misal Bagus, Sedang, Jelek dll.')
print('Kategori minimal ada 2')
time.sleep(1.5)

print('\nSilahkan input Label (minimal 2),')
print('dan tekan ENTER jika sudah selesai')
k = 1
while True:
    kLabel = input(f'Label untuk kategori {k} : ')
    if kLabel == '':
        if k < 3:
            continue
        else:
            break
    classes[str(k)] = kLabel.upper()
    k += 1

input('\nTekan ENTER untuk mulai')

while True:
    ncases += 1
    print('\n\nTrial ke', ncases, end='. ')

    d = random.randint(1, 100)
    print('Angka random =', d, end=' ', flush=True)

    # AI akan menunggu dengan KNN
    g = guess(d)
    time.sleep(1.5) # efek menunggu berpikir
    print('<-- AI:', classes[g])

    time.sleep(1) # efek menunggu konfirmasi
    # menunggu konfirmasi dan koreksi dari user
    while True:
        print('\nIngin dikoreksi? Pilih ', end='')
        for k, v in classes.items():
            print(f'{k}-{v}', end=' ')
        ans = input('\natau tekan ENTER saja kalau sudah benar: ')

        if ans == '':
            # dugaan dianggap benar
            dbase_d.append(d)
            dbase_c.append(g)
            ncases_true += 1
            break

        elif ans in classes.keys():
            # dugaan perlu dikoreksi
            print(f'Menurut user {d} itu {classes[ans]}')
            dbase_d.append(d)
            dbase_c.append(ans)
            if ans == g:
                ncases_true += 1
            break

    print('Akurasi', format(ncases_true/ncases*100, '.2f'), '%')