import tkinter as tk
from tkinter import filedialog
import threading
import time

from whatsapp_sender import WhatsAppSender
from html_updater import update_html

import cloudinary
import cloudinary.uploader

# 🔥 CONFIGURE CLOUDINARY
cloudinary.config(
    cloud_name="dfxpmsy9l",
    api_key="329984749582184",
    api_secret="Sf1HfKTwv_GCCcgfAzJVlDeNfT0"
)

sender = WhatsAppSender()

current_link = "https://offer-preview.vercel.app/followup.html"


def upload_image():
    global current_link

    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    status_label.config(text="Uploading image...", fg="yellow")

    result = cloudinary.uploader.upload(file_path)
    image_url = result["secure_url"]

    current_link = update_html(image_url)

    print("⏳ Waiting for Vercel deploy...")
    time.sleep(6)   # 🔥 VERY IMPORTANT

    status_label.config(text="Image updated ✅", fg="green")


def send_followup():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not phone:
        status_label.config(text="Enter all details ❗", fg="orange")
        return

    if not phone.startswith("91"):
        phone = "91" + phone

    message = f"""🙏 Thank you for visiting our store, {name} 😊

We hope you liked our collection!

✨ Visit us again soon  
🛍️ Exciting offers waiting for you  

Check this 👇
{current_link}
"""

    status_label.config(text="Sending...", fg="yellow")

    threading.Thread(target=send_thread, args=(phone, message)).start()


def send_thread(phone, message):
    try:
        sender.send_text(phone, message)
        status_label.config(text="Sent ✅", fg="green")
    except:
        status_label.config(text="Failed ❌", fg="red")


# UI
root = tk.Tk()
root.title("WhatsApp Tool")
root.geometry("400x320")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="📤 Send Message", command=send_followup).pack(pady=10)
tk.Button(root, text="🖼 Upload Image", command=upload_image).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()