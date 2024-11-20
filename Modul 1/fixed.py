# Data profil pengguna (email -> {name, password, role})
profile = {
    'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
    're@gmail.com' : {'id': 2, 'name': 'reza', 'password': '1234', 'role': 'user'},
    'ig@gmail.com' : {'id': 3, 'name': 'igo', 'password': '1234', 'role': 'user'},
    'ib@gmail.com' : {'id': 4, 'name': 'indra', 'password': '1234', 'role': 'user'}
}

# Data teman pengguna (email -> list of friends)
friends = {
    'admin@gmail.com': ['Teman Admin 1', 'Teman Admin 2']
}

# Data pacar yang tersedia (list of dictionaries)
partners = [
    {'id': 1, 'name': 'Alice', 'description': 'Suka nonton film dan jalan-jalan', 'reserved': False},
    {'id': 2, 'name': 'Bob', 'description': 'Pencinta olahraga dan musik', 'reserved': False},
    {'id': 3, 'name': 'Charlie', 'description': 'Hobi membaca dan memasak', 'reserved': False},
]

# Data pemesanan (dictionary: email -> list of partner ids)
reservations = {}

def register():
    email = input("Masukkan email: ")
    if email in profile:
        print("Email sudah terdaftar! Silakan login.")
        return None
    name = input("Masukkan nama: ")
    password = input("Masukkan Password: ")

    new_id = len(profile) + 1  # Membuat ID unik berdasarkan jumlah akun yang ada
    profile[email] = {'id': new_id, 'name': name, 'password': password, 'role': 'user'}
    
    print("Registrasi berhasil!")
    return email

# Fungsi untuk menambah pacar (hanya untuk admin)
def add_partner():
    name = input("Masukkan nama pacar: ")
    description = input("Masukkan deskripsi pacar: ")
    new_id = len(partners) + 1
    partners.append({'id': new_id, 'name': name, 'description': description, 'reserved': False})
    print("Pacar berhasil ditambahkan!")

# Fungsi untuk menghapus pacar (hanya untuk admin)
def delete_partner():
    partner_id = int(input("Masukkan ID pacar yang ingin dihapus: "))
    for partner in partners:
        if partner['id'] == partner_id:
            partners.remove(partner)
            print("Pacar berhasil dihapus!")
            return
    print("Pacar tidak ditemukan!")

# Fungsi untuk melihat semua akun (untuk admin)
def view_all_users():
    print("\nDaftar Akun:")
    for email, details in profile.items():
        print(f"ID: {details['id']}, Email: {email}, Nama: {details['name']}")

# Fungsi untuk menambah daftar teman (fitur tambahan pada menu)
def add_friends(email):
    friends_list = []
    while True:
        add_friend = input("Ingin menambah teman? (y/n): ")
        if add_friend.lower() == 'y':
            friend = input("Masukkan nama teman: ")
            friends_list.append(friend)
        else:
            break

    # Menambahkan daftar teman ke dictionary 'friends'
    if email in friends:
        friends[email].extend(friends_list)
    else:
        friends[email] = friends_list
    print("Daftar teman berhasil disimpan!")

# Fungsi login menggunakan profile data
def login():
    email = input("Masukkan email: ")
    password = input("Masukkan Password: ")
    if email in profile and profile[email]['password'] == password:
        print("Login berhasil!")
        return email
    else:
        print("Login gagal! Email atau password salah.")
        return None

# Fungsi untuk melihat profil (hanya admin)
def view_profile(email):
    if email in profile and profile[email]['role'] == 'admin':
        print("\nProfil Anda:")
        for user_email in profile:
            print(f"Email: {user_email}, Nama: {profile[user_email]['name']}")
    else:
        print("Anda tidak memiliki izin untuk melihat profil.")

# Fungsi untuk mengedit profil (hanya admin)
def edit_profile():
    email = input("Masukkan email pengguna yang ingin diedit: ")
    if email in profile:
        name = input("Masukkan nama baru: ")
        profile[email]['name'] = name
        print("Profil berhasil diupdate!")
    else:
        print("Profil tidak ditemukan!")

# Fungsi untuk melihat daftar teman sendiri
def view_friends(email):
    if email in friends:
        print(f"\nDaftar teman Anda: {friends[email]}")
    else:
        print("Anda tidak memiliki daftar teman!")


# Fungsi untuk menampilkan semua pacar yang tersedia
def view_partners():
    print("\nDaftar Pacar:")
    available_partners = [partner for partner in partners if not partner['reserved']]
    if available_partners:
        for partner in available_partners:
            print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
    else:
        print("Tidak ada pacar yang tersedia saat ini.")

# Fungsi untuk memesan pacar
def reserve_partner(email):
    view_partners()
    partner_id = int(input("Masukkan ID pacar yang ingin dipesan: "))
    for partner in partners:
        if partner['id'] == partner_id and not partner['reserved']:
            partner['reserved'] = True  # Tandai pacar sebagai sudah dipesan
            if email not in reservations:
                reservations[email] = []
            reservations[email].append(partner_id)
            print("Pacar berhasil dipesan!")
            return
    print("Pacar tidak ditemukan atau sudah dipesan!")

# Fungsi untuk melihat pacar yang sudah dipesan
def view_reservations(email):
    if email in reservations:
        print("\nDaftar pacar yang dipesan:")
        for partner_id in reservations[email]:
            partner = next((p for p in partners if p['id'] == partner_id), None)
            if partner:
                print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
    else:
        print("Anda belum memesan pacar.")

# Menu utama
def main():
    while True:
        print("\n========================")
        print("WELLCOME TO\nRENTAL PACAR APP SIMULATOR")
        print("========================")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih opsi (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            user_email = login()
            if user_email:
                if profile[user_email]['role'] == 'admin':
                    while True:
                        print("\nMenu Admin:")
                        print("1. Lihat Profil Semua Pengguna")
                        print("2. Edit Profil Pengguna")
                        print("3. Lihat Pacar")
                        print("4. Tambah Pacar")
                        print("5. Hapus Pacar")
                        print("6. Logout")
                        admin_choice = input("Pilih opsi (1-6): ")

                        if admin_choice == '1':
                            view_profile(user_email)
                        elif admin_choice == '2':
                            edit_profile()
                        elif admin_choice == '3':
                            view_partners()
                        elif admin_choice == '4':
                            add_partner()
                        elif admin_choice == '5':
                            delete_partner()
                        elif admin_choice == '6':
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid! Silakan pilih lagi.")
                else:
                    while True:
                        print("\nMenu Pengguna:")
                        print("1. Lihat Daftar Semua Pengguna")
                        print("2. Lihat Teman")
                        print("3. Tambah Teman")
                        print("4. Lihat Pacar")
                        print("5. Pesan Pacar")
                        print("6. Lihat Pacar yang Dipesan")
                        print("7. Logout")
                        user_choice = input("Pilih opsi (1-7): ")

                        if user_choice == '1':
                            view_all_users()
                        elif user_choice == '2':
                            view_friends(user_email)
                        elif user_choice == '3':
                            add_friends(user_email)
                        elif user_choice == '4':
                            view_partners()
                        elif user_choice == '5':
                            reserve_partner(user_email)
                        elif user_choice == '6':
                            view_reservations(user_email)
                            break
                        elif user_choice == '7':
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid! Silakan pilih lagi.")
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih lagi.")

if __name__ == "__main__":
    main()