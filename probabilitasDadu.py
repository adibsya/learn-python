from fractions import Fraction


def probabilitas_dadu(target):
    # ini nilai awal hitungan hasil yang berhasil
    dapat_target = 0

    # perulangan untuk mencari seberapa banyak nilai target dari lempar2 daadu
    for i in range(1, 7):
        for j in range(1, 7):
            # ketika dadu sama dengan target, tambah jumlah dapat_target
            if i + j == target:
                dapat_target += 1
    # Jumlah total hasil / semeseta saat melempar dua dadu adalah 36 karena 6X6 = 36, gitu cuy
    nilai_semesta = 36
    # Hitung peluang
    probability = Fraction(dapat_target, nilai_semesta)
    return probability


# ini buat inputan user
target = int(input("Masukkan target bilangan dadu: "))

# Hitung probabilitas dan cetak hasilnya
print("Probabilitas melempar dua dadu mendapat bilangan ",
      target, " adalah ", probabilitas_dadu(target))
