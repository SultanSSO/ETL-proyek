# Unified Workspace Setup - Docling Projects

## Struktur Folder

```
projek/                          # Main workspace folder (C:\Users\Sultan\...\Docling\projek\)
│
├── .venv/                       # SHARED Virtual Environment (digunakan oleh kedua project)
│   ├── Scripts/
│   ├── Lib/
│   ├── Include/
│   └── pyvenv.cfg
│
├── requirements.txt             # Centralized dependency list
│   └── docling
│
├── projekone/                   # Sub-project 1 - Document to JSON Converter
│   ├── main.py                  # Konversi PDF ke JSON
│   ├── README.md
│   ├── PRD_pipeline.md
│   ├── dataset/                 # Input folder untuk PDF files
│   ├── output/                  # Output folder untuk hasil JSON
│   └── .venv/                   # (Old - tidak digunakan lagi)
│
└── projektwo/                   # Sub-project 2 - Web Scraper to Markdown/JSON
    ├── main.py                  # Web scraping dan konversi
    ├── README.md
    ├── PRD_pipeline.md
    ├── output/                  # Output folder (json/ dan markdown/)
    └── .venv/                   # (Old - tidak digunakan lagi)
```

## Cara Menggunakan

### 1. Activate Shared Virtual Environment
```bash
cd "D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek"
.\.venv\Scripts\activate.bat
```

Prompt akan berubah menjadi:
```
(.venv) D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek>
```

### 2. Jalankan Project One (Document Converter)
```bash
cd projekone
python main.py
```

**Output:** File JSON akan disimpan di `projekone/output/`

### 3. Jalankan Project Two (Web Scraper)
```bash
cd ..\projektwo
python main.py
```

**Output:** File Markdown dan JSON akan disimpan di `projektwo/output/json/` dan `projektwo/output/markdown/`

### 4. Deactivate Virtual Environment (setelah selesai)
```bash
deactivate
```

## Keuntungan Unified Workspace

✅ **Hemat Storage** - Virtual environment hanya 1 copy (~3GB), bukan 2
✅ **Centralized Dependency Management** - requirements.txt di root folder
✅ **Konsisten** - Kedua project menggunakan versi docling dan dependency yang sama
✅ **Professional Structure** - Sesuai best practice Python project organization
✅ **Mudah Maintain** - Jika ada update dependency, update di 1 tempat saja

## Quick Start (One-liner)

```bash
cd "D:\SULTAN NAUFAL\KULIAH\PUSAT PEMBELAJARAN\Docling\projek" && .\.venv\Scripts\activate.bat && cd projektwo && python main.py
```

## Notes

- Folder `.venv` lama di dalam `projekone/` dan `projektwo/` tidak digunakan lagi
- Semua dependencies terinstall di `.venv/` utama
- Pastikan path folder sudah benar sebelum menjalankan command

---

**Setup Date:** 2026-10-06  
**Status:** ✅ Ready to use
