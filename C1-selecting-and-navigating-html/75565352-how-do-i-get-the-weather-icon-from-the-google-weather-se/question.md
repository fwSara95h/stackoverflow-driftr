---
title: "How do I get the weather icon from the google weather service using BeautifulSoup?"
site: stackoverflow
question_id: 75565352
url: https://stackoverflow.com/q/75565352
asked: 2023-02-25T12:16:10Z
asked_by: "user21285706"
asked_by_url: https://stackoverflow.com/users/21285706
last_edited: never
tags: [python, beautifulsoup, pysimplegui]
score: 0
views_at_snapshot: 321
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5bacc9cd493b84425c10c05be7bb178959f432efff96185166cd11386ca5c3ce
---

# How do I get the weather icon from the google weather service using BeautifulSoup?

Asked by [user21285706](https://stackoverflow.com/users/21285706) on Stack Overflow, <https://stackoverflow.com/q/75565352>, 2023-02-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to create a weatherapp to learn about PySimpleGUI, where I'm scraping data of google weather service (the one that appears when you google "Weather [insert location]" using BeautifulSoup. I've been able to get the location, time and temperature but am having trouble with the weather icon. I found the element in the HTML code:


`<img id="dimg_1" src="data:image/png;base64,iVBOR…6Bd0LJ+BorgAAAABJRU5ErkJggg==" class="YQ4gaf zr758c" height="60" width="60" alt="Övervägande molnigt" data-atf="1" data-frt="0">`

But my code doesn't seem to find the ID when I search for it using soup.find. I think the problem is in the get_weather data function but I'll include the whole code if it's somewhere else. I also get the following message in the terminal when entering a location into the input field:

[path]:5524: UserWarning: Image element - source is not a valid type: <class 'PySimpleGUI.PySimpleGUI.Image'>
  warnings.warn('Image element - source is not a valid type: {}'.format(type(source)), UserWarning)

Here is the code:

```
import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests
import base64
from io import BytesIO

def get_weather_data(location):
    """ Scrapes the weather data off the internet and returns the location name,
        local time, weather, temperature and an image object."""
    
    url = 'https://www.google.com/search?q=weather+' + location.replace(' ', '')
    session = requests.Session()
    session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get(url)
    soup = bs(html.text, 'html.parser')

    # Gets the information
    name = soup.find('span', class_ = 'BBwThe').text
    time = soup.find('div', id = 'wob_dts').text
    weather = soup.find('span', id = 'wob_dc').text
    temp = soup.find('span', id = 'wob_tm').text

    # Gets the image data and creates an object
    img = soup.find('img', id = 'dimg_1')
    if img:
        img_data = img['src'].split(',', 1)[1]
        img_binary = base64.b16decode(img_data)
        img_obj = sg.Image(data = img_binary, size = (60,60), pad = (5,5))
    else:
        img_obj = sg.Image(size=(60, 60), pad=(5,5))

    return name, time, weather, temp, img_obj

# Layout and theme
sg.theme('reddit')
image_col = sg.Column([[sg.Image(key = '-IMAGE-', background_color = '#FFFFFF')]])
info_col = sg.Column([
    [sg.Text('', key = '-LOCATION-', font = 'Calibri 30', background_color = '#FF0000', text_color = '#FFFFFF', pad = 0, visible = False)],
    [sg.Text('', key = '-TIME-', font = 'Calibri 16', background_color = '#000000', text_color = '#FFFFFF', pad = 0, visible = False)],
    [sg.Text('', key = '-TEMP-', font = 'Calibri 16', background_color = '#FFFFFF', text_color = '#000000', pad = (0,10), justification = 'center', visible = False)]
])
layout = [
    [sg.Input(expand_x = True, key = '-INPUT-'), sg.Button('Enter', key = '-ENTER-', bind_return_key = True, button_color = '#000000', border_width = 0)],
    [image_col, info_col]
]

window = sg.Window('Weather app', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-ENTER-':
        name, time, weather, temp, img = get_weather_data(values['-INPUT-'])
        window['-LOCATION-'].update(name, visible = True)
        window['-TIME-'].update(time, visible = True)
        window['-TEMP-'].update(temp + 'C', visible = True)
        window['-IMAGE-'].update(img)

window.close()
```


Any help would be appreciated!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[RJ Adriaansen](https://stackoverflow.com/users/11380795)** (2023-02-25): Why scrape google in stead of using an open weather api?
- **[Jason Yang](https://stackoverflow.com/users/11936135)** (2023-02-25): `window['-IMAGE-'].update(img)` where `img` should be the image in `str` or `bytes`, not the instance of the `sg.Image` element returned from the function `get_weather_data`.
