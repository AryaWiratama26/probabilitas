# Pengenalan Probablitas

## Apa itu Probability?

**Probability** adalah pengukuran terhadap suatu kemungkinan atau peluang.

Pemahaman terkait probability merupakan dasar untuk melangkah ke Statistika Inferensi (Inferential Statistics)

## Terminologi

- Hasil dari suatu percobaan (trial) dikenal sebagai **outcome**.
- Himpunan dari seluruh kemungkinan outcome pada suatu probability experiment dikenal dengan **sample space**.
- Bagian dari sample space dikenal sebagai **event**.
- Event terdiri dari satu atau lebih **outcomes**.

## Probability Experiments

**Probability Experiments** adalah aksi atau percobaan (trial) yang menghasilkan suatu perhitungan, pengukuran, atau respon (counts, measurements, or response).

![Contoh Probablity Eksperiment](/img/prob-ex-example.png)

## Tree Diagram

**Tree Diagram** digunakan untuk memberikan gambaran secara visual terkait setiap outcome dari suatu probability experiment.

![Contoh Tree Diagram](/img/tree-diagram-ex.png)

## Event

- Event umumnya direpresentasikan dengan **huruf kapital** (uppercase letters), seperti A, B, C.
- Suatu event yang didiri dari suatu outcome dikenal dengan **simple event**.

## Event: Contoh

- Event melempar sebuah koin dan dadu enam sisi serta mendapatkan head dan 3 merupakan event dan bisa direpresentasikan sebagai A = {H3}.
- Sedangkan event melempar sebuah koin dan dadu enam sisi serta mendapatkan head dan bilangan genap bukan merupakan simple event karena memiliki 3 kemungkinan outcomes; event ini bisa direpresentasikan sebagai B = {H2, H4, H6}.

## Fundamental Counting Principle

- Pemanfaatan Tree Diagram untuk menghitung banyaknya outcome dari sejumlah event tidaklah praktis.
- Sebagai alternatif, kita bisa memanfaatkan **Fundamental Counting Principle** untuk mengetahui jumlah kemungkinan outcomes dari dua atau lebih event yang muncul serta secara berurutan.

![FCP contoh](/img/fop-ex.png)

## Types of Probability

- Probability dapat dituliskan dalam format pecahan, desimal dan presentase.
- Probability untuk kemunculan event E dapat dituliskan sebagai P(E)

Terdapat 3 tipe probability:

- Classical (theoritical) Probability
- Empirical (statistical) Probability
- Subjective Probability

## Classical Probability

**Classical Probability** digunakan ketika setiap outcome pada sample space memiliki peluang yang sama untuk muncul.

$P(E) = \frac{\text{Number of outcomes in event E}}{\text{Total Number of outcomes in sample space}}$

![CS Example](/img/classical-prob-example.png)

## Empirical Probability

**Empirical Probability** didasarkan pada **observasi** dan **probability experiments**.

$P(E) = \frac{\text{Frequency of Event E}}{\text{Total Frequency}}$

![EP Example](/img/EP-example.png)

## Law of Large Number

Ketika suatu probability experiment dilakukan secara berulang-ulang, maka empirical probability yang dihasilkan akan mendekati nilai theoritical probability dari event terkait.

![LLM Simulator](/img/LLM-simulator.png)

## Subjective Probability

**Subjective Probability** didasarkan pada **intuisi**, **educated guesses**, dan **estimasi**.

Contoh:

- Seseorang dokter memberikan estimasi keberhasilan dari proses operasi yang ditanganinya sebesar 90%
- Seseorang mahasiswa merasa yakin bahwa peluang untuk lulus di matakuliah statistika adalah 70%.

## Range of Probability

![Range of Probability](/img/range-of-probability.png)

## Complementary Event

![CE](/img/compmentary-event.png)

![CE Event](/img/CE-example.png)

## Complementary Event: Contoh

![CE Example](/img/CE-example-data.png)

