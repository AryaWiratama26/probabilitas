## 🔹 Apa itu Conditional Probability?

Bayangkan kamu punya dua kejadian (event), misalnya:

* **A** = "hari ini hujan"
* **B** = "jalan menjadi basah"

**Conditional Probability** = Probabilitas suatu kejadian terjadi **jika kita sudah tahu** kejadian lain terjadi.

👉 Notasi:
**P(B|A)** artinya “probabilitas jalan basah **dengan syarat** sudah hujan”.

Kalau hujan, kemungkinan jalan basah jadi lebih besar.

---

## 🔹 Independent Events (Kejadian yang Tidak Saling Pengaruh)

Dua kejadian **independent** kalau salah satunya **tidak mempengaruhi** yang lain.

Contoh:

* Melempar koin pertama → hasilnya **tidak mempengaruhi** koin kedua.
* Jadi: **P(B|A) = P(B)**

👉 Artinya, meskipun kita tahu hasil A, peluang B tetap sama.

---

## 🔹 Dependent Events (Kejadian yang Saling Pengaruh)

Dua kejadian **dependent** kalau hasil dari yang satu **mempengaruhi** kejadian yang lain.

Contoh:

* Mengambil kartu dari 52 kartu TANPA dikembalikan.
* Kalau kartu pertama sudah diambil, kartu kedua jadi dipengaruhi (jumlah kartu berkurang).

Jadi: **P(B|A) ≠ P(B)**

---

## 🔹 The Multiplication Rule (Aturan Perkalian)

Kalau kita mau tahu peluang **dua kejadian terjadi berurutan**, kita pakai rumus perkalian.

👉 Rumus umum:
**P(A dan B) = P(A) × P(B|A)**

Artinya: peluang A terjadi, dikali peluang B terjadi **setelah A terjadi**.

Kalau A dan B independent → rumusnya lebih mudah:
**P(A dan B) = P(A) × P(B)**

---

## 🔹 Contoh Sederhana

1. **Independent:**
   Melempar dua koin.

   * P(koin 1 = kepala) = 1/2
   * P(koin 2 = kepala) = 1/2
     Jadi: P(keduanya kepala) = 1/2 × 1/2 = 1/4

2. **Dependent:**
   Mengambil 2 kartu dari 52 kartu tanpa dikembalikan.

   * P(kartu pertama As) = 4/52
   * P(kartu kedua As, setelah 1 As sudah diambil) = 3/51
     Jadi: P(keduanya As) = (4/52) × (3/51)

---

👉 Jadi intinya:

* **Conditional Probability** = peluang B kalau kita sudah tahu A terjadi.
* **Independent** = tidak saling pengaruh.
* **Dependent** = saling pengaruh.
* **Multiplication Rule** = dipakai buat menghitung peluang dua kejadian berurutan.

---
