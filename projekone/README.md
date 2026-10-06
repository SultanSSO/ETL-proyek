# 📂 Projekone - PDF to JSON Converter

Proyek ini adalah bagian dari **unified workspace** yang mengkonversi file PDF menjadi JSON menggunakan library Docling.

---

## 1. Pohon Struktur Workspace

```text
projek/                               # Root workspace (shared venv)
│
├── .venv/                            # SHARED Virtual Environment Python
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── requirements.txt                  # Centralized Dependencies
│
├── projekone/                        # Project ini
│   │
│   ├── main.py                       # Core Pipeline Execution Script
│   ├── PRD_pipeline.md               # Product Requirements Document
│   ├── README.md                     # Dokumentasi & Panduan
│   │
│   ├── dataset/                      # Sumber Data Masukan (File PDF)
│   │   ├── PAMJ_Unit1_Sultan...pdf
│   │   ├── PAMJ_Unit3_Sultan...pdf
│   │   └── ...
│   │
│   └── output/                       # Artefak Hasil Ekstraksi (File JSON)
│       ├── PAMJ_Unit1_Sultan...json
│       ├── PAMJ_Unit3_Sultan...json
│       └── ...
│
└── projektwo/                        # Project lainnya (Web Scraper)
```

---

## 2. Deskripsi Komponen

### 2.1 `.venv/` - Virtual Environment (Shared)
Virtual environment yang di-share dengan `projektwo`. Semua dependencies (termasuk `docling`) terinstall di sini.

### 2.2 `dataset/` - Input Directory
Folder untuk menempatkan file PDF yang akan dikonversi. Program secara otomatis akan:
- Memindai semua file `.pdf` di folder ini
- Mendukung file dengan berbagai format (`.pdf`, `.docx`, `.pptx`, `.html`)

### 2.3 `output/` - Output Directory
Folder tempat hasil konversi JSON disimpan. Struktur:
- Satu PDF → Satu JSON file
- Nama file output: `{nama_file_asli}.json`
- Encoding: UTF-8 dengan indentasi 2 spasi

### 2.4 `main.py` - Pipeline Script
Skrip utama yang:
1. Memindai folder `dataset/`
2. Mengekstrak setiap PDF menggunakan Docling
3. Menyimpan hasil ke folder `output/`

---

## 3. Cara Menggunakan

### Step 1: Persiapkan File PDF
1. Letakkan file PDF di folder `dataset/`
2. Contoh:
   ```
   dataset/
   ├── PAMJ_Unit1_Sultan.pdf
   ├── PAMJ_Unit3_Sultan.pdf
   └── PAMJ_Unit5_Sultan.pdf
   ```

### Step 2: Aktivasi Virtual Environment
```bash
cd "D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek"
.\.venv\Scripts\activate.bat
```

Prompt akan berubah menjadi:
```
(.venv) D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek>
```

### Step 3: Navigasi ke Projekone
```bash
cd projekone
```

### Step 4: Jalankan Pipeline
```bash
python main.py
```

### Step 5: Lihat Output
File JSON akan tersimpan di folder `output/`:
```
output/
├── PAMJ_Unit1_Sultan.json
├── PAMJ_Unit3_Sultan.json
└── PAMJ_Unit5_Sultan.json
```

---

## 4. Quick Start (One-liner untuk Windows)

```bash
cd "D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek" && .\.venv\Scripts\activate.bat && cd projekone && python main.py
```

---

## 5. Fitur & Capabilities

✅ **Batch Processing** - Proses banyak PDF sekaligus
✅ **Auto Directory Creation** - Folder output dibuat otomatis jika belum ada
✅ **Error Handling** - Kegagalan satu file tidak menghentikan proses file lain
✅ **Detailed Logging** - Output log yang jelas untuk setiap file
✅ **UTF-8 Encoding** - Mendukung karakter non-Latin
✅ **Structured JSON** - Output JSON dengan format rapi dan terstruktur

---

## 6. Supported File Formats

Docling mendukung format berikut:
- ✅ PDF (`.pdf`)
- ✅ Word Documents (`.docx`)
- ✅ PowerPoint (`.pptx`)
- ✅ HTML (`.html`)

---

## 7. Struktur JSON Output

Setiap file PDF dikonversi menjadi JSON dengan struktur hierarki yang mencakup:
- Document metadata (judul, penulis, tanggal)
- Content (paragraf, heading, list, table)
- Layout information (posisi, ukuran teks)
- Table data (structured table information)

Contoh:
```json
{
  "kind": "document",
  "path_id": "/",
  "content": [
    {
      "kind": "heading",
      "level": 1,
      "content": "Chapter 1: Introduction"
    },
    {
      "kind": "paragraph",
      "content": "Lorem ipsum dolor sit amet..."
    }
  ]
}
```

---

## 8. Troubleshooting

### Error: "ModuleNotFoundError: No module named 'docling'"
**Solusi:** Pastikan virtual environment sudah di-activate:
```bash
.\.venv\Scripts\activate.bat
```

### Error: "FileNotFoundError: [Errno 2] No such file or directory: 'dataset'"
**Solusi:** Pastikan folder `dataset/` sudah ada dan berisi file PDF.

### Error: "Gagal memproses {filename}"
**Solusi:** 
- Cek apakah file PDF valid dan tidak corrupt
- Coba buka file dengan PDF reader biasa
- Cek permission folder

### Pipeline berjalan lambat
**Catatan:** Kecepatan tergantung pada:
- Ukuran file PDF (file besar = lebih lambat)
- Kompleksitas layout dokumen
- Spesifikasi hardware

---

## 9. Log Output Example

```
2026-10-06 - INFO - Memproses file: PAMJ_Unit1_Sultan.pdf
2026-10-06 - INFO - Berhasil disimpan ke: output/PAMJ_Unit1_Sultan.json
2026-10-06 - INFO - Memproses file: PAMJ_Unit3_Sultan.pdf
2026-10-06 - INFO - Berhasil disimpan ke: output/PAMJ_Unit3_Sultan.json
2026-10-06 - INFO - Semua pemrosesan dokumen selesai.
```

---

## 10. Integration dengan Workspace

Projekone adalah bagian dari workspace yang lebih besar:
- **Virtual Environment**: Shared dengan `projektwo`
- **Dependencies**: Semua terinstall di `projek/.venv/`
- **Workflow**: Bisa menjalankan multiple projects tanpa perlu setup ulang

Untuk menggunakan project lain (projektwo), cukup:
```bash
# Dari folder projek (venv sudah active)
cd ..\projektwo
python main.py
```

---

**Last Updated:** 2026-10-06  
**Status:** ✅ Production Ready
