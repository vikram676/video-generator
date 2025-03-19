import requests

def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.json().get("text")
        return fact
    else:
        print("Failed to fetch fact:", response.status_code)
        return None

if __name__ == "__main__":
    fact = get_fact()
    if fact:
        print(f"Fact: {fact}")