# Dictionary untuk menyimpan data pengguna (NIM dan password)
user_data = {}  # Key: NIM, Value: {'password': str, 'friends': list}

# List kontak teman yang tersedia secara global dengan tuple (ID, nama, email)
friend_directory = [
    (1, 'Re', 'alice@example.com'),
    (2, 'Igo', 'bob@example.com'),
    (3, 'Bi', 'charlie@example.com')
]

# Fungsi untuk mendaftarkan pengguna baru
def register_user():
    nim = input("Masukkan NIM Anda: ")
    if nim in user_data:
        print("NIM ini sudah terdaftar.")
        return
    password = input("Buat password: ")
    user_data[nim] = {'password': password, 'friends': []}
    print("Pendaftaran berhasil!")

# Fungsi untuk login pengguna
def user_login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")
    
    if nim in user_data and user_data[nim]['password'] == password:
        print("Login berhasil!")
        user_dashboard(nim)
    else:
        print("NIM atau password salah.")

# Fungsi untuk melihat daftar teman yang tersedia
def show_friends():
    print("\nDaftar Teman (Global):")
    for friend in friend_directory:
        friend_id, name, email = friend  # Mengambil ID, nama, dan email dari tuple
        print(f"ID: {friend_id}, Nama: {name}, Email: {email}")

# Fungsi untuk menambahkan teman baru ke kontak
def add_new_friend():
    while True:
        new_friend_id = input("Masukkan ID teman baru: ")
        # Cek apakah ID sudah digunakan
        if any(friend[0] == int(new_friend_id) for friend in friend_directory):
            print("ID ini sudah ada. Silakan masukkan ID yang berbeda.")
        else:
            break

    friend_name = input("Masukkan nama teman: ")
    friend_email = input("Masukkan email teman: ")
    
    friend_info = (int(new_friend_id), friend_name, friend_email)
    friend_directory.append(friend_info)
    print(f"Teman '{friend_name}' telah berhasil ditambahkan.")

# Fungsi untuk mengubah informasi teman di kontak global
def update_friend(friend):
    friend_id, name, email = friend  # Mengambil ID, nama, dan email dari tuple
    print(f"Edit teman '{name}':")
    updated_name = input(f"Nama baru ({name}): ") or name
    updated_email = input(f"Email baru ({email}): ") or email
    
    # Mengembalikan tuple yang diperbarui dengan data baru
    return (friend_id, updated_name, updated_email)

# Fungsi untuk menghapus teman dari daftar kontak
def delete_friend():
    show_friends()
    if friend_directory:
        selected_id = int(input("Masukkan ID teman yang ingin dihapus: "))
        
        # Cari teman berdasarkan ID
        for i, friend in enumerate(friend_directory):
            if friend[0] == selected_id:
                removed_friend = friend_directory.pop(i)
                print(f"Teman '{removed_friend[1]}' telah dihapus.")
                return
        print("ID tidak ditemukan.")
    else:
        print("Kontak teman kosong.")

# Fungsi menu untuk pengguna setelah login
def user_dashboard(nim):
    while True:
        print("\nDashboard Pengguna:")
        print("1. Lihat Daftar Teman")
        print("2. Tambah Teman Baru")
        print("3. Edit Teman")
        print("4. Hapus Teman")
        print("0. Logout")
        
        selection = input("Pilih opsi: ")
        if selection == '1':
            show_friends()
        elif selection == '2':
            add_new_friend()
        elif selection == '3':
            show_friends()
            if friend_directory:
                edit_id = int(input("Masukkan ID teman yang ingin diedit: "))
                for friend in friend_directory:
                    if friend[0] == edit_id:
                        updated_friend = update_friend(friend)
                        friend_directory[edit_id - 1] = updated_friend
                        print("Data teman telah diperbarui.")
                        break
                else:
                    print("ID tidak ditemukan.")
            else:
                print("Tidak ada teman dalam daftar.")
        elif selection == '4':
            delete_friend()
        elif selection == '0':
            print("Anda telah logout.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi utama untuk menampilkan menu awal
def main():
    while True:
        print("\nMenu Utama:")
        print("1. Daftar Pengguna Baru")
        print("2. Login")
        print("3. Keluar")
        
        action = input("Pilih opsi: ")
        if action == '1':
            register_user()
        elif action == '2':
            user_login()
        elif action == '3':
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan aplikasi
main()
