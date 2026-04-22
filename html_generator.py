import time
import os

# 🔥 CHANGE THIS to your GitHub repo link
BASE_URL = "https://chetanvk-auto.github.io/offer-preview/"

# 📄 HTML Template
TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{image}">
  <meta property="og:url" content="{url}">
  <meta property="og:type" content="website">

  <title>Offer</title>

  <style>
    body {{
      font-family: Arial;
      background-color: #f5f5f5;
      margin: 0;
      padding: 20px;
      text-align: center;
    }}

    .container {{
      background: white;
      padding: 20px;
      border-radius: 12px;
      max-width: 500px;
      margin: auto;
      box-shadow: 0 0 12px rgba(0,0,0,0.1);
    }}

    img {{
      width: 100%;
      border-radius: 10px;
      margin-top: 15px;
    }}

    .btn {{
      display: block;
      margin: 15px 0;
      padding: 12px;
      text-decoration: none;
      color: white;
      border-radius: 8px;
      font-size: 16px;
      font-weight: bold;
    }}

    .call {{
      background-color: #28a745;
    }}

    .whatsapp {{
      background-color: #25D366;
    }}
  </style>
</head>

<body>

<div class="container">

  <h2>{title}</h2>
  <p>{desc}</p>

  <img src="{image}" />

  <a class="btn call" href="tel:9703354487">📞 Call Now</a>

  <a class="btn whatsapp" href="https://wa.me/919703354487?text=Hi%20I%20am%20interested%20in%20your%20offer">
    💬 Chat on WhatsApp
  </a>

</div>

</body>
</html>
"""


# 🔥 MAIN FUNCTION
def create_html(title, desc, image_url):
    # Unique filename (prevents WhatsApp cache)
    filename = f"offer_{int(time.time())}.html"

    # Full URL (for preview)
    full_url = BASE_URL + filename

    # Generate HTML
    html_content = TEMPLATE.format(
        title=title,
        desc=desc,
        image=image_url,
        url=full_url
    )

    # Save inside your project folder
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("\n✅ HTML Created Successfully")
    print("📄 File:", filename)
    print("🔗 Link:", full_url)

    return filename, full_url


# 🔥 TEST RUN
if __name__ == "__main__":
    print("=== Generate Offer Page ===")

    title = input("Enter title: ")
    desc = input("Enter description: ")
    image = input("Enter image URL (Cloudinary): ")

    create_html(title, desc, image)