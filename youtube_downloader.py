try:
    from pytube import YouTube
    from pytube import Playlist
    import PySimpleGUI as sg
except :
    print('Required modules not found ')


sg.theme('DarkAmber')

layout = [
         [sg.Text('Enter the video link below')],
         [sg.Input()],
         [sg.Button('Download')],
        ]

window = sg.Window('Youtube Downloader', layout, size=(640, 480))

i = 0
while True :
    i +=1
    event, values = window.read()
    print(event, values)
    vidURL = values[0]
    print('VideoURL', type(vidURL))

    try:
        YouTube(vidURL).streams.get_highest_resolution().download()
    except:
        print('Invalid URL')

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
window.close()


