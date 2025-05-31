# pierut

import time
import board
import digitalio
import subprocess
import adafruit_character_lcd.character_lcd as characterlcd
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D22)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_backlight = digitalio.DigitalInOut(board.D5)
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)
try:
	while True:
		lcd.message = subprocess.check_output("ssh you@host.local weather-util 41008 |grep \"Temperature\" | cut -f5- -d\" \"", shell=True, universal_newlines=True) + subprocess.check_output("ssh you@host.local /usr/local/bin/temp.sh", shell=True, universal_newlines=True)
		time.sleep(5)
		lcd.clear()
		lcd.message = subprocess.check_output("ssh you@host.local weather-util 41008 |grep \"Weather\" |cut -f 5- -d\" \"", shell=True, universal_newlines=True) + subprocess.check_output("ssh you@host.local weather-util 41008 |grep \"Sky conditions\" |cut -f 6- -d\" \"", shell=True, universal_newlines=True)
		time.sleep(5)
		lcd.clear()
		scroll_msg = subprocess.check_output("ssh you@host.local uptime | cut -f14- -d\" \"", shell=True, universal_newlines=True)
		lcd.message = scroll_msg
		time.sleep(5)
		lcd.clear()
		scroll_msg = subprocess.check_output("ssh you@host.local uptime | cut -f2-8 -d\" \"", shell=True, universal_newlines=True)
		time.sleep(5)
		lcd.clear()
		scroll_msg = subprocess.check_output("ssh you@host.local date | cut -f1-3 -d\" \"", shell=True, universal_newlines=True)
		lcd.message = scroll_msg
		time.sleep(5)
		lcd.clear()
		scroll_msg = subprocess.check_output("ssh you@host.local ip a | grep \"inet 192\" | cut --delimiter=\" \" -f6", shell=True, universal_newlines=True)
		lcd.message = scroll_msg
		time.sleep(5)
		lcd.clear()
except KeyboardInterrupt:
	lcd.clear()
	lcd.message = "Keyboard Interrupt"
	time.sleep(0.5)
	lcd.clear()
