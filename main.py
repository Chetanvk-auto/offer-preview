import tkinter as tk
import threading
from whatsapp_sender import WhatsAppSender
from html_generator import create_html   # 🔥 IMPORTANT

# Initialize sender
sender = WhatsAppSender()


def send_followup():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not phone:
        status_label.config(text="Enter all details ❗", fg="orange")
        return

    if not phone.isdigit() or len(phone) < 10:
        status_label.config(text="Invalid phone ❌", fg="red")
        return

    if not phone.startswith("91"):
        phone = "91" + phone

    # 🔥 STEP 1 → Generate NEW HTML dynamically
    title = "🙏 Thank You for Visiting"
    desc = "Explore our latest furniture collections!"

    # 👉 You can later make this dynamic
    image_url = "https://res.cloudinary.com/dfxpmsy9l/image/upload/v1776870879/Sofa_n5o3yc.png"

    filename, link = create_html(title, desc, image_url)

    # 🔥 STEP 2 → Use GENERATED LINK (NOT followup.html)
    message = f"""🙏 Thank you for visiting our store, {name} 😊

We hope you liked our collection!

✨ Visit us again soon  
🛍️ Exciting offers waiting for you  

Check this 👇
{link}
"""

    status_label.config(text="Sending... ⏳", fg="yellow")

    threading.Thread(target=send_message_thread, args=(phone, message)).start()


def send_message_thread(phone, message):
    try:
        sender.send_text(phone, message)
        status_label.config(text="Message Sent ✅", fg="green")
    except Exception as e:
        print(e)
        status_label.config(text="Failed ❌", fg="red")


# UI
root = tk.Tk()
root.title("WhatsApp Follow-up Tool")
root.geometry("400x300")
root.configure(bg="#1e1e2f")

tk.Label(root, text="Customer Name", fg="white", bg="#1e1e2f").pack(pady=(15, 5))
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Phone Number", fg="white", bg="#1e1e2f").pack(pady=(10, 5))
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

tk.Button(root, text="Send Follow-up", command=send_followup).pack(pady=20)

status_label = tk.Label(root, text="", fg="green", bg="#1e1e2f")
status_label.pack()

root.mainloop()