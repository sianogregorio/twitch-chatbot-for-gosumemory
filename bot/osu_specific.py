import re
import urllib.request
from bs4 import BeautifulSoup

def is_map_request(message: str):
    '''Checks if the message is a map request'''
    url_pattern = r'(https?:\/\/)?(osu|old).ppy.sh\/(p|b|beatmap|beatmaps|beatmapsets|s)\/(beatmap\?b=)?([\d]+#(osu|taiko|mania)\/[\d]+|[\d]+)(\&m=[\d])?'
    return True if re.findall(url_pattern, message) else False 

def find_osu_url(message: str):
    '''Returns the osu url'''
    url_pattern = r'(https?:\/\/)?(osu|old).ppy.sh\/(p|b|beatmap|beatmaps|beatmapsets|s)\/(beatmap\?b=)?([\d]+#(osu|taiko|mania)\/[\d]+|[\d]+)(\&m=[\d])?'
    for str in message.split():
        if re.findall(url_pattern, str):
            return str

def find_osu_map_name(osu_url: str):
    '''Returns the osu map name via url'''
    page = urllib.request.urlopen(osu_url)
    html = BeautifulSoup(page.read(), "html.parser")

    for tags in html.find_all("meta"):
        if (tags.get('name') == "description"):
            content = str(tags.get('content')).split("»")
            return content[2]
