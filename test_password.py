# ==========================================
# FILE: test_jawaban.py
# PERINGATAN: MAHASISWA DILARANG MENGUBAH FILE INI!
# File ini digunakan oleh GitHub Actions Autograder.
# ==========================================

import pytest
from jawaban_mahasiswa import tambah, kurang, kali, bagi

# 1. Test Skenario Penjumlahan
def test_tambah():
    assert tambah(5, 3) == 8, "Gagal: 5 + 3 seharusnya 8"
    assert tambah(-2, 2) == 0, "Gagal: -2 + 2 seharusnya 0"
    assert tambah(0, 0) == 0, "Gagal: 0 + 0 seharusnya 0"

# 2. Test Skenario Pengurangan
def test_kurang():
    assert kurang(10, 4) == 6, "Gagal: 10 - 4 seharusnya 6"
    assert kurang(5, 10) == -5, "Gagal: 5 - 10 seharusnya -5"
    assert kurang(0, 0) == 0, "Gagal: 0 - 0 seharusnya 0"

# 3. Test Skenario Perkalian
def test_kali():
    assert kali(4, 3) == 12, "Gagal: 4 * 3 seharusnya 12"
    assert kali(-5, 2) == -10, "Gagal: -5 * 2 seharusnya -10"
    assert kali(10, 0) == 0, "Gagal: Apapun dikali 0 seharusnya 0"

# 4. Test Skenario Pembagian
def test_bagi():
    assert bagi(10, 2) == 5, "Gagal: 10 / 2 seharusnya 5"
    assert bagi(9, 3) == 3, "Gagal: 9 / 3 seharusnya 3"
    assert bagi(-10, 2) == -5, "Gagal: -10 / 2 seharusnya -5"
