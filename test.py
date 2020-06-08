import time
import chromewrapper

if __name__ == "__main__":
	chrome = ChromeWrapper({
			"window_name": "Disney+ | Video Player"
		})
	chrome.open_in_kiosk_mode( "https://www.disneyplus.com/video/e85916bf-5b05-4414-978d-a8c797a7d0c2" )
	time.sleep( 1 )
	print( chrome.xdotool.get_window_geometry() )
	time.sleep( 3 )
	chrome.xdotool.fullscreen()