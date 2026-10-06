import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from docling.document_converter import DocumentConverter

# ----------------------------------------------------------------------
# Konfigurasi Logging
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# Helper Functions & Utilities
# ----------------------------------------------------------------------
def validate_url(url: str) -> bool:
    """Memeriksa validitas sintaks URL."""
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except Exception:
        return False


def generate_folder_name(url: str) -> str:
    """
    Menghasilkan nama folder aman berdasarkan domain/path URL dan timestamp.
    Contoh: 'example_com_article_20261006_080000'
    """
    parsed = urlparse(url)
    raw_slug = f"{parsed.netloc}{parsed.path}"
    # Sanitasi karakter non-alphanumeric
    sanitized_slug = re.sub(r"[^\w\-_]", "_", raw_slug).strip("_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{sanitized_slug[:50]}_{timestamp}"


def create_url_output_directories(url: str, base_dir: Path = Path("output")) -> tuple[Path, Path]:
    """
    Membuat direktori terpisah untuk setiap URL dengan subfolder json/ dan markdown/.
    
    Struktur:
    output/
    ├── example_com_20261006_080000/
    │   ├── json/
    │   └── markdown/
    """
    folder_name = generate_folder_name(url)
    url_dir = base_dir / folder_name
    
    json_dir = url_dir / "json"
    markdown_dir = url_dir / "markdown"
    
    json_dir.mkdir(parents=True, exist_ok=True)
    markdown_dir.mkdir(parents=True, exist_ok=True)
    
    return json_dir, markdown_dir


# ----------------------------------------------------------------------
# Core Processing Logic
# ----------------------------------------------------------------------
def process_url(url: str) -> bool:
    """
    Mengekstrak konten URL menggunakan Docling dan menyimpan hasil ke JSON & Markdown
    dalam folder terpisah untuk setiap URL.
    """
    if not validate_url(url):
        logger.error(f"URL tidak valid: '{url}'")
        return False

    logger.info(f"Memulai pemrosesan URL: {url}")
    
    # Buat direktori terpisah untuk URL ini
    json_dir, markdown_dir = create_url_output_directories(url)
    folder_name = json_dir.parent.name
    
    try:
        # Inisialisasi dan konversi menggunakan Docling
        converter = DocumentConverter()
        result = converter.convert(url)
        doc = result.document

        # Gunakan nama file yang sederhana (tanpa timestamp, karena folder sudah punya)
        filename_base = "content"

        # 1. Export ke Markdown
        md_content = doc.export_to_markdown()
        md_file_path = markdown_dir / f"{filename_base}.md"
        md_file_path.write_text(md_content, encoding="utf-8")
        logger.info(f"Berhasil menyimpan Markdown: {md_file_path}")

        # 2. Export ke JSON
        json_content = doc.export_to_dict()
        json_file_path = json_dir / f"{filename_base}.json"
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(json_content, f, ensure_ascii=False, indent=2)
        logger.info(f"Berhasil menyimpan JSON: {json_file_path}")
        
        logger.info(f"Hasil disimpan di: output/{folder_name}/")

        return True

    except Exception as e:
        logger.error(f"Gagal memproses URL '{url}': {e}", exc_info=True)
        return False


def run_pipeline(urls: list[str]) -> None:
    """
    Menjalankan seluruh alur eksekusi pipeline untuk daftar URL.
    Setiap URL akan diproses ke folder terpisah.
    """
    logger.info(f"Memulai pipeline untuk {len(urls)} target URL.")
    
    for url in urls:
        success = process_url(url)
        if success:
            logger.info(f"Selesai memproses: {url}\n")
        else:
            logger.warning(f"Proses gagal untuk: {url}\n")


# ----------------------------------------------------------------------
# Entry Point - Interactive Input
# ----------------------------------------------------------------------
if __name__ == "__main__":
    logger.info("=== Web Content Extractor & Converter Pipeline ===\n")
    
    target_urls = []
    
    print("Masukkan URL yang ingin di-scrape (ketik 'done' untuk selesai):")
    print("-" * 60)
    
    while True:
        user_input = input("\n📌 Masukkan URL (atau 'done' untuk mulai proses): ").strip()
        
        if user_input.lower() == "done":
            if not target_urls:
                logger.warning("Tidak ada URL yang diinputkan. Program dihentikan.")
                sys.exit(0)
            break
        
        if user_input:
            if validate_url(user_input):
                target_urls.append(user_input)
                logger.info(f"✅ URL ditambahkan: {user_input}")
            else:
                logger.error(f"❌ URL tidak valid: {user_input}")
        else:
            logger.warning("⚠️  Input kosong, coba lagi.")
    
    print("\n" + "=" * 60)
    logger.info(f"Total URL yang akan diproses: {len(target_urls)}\n")
    
    run_pipeline(target_urls)
    
    logger.info("\n=== Pipeline Selesai ===")
    print("✅ Semua proses selesai! Cek folder 'output/' untuk hasil.")