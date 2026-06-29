import requests

url = "https://basvuru.cankaya.bel.tr/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html",
    "Accept-Language": "tr-TR,tr;q=0.9"
}

try:
    r = requests.get(url, headers=headers, timeout=30)

    print("Status:", r.status_code)
    print("Length:", len(r.text))
    print(r.text[:500])

except Exception as e:
    print(e)
    raise
