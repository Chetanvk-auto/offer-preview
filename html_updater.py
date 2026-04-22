import re
import time
import subprocess

HTML_FILE = "followup.html"
BASE_URL = "https://offer-preview.vercel.app/followup.html"


def update_html(image_url):
    version = int(time.time())

    new_image = f"{image_url}?v={version}"
    new_url = f"{BASE_URL}?v={version}"

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace OG image
    content = re.sub(
        r'<meta property="og:image".*?>',
        f'<meta property="og:image" content="{new_image}">',
        content
    )

    # Replace OG URL
    content = re.sub(
        r'<meta property="og:url".*?>',
        f'<meta property="og:url" content="{new_url}">',
        content
    )

    # Replace IMG tag
    content = re.sub(
        r'<img src=".*?"',
        f'<img src="{new_image}"',
        content
    )

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ HTML Updated")

    auto_push()

    return new_url


def auto_push():
    try:
        subprocess.run("git add .", shell=True)
        subprocess.run('git commit -m "auto image update"', shell=True)
        subprocess.run("git push", shell=True)
        print("🚀 Pushed to GitHub (Vercel auto deploy)")
    except Exception as e:
        print("❌ Push failed:", e)