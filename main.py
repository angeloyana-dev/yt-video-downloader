import sys
from pytube import YouTube
from termcolor import colored as clr

def error(message):
	print(clr(message, 'red'))

def main_display():
	print(clr('YouTube Video Downloader', 'blue', attrs=['bold']))
	print('[1] Download Video')
	print('[2] Download Audio')
	print('[3] Quit')

def video():
	print(clr('Download video', 'blue', attrs=['bold']))
	print('Enter x to go back to main menu.')
	while True:
		try:
			url = input('Enter url: ')
			if url == 'x':
				break
			yt = YouTube(url)
			streams = yt.streams.filter(progressive=True, file_extension='mp4')
			
			print(clr('Resolutions', 'magenta'))
			for index, stream in enumerate(streams):
				print(f'[{index+1}] - {stream.resolution}|{(stream.filesize / (1024 * 1024)):.2f}mb')
			while True:
				try:
					choice = int(input('>> '))
					if choice < len(streams) < choice:
						raise
					else:
						break
				except:
					error('Not in the list!')
			to_download = streams[choice-1]
			filename = input('File name[extension excluded]: ') + '.mp4'
			print(clr(f'Saving as {filename}', 'yellow'))
			to_download.download(filename=filename)
			print(clr('Succesfully downloaded!', 'green'))
			break
		except:
			error('Invalid URL!')
	
def audio():
	print(clr('Download audio', 'blue', attrs=['bold']))
	print('Enter x to go back to main menu.')
	while True:
		try:
			url = input('Enter url: ')
			if url == 'x':
				break
			yt = YouTube(url)
			streams = yt.streams.filter(only_audio=True)
			
			print(clr('Quality', 'magenta'))
			for index, stream in enumerate(streams):
				print(f'[{index+1}] - {stream.abr}|{(stream.filesize / (1024 * 1024)):.2f}mb')
			while True:
				try:
					choice = int(input('>> '))
					if choice < len(streams) < choice:
						raise
					else:
						break
				except:
					error('Not in the list!')
			to_download = streams[choice-1]
			filename = input('File name[extension excluded]: ') + '.mp3'
			print(clr(f'Saving as {filename}', 'yellow'))
			to_download.download(filename=filename)
			print(clr('Succesfully downloaded!', 'green'))
			break
		except:
			error('Invalid URL!')

def quit():
	sys.exit()
	
def default():
	error('Invalid action!')

actions = {
	'1': video,
	'2': audio,
	'3': quit,
}

def main():
	while True:
		main_display()
		action = input('>> ')
		actions.get(action, default)()
		
if __name__ == '__main__':
	main()