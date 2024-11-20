# Data Penginapan
data_penginapan = [
    {"room_id": "GJ123", "cust_name": "Aisyah", "expenses": 150000, "jumlah_orang": 3, "tanggal": "2024-08-03"},
    {"room_id": "GJ124", "cust_name": "Budi", "expenses": 180000, "jumlah_orang": 2, "tanggal": "2024-08-03"},
    {"room_id": "GJ125", "cust_name": "Citra", "expenses": 200000, "jumlah_orang": 4, "tanggal": "2024-08-03"},
    {"room_id": "GJ126", "cust_name": "Dodi", "expenses": 170000, "jumlah_orang": 3, "tanggal": "2024-08-03"},
    {"room_id": "GJ223", "cust_name": "Elok", "expenses": 120000, "jumlah_orang": 1, "tanggal": "2024-08-04"},
    {"room_id": "GJ224", "cust_name": "Fikri", "expenses": 140000, "jumlah_orang": 2, "tanggal": "2024-08-04"},
    {"room_id": "GJ225", "cust_name": "Gita", "expenses": 160000, "jumlah_orang": 3, "tanggal": "2024-08-04"},
    {"room_id": "GJ226", "cust_name": "Hendra", "expenses": 150000, "jumlah_orang": 4, "tanggal": "2024-08-04"},
    {"room_id": "GJ323", "cust_name": "Ika", "expenses": 130000, "jumlah_orang": 2, "tanggal": "2024-08-05"},
    {"room_id": "GJ324", "cust_name": "Joko", "expenses": 180000, "jumlah_orang": 3, "tanggal": "2024-08-05"},
    {"room_id": "GJ325", "cust_name": "Kiki", "expenses": 170000, "jumlah_orang": 4, "tanggal": "2024-08-05"},
    {"room_id": "GJ326", "cust_name": "Lina", "expenses": 160000, "jumlah_orang": 2, "tanggal": "2024-08-05"}
]

# Fungsi pure untuk mencari customer
def cari_customer(data, nama):
    try:
        customer_data = next(
            (item for item in data if item["cust_name"].lower() == nama.lower()), None
        )
        if customer_data is None:
            raise ValueError(f"Customer dengan nama '{nama}' tidak ditemukan.")
        return {
            "room_id": customer_data["room_id"],
            "cust_name": customer_data["cust_name"],
            "expenses": customer_data["expenses"],
            "jumlah_orang": customer_data["jumlah_orang"],
            "tanggal": customer_data["tanggal"]
            
        }
    except Exception as e:
        return str(e)

# Fungsi pure untuk menghitung rata-rata menginap
def rata_rata_menginap(data):
    try:
        rata_rata_per_tanggal = {
            tanggal: {
                "rata_rata": round(
                    sum(entry["jumlah_orang"] for entry in entries) / len(entries), 2
                )
            }
            for tanggal, entries in group_by(data, "tanggal").items()
        }
        return rata_rata_per_tanggal
    except Exception as e:
        return str(e)

# Fungsi pure untuk menghitung total pendapatan
def total_pendapatan(data):
    try:
        pendapatan_per_tanggal = {
            tanggal: {
                "total_pendapatan": sum(entry["expenses"] for entry in entries),
                "jumlah_customer": len(entries)
            }
            for tanggal, entries in group_by(data, "tanggal").items()
        }
        return pendapatan_per_tanggal
    except Exception as e:
        return str(e)

# Fungsi pembantu untuk gruping data berdasarkan key tertentu
def group_by(data, key):
    result = {}
    for item in data:
        result.setdefault(item[key], []).append(item)
    return result

# Sistem Menu
def menu():
    while True:
        print("\nSistem Pengelolaan Data Penginapan")
        print("1. Cari Customer")
        print("2. Rata-rata Menginap")
        print("3. Total Pendapatan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama customer: ")
            hasil = cari_customer(data_penginapan, nama)
            if isinstance(hasil, dict):
                print(
                    f"\nID Kamar: {hasil['room_id']}\n"
                    f"Nama: {hasil['cust_name']}\n"
                    f"Tagihan: {hasil['expenses']}\n"
                    f"Jumlah Orang: {hasil['jumlah_orang']}\n"
                    f"Tanggal: {hasil['tanggal']}\n"
                    f"Total Tagihan: {hasil['expenses']}\n"
                )
            else:
                print(f"\n{hasil}\n")
        elif pilihan == "2":
            hasil = rata_rata_menginap(data_penginapan)
            if isinstance(hasil, dict):
                print("\nRata-rata jumlah orang yang menginap tiap tanggal:")
                for tanggal, values in hasil.items():
                    print(f"Tanggal: {tanggal}, Rata-rata yang menginap: {values['rata_rata']}")
            else:
                print(f"\n{hasil}\n")
        elif pilihan == "3":
            hasil = total_pendapatan(data_penginapan)
            if isinstance(hasil, dict):
                print("\nTotal Pendapatan tiap tanggal:")
                for tanggal, values in hasil.items():
                    print(f"Tanggal: {tanggal}, Jumlah Customer: {values['jumlah_customer']}, Total Pendapatan: {values['total_pendapatan']}")
            else:
                print(f"\n{hasil}\n")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.\n")

# Menjalankan Menu
menu()
