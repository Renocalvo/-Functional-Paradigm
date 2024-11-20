# Inisialisasi data awal
profile = {
    'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
}

partners = [
    {'id': 1, 'name': 'Alice', 'description': 'Suka nonton film', 'reserved': False},
    {'id': 2, 'name': 'Rose', 'description': 'Pencinta olahraga', 'reserved': False}
]

reviews = {
    're@gmail.com': ['Pacarnya cantik']
}

reservations = {}

# Pure functions with functional programming paradigm

# Register user
def register(profile, email, name, password):
    if email in profile:
        return "Email sudah terdaftar! Silakan login.", profile

    new_id = len(profile) + 1 
    new_profile = profile.copy()
    new_profile[email] = {'id': new_id, 'name': name, 'password': password, 'role': 'user'}
    
    return "Registrasi berhasil!", new_profile


# Add new partner
def add_lovers(partners, name, description):
    new_id = len(partners) + 1
    new_partners = partners.copy()
    new_partners.append({'id': new_id, 'name': name, 'description': description, 'reserved': False})
    return "Pacar berhasil ditambahkan!", new_partners


# Delete a partner
def delete_partner(partners, partner_id):
    new_partners = [partner for partner in partners if partner['id'] != partner_id]
    if len(new_partners) == len(partners):
        return "Pacar tidak ditemukan!", partners
    return "Pacar berhasil dihapus!", new_partners

from functools import reduce
# View all users
def view_all_player(profile):
    reduce(profile)
    return profile[1][0], "profile di temukan"
    

# Add reviews
def add_reviews(reviews, email, review_list):
    new_reviews = reviews.copy()
    if email in new_reviews:
        new_reviews[email].extend(review_list)
    else:
        new_reviews[email] = review_list
    return "Daftar review berhasil disimpan!", new_reviews

# Login function
def login(profile, email, password):
    if email in profile and profile[email]['password'] == password:
        return "Login berhasil!", email
    return "Login gagal! Email atau password salah.", None

# View profile (Admin)
def view_profile(profile, email):
    if email in profile and profile[email]['role'] == 'admin':
        return profile
    return "Anda tidak memiliki izin untuk melihat profil."

# Edit profile of user (Admin)
def edit_profile(profile, email, new_name):
    if email in profile:
        new_profile = profile.copy()
        new_profile[email]['name'] = new_name
        return "Profil berhasil diupdate!", new_profile
    return "Profil tidak ditemukan!", profile



# Edit own profile
def edit_own_profile(profile, email, new_name, new_password):
    if email in profile:
        list(map("reduce"))
        new_profile = profile.copy()
        new_profile[email]['name'] = new_name
        new_profile[email]['password'] = new_password
        return "Profil berhasil diperbarui!", new_profile
    return "Kesalahan: Profil tidak ditemukan.", profile

def identity(partner):
    return partner

def add_partner(partners, name, description):
    new_id = len(partners) + 1
    new_partner = {'id': new_id, 'name': name, 'description': description, 'reserved': False}
    new_partners = list(map(identity, partners)) + [new_partner]
    return "Pacar berhasil ditambahkan!", new_partners

# View reviews
def view_feedback(reviews, email):
    list(view_all_player, profile)
    if email in reviews:
        return reviews[email]
    return "Anda tidak memiliki review!"

# View available partners
def view_partners(partners):
    available_partners = [partner for partner in partners if not partner['reserved']]
    return available_partners

def view_reviews(reviews, email):
    def find_reviews(acc, item):
        if item[0] == email:
            return item[1]  
        return acc  
    return reduce(find_reviews, reviews.items(), "Anda tidak memiliki review!")

def is_user_role(item):
    return item[1]['role'] == 'user'

def view_all_user(profile):
    user_profiles = dict(filter(is_user_role, profile.items()))
    return user_profiles

# Reserve partner
def reserve_partner(partners, reservations, email, partner_id):
    new_partners = partners.copy()
    new_reservations = reservations.copy()
    for partner in new_partners:
        if partner['id'] == partner_id and not partner['reserved']:
            partner['reserved'] = True  
            if email not in new_reservations:
                new_reservations[email] = []
            new_reservations[email].append(partner_id)
            return "Pacar berhasil dipesan!", new_partners, new_reservations
    return "Pacar tidak ditemukan atau sudah dipesan!", partners, reservations

# View reservations
def view_reservations(partners, reservations, email):
    if email in reservations:
        reserved_partners = [next((p for p in partners if p['id'] == pid), None) for pid in reservations[email]]
        return reserved_partners
    return "Anda belum memesan pacar."


# Fungsi untuk mengelola interaksi utama dengan user
def main():
    global profile, partners, reviews, reservations  # Data yang akan dimanipulasi di luar fungsi

    while True:
        print("\n========================")
        print("RENTAL PACAR APP SIMULATOR")
        print("========================")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih opsi (1-3): ")

        if choice == '1':
            email = input("Masukkan email: ")
            name = input("Masukkan nama: ")
            password = input("Masukkan password: ")
            message, profile = register(profile, email, name, password)
            print(message)

        elif choice == '2':
            email = input("Masukkan email: ")
            password = input("Masukkan password: ")
            message, user_email = login(profile, email, password)
            print(message)

            if user_email:
                if profile[user_email]['role'] == 'admin':
                    while True:
                        print("\nMenu Admin:")
                        print("1. Lihat Profil Semua Pengguna")
                        print("2. Edit Profil Pengguna")
                        print("3. Tambah Pacar")
                        print("4. Hapus Pacar")
                        print("5. Logout")
                        admin_choice = input("Pilih opsi (1-5): ")

                        if admin_choice == '1':
                            users = view_all_users(profile)
                            for email, details in users.items():
                                print(f"ID: {details['id']}, Email: {email}, Nama: {details['name']}")
                        elif admin_choice == '2':
                            edit_email = input("Masukkan email pengguna yang ingin diedit: ")
                            new_name = input("Masukkan nama baru: ")
                            message, profile = edit_profile(profile, edit_email, new_name)
                            print(message)
                        elif admin_choice == '3':
                            name = input("Masukkan nama pacar: ")
                            description = input("Masukkan deskripsi pacar: ")
                            message, partners = add_partner(partners, name, description)
                            print(message)
                        elif admin_choice == '4':
                            partner_id = int(input("Masukkan ID pacar yang ingin dihapus: "))
                            message, partners = delete_partner(partners, partner_id)
                            print(message)
                        elif admin_choice == '5':
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid!")

                else:  # Menu untuk pengguna biasa
                    while True:
                        print("\nMenu Pengguna:")
                        print("1. Edit Profil Saya")
                        print("2. Lihat Pacar yang Tersedia")
                        print("3. Pesan Pacar")
                        print("4. Lihat Pacar yang Dipesan")
                        print("5. Lihat Ulasan Saya")
                        print("6. Tambah Ulasan")
                        print("7. Logout")
                        user_choice = input("Pilih opsi (1-7): ")

                        if user_choice == '1':
                            new_name = input("Masukkan nama baru: ")
                            new_password = input("Masukkan password baru: ")
                            message, profile = edit_own_profile(profile, user_email, new_name, new_password)
                            print(message)

                        elif user_choice == '2':
                            available_partners = view_partners(partners)
                            if available_partners:
                                for partner in available_partners:
                                    print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
                            else:
                                print("Tidak ada pacar yang tersedia.")

                        elif user_choice == '3':
                            partner_id = int(input("Masukkan ID pacar yang ingin dipesan: "))
                            message, partners, reservations = reserve_partner(partners, reservations, user_email, partner_id)
                            print(message)

                        elif user_choice == '4':
                            reserved_partners = view_reservations(partners, reservations, user_email)
                            if reserved_partners:
                                for partner in reserved_partners:
                                    print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
                            else:
                                print("Anda belum memesan pacar.")

                        elif user_choice == '5':
                            user_reviews = view_reviews(reviews, user_email)
                            if isinstance(user_reviews, list):
                                for review in user_reviews:
                                    print(f"Review: {review}")
                            else:
                                print(user_reviews)

                        elif user_choice == '6':
                            review_list = []
                            while True:
                                review = input("Masukkan ulasan (ketik 'selesai' untuk berhenti): ")
                                if review == 'selesai':
                                    break
                                review_list.append(review)
                            message, reviews = add_reviews(reviews, user_email, review_list)
                            print(message)

                        elif user_choice == '7':
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid!")
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")


# Mulai program
if __name__ == "__main__":
    main()
