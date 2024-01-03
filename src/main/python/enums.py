from enum import Enum


class ParserTypeEnum(Enum):
    youtube = 1
    songlyrics = 2
    js_enums = 3
    with_headers = 4


class ParserYoutubeActionEnum(Enum):
    one_mp4 = 1
    one_opus = 2
    playlist_mp4 = 3
    playlist_opus = 4


class ParserSonglyricsActionEnum(Enum):
    one_song = 1
    playlist_song = 2


class Roles(Enum):
    admin = 1
    user = 2
