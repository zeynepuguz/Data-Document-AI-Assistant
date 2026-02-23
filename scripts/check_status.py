from dotenv import load_dotenv
load_dotenv()

import sys
from openai import OpenAI

client = OpenAI()

def main():
    if len(sys.argv) < 2:
        raise SystemExit("Kullanım: python scripts/check_status.py <vector_store_id>")

    vs_id = sys.argv[1]
    result = client.vector_stores.files.list(vector_store_id=vs_id)
    print(result)

if __name__ == "__main__":
    main()