import math

def g1B(x, y):
    if x == 0:
        x = 1e-6
    return (10 - x * y) / x

def g2A(x, y):
    val = 57 - 3 * x * y**2
    if val < 0:
        return float('nan')
    return math.sqrt(val)

def iterasi_titik_tetap_jacobi(x0, y0, eps=1e-6, max_iter=100):
    print("=== Iterasi Titik Tetap - Jacobi (g1B, g2A) ===")
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

    print(f"Hasil akhir: x = {xr:.6f}, y = {yr:.6f}")

if __name__ == "__main__":
    iterasi_titik_tetap_jacobi(1.5, 3.5)
