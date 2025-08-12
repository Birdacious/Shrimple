entry_strokes={ # TODO maybe implement later
    "HR"        : {"prefix":"",
                   "suffix":""},

    "TPH*"      : {"prefix":"{-|}", #capitalise first letter
                   "suffix":""},

    "KAPS"      : {"prefix":"{mode:caps}", #capitalise everything
                   "suffix":"{mode:reset}"}
}
exit_strokes={
    "HR"
}
overrides={
  # RHS lone spellings are symbols. If you want to type a lone letter, use LHS.
  "#":   "0",
  "-BG": "*",
  "-P":  ".",
  "-PL": "'",
  "-T":  "<",
  "-G":  "-",
  "-S":  "_",
  "-D":  ",",

  "-F":  " ",

  # RHS lone spellings + -L. NOTE: FR is an extra space.
  "#-L":   "{#Tab}",
  "*LG":   "^",
  "-PLZ":  "!",
  "-PLSZ": "(",
  "-LT":   ")",
  "-LG":   "|",
  "-LS":   "$",
  "-LD":   "/",

  "-FR":   " ",

  # RHS lone double-taps
  "HA*ERB":   "#",
  "OEU":      "/",
  "STPH-FPT": ":",
  "KR*GS":    "\"",
  "TKPWR*PB": ">",
  "PHR*US":   "+",
  "KW*":      "=",
  "STPH*FPT": ";",

  # RHS lone double-taps + -L
  "HA*ERBL":   "@",
  "OEUL":      "%",
  "STPH-FPLT": "`",
  "KR*LGS":    "[",
  "TKPWR*PBL": "]",
  "PHR*ULS":   "&",
  "KW*L":      "~",
  "STPH*FPLT": "?",

  # RHS lone cross-deadzone taps + -L
  "-PLT": "\\{",
  "-PBLT": "\\}"

}
starters={
    "" : "",

    # A        a
    "PW":     "b",
    "KR":     "c",
    "TK":     "d",
    # E        e
    "TP":     "f",
    "TKPW":   "g",
    "H":      "h",
    # EU       i
    "SKWR":   "j",
    "K":      "k",
    #"HR":     "l", # If alone, exits Shrimple.
    "PH":     "m",
    "TPH":    "n",
    # O        o
    "P":      "p",
    "KW":     "q",
    "R":      "r",
    "S":      "s",
    "T":      "t",
    # U        u
    "SR":     "v",
    "W":      "w",
    "KP":     "x",
    "KWR":    "y",
    "STKPW":  "z",

    "PWHR":   "bl",
    "PWR":    "br",
    "KH":     "ch",
    "KHR":    "cl",
    #"KR":    "cr",  # TODO: this is common enough that maybe should change the fingerspelling of c
    "TKHR":   "del",
    "TKR":    "dr",
    "TPHR":   "fl",
    "TPR":    "fr",
    "TKPWHR": "gl",
    "TKPWR":  "gr",
    #"KL":    "kl",
    #"KR":    "kr",
    "PHR":    "pl",
    "PR":     "pr",
    "KWHR":   "qu",  # meh idk
    #"KW":    "qu",
    "SKR":    "sc",
    #"SKR":   "scr", # TODO: this is common enough that maybe should change the fingerspelling of c
    #"SH":    "sh",  # Overridden by "8"
    "SKHR":   "shr", # Josiah theory
    #"SK":    "sk",  # Overriden by "2"
    #"SHR":   "sl",  # Josiah theory; overridden by "5"
    #"SPH":   "sm",  # Overridden by "4"
    "STPH":   "sn",
    #"SP":    "sp",  # Overriden by "3"
    "SPR":    "spr",
    "SPHR":   "spl",
    "SKW":    "squ",
    #"ST":    "st",  # Overridden by "6"
    "STR":    "str",
    "TH":     "th",
    "THR":    "thr",
    "TR":     "tr",

    # TODO add @ key to lhs, to differentiate lhs and rhs "#"
    # As it is now, can't type "0" or "1" two-handed.
    #"@":    "0",
    #"@S":   "1",
    "SK":    "2",
    "SP":    "3",
    "SPH":   "4",
    "SHR":   "5",
    "ST":    "6",
    "STPKW": "7",
    "SH":    "8",
    "STK":   "9",
}
vowels={
    "-":"",
    "":"",

    "A":    "a",
    "O":    "o",
    "E":    "e",
    "U":    "u",

    "EU":   "i",
    #"*EU": "eu",
    "*EU":  "y",
    "AEU":  "ai",
    "*AEU": "ay",
    "OEU":  "oi",
    "*OEU": "oy",

    "AO":   "oo",
    "AE":   "ea",
    "AOE":  "ee",

    "*OE":  "ow",
    "*OU":  "ow",

    "AOEU": "i[e]",
    "AOU":  "u[e]",
    "AEU":  "a[e]",
    "AU":   "au",

    "OE":   "o[e]",
    "OU":   "ou",
}
enders={
    "":"",
    #"*":"", #asterisk on its own is invalid

    # A      a
    "B":    "b",
    "RBG":  "c", # meh
    #"SZ":  "c", # maybe?
    "SZ":   "ss",
    "D":    "d",
    # E      e
    "F":    "f",
    "G":    "g",
    "RB":   "h",
    #"RB":  "sh", # unless AU to make it rb carb barb
    # EU     i
    "PBLG": "j",
    "BG":   "k",
    "L":    "l",
    "PL":   "m",
    "PB":   "n",
    # O      o
    "P":    "p",
    # ???   "q",
    "R":    "r", # If alone, repeats last stroke.
    "S":    "s",
    "T":    "t",
    # U      u
    "FB":   "v",
    # ???   "w",
    "BGS":  "x",
    "Z":    "z",

    #"FP":"ch", # Overridden by "3"
    #"FT":"ft", # Overridden by "6"
    "*FT":"st",

    "*T":"th",
    "TD":"ted",
    "*TD":"thed",
    "TS":"ts",

    #"*PL":"mp", # IDK, I need to think about -mp more. FRP or *PL?
    #"FRPL":"mpl",
    #"FRB":"mb",
    #"FRL":"ml",
    #"FRBL":"mbl",
    "FRPB":"rch",

    "PBG":"ng",
    "*PBG":"nk",
    "*BG":"ck",
    "*BGD":"cked",
    "BGT":"cket",
    "BGTS":"ckets",
    "RBG":"rk",
    "RBGT":"rket",
    "RBGTS":"rkets",

    "GT":"ght",
    "GTS":"ghts",

    "#":   "0",
    "#F":  "1",
    "FBG": "2",
    "FP":  "3",
    "FPL": "4",
    "FL":  "5",
    "FT":  "6",
    "FG":  "7",
    "FS":  "8",
    "FD":  "9",
}

import re
LONGEST_KEY = 1
def lookup(chord):
    if len(chord) != 1: raise KeyError
    assert len(chord) <= LONGEST_KEY

    if chord[0] ==      'HR': return "{PLOVER:END_SOLO_DICT}"
    if chord[0] ==  'PHOUPL': return "{PLOVER:END_SOLO_DICT}{PLOVER:SOLO_DICT:+mouse_mode.json,+suppress_untranslates.py,+mouse-modifiers.py,+repeat_last.json}"
    if chord[0] in overrides:
      out = overrides[chord[0]]
      if '{' == out[0]: return        out 
      else            : return '{^' + out + '^}'

    match = re.fullmatch(r'(#?)([STKPWHR]*)([AO]*)[-]?([*]?)([EU]*)([FRPBLGTSDZ]*)', chord[0])
    if match is None: raise KeyError
    (num, lhs, vowel1, asterisk, vowel2, rhs) = match.groups()

    out = '{^' + starters[lhs] + vowels[vowel1+vowel2] + enders[num+asterisk+rhs] + '^}'
    if num=='#' and (lhs!='' or vowels!=''): out = out.replace('0','').upper()

    return out
