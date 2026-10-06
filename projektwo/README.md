# Projektwo - Web Content Extractor & Converter

## Deskripsi
Projektwo adalah pipeline untuk mengekstrak konten dari URL website menggunakan Docling, kemudian mengkonversinya ke format Markdown dan JSON.

## Struktur Output

Setiap URL yang di-scrape akan membuat **1 folder terpisah** dengan struktur:

```
output/
├── wikipedia_org_wiki_Albert_Einstein_20261006_090530/
│   ├── json/
│   │   └── content.json
│   └── markdown/
│       └── content.md
├── github_com_openai_20261006_090600/
│   ├── json/
│   │   └── content.json
│   └── markdown/
│       └── content.md
└── ...
```

**Nama folder:** `{domain}_{path}_{timestamp}`
- `domain`: Domain website (contoh: wikipedia_org)
- `path`: Path URL yang di-sanitasi
- `timestamp`: Format YYYYMMDD_HHMMSS

## Cara Menggunakan

### 1. Aktivasi Virtual Environment
```bash
cd "D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek"
.\.venv\Scripts\activate.bat
```

### 2. Jalankan Program
```bash
cd projektwo
python main.py
```

### 3. Input URL
Program akan menanyakan URL satu per satu:
```
Masukkan URL yang ingin di-scrape (ketik 'done' untuk selesai):
------------------------------------------------------------

📌 Masukkan URL (atau 'done' untuk mulai proses): https://example.com
2026-10-06 09:05:30 [INFO] ✅ URL ditambahkan: https://example.com

📌 Masukkan URL (atau 'done' untuk mulai proses): https://example.org
2026-10-06 09:05:35 [INFO] ✅ URL ditambahkan: https://example.org

📌 Masukkan URL (atau 'done' untuk mulai proses): done
```

### 4. Proses Dimulai
Program akan:
- Membuat folder output terpisah untuk setiap URL
- Scrape konten dari URL
- Export ke Markdown dan JSON
- Tampilkan log progress

```
Total URL yang akan diproses: 2

2026-10-06 09:05:40 [INFO] Memulai pemrosesan URL: https://example.com
2026-10-06 09:05:45 [INFO] Berhasil menyimpan Markdown: ...
2026-10-06 09:05:46 [INFO] Berhasil menyimpan JSON: ...
2026-10-06 09:05:46 [INFO] Hasil disimpan di: output/example_com_20261006_090540/
```

## Fitur

✅ **1 URL = 1 Folder** - Struktur output rapi dan terorganisir
✅ **JSON + Markdown** - Setiap URL mendapat kedua format
✅ **Interactive Input** - Input URL secara interaktif
✅ **Error Handling** - Menangani URL invalid dan network error
✅ **Timestamp** - Setiap folder punya timestamp unik
✅ **Logging** - Output log yang jelas dan informatif

## Struktur Kode

```
main.py
├── validate_url()                    # Validasi URL
├── generate_folder_name()            # Generate nama folder berdasarkan URL
├── create_url_output_directories()   # Buat folder output per URL
├── process_url()                     # Process 1 URL (scrape + convert)
├── run_pipeline()                    # Jalankan untuk banyak URL
└── main entry point                  # Interactive input & orchestration
```

## Requirements

- Python 3.10+
- Docling (install via parent venv)

## Troubleshooting

### "ModuleNotFoundError: No module named 'docling'"
Pastikan virtual environment sudah di-activate:
```bash
.\.venv\Scripts\activate.bat
```

### URL tidak bisa di-scrape
Beberapa website mungkin:
- Menolak akses dari scraper (Anti-bot protection)
- Membutuhkan JavaScript rendering
- Memiliki struktur HTML kompleks

Coba URL lain atau cek koneksi internet.

### Folder output tidak terbuat
Pastikan Anda punya write permission di folder `projektwo/`.

---

**Last Updated:** 2026-10-06
