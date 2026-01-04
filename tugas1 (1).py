# =====================================
# 0/1 Knapsack Problem - Dynamic Programming
# Studi Kasus: Penjualan Elektronik UMKM
# =====================================

# Data item: (Kode, Nama, Berat, Keuntungan)
items = [
    ("A", "Rice Cooker", 10, 12),
    ("B", "Blender", 8, 10),
    ("C", "Setrika", 6, 8),
    ("D", "Dispenser", 25, 30),
    ("E", "Kipas Angin", 15, 18),
    ("F", "Microwave", 30, 38),
    ("G", "Air Fryer", 20, 26),
    ("H", "Mesin Kopi", 18, 24),
    ("I", "Oven Listrik", 22, 28),
    ("J", "Vacuum Cleaner", 12, 15)
]

capacity = 100
n = len(items)

# Inisialisasi tabel DP
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Proses Dynamic Programming
for i in range(1, n + 1):
    _, _, weight, profit = items[i - 1]
    for w in range(capacity + 1):
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w],
                           profit + dp[i - 1][w - weight])
        else:
            dp[i][w] = dp[i - 1][w]

# Hasil maksimum
max_profit = dp[n][capacity]

# Backtracking untuk item terpilih
selected_items = []
total_weight = 0
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        code, name, weight, profit = items[i - 1]
        selected_items.append((code, name))
        total_weight += weight
        w -= weight

remaining_capacity = capacity - total_weight

# ======================
# OUTPUT SESUAI CONTOH + NAMA ITEM
# ======================
print("=" * 45)
print("HASIL 0/1 KNAPSACK PROBLEM")
print("Studi Kasus : Penjualan Elektronik UMKM")
print("=" * 45)
print(f"Kapasitas gudang maksimum : {capacity}")
print(f"Keuntungan maksimum       : {max_profit} juta rupiah")

print("Item terpilih             :")
for code, name in reversed(selected_items):
    print(f" - {code} : {name}")

print(f"Total kapasitas digunakan : {total_weight}")
print(f"Sisa kapasitas gudang     : {remaining_capacity}")
print("=" * 45)
