
"""
Praktik 4 - Debugging dan Testing
Pertemuan 13
"""

def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


def jalankan_test():
    test_cases = [
        ("T1 - Rata-rata 4 nilai",
         hitung_rata_rata, ([80, 60, 90, 70],), 75.0),

        ("T2 - Rata-rata 2 nilai",
         hitung_rata_rata, ([100, 80],), 90.0),

        ("T3 - Nilai batas kelulusan",
         status, (60,), "Lulus"),

        ("T4 - Nilai di bawah batas",
         status, (59,), "Tidak lulus"),

        ("T5 - Nilai tertinggi",
         nilai_tertinggi, ([80, 60, 90, 70],), 90),

        ("T6 - Rata-rata list kosong",
         hitung_rata_rata, ([],), 0),

        ("T7 - Nilai tertinggi list kosong",
         nilai_tertinggi, ([],), None),
    ]

    semua_lulus = True

    print("=== HASIL PENGUJIAN ===")

    for nama, fungsi, argumen, expected in test_cases:
        actual = fungsi(*argumen)
        lulus = actual == expected

        if not lulus:
            semua_lulus = False

        print(f"\n{nama}")
        print(f"Expected : {expected}")
        print(f"Actual   : {actual}")
        print(f"Status   : {'PASS' if lulus else 'FAIL'}")

    if semua_lulus:
        print("\nKesimpulan: Semua test PASS.")
    else:
        print("\nKesimpulan: Masih ada test FAIL.")


if __name__ == "__main__":
    nilai = [80, 60, 90, 70]

    print("=== HASIL PROGRAM ===")
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(nilai))

    jalankan_test()
