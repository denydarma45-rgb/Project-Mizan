# Project Mizan
## Database Blueprint (Versi 1)

### Tujuan

Database Project Mizan dirancang sebagai sumber data utama untuk seluruh fitur aplikasi.

Prinsip utama:

- Tidak bergantung pada API pihak ketiga.
- Data berada di bawah kendali Project Mizan.
- Mudah dikembangkan.
- Mudah diperbarui.
- Mendukung pencarian cepat.

---

## Informasi yang disimpan pada setiap hadis

- ID
- Nama kitab
- Nama bab
- Nomor hadis
- Teks Arab
- Terjemahan Indonesia
- Nama perawi
- Derajat hadis
- Sumber penilaian derajat
- Kata kunci
- Penjelasan ringkas
- Referensi syarah

---

## Tujuan database

Database harus mampu mendukung pencarian berdasarkan:

- kata kunci
- tema
- penggalan hadis
- nomor hadis
- nama kitab
- nama perawi

Database juga harus dapat berkembang untuk mendukung fitur-fitur baru di masa depan tanpa mengubah struktur dasar.