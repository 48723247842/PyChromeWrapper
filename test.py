import time
from chromewrapper import ChromeWrapper

if __name__ == "__main__":
	chrome = ChromeWrapper({
			"window_name": "Disney+ | Video Player" ,
			"extension_paths": [
				# Tampermonkey
				"/home/morphs/.config/google-chrome/Default/Extensions/dhdgffkkebhmkfjojejmpbldmpobfkfo"
			]
		})
	chrome.open_in_kiosk_mode( "https://www.disneyplus.com/video/e85916bf-5b05-4414-978d-a8c797a7d0c2" )
	time.sleep( 20 )
	chrome.xdotool.press_keyboard_key( "Ctrl+r" )
	print( chrome.xdotool.get_window_geometry() )
	time.sleep( 3 )
	chrome.xdotool.fullscreen()