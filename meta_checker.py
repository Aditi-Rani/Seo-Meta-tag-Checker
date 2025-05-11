import requests
from bs4 import BeautifulSoup

def check_meta_tags(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else ""
        description_tag = soup.find("meta", attrs={"name": "description"})
        keywords_tag = soup.find("meta", attrs={"name": "keywords"})

        description = description_tag["content"].strip() if description_tag else ""
        keywords = keywords_tag["content"].strip() if keywords_tag else ""

        print(f"\n🔍 URL: {url}")

        # Title
        if title:
            print(f"📌 Title: {title}")
            title_len = len(title)
            print(f"📏 Title Length: {title_len} characters")
            if title_len < 50:
                print("⚠️ Recommendation: Title is too short. Aim for 50–65 characters.")
            elif title_len > 65:
                print("⚠️ Recommendation: Title is too long. It may get truncated in search results.")
            else:
                print("✅ Title length is optimal.")
        else:
            print("❌ No title tag found. Add a title between 50–65 characters.")

        #Description
        if description:
            print(f"\n📝 Meta Description: {description}")
            desc_len = len(description)
            print(f"📏 Description Length: {desc_len} characters")
            if desc_len < 100:
                print("⚠️ Recommendation: Description is too short. Aim for around 155 characters.")
            elif desc_len > 160:
                print("⚠️ Recommendation: Description is too long and may be truncated.")
            else:
                print("✅ Description length is optimal.")
        else:
            print("❌ No meta description found. Add one around 155 characters.")

        # Keywords
        print(f"\n🔑 Meta Keywords: {keywords if keywords else 'No meta keywords'}")
        if not keywords:
            print("ℹ️ Recommendation: Although not critical for SEO anymore, adding relevant keywords can help organize content.")

    except Exception as e:
        print(f"\n❌ Error fetching or parsing {url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL (include https://): ").strip()
    check_meta_tags(url)
