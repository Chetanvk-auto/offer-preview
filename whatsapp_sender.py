from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pyperclip


class WhatsAppSender:

    def __init__(self):
        
        chrome_options = Options()

        # Force Chrome
        chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        # Persistent login profile
        profile_path = os.path.abspath("chrome_profile")
        chrome_options.add_argument(f"user-data-dir={profile_path}")

        # 🔥 IMPORTANT FIXES
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")

        # Stability
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        self.wait = WebDriverWait(self.driver, 30)

        self.driver.get("https://web.whatsapp.com")
        print("👉 Please scan QR code if not logged in...")
        input("Press ENTER after WhatsApp is ready...")

    def send_text(self, phone, message):
        try:
            if not phone.startswith("91"):
                phone = "91" + phone

            url = f"https://web.whatsapp.com/send?phone={phone}"
            self.driver.get(url)

            time.sleep(5)

            # ❗ Check invalid number
            error_popup = self.driver.find_elements(By.XPATH, "//div[contains(text(),'isn’t on WhatsApp')]")
            if error_popup:
                print(f"❌ {phone} not on WhatsApp")
                return

            # Wait for input box
            box = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//footer//div[@contenteditable='true']")
                )
            )

            box.click()

            # Paste message
            pyperclip.copy(message)
            box.send_keys(Keys.CONTROL, 'v')

            print("⌛ Waiting for preview to load...")

            preview_loaded = False

            for i in range(15):  # wait max 15 sec
                try:
                    preview = self.driver.find_elements(
                        By.XPATH,
                        "//div[@data-testid='link-preview']"
                    )

                    if preview:
                        preview_loaded = True
                        print("✅ Preview loaded")
                        break

                except:
                    pass

                time.sleep(1)

            if not preview_loaded:
                print("⚠️ Preview NOT detected, sending anyway")

            time.sleep(1)
            box.send_keys(Keys.ENTER)

            print(f"✅ Sent to {phone}")

        except Exception as e:
            print(f"❌ Failed for {phone}: {e}")