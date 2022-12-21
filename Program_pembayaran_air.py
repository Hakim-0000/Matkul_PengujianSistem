# import libary
import sys
import numpy as np
sys.tracebacklimit=0

# Data User dari Input
print(57*'*')
print(23*'*'+' Data User '+23*'*')
print(57*'*')
noPel = int(input('No. Pelanggan           : '))
nama = input('Nama                    : ')
alamat = input('Alamat                  : ')
bulan = input('Bulan                   : ')
meter_awal = input('Meter Awal              : ')
meter_akhir = input('Meter Akhir             : ')
penggunaan = int(meter_awal)-int(meter_akhir)
print(f'Jumlah Pemakaian Air    : {penggunaan}m³\n\n')

# Rumus untuk menghitung tagihan
# 0 - 10m³ = Rp2500/m³
# 11 - 20m³ = Rp5000/m³
# 21 - 30m³ = Rp7000/m³
# > 31m³ = Rp10000/m³
def tagihan(penggunaan):
    if penggunaan in np.arange(0,11):
        total = penggunaan*2500
    elif penggunaan in np.arange(11, 21):
        kubikPertama = 10*2500
        kubikKedua = (penggunaan-10)*5000
        total = kubikPertama+kubikKedua
    elif penggunaan in np.arange(21, 31):
        kubikPertama = 10*2500
        kubikKedua = 10*5000
        kubikKetiga = (penggunaan-20)*7000
        total = kubikPertama+kubikKedua+kubikKetiga
    elif penggunaan>30:
        kubikPertama = 10*2500
        kubikKedua = 10*5000
        kubikKetiga = 10*7000
        kubikKeempat = (penggunaan-30)*10000
        total = kubikPertama+kubikKedua+kubikKetiga+kubikKeempat

    return total

# Menampilkan Hasil
def main():
    print(55*'=')
    print(20*'='+' Total tagihan '+20*'=')
    print(55*'=')
    print(f'No. Pelanggan           : {noPel}')
    print(f'Nama                    : {nama}')
    print(f'Alamat                  : {alamat}')
    print(f'Bulan                   : {bulan}')
    print(f'Meter Awal              : {meter_awal}')
    print(f'Meter Akhir             : {meter_akhir}')
    print(f'Jumlah Pemakaian Air    : {penggunaan}m³')
    print(55*'-')
    print(f'Total tagihan           : Rp{tagihan(penggunaan)}')
    print(55*'=')

if __name__ == "__main__":
    main()