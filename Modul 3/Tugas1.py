from functools import reduce

def arithmetic_geometric_sequence(a, d, r, n, current=1, result=None):
    """Fungsi rekursif untuk menghasilkan baris aritmetika-geometri."""
    if result is None:
        result = []  # Inisialisasi list hasil

    # Basis rekursi: berhenti jika current lebih dari n
    if current > n:
        return result

    # Hitung nilai suku ke-n: (a + (n - 1) * d) * r^(n - 1)
    an = (a + (current - 1) * d) * (r ** (current - 1))
    result.append(an)

    # Panggil rekursi untuk suku berikutnya
    return arithmetic_geometric_sequence(a, d, r, n, current + 1, result)

def add(x, y):
    """Fungsi untuk menjumlahkan dua angka."""
    return x + y

def main():
    # Input nilai dari pengguna
    print("Masukkan nilai untuk baris aritmetika-geometri:")
    a = int(input("Suku pertama (a): "))
    d = int(input("Beda aritmetika (d): "))
    r = int(input("Rasio geometri (r): "))
    n = int(input("Jumlah suku (n): "))

    # Menghasilkan baris aritmetika-geometri
    sequence = arithmetic_geometric_sequence(a, d, r, n)
    print("Baris aritmetika-geometri:", sequence)

    # Menggunakan reduce untuk menghitung jumlah deret
    deret_sum = reduce(add, sequence)
    print("Jumlah deret:", deret_sum)

# Panggil fungsi utama
if __name__ == "__main__":
    main()
