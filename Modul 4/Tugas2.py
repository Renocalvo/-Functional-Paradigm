import time
import math

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end_time - start_time:.4f} detik")
        return result
    return wrapper

@measure_time
def parse_input(input_string):
    data = list(map(int, input_string.split(',')))
    
    if len(data) % 2 != 0:
        raise ValueError("Jumlah elemen harus genap untuk membentuk pasangan (x, y).")
    
    points = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    return points

def translate(tx, ty):
    def apply(point):
        x, y = point
        return x + tx, y + ty
    return apply

def rotate(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_theta, sin_theta = math.cos(angle_radians), math.sin(angle_radians)
    def apply(point):
        x, y = point
        return x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta
    return apply

def scale(factor):
    def apply(point):
        x, y = point
        return x * factor, y * factor
    return apply

@measure_time
def apply_transformation(points, transformation):
    return list(map(transformation, points))

def main():
    
    input_string = input("Masukkan koordinat (x,y) dipisahkan dengan koma, misalnya '1,2,3,4,5,6': ")
    
    try:
        points = parse_input(input_string)
        print("Titik awal:", points)

        # Transformasi 1: Translasi dengan tx=3 dan ty=7
        translated_points = apply_transformation(points, translate(3, 7))
        print("Setelah translasi (tx=3, ty=7):", translated_points)

        # Transformasi 2: Rotasi sebesar 60 derajat
        rotated_points = apply_transformation(translated_points, rotate(60))
        print("Setelah rotasi 60 derajat:", rotated_points)

        # Transformasi 3: Dilatasi dengan faktor skala 1.5
        scaled_points = apply_transformation(rotated_points, scale(1.5))
        print("Setelah dilatasi (skala=1.5):", scaled_points)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
