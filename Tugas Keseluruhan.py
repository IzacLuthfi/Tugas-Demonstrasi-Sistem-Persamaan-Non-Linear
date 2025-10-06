import math

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57


def g1B(x, y):
    if x == 0:
        x = 1e-6
    return (10 - x*y) / x

def g2A(x, y):
    val = 57 - 3*x*y**2
    if val < 0:
        return float('nan')
    return math.sqrt(val)


def iterasi_titik_tetap_jacobi(x0, y0, eps=1e-6, max_iter=100):
    print("\n=== Iterasi Titik Tetap - Jacobi (g1B, g2A) ===")
    print("r\t x\t\t y\t\t Δx\t\t Δy")
    xr, yr = x0, y0
    for r in range(max_iter):
        x_next = g1B(xr, yr)
        y_next = g2A(xr, yr)
        if math.isnan(x_next) or math.isnan(y_next):
            print("Iterasi divergen (akar kompleks muncul).")
            break
        dx = abs(x_next - xr)
        dy = abs(y_next - yr)
        print(f"{r}\t {x_next:.6f}\t {y_next:.6f}\t {dx:.6f}\t {dy:.6f}")
        if dx < eps and dy < eps:
            break
        xr, yr = x_next, y_next
    print(f"Hasil akhir: x = {xr:.6f}, y = {yr:.6f}\n")


def iterasi_titik_tetap_seidel(x0, y0, eps=1e-6, max_iter=100):
    print("\n=== Iterasi Titik Tetap - Seidel (g1B, g2A) ===")
    print("r\t x\t\t y\t\t Δx\t\t Δy")
    xr, yr = x0, y0
    for r in range(max_iter):
        x_next = g1B(xr, yr)
        y_next = g2A(x_next, yr)  
        if math.isnan(x_next) or math.isnan(y_next):
            print("Iterasi divergen (akar kompleks muncul).")
            break
        dx = abs(x_next - xr)
        dy = abs(y_next - yr)
        print(f"{r}\t {x_next:.6f}\t {y_next:.6f}\t {dx:.6f}\t {dy:.6f}")
        if dx < eps and dy < eps:
            break
        xr, yr = x_next, y_next
    print(f"Hasil akhir: x = {xr:.6f}, y = {yr:.6f}\n")


def newton_raphson(x0, y0, eps=1e-6, max_iter=50):
    print("\n=== Metode Newton-Raphson ===")
    print("r\t x\t\t y\t\t Δx\t\t Δy")
    xr, yr = x0, y0
    for r in range(max_iter):
        u = f1(xr, yr)
        v = f2(xr, yr)

        du_dx = 2*xr + yr
        du_dy = xr
        dv_dx = 3 * yr**2
        dv_dy = 1 + 6*xr*yr

        D = du_dx * dv_dy - du_dy * dv_dx
        if D == 0:
            print("Determinannya 0, tidak bisa lanjut iterasi.")
            break

        x_next = xr - (u * dv_dy - v * du_dy) / D
        y_next = yr + (u * dv_dx - v * du_dx) / D

        dx = abs(x_next - xr)
        dy = abs(y_next - yr)

        print(f"{r}\t {x_next:.6f}\t {y_next:.6f}\t {dx:.6f}\t {dy:.6f}")
        if dx < eps and dy < eps:
            break

        xr, yr = x_next, y_next

    print(f"Hasil akhir: x = {xr:.6f}, y = {yr:.6f}\n")


def secant_method(x0, y0, x1, y1, eps=1e-6, max_iter=50):
    print("\n=== Metode Secant (Pendekatan dua titik awal) ===")
    print("r\t x\t\t y\t\t Δx\t\t Δy")
    for r in range(max_iter):

        f1_0, f2_0 = f1(x0, y0), f2(x0, y0)
        f1_1, f2_1 = f1(x1, y1), f2(x1, y1)

        df1x = f1_1 - f1_0
        df2y = f2_1 - f2_0

        if abs(df1x) < 1e-12 or abs(df2y) < 1e-12:
            print("Kenaikan sangat kecil, iterasi berhenti.")
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

    print(f"Hasil akhir: x = {x1:.6f}, y = {y1:.6f}\n")


if __name__ == "__main__":
    x0, y0 = 1.5, 3.5

    iterasi_titik_tetap_jacobi(x0, y0)
    iterasi_titik_tetap_seidel(x0, y0)
    newton_raphson(x0, y0)
    secant_method(1.5, 3.5, 1.6, 3.4)
