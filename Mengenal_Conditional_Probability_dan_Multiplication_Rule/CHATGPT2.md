
## 1) Conditional Probability (Probabilitas Bersyarat)

👉 Artinya: **peluang suatu kejadian kalau kita sudah tahu kejadian lain terjadi.**
Notasi: **P(B|A)** = peluang B terjadi dengan syarat A sudah terjadi.

### 🎒 Studi Kasus: Payung & Hujan

* Misal 30% orang bawa payung (A = bawa payung).
* Kalau hujan, **80%** orang bawa payung (P(A|Hujan) = 0,8).

Pertanyaan: Kalau kamu lihat orang bawa payung, berapa kemungkinan sedang hujan?
Itu yang disebut **conditional probability**: P(Hujan|Bawa Payung).

---

## 2) Independent Events (Tidak Saling Pengaruh)

👉 Dua kejadian **tidak berhubungan**, jadi yang satu **tidak mempengaruhi** yang lain.

### 🎲 Studi Kasus: Lempar Koin & Dadu

* Lempar koin → peluang kepala = 1/2.
* Lempar dadu → peluang keluar 6 = 1/6.
* Hasil koin **tidak mempengaruhi** hasil dadu.

Jadi:

$$
P(Kepala \, \text{dan} \, Enam) = \tfrac{1}{2} \times \tfrac{1}{6} = \tfrac{1}{12}
$$

---

## 3) Dependent Events (Saling Pengaruh)

👉 Dua kejadian **berhubungan**, hasil pertama mempengaruhi hasil kedua.

### 🃏 Studi Kasus: Ambil Kartu Tanpa Dikembalikan

* Dari 52 kartu, peluang ambil As pertama = 4/52.
* Kalau sudah ambil 1 As, tersisa 3 As dari 51 kartu.
* Jadi peluang ambil As kedua jadi **berubah** jadi 3/51.

Artinya peluang kedua **dipengaruhi** oleh hasil pertama.

---

## 4) Multiplication Rule (Aturan Perkalian)

👉 Untuk menghitung peluang **dua kejadian berurutan**.

* Kalau **independent**: P(A ∩ B) = P(A) × P(B).
* Kalau **dependent**: P(A ∩ B) = P(A) × P(B|A).

### 🏀 Studi Kasus: Pemain Basket

* Peluang masuk tembakan pertama = 0,7 (70%).
* Kalau tembakan pertama masuk, peluang masuk tembakan kedua naik jadi 0,8.

Peluang **dua-duanya masuk**:

$$
P = 0{,}7 \times 0{,}8 = 0{,}56
$$

(Artinya 56% kemungkinan dua-duanya masuk).

---

## 🎯 Kesimpulan

* **Conditional Probability** = peluang dengan syarat lain sudah terjadi.
* **Independent Events** = tidak saling pengaruh (contoh: koin & dadu).
* **Dependent Events** = saling pengaruh (contoh: ambil kartu tanpa dikembalikan).
* **Multiplication Rule** = cara hitung peluang dua kejadian berurutan.

---