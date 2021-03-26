from pygame import Color

WIDTH = 600
HEIGHT = 600
TITLE = "2048 Game"
FPS = 60

THEMES = { 
    "default" : {
        "background" : Color("#FAF8EF"),
        "frame1" : Color("#BBADA0"),
        "frame2" : Color("#CDC1B4"),
        "title-text" : Color("#756e66"),
        "box-text" : Color("#3c3a32"),
        2 :  Color("#EEE4DA"),
        4 : Color("#EEE1C9"),
        8 : Color("#F3B27A"),
        16 : Color("#f59663"),
        32 : Color("#f67d5f"),
        64 : Color("#f65d3b"),
        128 : Color("#edcf72"),
        256 : Color("#edcc61"),
        512 : Color("#f5cb42"),
        1024 : Color("#edc53f"),
        2048 : Color("#edc22e"),
        4096 : Color("#3c3a32"),
    },
    "tokyo night" : {
        "background" : Color("#a5add0"),
        "frame1" : Color("#1a1b26"),
        "frame2" : Color("#1e202e"),
        "title-text" : Color("#1e202e"),
        "box-text" : Color("#edf2fa"),
        2 :  Color("#b796f1"),
        4 : Color("#a476f5"),
        8 : Color("#8eaded"),
        16 : Color("#7aa2f7"),
        32 : Color("#5a8af2"),
        64 : Color("#3e7afa"),
        128 : Color("#f2889b"),
        256 : Color("#f7768e"),
        512 : Color("#f05471"),
        1024 : Color("#fa3e61"),
        2048 : Color("#fc9c63"),
        4096 : Color("#ddad67")
    },
    "tortoise" : {
        "background" : Color("#5c6e74"),
        "frame1" : Color("#394548"),
        "frame2" : Color("#455257"),
        "title-text" : Color("#455257"),
        "box-text" : Color("#edf2fa"),
        2 :  Color("#9dc97b"),
        4 : Color("#82b45b"),
        8 : Color("#86d44a"),
        16 : Color("#79b8d1"),
        32 : Color("#569eba"),
        64 : Color("#3ba9d4"),
        128 : Color("#dbca76"),
        256 : Color("#e8cf54"),
        512 : Color("#9a89d9"),
        1024 : Color("#7f69cf"),
        2048 : Color("#7659e3"),
        4096 : Color("#f05959")
    },
    "dracula" : {
        "background" : Color("#546898"),
        "frame1" : Color("#394548"),
        "frame2" : Color("#353745"),
        "title-text" : Color("#353745"),
        "box-text" : Color("#edf2fa"),
        2 :  Color("#d678b0"),
        4 : Color("#ed5fb4"),
        8 : Color("#9e8ad8"),
        16 : Color("#8e6ded"),
        32 : Color("#72d47d"),
        64 : Color("#53ed64"),
        128 : Color("#9be2f8"),
        256 : Color("#62d2f5"),
        512 : Color("#e9b172"),
        1024 : Color("#f5a347"),
        2048 : Color("#f0f293"),
        4096 : Color("#f4f760")
    }
}

TILESIZE = 100
SPACING = 10