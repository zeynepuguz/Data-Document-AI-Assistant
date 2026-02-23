import sys
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI()


def main():
    if len(sys.argv) < 3:
        raise SystemExit('Kullanım: python scripts/ask.py <vector_store_id> "Soru"')

    vs_id = sys.argv[1]
    question = sys.argv[2]

    input_text = f"""
Sadece sağlanan dokümanlardan yararlanarak cevap ver.
Eğer cevap dokümanlarda yoksa aynen şu cümleyi yaz:
"Bu bilgi dokümanlarda bulunmuyor."

Soru: {question}
""".strip()

    resp = client.responses.create(
        model="gpt-4o",
        input=input_text,
        tools=[
            {
                "type": "file_search",
                "vector_store_ids": [vs_id],
            }
        ],
        include=["file_search_call.results"],
    )

    print(resp.output_text)

    print("\n--- Kaynaklar ---")
    found_any = False

    for item in getattr(resp, "output", []) or []:
        if getattr(item, "type", None) != "file_search_call":
            continue

        results = getattr(item, "results", None)
        if not results:
            continue

        for r in results:
            found_any = True
            file_id = getattr(r, "file_id", None)
            if file_id:
                print(f"- file_id: {file_id}")
            else:
                print("- file_id: (bilinmiyor)")

    if not found_any:
        print("Kaynak bulunamadı (dokümanlardan sonuç gelmedi).")


if __name__ == "__main__":
    main()