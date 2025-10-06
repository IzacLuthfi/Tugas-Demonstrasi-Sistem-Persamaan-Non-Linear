import math

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def secant_method(x0, y0, x1, y1, eps=1e-6, max_iter=50):
    print("=== Metode Secant (Pendekatan dua titik awal) ===")
    print("r\t x\t\t y\t\t Δx\t\t Δy")

    for r in range(max_iter):
        f1_0, f2_0 = f1(x0, y0), f2(x0, y0)
        f1_1, f2_1 = f1(x1, y1), f2(x1, y1)

        df1x = f1_1 - f1_0
        df2y = f2_1 - f2_0

        if abs(df1x) < 1e-12 or abs(df2y) < 1e-12:
            print("Perubahan terlalu kecil, iterasi berhenti.")
            break

        x2 = x1 - f1_1 * (x1 - x0) / df1x
        y2 = y1 - f2_1 * (y1 - y0) / df2y

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        print(f"{r}\t {x2:.6f}\t {y2:.6f}\t {dx:.6f}\t {dy:.6f}")

        if dx < eps and dy < eps:
            break

        x0, y0 = x1, y1
        x1, y1 = x2, y2

    print(f"Hasil akhir: x = {x1:.6f}, y = {y1:.6f}")

if __name__ == "__main__":
    secant_method(1.5, 3.5, 1.6, 3.4)
