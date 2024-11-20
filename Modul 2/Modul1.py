#(email -> {name, password, role})
profile = {
    'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
    're@gmail.com' : {'id': 2, 'name': 'Reza', 'password': '1234', 'role': 'user'},
    'ig@gmail.com' : {'id': 3, 'name': 'Igo', 'password': '1234', 'role': 'user'},
    'ib@gmail.com' : {'id': 4, 'name': 'Indra', 'password': '1234', 'role': 'user'}
}

#(email -> list of reviews)
reviews = {
    're@gmail.com': ['Pacarnya cantik2'],
    'ig@gmail.com': ['Bintang 5 deh','Kangen sama mama freya'],
    'ib@gmail.com': ['app nya jelek']

}

#(list of dictionaries)
partners = [
    {'id': 1, 'name': 'Alice', 'description': 'Suka nonton film dan jalan-jalan', 'reserved': False},
    {'id': 2, 'name': 'Rose', 'description': 'Pencinta olahraga dan musik', 'reserved': False},
    {'id': 3, 'name': 'Susi', 'description': 'Hobi membaca dan memasak', 'reserved': False},
    {'id': 4, 'name': 'lily', 'description': 'Suka bermain game seorang proplayer', 'reserved': False}
]

#(dictionary: email -> list of partner ids)
reservations = {}

def register():
    email = input("Masukkan email: ")
    if email in profile:
        print("Email sudah terdaftar! Silakan login.")
        return None
    name = input("Masukkan nama: ")
    password = input("Masukkan Password: ")

    new_id = len(profile) + 1 
    profile[email] = {'id': new_id, 'name': name, 'password': password, 'role': 'user'}
    
    print("Registrasi berhasil!")
    return email

def add_partner():
    name = input("Masukkan nama pacar: ")
    description = input("Masukkan deskripsi pacar: ")
    new_id = len(partners) + 1
    partners.append({'id': new_id, 'name': name, 'description': description, 'reserved': False})
    print("Pacar berhasil ditambahkan!")

def delete_partner():
    print("\nDaftar Pacar:")
    available_partners = [partner for partner in partners if not partner['reserved']]
    if available_partners:
        for partner in available_partners:
            print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
    else:
        print("Tidak ada pacar yang tersedia saat ini.")

    partner_id = int(input("Masukkan ID pacar yang ingin dihapus: "))
    for partner in partners:
        if partner['id'] == partner_id:
            partners.remove(partner)
            print("Pacar berhasil dihapus!")
            return
    print("Pacar tidak ditemukan!")

def view_all_users():
    print("\nDaftar Akun:")
    for email, details in profile.items():
        print(f"ID: {details['id']}, Email: {email}, Nama: {details['name']}")

def add_reviews(email):
    review_list = []
    while True:
        add_review = input("Ingin menambah review? (y/n): ")
        if add_review.lower() == 'y':
            review = input("Masukkan review: ")
            review_list.append(review)
        else:
            break

    if email in reviews:
        reviews[email].extend(review_list)
    else:
        reviews[email] = review_list
    print("Daftar review berhasil disimpan!")

def login():
    email = input("Masukkan email: ")
    password = input("Masukkan Password: ")
    if email in profile and profile[email]['password'] == password:
        print("Login berhasil!")
        return email
    else:
        print("Login gagal! Email atau password salah.")
        return None

def view_profile(email):
    if email in profile and profile[email]['role'] == 'admin':
        print("\nProfil Anda:")
        for user_email in profile:
            print(f"Email: {user_email}, Nama: {profile[user_email]['name']}")
    else:
        print("Anda tidak memiliki izin untuk melihat profil.")

def edit_profile():
    email = input("Masukkan email pengguna yang ingin diedit: ")
    if email in profile:
        name = input("Masukkan nama baru: ")
        profile[email]['name'] = name
        print("Profil berhasil diupdate!")
    else:
        print("Profil tidak ditemukan!")

def edit_own_profile(email):
    if email in profile:
        print(f"Profil Anda Saat Ini: {profile[email]}")
        new_name = input("Masukkan nama baru: ")
        new_password = input("Masukkan password baru: ")
        
        profile[email]['name'] = new_name
        profile[email]['password'] = new_password
        
        print("Profil berhasil diperbarui!")
    else:
        print("Kesalahan: Profil tidak ditemukan.")

def view_reviews(email):
    if email in reviews:
        print(f"\nDaftar review Anda: {reviews[email]}")
    else:
        print("Anda tidak memiliki review!")

def view_partners():
    print("\nDaftar Pacar:")
    available_partners = [partner for partner in partners if not partner['reserved']]
    if available_partners:
        for partner in available_partners:
            print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
    else:
        print("Tidak ada pacar yang tersedia saat ini.")

def reserve_partner(email):
    view_partners()
    partner_id = int(input("Masukkan ID pacar yang ingin dipesan: "))
    for partner in partners:
        if partner['id'] == partner_id and not partner['reserved']:
            partner['reserved'] = True  
            if email not in reservations:
                reservations[email] = []
            reservations[email].append(partner_id)
            print("Pacar berhasil dipesan!")
            return
    print("Pacar tidak ditemukan atau sudah dipesan!")

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
                        print("1. Edit Profil Saya")
                        print("2. Lihat Pacar")
                        print("3. Pesan Pacar")
                        print("4. Lihat Pacar yang Dipesan")
                        print("5. Lihat Ulasan saya")
                        print("6. Tambah Ulasan")
                        print("7. Logout")
                        user_choice = input("Pilih opsi (1-7): ")

                        if user_choice == '1':
                            edit_own_profile(user_email)
                        elif user_choice == '2':
                            view_partners()
                        elif user_choice == '3':
                            reserve_partner(user_email)
                        elif user_choice == '4':
                            view_reservations(user_email)
                        elif user_choice == '5':
                            view_reviews(user_email)
                        elif user_choice == '6':
                            add_reviews(user_email)
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
