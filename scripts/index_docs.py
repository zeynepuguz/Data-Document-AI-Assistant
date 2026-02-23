import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

DOCS_DIR = Path("documents")

def upload_file(path: Path) -> str:
    with path.open("rb") as f:
        file_obj = client.files.create(file=f, purpose="assistants")
    return file_obj.id

def main():
    if not DOCS_DIR.exists():
        raise SystemExit("documents/ klasörü yok. Önce documents/ oluştur ve PDF'leri içine koy.")

    paths = [p for p in DOCS_DIR.glob("*") if p.is_file()]
    if not paths:
        raise SystemExit("documents/ boş. İçine en az 1 PDF/DOCX koy.")

    file_ids = []
    for p in paths:
        fid = upload_file(p)
        print(f"Uploaded: {p.name} -> {fid}")
        file_ids.append(fid)

    vs = client.vector_stores.create(name="knowledge_base")
    print("Vector store:", vs.id)

    for fid in file_ids:
        client.vector_stores.files.create(vector_store_id=vs.id, file_id=fid)

    print("\nIndexing başlatıldı. Durumu kontrol etmek için:")
    print(f"  python scripts/check_status.py {vs.id}")
    print("\nHazır olunca soru sormak için:")
    print(f"  python scripts/ask.py {vs.id} \"Soru...\"")

if __name__ == "__main__":
    main()