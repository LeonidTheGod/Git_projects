# NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# TONALS = ['C', 'G', 'D',  'A', 'E',  'B',  'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F',
#           'Am', 'Em', 'Bm', 'F#m', 'C#m', 'G#m', 'Ebm', 'Bbm', 'Fm', 'Cm', 'Gm', 'Dm']

CIRCLES = {
    'All':   'all.jpg',
    'Am':    'am.jpg',
    'Ab':    'ab.jpg',
    'A':    'a.jpg',
    'B':    'b.jpg',
    'Bm':    'bm.jpg',
    'Bb':    'bb.jpg',
    'Bbm':    'bbm.jpg',
    'Cm':    'cm.jpg',
    'C#m':    'c#m.jpg',
    'C':    'c.jpg',
    'Dm':    'dm.jpg',
    'D':    'd.jpg',
    'Db':    'db.jpg',
    'Em':    'em.jpg',
    'E':    'e.jpg',
    'Eb':    'eb.jpg',
    'Ebm':    'ebm.jpg',
    'Fm':    'fm.jpg',
    'F#m':    'f#m.jpg',
    'F':    'f.jpg',
    'Gm':    'gm.jpg',
    'G#m':    'g#m.jpg',
    'Gb':    'gb.jpg',
    'G':       'g.jpg'

}

RECT_FOR_BUTTONS = {
    'All': [[130,255], [130,255]],

    'Am':  [[170,215], [70,125]],
    'Em':  [[220,265], [85,123]],
    'Bm':  [[265,303], [125,168]],
    'F#m': [[265,313], [170,217]],  
    'C#m': [[270,305], [217,260]],  
    'G#m': [[218,262], [253,295]],  
    'Ebm': [[170,215], [260,312]],
    'Bbm': [[125,170], [260,302]],
    'Fm':  [[90,134],  [217,260]],
    'Cm':  [[70,130],  [170,217]],
    'Gm':  [[85,130],  [125,168]],
    'Dm':  [[130,168], [85,123]],

    'C': [[160,225], [5,65]],
    'G': [[230,305], [20,80]],
    'D': [[306,365], [82,150]],
    'A': [[320,378], [152,210]],
    'E': [[305,365], [212,295]],
    'B': [[235,305], [296,360]],
    'Gb':[[160,230], [312,365]],
    'Db':[[85,150], [296,360]],
    'Ab':[[28,88], [212,295]],
    'Eb':[[7,65], [152,210]],
    'Bb':[[22,85], [82,150]],
    'F': [[85,152], [15,80]]

}

TONALS_NOTES = {

    None:[],
    'All': ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],

    'Am': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'C':  ['C', 'D', 'E', 'F', 'G', 'A', 'B'],

    'Em': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'G':  ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],

    'Bm': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    'D':  ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],

    'F#m': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'A':   ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],

    'C#m': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'E':   ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],

    'G#m': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
    'B':   ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],

    'Ebm': ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#'],
    'Gb':  ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],

    'Bbm': ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#'],
    'Db':  ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],

    'Fm':  ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#'],
    'Ab':  ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'],

    'Cm':  ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'],
    'Eb':  ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],

    'Gm':  ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
    'Bb':  ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],

    'Dm':  ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
    'F':   ['F', 'G', 'A', 'A#', 'C', 'D', 'E']

}

grif_field = [
            ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
            ['B', 'C', 'C#', 'D', 'D#', 'E', 'F',
                'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
            ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#',
                'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A'],
            ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
                'A', 'A#', 'B', 'C', 'C#', 'D', 'D#','E'],
            ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#',
                'E', 'F', 'F#', 'G', 'G#', 'A', 'A#','B'],
            ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#']
        ]

X_ES = [
    51,
    162,
    310,
    442,
    565,
    684,
    791,
    895,
    992,
    1082,
    1171,
    1249,
    1326,
    1401,
    1468]

X_ES_NUM = {
    51: 0,
    162: 1,
    310: 2,
    442: 3,
    565: 4,
    684: 5,
    791: 6,
    895: 7,
    992: 8,
    1082: 9,
    1171: 10,
    1249: 11,
    1326: 12,
    1401: 13,
    1468: 14}

Y_ES = [
    35,
    72,
    109,
    148,
    187,
    224]

Y_ES_NUM = {
    35: 0,
    72: 1,
    109: 2,
    148: 3,
    187: 4,
    224: 5}
