
import time

def log_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Fungsi {func.__name__} selesai dalam {end_time - start_time:.4f} detik")
        return result
    return wrapper

def review_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

@log_function_call
def register(profiles, email, name, password):
    if email in profiles:
        return profiles, "Email sudah terdaftar!"
    
    new_id = len(profiles) + 1
    updated_profiles = {**profiles, email: {'id': new_id, 'name': name, 'password': password, 'role': 'user'}}
    return updated_profiles, "Registrasi berhasil!"

@log_function_call
def add_partner(partners, name, description):
    new_id = len(partners) + 1
    new_partner = {'id': new_id, 'name': name, 'description': description, 'reserved': False}
    updated_partners = [*partners, new_partner]
    return updated_partners, "Partner berhasil ditambahkan!"

@log_function_call
def delete_partner(partners, partner_id):
    def partner_not_id(partner):
        return partner['id'] != partner_id
    
    updated_partners = [partner for partner in partners if partner_not_id(partner)]
    if len(updated_partners) == len(partners):
        return partners, "Partner tidak ditemukan!"
    return updated_partners, "Partner berhasil dihapus!"

@log_function_call
def reserve_partner(email, partners, reservations, partner_id):
    def partner_is_available(partner):
        return partner['id'] == partner_id and not partner['reserved']
    
    partner = next(filter(partner_is_available, partners), None)
    if not partner:
        return partners, reservations, "Partner tidak ditemukan atau sudah dipesan!"
    
    partner['reserved'] = True
    updated_reservations = {**reservations, email: reservations.get(email, []) + [partner_id]}
    return partners, updated_reservations, "Partner berhasil dipesan!"

@log_function_call
def view_available_partners(partners):
    available_partners = list(filter(lambda partner: not partner['reserved'], partners))
    return available_partners if available_partners else "Tidak ada partner yang tersedia saat ini."

def add_reviews_with_closure(reviews, email):
    counter = review_counter()  
    @log_function_call
    def add_single_review(review):
        new_reviews = reviews.copy()
        if email in new_reviews:
            new_reviews[email].append(review)
        else:
            new_reviews[email] = [review]
        print(f"Review ke-{counter()}: {review}")
        return new_reviews, "Ulasan berhasil ditambahkan!"
    return add_single_review

@log_function_call
def view_reviews(reviews, email):
    return reviews.get(email, "Anda belum memiliki ulasan.")

@log_function_call
def login(profiles, email, password):
    user = profiles.get(email)
    if user and user['password'] == password:
        return email, "Login berhasil!"
    return None, "Login gagal! Email atau password salah."

@log_function_call
def view_all_users(profiles):
    return [{"id": v['id'], "email": k, "name": v['name']} for k, v in profiles.items()]


def main(state):
    print("\n========================")
    print("WELLCOME TO RENTAL PACAR APP SIMULATOR")
    print("========================")
    print("1. Registrasi")
    print("2. Login")
    print("3. Lihat Semua Partner")
    print("4. Tambah Partner (Admin Only)")
    print("5. Hapus Partner (Admin Only)")
    print("6. Pesan Partner")
    print("7. Tambah Ulasan")
    print("8. Lihat Ulasan")
    print("9. Keluar")

    choice = input("Pilih opsi (1-9): ")

    if choice == '1':
        email = input("Masukkan email: ")
        name = input("Masukkan nama: ")
        password = input("Masukkan password: ")
        state['profile'], message = register(state['profile'], email, name, password)
        print(message)

    elif choice == '2':
        email = input("Masukkan email: ")
        password = input("Masukkan password: ")
        user_email, message = login(state['profile'], email, password)
        print(message)
        if user_email:
            user_role = state['profile'][user_email]['role']
            print(f"Selamat datang, {state['profile'][user_email]['name']} ({user_role})!")
            state['current_user'] = user_email

    elif choice == '3':
        available_partners = view_available_partners(state['partners'])
        if isinstance(available_partners, list):
            for partner in available_partners:
                print(f"ID: {partner['id']}, Nama: {partner['name']}, Deskripsi: {partner['description']}")
        else:
            print(available_partners)

    elif choice == '4':
        email = input("Masukkan email admin untuk verifikasi: ")
        if state['profile'].get(email, {}).get('role') == 'admin':
            name = input("Nama Partner: ")
            description = input("Deskripsi Partner: ")
            state['partners'], message = add_partner(state['partners'], name, description)
            print(message)
        else:
            print("Hanya admin yang dapat menambah partner!")

    elif choice == '5':
        email = input("Masukkan email admin untuk verifikasi: ")
        if state['profile'].get(email, {}).get('role') == 'admin':
            partner_id = int(input("ID Partner yang ingin dihapus: "))
            state['partners'], message = delete_partner(state['partners'], partner_id)
            print(message)
        else:
            print("Hanya admin yang dapat menghapus partner!")

    elif choice == '6':
        email = input("Masukkan email Anda: ")
        partner_id = int(input("ID Partner yang ingin dipesan: "))
        state['partners'], state['reservations'], message = reserve_partner(email, state['partners'], state['reservations'], partner_id)
        print(message)

    elif choice == '7':
        email = input("Masukkan email Anda: ")
        review = input("Tulis ulasan Anda: ")
        add_review = add_reviews_with_closure(state['reviews'], email)
        state['reviews'], message = add_review(review)
        print(message)

    elif choice == '8':
        email = input("Masukkan email Anda: ")
        user_reviews = view_reviews(state['reviews'], email)
        if isinstance(user_reviews, list):
            for review in user_reviews:
                print(f"Ulasan: {review}")
        else:
            print(user_reviews)

    elif choice == '9':
        print("Keluar dari program.")
        return  # Mengakhiri rekursi

    else:
        print("Pilihan tidak valid!")

    return main(state)

if __name__ == "__main__":
    initial_state = {
        'profile': {
            'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
            'reno@gmail.com':{'id': 1, 'name':'reno', 'password':'test123', 'role':'user'}
        },
        'partners': [
            {'id': 1, 'name': 'Alice', 'description': 'Suka nonton film', 'reserved': False},
            {'id': 2, 'name': 'Rose', 'description': 'Pencinta olahraga', 'reserved': False},
            {'id': 3, 'name': 'Lily', 'description': 'Gemar membaca novel', 'reserved': False},
            {'id': 4, 'name': 'Daisy', 'description': 'Penggemar musik jazz', 'reserved': False},
            {'id': 5, 'name': 'Ivy', 'description': 'Hobi memasak makanan sehat', 'reserved': False},
            {'id': 6, 'name': 'Hazel', 'description': 'Suka bersepeda di pagi hari', 'reserved': False},
            {'id': 7, 'name': 'Jasmine', 'description': 'Penggemar seni dan lukisan', 'reserved': False},
            {'id': 8, 'name': 'Violet', 'description': 'Sering hiking di pegunungan', 'reserved': False},
            {'id': 9, 'name': 'Fern', 'description': 'Menikmati kopi dan membaca buku', 'reserved': False},
            {'id': 10, 'name': 'Willow', 'description': 'Hobi berkebun dan menanam bunga', 'reserved': False}
        ],
        'reviews': {
            'reno@gmail.com': [
                "Alice sangat ramah dan menyenangkan diajak nonton.",
                "Rose adalah teman olahraga yang luar biasa dan penuh semangat!"
            ],
            'admin@gmail.com': [
                "Lily suka berbicara tentang novel, cocok bagi yang suka diskusi buku.",
                "Daisy memiliki selera musik yang keren, terutama jazz."
            ]
        },
        'reservations': {},
        'current_user': None
    }
    main(initial_state)
