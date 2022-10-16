from enum import Enum

class Instruments(Enum):
    # These instruments appear in the same order they're shown on thirtydollar.website.
    # Personally, I disagree with some of the placements, but I didn't organize them so it's not my fault.
    # I also disagree with some of the names and have changed them to either be shorter or funnier.
    
    # Originals
    VINE_BOOM = "boom"
    BRUH = "bruh"
    TACO_BELL = "bong"
    # Emoji
    MC_SKELETON_HURT = "💀"
    RD_CLAP = "👏"
    WHAT_DA_DOG_DOIN = "🐶"
    MC_CAVE = "👽"
    PING = "🔔"
    RD_BOINK = "💢"
    FART = "💨"
    ERROR = "🚫"
    KACHING = "💰"
    SLAP = "🖐"
    BONK = "🏏"
    CENSOR = "🤬"
    ALARM = "🚨"
    # Loud noise
    BUZZER = "buzzer"
    E = "e"
    EIGHT = "eight"
    # Emojis v2 (and some sfx)
    AYO_THE_PIZZA_HERE = "🍕"
    METAL_GEAR_ALERT = "❗"
    MAC_QUAC = "🦆"
    HONK = "🦢" # This character pretty much completely breaks IDLE. I blame you, GDColon.
    GUN_RELOAD = "gun"
    HITMARKER = "hitmarker"
    *CLICK*_NOICE = "👌"
    MR_KRAAAAAAAABS = "🦀"
    HOO = "gnome"
    YOU_SPIN_ME_RIGHT_ROUND_BABY = "💿" # This one too
    TADAAA = "🎉"
    WHAT_THE_FUCK_WAS_THAT = "🎻"
    # Things hitting things
    PAN = "pan"
    SLIP = "slip"
    WHIP = "whipcrack"
    KABLOOEY = "explosion"
    # Samsung
    SAMSUNG_NOTIFICATION = "📲"
    SAMSUNG_ALARM = "🌄"
    SAMSUNG_WHISLE = "whatsapp"
    # Dramatic stings and a pufferfish
    OH_NO = "😱"
    AIRHORN = "airhorn"
    PUFFERFISH_AUGH = "🐡"
    ULTRA_INSTINCT = "ultrainstinct"
    # Misc videogame sfx
    RD_SAMURAI = "samurai"
    FROG = "flipnote"
    NOPE_AVI = "nope"
    HOENN_DOOT = "hoenn"
    DOOT = "🎺"
    OOF = "oof"
    SUBALUWA = "subaluwa"
    ANIME_CATGIRL = "necoarc"
    YODA_DIES = "yoda"
    HEHEHEHAW = "hehehehaw"
    GRAND_DAD = "granddad"
    MORSHU_HMMMM = "morshu"
    # Random meme sfx
    DING = "stopposting"
    TWANY_WAN = "21"
    OP = "op"
    SLAAAM = "SLAM"
    SCREAMING_DOG = "americano"
    # Mario
    SMW_COIN = "smw_coin"
    SMW_1UP = "smw_1up"
    SMW_SPINJUMP = "smw_spinjump"
    SMW_STOP = "smw_stop2"
    SMW_KICK = "smw_kick"
    SMW_BOSS_STOMP = "smw_stomp"
    SM64_YAHOOOOO = "yahoo"
    SM64_OUCHY = "sm64_hurt"
    SM64_BUP = "bup"
    SM64_THWOMP = "thwomp"
    SM64_PAINTING = "sm64_painting"
    SMM_SCREAM = "smm_scream" # This is the ONLY Super Mario Maker sound on the site.
    # Mario Paint
    MP_MARIO = "mariopaint_mario"
    SMW_LUIGI = "mariopaint_luigi" # This one is with the rest of the Mario Paint SFX and is called "mariopaint_luigi" internally, but its title on thirtydollar.website is "Steel Drum (Super Mario World)" and that's what it sounds like. Why is it with Mario Paint? We may never know.
    SMW_YOSHI = "smw_yoshi" # THIS one, however, is straight from Super Mario World AND even has an internal ID reflecting that, but on thirtydollar.website it's named "Yoshi (Mario Paint)". Why???
    MP_STAR = "mariopaint_star"
    MP_FLOWER = "mariopaint_flower"
    MP_GAMEBOY = "mariopaint_gameboy"
    MP_DOG = "mariopaint_dog"
    MP_CAT = "mariopaint_cat"
    MP_SWAN = "mariopaint_swan"
    MP_BABBY = "mariopaint_baby"
    MP_PLANE = "mariopaint_plane"
    MP_CAR = "mariopaint_car"
    # Rhythm Doctor (for some reason there are a few RD SFX that are elsewhere in this list, why make things easy when they can be hard???)
    RD_SHAKE = "shaker"
    RD_DRUM = "🥁"
    RD_SNARE_DRUM = "hammer"
    RD_TOM_DRUM = "🪘"
    RD_SIDESTICK = "sidestick"
    RD_CYMBAL = "ride2"
    RD_POP = "buttonpop"
    RD_SKIPSHOT = "skipshot"
    # Rhythm Doctor Otto
    RD_OTTO_ON = "otto_on"
    RD_OTTO_OFF = "otto_off"
    RD_OTTO_HAPPY = "otto_happy"
    RD_OTTO_STRESSED = "otto_stress"
    # Rhythm Doctor tabs
    RD_TAB_SOUNDS = "tab_sounds"
    RD_TAB_ROWS = "tab_rows"
    RD_TAB_ACTIONS = "tab_actions"
    RD_TAB_DECOR = "tab_decorations"
    RD_TAB_ROOMS= "tab_rooms"
    # Rest of the Rhythm Doctor SFX (that are cohesively organized, that is! :p)
    RD_PRE_ECHO_CLAP = "preecho"
    RD_TONK = "tonk"
    RD_CLAP = "rdclap" # Why does these two have a "rd" prefix? Who knows!
    RD_MISTAKE = "rdmistake"
    # A Dance of Fire and Ice
    ADOFAI_CLACK = "midspin"
    ADOFAI_FIRE = "adofai_fire"
    ADOFAI_ICE = "adofai_ice"
    ADOFAI_KICK = "adofaikick" # Why no underscore? Why no consistency? Why no sanity for Ginger?
    ADOFAI_LEVEL_COMPLETE = "adofaicymbal" # Two different names for the same thing, for some reason
    # Rhythm Heaven (which is in fact a different game)
    RH_COWBELL = "cowbell"
    RH_KARATE_TOSS = "karateman_throw"
    RH_KARATE_TOSS_BAD = "karateman_offbeat"
    RH_KARATE_HIT = "karateman_hit"
    RH_KARATE_BULB = "karateman_bulb"
    RH_MONKEY = "ook"
    RH_CHORUS = "choruskid"
    RH_WIDGET = "builttoscale" # What does this MEAN???
    RH_PERFECT_FAIL = "perfectfail"
    RH_SKILL_STAR = "🌟"
    
