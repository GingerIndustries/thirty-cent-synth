from enum import Enum

class SFX(Enum):
    # These instruments appear in the same order they're shown on thirtydollar.website.
    # Personally, I disagree with some of the placements, but I didn't organize them so it's not my fault.
    # I also disagree with some of the names and have changed them to either be shorter or funnier.
    
    # Originals
    VINE_BOOM = "boom"
    BRUH = "bruh"
    TACO_BELL = "bong"
    # Emoji
    MC_SKELETON_HURT = "💀"
    CLAP = "👏"
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
    CLICK_NOICE = "👌"
    MR_KRAAAAAAAABS = "🦀"
    HOO = "gnome"
    YOU_SPIN_ME_RIGHT_ROUND_BABY = "💿" # This one too
    TADAAA = "🎉"
    WHAT_THE_HELL_WAS_THAT = "🎻"
    # Things hitting things
    PAN = "pan"
    SLIP = "slip"
    WHIP = "whipcrack"
    KABLOOEY = "explosion"
    # Samsung
    SAMSUNG_NOTIFICATION = "📲"
    SAMSUNG_ALARM = "🌄"
    SAMSUNG_WHISTLE = "whatsapp"
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
    SMW_STEEL_DRUM = "mariopaint_luigi" # This one is with the rest of the Mario Paint SFX and is called "mariopaint_luigi" internally, but its title on thirtydollar.website is "Steel Drum (Super Mario World)" and that's what it sounds like. Why is it with Mario Paint? We may never know.
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
    # Funky Friday
    FNF_LEFT = "fnf_left"
    FNF_DOWN = "fnf_down"
    FNF_UP = "fnf_up"
    FNF_RIGHT = "fnf_right"
    FNF_FAIL = "fnf_death"
    # Geometry Dash
    GD_CRASH = "gdcrash" # WHY NO SPACE???
    GD_CRASH_MANA_ORBS = "gdcrash_orbs"
    GD_SECRET_COIN = "gd_coin"
    GD_MANA_ORBS = "gd_orbs"
    GD_DIAMOND = "gd_diamonds"
    GD_QUIT = "gd_quit"
    GD_BWOMP = "bwomp" # "Blast Processing" on the site
    # Undertale and Deltarune
    UT_HIT = "undertale_hit"
    UT_GAMEOVER = "undertale_crack" # ???
    SANS = "sans_voice"
    MEGALOVANIA = "megalovania"
    MEGALOVANIA_NOTE = "🦴"
    UT_ENCOUNTER = "undertale_encounter"
    UT_BORK = "toby" # This one does kinda make sense, I guess
    UT_VANISH = "gaster" # This one makes less sense.
    DR_SPLAT = "lancer_splat"
    # The Binding of Isaac
    ISAAC_HURT = "isaac_hurt"
    ISAAC_DEAD = "isaac_dead"
    HOLY_MANTLE = "isaac_mantle"
    # BABA IS YOU
    BABA_MOVE = "BABA"
    BABA_RULE = "YOU" # ?????
    BABA_DEFEAT = "DEFEAT"
    # vvvvvv
    VVVVVV_FLIP = "vvvvvv_flip"
    VVVVVV_HURT = "vvvvvv_hurt" # Just called "sad" on the site for some reason
    VVVVVV_CHECKPOINT = "vvvvvv_checkpoint"
    VVVVVV_FLASH = "vvvvvv_flash"
    # Terraria
    TERRARIA_STAR = "terraria_star"
    TERRARIA_SHATTER = "terraria_pot"
    TERRARIA_REFORGE = "terraria_reforge"
    TERRARIA_GUITAR = "terraria_guitar"
    TERRARIA_HEAVY_GUITAR = "terraria_axe"
    # Celeste
    CELESTE_DASH = "celeste_dash"
    CELESTE_DEATH = "celeste_death"
    CELESTE_SPRING = "celeste_spring"
    CELESTE_DASH_DIAMOND = "celeste_diamond"
    # AMOGUS
    EMERGENCY_MEETING = "amogus_emergency"
    AMOGUS_KILL = "amogus_kill"
    AMONGUS = "amongus"
    AMOGUS_DRIP = "amongdrip"
    AMOGUS = "amogus"
    # Minecraft
    MC_KABLOOEY = "minecraft_explosion"
    MC_ANVIL = "minecraft_anvil"
    MC_BELL = "minecraft_bell"
    # Minecraft noteblocks
    NB_HARP = "noteblock_harp"
    NB_BASS = "noteblock_bass"
    NB_SNARE = "noteblock_snare"
    NB_CLICK = "noteblock_click"
    NB_BELL = "noteblock_bell"
    NB_BANJO = "noteblock_banjo"
    NB_BIT = "noteblock_bit"
    NB_CHIME = "noteblock_chime"
    NB_XYLOPHONE = "noteblock_xylophone"
    NB_GUITAR = "noteblock_guitar"
    NB_FLUTE = "noteblock_flute"
    NB_PLING = "noteblock_pling"

MIDI_TO_SFX_PRE = {
    # Pianos
    (1, 2, 3, 4): SFX.NB_PLING,
    (5, 6): SFX.UT_ENCOUNTER,
    (7, 8): SFX.NB_HARP,
    # Chromatic Percussion
    (10,): SFX.GD_DIAMOND,
    (9, 11, 12): SFX.MC_BELL,
    (13, 14): SFX.TERRARIA_REFORGE,
    (15, 16): SFX.DING,
    # Organs
    (17, 18, 19, 20, 21, 22, 24): SFX.EMERGENCY_MEETING,
    (23,): SFX.MP_BABBY,
    # Guitars
    (25, 26): SFX.WHAT_THE_HELL_WAS_THAT,
    (27, 28, 29): SFX.MP_PLANE,
    (30, 31, 32): SFX.MP_SWAN,
    # Bass
    (33, 34, 35): SFX.WHAT_THE_HELL_WAS_THAT,
    (36, 37, 38): SFX.SMW_BOSS_STOMP,
    (39, 40): SFX.MEGALOVANIA_NOTE,
    # Strings
    (41, 42, 43, 44): SFX.SM64_OUCHY,
    (45, 46, 48): SFX.MP_STAR,
    (47,): SFX.NB_HARP,
    # Ensemble
    (49, 50, 51, 52): SFX.MP_STAR,
    (53,): SFX.AMOGUS,
    (54,): SFX.OOF,
    (56,): SFX.SANS,
    (55,): SFX.AMONGUS,
    # Brass
    (57, 60, 61, 62): SFX.SM64_BUP,
    (58,): SFX.AIRHORN,
    (59,): SFX.HOO,
    (63, 64): SFX.UT_VANISH,
    # Reed
    (65, 66, 67, 68, 69): SFX.ULTRA_INSTINCT,
    (70,): SFX.SM64_BUP,
    (71, 72): SFX.SM64_THWOMP,
    # Pipe
    (73, 74, 76): SFX.UT_BORK,
    (75,): SFX.VVVVVV_HURT,
    (77, 78, 80): SFX.TERRARIA_SHATTER,
    (79,): SFX.SAMSUNG_WHISTLE,
    # Synth leads
    (81, 82, 83, 84, 85, 87): SFX.SMW_1UP,
    (86,): SFX.SM64_BUP,
    (88,): SFX.SMW_STEEL_DRUM,
    # Synth pads
    (89, 90, 91): SFX.TWANY_WAN,
    (92, 95): SFX.SMM_SCREAM,
    (93, 94, 96): SFX.BRUH,
    # Synth effects
    (97,): SFX.RD_SHAKE,
    (98,): SFX.YODA_DIES,
    (99, 100, 101, 103, 104): SFX.MC_CAVE,
    (102,): SFX.SUBALUWA,
    # Ethic
    (105, 106, 107, 108, 109, 110, 111, 112): SFX.PAN, # Forgot to ask lyxal for these, whoops! :b
    # Percussive
    (113, 114): SFX.MC_BELL,
    (115,): SFX.SMW_STEEL_DRUM,
    (116,): SFX.RD_TONK,
    (118,): SFX.RD_TOM_DRUM,
    (117, 119): SFX.RD_DRUM,
    (120,): SFX.PUFFERFISH_AUGH,
    # Sound effects
    (121,): SFX.MP_DOG,
    (122,): SFX.YODA_DIES, # That's what breathing sounds like, right? Yoda dying?
    (123,): SFX.ADOFAI_ICE,
    (124,): SFX.SAMSUNG_WHISTLE,
    (125,): SFX.SCREAMING_DOG, # The ideal ringtone
    (126,): SFX.MR_KRAAAAAAAABS,
    (127,): SFX.CLAP,
    (128,): SFX.HITMARKER
}
MIDI_TO_SFX = {}
# Janky ass conversion
for instruments in MIDI_TO_SFX_PRE:
    for instrument in instruments:
        MIDI_TO_SFX[instrument] = MIDI_TO_SFX_PRE[instruments]
