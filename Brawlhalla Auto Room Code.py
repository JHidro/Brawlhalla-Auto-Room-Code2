import subprocess
import time
import pyautogui
from pytesseract import pytesseract

tesseract_path = r'C:\Users\Alienware Joeld\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = tesseract_path

# Brawlhalla Game ID
steam_game_id = "291550"

# Construct the command to launch the game through Steam
steam_executable = "C:\\Program Files (x86)\\Steam\\Steam.exe"  # Replace with your Steam installation path
game_launch_command = f'"{steam_executable}" -applaunch {steam_game_id}'
subprocess.Popen(game_launch_command, shell=True)

# How long is should pause before going onto the next program (let brawlhalla fully open)
time.sleep(40)

def customGR():
    # Point(x=228, y=551) Custom Game Room, Point(x=561, y=559) Create Room, Point(x=731, y=569) Private Room
    pyautogui.moveTo(228, 551, duration=0.50)
    time.sleep(1)
    pyautogui.click()

def createGR():
    pyautogui.moveTo(561, 559, duration=0.50)
    time.sleep(1)
    pyautogui.click()

def privateGR():
    pyautogui.moveTo(731, 569, duration=0.50)
    time.sleep(1)
    pyautogui.click()

def saveScreenshot():
    time.sleep(0.5)
    # 1920x1080 coordinates
    screenshot = pyautogui.screenshot(region=(970, 58, 90, 40))
    text = pytesseract.image_to_string(screenshot)
    return text

customGR()
createGR()
privateGR()

room_code = saveScreenshot()
print(room_code.strip('#\n'))