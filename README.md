
# Pertemuan 13 - Debugging dan Testing

Repository ini berisi tugas Praktik 4 mata kuliah Algoritma dan Pemrograman tentang debugging, tracing, testing, dan test case menggunakan Python.

## Identitas Mahasiswa

- **Nama:** Aulia Nurrizqi
- **NIM:** 2225250160
- **Kelas:** 3A
- **Program Studi:** S1 Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan Praktik

1. Mengidentifikasi bug pada program Python.
2. Melakukan tracing untuk memahami alur program.
3. Membuat dan menjalankan test case.
4. Memperbaiki bug berdasarkan hasil pengujian.
5. Melakukan pengujian ulang setelah perbaikan.
6. Mendokumentasikan proses debugging melalui Git dan GitHub.

## Struktur Folder

```text
pertemuan-13-debugging-NIM/
├── README.md
├── .gitignore
├── kasus/
│   └── program_awal_bermasalah.py
└── praktik/
    └── praktik_4_debugging.py
```

## Studi Kasus

Program mengolah data nilai mahasiswa dengan tiga fungsi utama:

- `hitung_rata_rata()` untuk menghitung rata-rata nilai.
- `status()` untuk menentukan status kelulusan.
- `nilai_tertinggi()` untuk mencari nilai tertinggi.

Program awal memiliki tiga bug logika yang perlu diidentifikasi dan diperbaiki.

## Test Case

| ID | Input | Hasil |
|---|---|---|
| T1 | `[80, 60, 90, 70]` | Rata-rata 75.0 |
| T2 | `[100, 80]` | Rata-rata 90.0 |
| T3 | Nilai 60 | Lulus |
| T4 | Nilai 59 | Tidak lulus |
| T5 | `[80, 60, 90, 70]` | Nilai tertinggi 90 |
| T6 | List kosong untuk rata-rata | 0 |
| T7 | List kosong untuk nilai tertinggi | None |

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang.

Jalankan program awal untuk mengamati bug:

```bash
python kasus/program_awal_bermasalah.py
```

Jalankan program setelah perbaikan dan pengujian:

```bash
python praktik/praktik_4_debugging.py
```

## Bug Report

### B01 - Perhitungan Rata-rata

- **Penyebab:** Pembagi selalu menggunakan angka 5.
- **Perbaikan:** Menggunakan jumlah data dengan `len(nilai)`.
- **Pengujian:** T1, T2, dan T6.

### B02 - Status Kelulusan

- **Penyebab:** Operator `>` membuat nilai 60 tidak dinyatakan lulus.
- **Perbaikan:** Menggunakan operator `>=`.
- **Pengujian:** T3 dan T4.

### B03 - Nilai Tertinggi

- **Penyebab:** Kondisi perbandingan menggunakan operator yang terbalik.
- **Perbaikan:** Membandingkan nilai dengan operator `>`.
- **Pengujian:** T5 dan T7.

## Hasil Retest

Setelah perbaikan, jalankan kembali seluruh test case.

Program dinyatakan berhasil apabila seluruh test menghasilkan status `PASS`.

## Kesimpulan

Debugging membantu menemukan dan memperbaiki penyebab kesalahan program. Test case digunakan untuk membandingkan hasil aktual dengan hasil yang diharapkan. Pengujian ulang dilakukan untuk memastikan perbaikan bekerja dengan benar dan tidak menimbulkan kesalahan baru.

## Riwayat Git

Perubahan program didokumentasikan melalui commit, misalnya:

- `chore: menambahkan kasus debugging awal`
- `test: menambahkan test case dan bug report`
- `fix: memperbaiki bug program`
- `docs: menambahkan hasil retest dan refleksi`
