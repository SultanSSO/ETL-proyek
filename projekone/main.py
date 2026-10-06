import json
import logging
from pathlib import Path
from docling.document_converter import DocumentConverter

# Konfigurasi logging untuk pemantauan proses
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Definisi Direktori
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
OUTPUT_DIR = BASE_DIR / "output"

# Ekstensi dokumen yang didukung
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".pptx", ".html"}


def setup_directories() -> None:
    """Memastikan direktori output tersedia."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def process_document(converter: DocumentConverter, file_path: Path) -> None:
    """Konversi satu dokumen ke JSON dan simpan ke folder output.
    
    :param converter: Instance DocumentConverter
    :param file_path: Path file dokumen yang akan diproses
    """
    logging.info(f"Memproses file: {file_path.name}")
    try:
        # Melakukan konversi dokumen
        result = converter.convert(file_path)
        
        # Mengubah hasil konversi menjadi dictionary / JSON format
        doc_dict = result.document.export_to_dict()
        
        # Menentukan path output dengan ekstensi .json
        output_file_path = OUTPUT_DIR / f"{file_path.stem}.json"
        
        # Menyimpan hasil ke file JSON
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(doc_dict, f, ensure_ascii=False, indent=2)
            
        logging.info(f"Berhasil disimpan ke: {output_file_path.relative_to(BASE_DIR)}")

    except Exception as e:
        logging.error(f"Gagal memproses {file_path.name}: {e}")


def main() -> None:
    """Fungsi utama untuk menjalankan pipeline pemrosesan dataset."""
    setup_directories()

    if not DATASET_DIR.exists():
        logging.error(f"Folder dataset tidak ditemukan di: {DATASET_DIR}")
        return

    # Inisialisasi converter docling
    converter = DocumentConverter()

    # Ambil semua file dokumen pendukung dari direktori dataset
    files_to_process = [
        file for file in DATASET_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not files_to_process:
        logging.warning("Tidak ditemukan file dokumen yang valid di folder dataset.")
        return

    logging.info(f"Ditemukan {len(files_to_process)} file untuk diproses.")

    # Iterasi dan proses setiap file
    for file_path in files_to_process:
        process_document(converter, file_path)

    logging.info("Semua pemrosesan dokumen selesai.")


if __name__ == "__main__":
    main()