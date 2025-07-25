import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers




encoder_handler = EncoderHandler()

keyboard = KMKKeyboard()

keyboard.modules.append(encoder_handler)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(Layers())

encoder_handler.pins = [
    (board.GP0,board.GP1,None)
]
encoder_handler.map = [
    [(KC.VOLD,KC.VOLU,None)]
]


layer = KC.MO(1)

keyboard.col_pins = (board.GP16,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,board.GP22,board.GP26,board.GP27,board.GP28,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP10,board.GP9,board.GP8)
keyboard.row_pins = (board.GP2,board.GP3,board.GP4,board.GP5,board.GP7,board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESC,KC.N6,None,None,None,None,None,None,None,None,None,None,None,None,KC.PSCR,KC.SLCK,KC.PAUSE,KC.MUTE,
     KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINS,KC.EQUAL,KC.BSPACE,KC.INS,KC.HOME,KC.PGUP,KC.F13,KC.F14,
     KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.U,KC.I,KC.O,KC.P,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,KC.DEL,KC.END,KC.PGDN,KC.F23,KC.F16,
     KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.ENTER,None,None,None,KC.F17,KC.F18,
     KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,None,KC.RSHIFT,None,KC.UP,None,KC.F19,KC.F20,
     KC.LCTRL,KC.LWIN,KC.LALT,None,None,KC.SPACE,KC.Y,None,None,KC.RALT,layer,KC.RWIN,KC.RCTRL,KC.LEFT,KC.DOWN,KC.RIGHT,KC.F21,KC.F22],
    

    [KC.ESC,KC.N6,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.PSCR,KC.SLCK,KC.PAUSE,KC.MUTE,
     KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINS,KC.EQUAL,KC.BSPACE,KC.INS,KC.HOME,KC.PGUP,KC.F13,KC.F14,
     KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.U,KC.I,KC.O,KC.P,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,KC.DEL,KC.END,KC.PGDN,KC.F23,KC.F16,
     KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.ENTER,None,None,None,KC.F17,KC.F18,
     KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,None,KC.RSHIFT,None,KC.UP,None,KC.F19,KC.F20,
     KC.LCTRL,KC.LWIN,KC.LALT,None,None,KC.SPACE,KC.Y,None,None,KC.RALT,layer,KC.RWIN,KC.RCTRL,KC.LEFT,KC.DOWN,KC.RIGHT,KC.F21,KC.F22]
]

if __name__ == "__main__":
    keyboard.go()