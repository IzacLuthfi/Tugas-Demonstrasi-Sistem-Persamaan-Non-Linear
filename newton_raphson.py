import math

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def newton_raphson(x0, y0, eps=1e-6, max_iter=50):
    print("=== Metode Newton-Raphson ===")
    print("r\t x\t\t y\t\t Δx\t\t Δy")
    xr, yr = x0, y0

    for r in range(max_iter):
        u = f1(xr, yr)
        v = f2(xr, yr)

        du_dx = 2 * xr + yr
        du_dy = xr
        dv_dx = 3 * yr**2
        dv_dy = 1 + 6 * xr * yr

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

    print(f"Hasil akhir: x = {xr:.6f}, y = {yr:.6f}")

if __name__ == "__main__":
    newton_raphson(1.5, 3.5)
