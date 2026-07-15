# Project Mizan Backend Architecture

Version: 1.0

---

# Tujuan

Dokumen ini menjelaskan arsitektur backend Project Mizan sebagai acuan pengembangan selanjutnya.

---

# Teknologi

- Python 3.12
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic

---

# Struktur Folder

Project-Mizan/

backend/
app/

database/
raw/
sqlite/

docs/

---

# Database

Saat ini database terdiri dari dua tabel.

## books

| Field | Tipe |
|--------|------|
| id | Integer |
| name | String |

Satu record untuk setiap kitab hadis.

---

## hadiths

| Field | Tipe |
|--------|------|
| id | Integer |
| book_id | Integer |
| hadith_number | Integer |
| arabic | String |
| translation_id | String |

Relasi:

Book (1)

↓

Hadith (N)

---

# API

GET /

GET /hadiths

GET /hadiths/{id}

GET /hadiths/search

---

# Importer

Importer bersifat idempotent.

Importer akan:

- membuat kitab jika belum ada
- mengecek hadis yang sudah ada
- menghindari duplikasi data

---

# Status

Sprint 14 selesai.

Backend siap menerima seluruh koleksi hadis.