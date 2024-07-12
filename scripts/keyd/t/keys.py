class Key:
    def __init__(self, name, code, alt_name, shifted_name):
        self.name = name
        self.code = code
        self.alt_name = alt_name
        self.shifted_name = shifted_name

    def __str__(self):
        return self.name


def is_mouse_button(key):
    return ((key.code) >= names["btn left"].code and (key.code) <= names["btn task"].code) or\
        ((key.code) >= names["btn 0"].code and (
            key.code) <= names["btn 9"].code)


codes = {
    1: Key("esc", 1, "escape", ""),
    2: Key("1", 2, "", "!"),
    3: Key("2", 3, "", "@"),
    4: Key("3", 4, "", "#"),
    5: Key("4", 5, "", "$"),
    6: Key("5", 6, "", "%"),
    7: Key("6", 7, "", "^"),
    8: Key("7", 8, "", "&"),
    9: Key("8", 9, "", "*"),
    10: Key("9", 10, "", "("),
    11: Key("0", 11, "", ")"),
    12: Key("-", 12, "minus", "_"),
    13: Key("=", 13, "equal", "+"),
    14: Key("backspace", 14, "", ""),
    15: Key("tab", 15, "", ""),
    16: Key("q", 16, "", "Q"),
    17: Key("w", 17, "", "W"),
    18: Key("e", 18, "", "E"),
    19: Key("r", 19, "", "R"),
    20: Key("t", 20, "", "T"),
    21: Key("y", 21, "", "Y"),
    22: Key("u", 22, "", "U"),
    23: Key("i", 23, "", "I"),
    24: Key("o", 24, "", "O"),
    25: Key("p", 25, "", "P"),
    26: Key("[", 26, "leftbrace", "{"),
    27: Key("]", 27, "rightbrace", "}"),
    28: Key("enter", 28, "\n", ""),
    29: Key("control", 29, "leftcontrol", ""),
    30: Key("a", 30, "", "A"),
    31: Key("s", 31, "", "S"),
    32: Key("d", 32, "", "D"),
    33: Key("f", 33, "", "F"),
    34: Key("g", 34, "", "G"),
    35: Key("h", 35, "", "H"),
    36: Key("j", 36, "", "J"),
    37: Key("k", 37, "", "K"),
    38: Key("l", 38, "", "L"),
    39: Key(";", 39, "semicolon", ":"),
    40: Key("'", 40, "apostrophe", "\""),
    41: Key("`", 41, "grave", "~"),
    42: Key("shift", 42, "leftshift", ""),
    43: Key("\\", 43, "backslash", " |"),
    44: Key("z", 44, "", "Z"),
    45: Key("x", 45, "", "X"),
    46: Key("c", 46, "", "C"),
    47: Key("v", 47, "", "V"),
    48: Key("b", 48, "", "B"),
    49: Key("n", 49, "", "N"),
    50: Key("m", 50, "", "M"),
    51: Key(",", 51, "comma", "<"),
    52: Key(".", 52, "dot", ">"),
    53: Key("/", 53, "slash", "?"),
    54: Key("rightshift", 54, "", ""),
    55: Key("kpasterisk", 55, "", ""),
    56: Key("alt", 56, "leftalt", ""),
    57: Key("space", 57, " ", ""),
    58: Key("capslock", 58, "", ""),
    59: Key("f1", 59, "", ""),
    60: Key("f2", 60, "", ""),
    61: Key("f3", 61, "", ""),
    62: Key("f4", 62, "", ""),
    63: Key("f5", 63, "", ""),
    64: Key("f6", 64, "", ""),
    65: Key("f7", 65, "", ""),
    66: Key("f8", 66, "", ""),
    67: Key("f9", 67, "", ""),
    68: Key("f10", 68, "", ""),
    69: Key("numlock", 69, "", ""),
    70: Key("scrolllock", 70, "", ""),
    71: Key("kp7", 71, "", ""),
    72: Key("kp8", 72, "", ""),
    73: Key("kp9", 73, "", ""),
    74: Key("kpminus", 74, "", ""),
    75: Key("kp4", 75, "", ""),
    76: Key("kp5", 76, "", ""),
    77: Key("kp6", 77, "", ""),
    78: Key("kpplus", 78, "", ""),
    79: Key("kp1", 79, "", ""),
    80: Key("kp2", 80, "", ""),
    81: Key("kp3", 81, "", ""),
    82: Key("kp0", 82, "", ""),
    83: Key("kpdot", 83, "", ""),
    85: Key("zenkakuhankaku", 85, "", ""),
    86: Key("102nd", 86, "", ""),
    87: Key("f11", 87, "", ""),
    88: Key("f12", 88, "", ""),
    89: Key("ro", 89, "", ""),
    90: Key("katakana", 90, "", ""),
    91: Key("hiragana", 91, "", ""),
    92: Key("henkan", 92, "", ""),
    93: Key("katakanahiragana", 93, "", ""),
    94: Key("muhenkan", 94, "", ""),
    95: Key("kpjpcomma", 95, "", ""),
    96: Key("kpenter", 96, "", ""),
    97: Key("rightcontrol", 97, "", ""),
    98: Key("kpslash", 98, "", ""),
    99: Key("sysrq", 99, "", ""),
    100: Key("rightalt", 100, "", ""),
    101: Key("linefeed", 101, "", ""),
    102: Key("home", 102, "", ""),
    103: Key("up", 103, "", ""),
    104: Key("pageup", 104, "", ""),
    105: Key("left", 105, "", ""),
    106: Key("right", 106, "", ""),
    107: Key("end", 107, "", ""),
    108: Key("down", 108, "", ""),
    109: Key("pagedown", 109, "", ""),
    110: Key("insert", 110, "", ""),
    111: Key("delete", 111, "", ""),
    112: Key("macro", 112, "", ""),
    113: Key("mute", 113, "", ""),
    114: Key("volumedown", 114, "", ""),
    115: Key("volumeup", 115, "", ""),
    116: Key("power", 116, "", ""),
    117: Key("kpequal", 117, "", ""),
    118: Key("kpplusminus", 118, "", ""),
    119: Key("pause", 119, "", ""),
    120: Key("scale", 120, "", ""),
    121: Key("kpcomma", 121, "", ""),
    122: Key("hangeul", 122, "", ""),
    123: Key("hanja", 123, "", ""),
    124: Key("yen", 124, "", ""),
    125: Key("meta", 125, "leftmeta", ""),
    126: Key("rightmeta", 126, "", ""),
    127: Key("compose", 127, "", ""),
    128: Key("stop", 128, "", ""),
    129: Key("again", 129, "", ""),
    130: Key("props", 130, "", ""),
    131: Key("undo", 131, "", ""),
    132: Key("front", 132, "", ""),
    133: Key("copy", 133, "", ""),
    134: Key("open", 134, "", ""),
    135: Key("paste", 135, "", ""),
    136: Key("find", 136, "", ""),
    137: Key("cut", 137, "", ""),
    138: Key("help", 138, "", ""),
    139: Key("menu", 139, "", ""),
    140: Key("calc", 140, "", ""),
    141: Key("setup", 141, "", ""),
    142: Key("sleep", 142, "", ""),
    143: Key("wakeup", 143, "", ""),
    144: Key("file", 144, "", ""),
    145: Key("sendfile", 145, "", ""),
    146: Key("deletefile", 146, "", ""),
    147: Key("xfer", 147, "", ""),
    148: Key("prog1", 148, "", ""),
    149: Key("prog2", 149, "", ""),
    150: Key("www", 150, "", ""),
    151: Key("msdos", 151, "", ""),
    152: Key("coffee", 152, "", ""),
    153: Key("display", 153, "", ""),
    154: Key("cyclewindows", 154, "", ""),
    155: Key("mail", 155, "", ""),
    156: Key("bookmarks", 156, "", ""),
    157: Key("computer", 157, "", ""),
    158: Key("back", 158, "", ""),
    159: Key("forward", 159, "", ""),
    160: Key("closecd", 160, "", ""),
    161: Key("ejectcd", 161, "", ""),
    162: Key("ejectclosecd", 162, "", ""),
    163: Key("nextsong", 163, "", ""),
    164: Key("playpause", 164, "", ""),
    165: Key("previoussong", 165, "", ""),
    166: Key("stopcd", 166, "", ""),
    167: Key("record", 167, "", ""),
    168: Key("rewind", 168, "", ""),
    169: Key("phone", 169, "", ""),
    170: Key("iso", 170, "", ""),
    171: Key("config", 171, "", ""),
    172: Key("homepage", 172, "", ""),
    173: Key("refresh", 173, "", ""),
    174: Key("exit", 174, "", ""),
    175: Key("move", 175, "", ""),
    176: Key("edit", 176, "", ""),
    177: Key("scrollup", 177, "", ""),
    178: Key("scrolldown", 178, "", ""),
    179: Key("kpleftparen", 179, "", ""),
    180: Key("kprightparen", 180, "", ""),
    181: Key("new", 181, "", ""),
    182: Key("redo", 182, "", ""),
    183: Key("f13", 183, "", ""),
    184: Key("f14", 184, "", ""),
    185: Key("f15", 185, "", ""),
    186: Key("f16", 186, "", ""),
    187: Key("f17", 187, "", ""),
    188: Key("f18", 188, "", ""),
    189: Key("f19", 189, "", ""),
    190: Key("f20", 190, "", ""),
    191: Key("f21", 191, "", ""),
    192: Key("f22", 192, "", ""),
    193: Key("f23", 193, "", ""),
    194: Key("f24", 194, "", ""),
    200: Key("playcd", 200, "", ""),
    201: Key("pausecd", 201, "", ""),
    202: Key("prog3", 202, "", ""),
    203: Key("prog4", 203, "", ""),
    204: Key("dashboard", 204, "", ""),
    205: Key("suspend", 205, "", ""),
    206: Key("close", 206, "", ""),
    207: Key("play", 207, "", ""),
    208: Key("fastforward", 208, "", ""),
    209: Key("bassboost", 209, "", ""),
    210: Key("print", 210, "", ""),
    211: Key("hp", 211, "", ""),
    212: Key("camera", 212, "", ""),
    213: Key("sound", 213, "", ""),
    214: Key("question", 214, "", ""),
    215: Key("email", 215, "", ""),
    216: Key("chat", 216, "", ""),
    217: Key("search", 217, "", ""),
    218: Key("connect", 218, "", ""),
    219: Key("finance", 219, "", ""),
    220: Key("sport", 220, "", ""),
    221: Key("shop", 221, "", ""),
    222: Key("alterase", 222, "", ""),
    223: Key("cancel", 223, "", ""),
    224: Key("brightnessdown", 224, "", ""),
    225: Key("brightnessup", 225, "", ""),
    226: Key("media", 226, "", ""),
    227: Key("switchvideomode", 227, "", ""),
    228: Key("kbdillumtoggle", 228, "", ""),
    229: Key("kbdillumdown", 229, "", ""),
    230: Key("kbdillumup", 230, "", ""),
    231: Key("send", 231, "", ""),
    232: Key("reply", 232, "", ""),
    233: Key("forwardmail", 233, "", ""),
    234: Key("save", 234, "", ""),
    235: Key("documents", 235, "", ""),
    236: Key("battery", 236, "", ""),
    237: Key("bluetooth", 237, "", ""),
    238: Key("wlan", 238, "", ""),
    239: Key("uwb", 239, "", ""),
    240: Key("unknown", 240, "", ""),
    241: Key("next", 241, "", ""),
    242: Key("prev", 242, "", ""),
    243: Key("cycle", 243, "", ""),
    244: Key("auto", 244, "", ""),
    245: Key("off", 245, "", ""),
    246: Key("wwan", 246, "", ""),
    247: Key("rfkill", 247, "", ""),
    248: Key("micmute", 248, "", ""),
    330: Key("btn dead", 330, "", ""),
    325: Key("btn dead", 325, "", ""),
    256: Key("btn 0", 256, "", ""),
    257: Key("btn 1", 257, "", ""),
    258: Key("btn 2", 258, "", ""),
    259: Key("btn 3", 259, "", ""),
    260: Key("btn 4", 260, "", ""),
    261: Key("btn 5", 261, "", ""),
    262: Key("btn 6", 262, "", ""),
    263: Key("btn 7", 263, "", ""),
    264: Key("btn 8", 264, "", ""),
    265: Key("btn 9", 265, "", ""),
    272: Key("btn left", 272, "", ""),
    273: Key("btn right", 273, "", ""),
    274: Key("btn middle", 274, "", ""),
    275: Key("btn side", 275, "", ""),
    276: Key("btn extra", 276, "", ""),
    277: Key("btn forward", 277, "", ""),
    278: Key("btn back", 278, "", ""),
    279: Key("btn task", 279, "", ""),
    352: Key("ok", 352, "", ""),
    353: Key("select", 353, "", ""),
    354: Key("goto", 354, "", ""),
    355: Key("clear", 355, "", ""),
    356: Key("power2", 356, "", ""),
    357: Key("option", 357, "", ""),
    358: Key("info", 358, "", ""),
    359: Key("time", 359, "", ""),
    360: Key("vendor", 360, "", ""),
    361: Key("archive", 361, "", ""),
    362: Key("program", 362, "", ""),
    363: Key("channel", 363, "", ""),
    364: Key("favorites", 364, "", ""),
    365: Key("epg", 365, "", ""),
    366: Key("pvr", 366, "", ""),
    367: Key("mhp", 367, "", ""),
    368: Key("language", 368, "", ""),
    369: Key("title", 369, "", ""),
    370: Key("subtitle", 370, "", ""),
    371: Key("angle", 371, "", ""),
    372: Key("zoom", 372, "", ""),
    373: Key("mode", 373, "", ""),
    374: Key("keyboard", 374, "", ""),
    375: Key("screen", 375, "", ""),
    376: Key("pc", 376, "", ""),
    377: Key("tv", 377, "", ""),
    378: Key("tv2", 378, "", ""),
    379: Key("vcr", 379, "", ""),
    380: Key("vcr2", 380, "", ""),
    381: Key("sat", 381, "", ""),
    382: Key("sat2", 382, "", ""),
    383: Key("cd", 383, "", ""),
    384: Key("tape", 384, "", ""),
    385: Key("radio", 385, "", ""),
    386: Key("tuner", 386, "", ""),
    387: Key("player", 387, "", ""),
    388: Key("text", 388, "", ""),
    389: Key("dvd", 389, "", ""),
    390: Key("aux", 390, "", ""),
    391: Key("mp3", 391, "", ""),
    392: Key("audio", 392, "", ""),
    393: Key("video", 393, "", ""),
    394: Key("directory", 394, "", ""),
    395: Key("list", 395, "", ""),
    396: Key("memo", 396, "", ""),
    397: Key("calendar", 397, "", ""),
    398: Key("red", 398, "", ""),
    399: Key("green", 399, "", ""),
    400: Key("yellow", 400, "", ""),
    401: Key("blue", 401, "", ""),
    402: Key("channelup", 402, "", ""),
    403: Key("channeldown", 403, "", ""),
    404: Key("first", 404, "", ""),
    405: Key("last", 405, "", ""),
    406: Key("ab", 406, "", ""),
    407: Key("next", 407, "", ""),
    408: Key("restart", 408, "", ""),
    409: Key("slow", 409, "", ""),
    410: Key("shuffle", 410, "", ""),
    411: Key("break", 411, "", ""),
    412: Key("previous", 412, "", ""),
    413: Key("digits", 413, "", ""),
    414: Key("teen", 414, "", ""),
    415: Key("twen", 415, "", ""),
    416: Key("videophone", 416, "", ""),
    417: Key("games", 417, "", ""),
    418: Key("zoomin", 418, "", ""),
    419: Key("zoomout", 419, "", ""),
    420: Key("zoomreset", 420, "", ""),
    421: Key("wordprocessor", 421, "", ""),
    422: Key("editor", 422, "", ""),
    423: Key("spreadsheet", 423, "", ""),
    424: Key("graphicseditor", 424, "", ""),
    425: Key("presentation", 425, "", ""),
    426: Key("database", 426, "", ""),
    427: Key("news", 427, "", ""),
    428: Key("voicemail", 428, "", ""),
    429: Key("addressbook", 429, "", ""),
    430: Key("messenger", 430, "", ""),
    431: Key("displaytoggle", 431, "", ""),
    432: Key("spellcheck", 432, "", ""),
    433: Key("logoff", 433, "", ""),
    434: Key("dollar", 434, "", ""),
    435: Key("euro", 435, "", ""),
    436: Key("frameback", 436, "", ""),
    437: Key("frameforward", 437, "", ""),
    438: Key("context_menu", 438, "", ""),
    439: Key("repeat", 439, "", ""),
    440: Key("10channelsup", 440, "", ""),
    441: Key("10channelsdown", 441, "", ""),
    442: Key("images", 442, "", ""),
    448: Key("eol", 448, "", ""),
    449: Key("eos", 449, "", ""),
    450: Key("ins_line", 450, "", ""),
    451: Key("del_line", 451, "", ""),
    464: Key("fn", 464, "", ""),
    465: Key("fnesc", 465, "", ""),
    466: Key("f1", 466, "", ""),
    467: Key("f2", 467, "", ""),
    468: Key("f3", 468, "", ""),
    469: Key("f4", 469, "", ""),
    470: Key("f5", 470, "", ""),
    471: Key("f6", 471, "", ""),
    472: Key("f7", 472, "", ""),
    473: Key("f8", 473, "", ""),
    474: Key("f9", 474, "", ""),
    475: Key("f10", 475, "", ""),
    476: Key("f11", 476, "", ""),
    477: Key("f12", 477, "", ""),
    478: Key("fn1", 478, "", ""),
    479: Key("fn2", 479, "", ""),
    480: Key("fnd", 480, "", ""),
    481: Key("fne", 481, "", ""),
    482: Key("fnf", 482, "", ""),
    483: Key("fns", 483, "", ""),
    484: Key("fnb", 484, "", ""),
    497: Key("dot1", 497, "", ""),
    498: Key("dot2", 498, "", ""),
    499: Key("dot3", 499, "", ""),
    500: Key("dot4", 500, "", ""),
    501: Key("dot5", 501, "", ""),
    502: Key("dot6", 502, "", ""),
    503: Key("dot7", 503, "", ""),
    504: Key("dot8", 504, "", ""),
    505: Key("dot9", 505, "", ""),
    506: Key("dot10", 506, "", ""),
    512: Key("np0", 512, "", ""),
    513: Key("np1", 513, "", ""),
    514: Key("np2", 514, "", ""),
    515: Key("np3", 515, "", ""),
    516: Key("np4", 516, "", ""),
    517: Key("np5", 517, "", ""),
    518: Key("np6", 518, "", ""),
    519: Key("np7", 519, "", ""),
    520: Key("np8", 520, "", ""),
    521: Key("np9", 521, "", ""),
    522: Key("npstar", 522, "", ""),
    523: Key("nppound", 523, "", ""),
    524: Key("npa", 524, "", ""),
    525: Key("npb", 525, "", ""),
    526: Key("npc", 526, "", ""),
    527: Key("npd", 527, "", ""),
    528: Key("focus", 528, "", ""),
    529: Key("button", 529, "", ""),
    530: Key("toggle", 530, "", ""),
    531: Key("on", 531, "", ""),
    532: Key("off", 532, "", ""),
    533: Key("zoomin", 533, "", ""),
    534: Key("zoomout", 534, "", ""),
    535: Key("up", 535, "", ""),
    536: Key("down", 536, "", ""),
    537: Key("left", 537, "", ""),
    538: Key("right", 538, "", ""),
    539: Key("on", 539, "", ""),
    540: Key("off", 540, "", ""),
    541: Key("attendant_toggle", 541, "", ""),
    542: Key("lights_toggle", 542, "", ""),
    560: Key("als_toggle", 560, "", ""),
    576: Key("buttonconfig", 576, "", ""),
    577: Key("taskmanager", 577, "", ""),
    578: Key("journal", 578, "", ""),
    579: Key("controlpanel", 579, "", ""),
    580: Key("appselect", 580, "", ""),
    581: Key("screensaver", 581, "", ""),
    582: Key("voicecommand", 582, "", ""),
    592: Key("min", 592, "", ""),
    593: Key("max", 593, "", ""),
    608: Key("prev", 608, "", ""),
    609: Key("next", 609, "", ""),
    610: Key("prevgroup", 610, "", ""),
    611: Key("nextgroup", 611, "", ""),
    612: Key("accept", 612, "", ""),
    613: Key("cancel", 613, "", ""),
    614: Key("up", 614, "", ""),
    615: Key("down", 615, "", ""),
    616: Key("up", 616, "", ""),
    617: Key("down", 617, "", ""),
    618: Key("root_menu", 618, "", ""),
    619: Key("media_top_menu", 619, "", ""),
    620: Key("11", 620, "", ""),
    621: Key("12", 621, "", ""),
    622: Key("desc", 622, "", ""),
    623: Key("mode", 623, "", ""),
    624: Key("favorite", 624, "", ""),
    625: Key("stop_record", 625, "", ""),
    626: Key("pause_record", 626, "", ""),
    627: Key("vod", 627, "", ""),
    628: Key("unmute", 628, "", ""),
    629: Key("fastreverse", 629, "", ""),
    630: Key("slowreverse", 630, "", ""),
    631: Key("data", 631, "", ""),
    635: Key("noop", 635, "", ""),
}

names = {key.name: key for key in codes.values()}
shifted_names = {key.shifted_name: key for key in codes.values()}
alt_names = {key.alt_name: key for key in codes.values()}
