
import pyautogui
import pyperclip
import time
import os
import webbrowser # <-- The star of the show for opening URLs

# --- Configuration ---
CONTACT_NAME = "Shivani"  # The name of the contact as it appears in your WhatsApp
MESSAGE = "Hello Kundamma Kundamma Kundamma!  This message was sent by a fully automated Python script. 🚀"
WHATSAPP_URL = "https://web.whatsapp.com"

# --- Safety First ---
pyautogui.FAILSAFE = True

# --- Helper Function (no changes needed here) ---
def find_and_click(image_name, confidence=0.9, max_wait=10):
    """
    Finds an image on the screen and clicks it.
    Saves a debug screenshot if the image is not found.
    """
    start_time = time.time()
    location = None
    image_path = os.path.join(os.path.dirname(__file__), image_name)

    while (time.time() - start_time) < max_wait:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                print(f"Image '{image_name}' found.")
                pyautogui.click(pyautogui.center(location))
                return True
        except pyautogui.ImageNotFoundException:
            print(f"Waiting for '{image_name}'...")
            time.sleep(1)
        except FileNotFoundError:
            print(f"FATAL ERROR: Image file not found at: {image_path}")
            return False
            
    # Debugging if image is not found
    debug_screenshot_path = os.path.join(os.path.dirname(__file__), 'debug_screenshot.png')
    pyautogui.screenshot(debug_screenshot_path)
    print(f"Error: Could not find '{image_name}'. A debug screenshot has been saved to '{debug_screenshot_path}'")
    return False

# --- The NEW AND IMPROVED Automation Logic ---

# 1. Open WhatsApp Web in the default browser
print(f"Opening WhatsApp Web at {WHATSAPP_URL}...")
webbrowser.open(WHATSAPP_URL)

# 2. IMPORTANT: Wait for the page to load completely.
# This is a critical step. 15-20 seconds is usually safe.
# You might see the QR code screen if you're not logged in.
print("Waiting 20 seconds for WhatsApp Web to load...")
time.sleep(20)

print("Starting automation on the page.")

# 3. Find the search bar and type the contact's name
# We give it a longer wait time here (e.g., 30s) in case the page is slow
if find_and_click('search_icon.png', max_wait=30):
    time.sleep(1) 
    print(f"Typing contact name: {CONTACT_NAME}")
    pyautogui.typewrite(CONTACT_NAME, interval=0.1)
    time.sleep(2) 
    pyautogui.press('enter') 
    print("Contact selected.")
else:
    print("Could not find the WhatsApp search bar. Is WhatsApp Web fully loaded and are you logged in? Exiting.")
    exit()

# 4. Find the message box and type the message
time.sleep(2) 
if find_and_click('message_box.png'):
    time.sleep(1)
    print(f"Typing message: {MESSAGE}")
    pyperclip.copy(MESSAGE)
    # Use 'command' for macOS, 'ctrl' for Windows/Linux
    if os.name == 'posix': 
        pyautogui.hotkey('command', 'v')
    else:
        pyautogui.hotkey('ctrl', 'v')
    print("Message pasted.")
else:
    print("Could not find the message box. Exiting.")
    exit()

# 5. Find the send button and click it
time.sleep(1)
if find_and_click('send_button.png'):
    print("Message sent successfully!")
else:
    print("Could not find the send button.")

print("--- Automation Complete! ---")