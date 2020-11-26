#!/usr/bin/python3
# LED Wall Template
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 256

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# Pixel Mapping for LED Wall
px_cord_A1 = 255
px_cord_B1 = 254
px_cord_C1 = 253
px_cord_D1 = 252
px_cord_E1 = 251
px_cord_F1 = 250
px_cord_G1 = 249
px_cord_H1 = 248
px_cord_I1 = 247
px_cord_J1 = 246
px_cord_K1 = 245
px_cord_L1 = 244
px_cord_M1 = 243
px_cord_N1 = 242
px_cord_O1 = 241
px_cord_O2 = 240
px_cord_N2 = 239
px_cord_M2 = 238
px_cord_L2 = 237
px_cord_K2 = 236
px_cord_J2 = 235
px_cord_I2 = 234
px_cord_H2 = 233
px_cord_G2 = 232
px_cord_F2 = 231
px_cord_E2 = 230
px_cord_D2 = 229
px_cord_C2 = 228
px_cord_B2 = 227
px_cord_A2 = 226
px_cord_A3 = 225
px_cord_B3 = 224
px_cord_C3 = 223
px_cord_D3 = 222
px_cord_E3 = 221
px_cord_F3 = 220
px_cord_G3 = 219
px_cord_H3 = 218
px_cord_I3 = 217
px_cord_J3 = 216
px_cord_K3 = 215
px_cord_L3 = 214
px_cord_M3 = 213
px_cord_N3 = 212
px_cord_O3 = 211
px_cord_O4 = 210
px_cord_N4 = 209
px_cord_M4 = 208
px_cord_L4 = 207
px_cord_K4 = 206
px_cord_J4 = 205
px_cord_I4 = 204
px_cord_H4 = 203
px_cord_G4 = 202
px_cord_F4 = 201
px_cord_E4 = 200
px_cord_D4 = 199
px_cord_C4 = 198
px_cord_B4 = 197
px_cord_A4 = 196
px_cord_A5 = 195
px_cord_B5 = 194
px_cord_C5 = 193
px_cord_D5 = 192
px_cord_E5 = 191
px_cord_F5 = 190
px_cord_G5 = 189
px_cord_H5 = 188
px_cord_I5 = 187
px_cord_J5 = 186
px_cord_K5 = 185
px_cord_L5 = 184
px_cord_M5 = 183
px_cord_N5 = 182
px_cord_O5 = 181
px_cord_O6 = 180
px_cord_N6 = 179
px_cord_M6 = 178
px_cord_L6 = 177
px_cord_K6 = 176
px_cord_J6 = 175
px_cord_I6 = 174
px_cord_H6 = 173
px_cord_G6 = 172
px_cord_F6 = 171
px_cord_E6 = 170
px_cord_D6 = 169
px_cord_C6 = 168
px_cord_B6 = 167
px_cord_A6 = 166
px_cord_A7 = 165
px_cord_B7 = 164
px_cord_C7 = 163
px_cord_D7 = 162
px_cord_E7 = 161
px_cord_F7 = 160
px_cord_G7 = 159
px_cord_H7 = 158
px_cord_I7 = 157
px_cord_J7 = 156
px_cord_K7 = 155
px_cord_L7 = 154
px_cord_M7 = 153
px_cord_N7 = 152
px_cord_O7 = 151
px_cord_O8 = 150
px_cord_N8 = 149
px_cord_M8 = 148
px_cord_L8 = 147
px_cord_K8 = 146
px_cord_J8 = 145
px_cord_I8 = 144
px_cord_H8 = 143
px_cord_G8 = 142
px_cord_F8 = 141
px_cord_E8 = 140
px_cord_D8 = 139
px_cord_C8 = 138
px_cord_B8 = 137
px_cord_A8 = 136
px_cord_A9 = 135
px_cord_B9 = 134
px_cord_C9 = 133
px_cord_D9 = 132
px_cord_E9 = 131
px_cord_F9 = 130
px_cord_G9 = 129
px_cord_H9 = 128
px_cord_I9 = 127
px_cord_J9 = 126
px_cord_K9 = 125
px_cord_L9 = 124
px_cord_M9 = 123
px_cord_N9 = 122
px_cord_O9 = 121
px_cord_O10 = 120
px_cord_N10 = 119
px_cord_M10 = 118
px_cord_L10 = 117
px_cord_K10 = 116
px_cord_J10 = 115
px_cord_I10 = 114
px_cord_H10 = 113
px_cord_G10 = 112
px_cord_F10 = 111
px_cord_E10 = 110
px_cord_D10 = 109
px_cord_C10 = 108
px_cord_B10 = 107
px_cord_A10 = 106
px_cord_A11 = 105
px_cord_B11 = 104
px_cord_C11 = 103
px_cord_D11 = 102
px_cord_E11 = 101
px_cord_F11 = 100
px_cord_G11 = 99
px_cord_H11 = 98
px_cord_I11 = 97
px_cord_J11 = 96
px_cord_K11 = 95
px_cord_L11 = 94
px_cord_M11 = 93
px_cord_N11 = 92
px_cord_O11 = 91
px_cord_O12 = 90
px_cord_N12 = 89
px_cord_M12 = 88
px_cord_L12 = 87
px_cord_K12 = 86
px_cord_J12 = 85
px_cord_I12 = 84
px_cord_H12 = 83
px_cord_G12 = 82
px_cord_F12 = 81
px_cord_E12 = 80
px_cord_D12 = 79
px_cord_C12 = 78
px_cord_B12 = 77
px_cord_A12 = 76
px_cord_A13 = 75
px_cord_B13 = 74
px_cord_C13 = 73
px_cord_D13 = 72
px_cord_E13 = 71
px_cord_F13 = 70
px_cord_G13 = 69
px_cord_H13 = 68
px_cord_I13 = 67
px_cord_J13 = 66
px_cord_K13 = 65
px_cord_L13 = 64
px_cord_M13 = 63
px_cord_N13 = 62
px_cord_O13 = 61
px_cord_O14 = 60
px_cord_N14 = 59
px_cord_M14 = 58
px_cord_L14 = 57
px_cord_K14 = 56
px_cord_J14 = 55
px_cord_I14 = 54
px_cord_H14 = 53
px_cord_G14 = 52
px_cord_F14 = 51
px_cord_E14 = 50
px_cord_D14 = 49
px_cord_C14 = 48
px_cord_B14 = 47
px_cord_A14 = 46
px_cord_A15 = 45
px_cord_B15 = 44
px_cord_C15 = 43
px_cord_D15 = 42
px_cord_E15 = 41
px_cord_F15 = 40
px_cord_G15 = 39
px_cord_H15 = 38
px_cord_I15 = 37
px_cord_J15 = 36
px_cord_K15 = 35
px_cord_L15 = 34
px_cord_M15 = 33
px_cord_N15 = 32
px_cord_O15 = 31
px_cord_O16 = 30
px_cord_N16 = 29
px_cord_M16 = 28
px_cord_L16 = 27
px_cord_K16 = 26
px_cord_J16 = 25
px_cord_I16 = 24
px_cord_H16 = 23
px_cord_G16 = 22
px_cord_F16 = 21
px_cord_E16 = 20
px_cord_D16 = 19
px_cord_C16 = 18
px_cord_B16 = 17
px_cord_A16 = 16
px_cord_A17 = 15
px_cord_B17 = 14
px_cord_C17 = 13
px_cord_D17 = 12
px_cord_E17 = 11
px_cord_F17 = 10
px_cord_G17 = 9
px_cord_H17 = 8
px_cord_I17 = 7
px_cord_J17 = 6
px_cord_K17 = 5
px_cord_L17 = 4
px_cord_M17 = 3
px_cord_N17 = 2
px_cord_O17 = 1
px_cord_CONTROL0 = 0

def clear_all_pixels():
	pixels[px_cord_A1]= (0, 0, 0)
	pixels[px_cord_B1]= (0, 0, 0)
	pixels[px_cord_C1]= (0, 0, 0)
	pixels[px_cord_D1]= (0, 0, 0)
	pixels[px_cord_E1]= (0, 0, 0)
	pixels[px_cord_F1]= (0, 0, 0)
	pixels[px_cord_G1]= (0, 0, 0)
	pixels[px_cord_H1]= (0, 0, 0)
	pixels[px_cord_I1]= (0, 0, 0)
	pixels[px_cord_J1]= (0, 0, 0)
	pixels[px_cord_K1]= (0, 0, 0)
	pixels[px_cord_L1]= (0, 0, 0)
	pixels[px_cord_M1]= (0, 0, 0)
	pixels[px_cord_N1]= (0, 0, 0)
	pixels[px_cord_O1]= (0, 0, 0)
	pixels[px_cord_O2]= (0, 0, 0)
	pixels[px_cord_N2]= (0, 0, 0)
	pixels[px_cord_M2]= (0, 0, 0)
	pixels[px_cord_L2]= (0, 0, 0)
	pixels[px_cord_K2]= (0, 0, 0)
	pixels[px_cord_J2]= (0, 0, 0)
	pixels[px_cord_I2]= (0, 0, 0)
	pixels[px_cord_H2]= (0, 0, 0)
	pixels[px_cord_G2]= (0, 0, 0)
	pixels[px_cord_F2]= (0, 0, 0)
	pixels[px_cord_E2]= (0, 0, 0)
	pixels[px_cord_D2]= (0, 0, 0)
	pixels[px_cord_C2]= (0, 0, 0)
	pixels[px_cord_B2]= (0, 0, 0)
	pixels[px_cord_A2]= (0, 0, 0)
	pixels[px_cord_A3]= (0, 0, 0)
	pixels[px_cord_B3]= (0, 0, 0)
	pixels[px_cord_C3]= (0, 0, 0)
	pixels[px_cord_D3]= (0, 0, 0)
	pixels[px_cord_E3]= (0, 0, 0)
	pixels[px_cord_F3]= (0, 0, 0)
	pixels[px_cord_G3]= (0, 0, 0)
	pixels[px_cord_H3]= (0, 0, 0)
	pixels[px_cord_I3]= (0, 0, 0)
	pixels[px_cord_J3]= (0, 0, 0)
	pixels[px_cord_K3]= (0, 0, 0)
	pixels[px_cord_L3]= (0, 0, 0)
	pixels[px_cord_M3]= (0, 0, 0)
	pixels[px_cord_N3]= (0, 0, 0)
	pixels[px_cord_O3]= (0, 0, 0)
	pixels[px_cord_O4]= (0, 0, 0)
	pixels[px_cord_N4]= (0, 0, 0)
	pixels[px_cord_M4]= (0, 0, 0)
	pixels[px_cord_L4]= (0, 0, 0)
	pixels[px_cord_K4]= (0, 0, 0)
	pixels[px_cord_J4]= (0, 0, 0)
	pixels[px_cord_I4]= (0, 0, 0)
	pixels[px_cord_H4]= (0, 0, 0)
	pixels[px_cord_G4]= (0, 0, 0)
	pixels[px_cord_F4]= (0, 0, 0)
	pixels[px_cord_E4]= (0, 0, 0)
	pixels[px_cord_D4]= (0, 0, 0)
	pixels[px_cord_C4]= (0, 0, 0)
	pixels[px_cord_B4]= (0, 0, 0)
	pixels[px_cord_A4]= (0, 0, 0)
	pixels[px_cord_A5]= (0, 0, 0)
	pixels[px_cord_B5]= (0, 0, 0)
	pixels[px_cord_C5]= (0, 0, 0)
	pixels[px_cord_D5]= (0, 0, 0)
	pixels[px_cord_E5]= (0, 0, 0)
	pixels[px_cord_F5]= (0, 0, 0)
	pixels[px_cord_G5]= (0, 0, 0)
	pixels[px_cord_H5]= (0, 0, 0)
	pixels[px_cord_I5]= (0, 0, 0)
	pixels[px_cord_J5]= (0, 0, 0)
	pixels[px_cord_K5]= (0, 0, 0)
	pixels[px_cord_L5]= (0, 0, 0)
	pixels[px_cord_M5]= (0, 0, 0)
	pixels[px_cord_N5]= (0, 0, 0)
	pixels[px_cord_O5]= (0, 0, 0)
	pixels[px_cord_O6]= (0, 0, 0)
	pixels[px_cord_N6]= (0, 0, 0)
	pixels[px_cord_M6]= (0, 0, 0)
	pixels[px_cord_L6]= (0, 0, 0)
	pixels[px_cord_K6]= (0, 0, 0)
	pixels[px_cord_J6]= (0, 0, 0)
	pixels[px_cord_I6]= (0, 0, 0)
	pixels[px_cord_H6]= (0, 0, 0)
	pixels[px_cord_G6]= (0, 0, 0)
	pixels[px_cord_F6]= (0, 0, 0)
	pixels[px_cord_E6]= (0, 0, 0)
	pixels[px_cord_D6]= (0, 0, 0)
	pixels[px_cord_C6]= (0, 0, 0)
	pixels[px_cord_B6]= (0, 0, 0)
	pixels[px_cord_A6]= (0, 0, 0)
	pixels[px_cord_A7]= (0, 0, 0)
	pixels[px_cord_B7]= (0, 0, 0)
	pixels[px_cord_C7]= (0, 0, 0)
	pixels[px_cord_D7]= (0, 0, 0)
	pixels[px_cord_E7]= (0, 0, 0)
	pixels[px_cord_F7]= (0, 0, 0)
	pixels[px_cord_G7]= (0, 0, 0)
	pixels[px_cord_H7]= (0, 0, 0)
	pixels[px_cord_I7]= (0, 0, 0)
	pixels[px_cord_J7]= (0, 0, 0)
	pixels[px_cord_K7]= (0, 0, 0)
	pixels[px_cord_L7]= (0, 0, 0)
	pixels[px_cord_M7]= (0, 0, 0)
	pixels[px_cord_N7]= (0, 0, 0)
	pixels[px_cord_O7]= (0, 0, 0)
	pixels[px_cord_O8]= (0, 0, 0)
	pixels[px_cord_N8]= (0, 0, 0)
	pixels[px_cord_M8]= (0, 0, 0)
	pixels[px_cord_L8]= (0, 0, 0)
	pixels[px_cord_K8]= (0, 0, 0)
	pixels[px_cord_J8]= (0, 0, 0)
	pixels[px_cord_I8]= (0, 0, 0)
	pixels[px_cord_H8]= (0, 0, 0)
	pixels[px_cord_G8]= (0, 0, 0)
	pixels[px_cord_F8]= (0, 0, 0)
	pixels[px_cord_E8]= (0, 0, 0)
	pixels[px_cord_D8]= (0, 0, 0)
	pixels[px_cord_C8]= (0, 0, 0)
	pixels[px_cord_B8]= (0, 0, 0)
	pixels[px_cord_A8]= (0, 0, 0)
	pixels[px_cord_A9]= (0, 0, 0)
	pixels[px_cord_B9]= (0, 0, 0)
	pixels[px_cord_C9]= (0, 0, 0)
	pixels[px_cord_D9]= (0, 0, 0)
	pixels[px_cord_E9]= (0, 0, 0)
	pixels[px_cord_F9]= (0, 0, 0)
	pixels[px_cord_G9]= (0, 0, 0)
	pixels[px_cord_H9]= (0, 0, 0)
	pixels[px_cord_I9]= (0, 0, 0)
	pixels[px_cord_J9]= (0, 0, 0)
	pixels[px_cord_K9]= (0, 0, 0)
	pixels[px_cord_L9]= (0, 0, 0)
	pixels[px_cord_M9]= (0, 0, 0)
	pixels[px_cord_N9]= (0, 0, 0)
	pixels[px_cord_O9]= (0, 0, 0)
	pixels[px_cord_O10] = (0, 0, 0)
	pixels[px_cord_N10] = (0, 0, 0)
	pixels[px_cord_M10] = (0, 0, 0)
	pixels[px_cord_L10] = (0, 0, 0)
	pixels[px_cord_K10] = (0, 0, 0)
	pixels[px_cord_J10] = (0, 0, 0)
	pixels[px_cord_I10] = (0, 0, 0)
	pixels[px_cord_H10] = (0, 0, 0)
	pixels[px_cord_G10] = (0, 0, 0)
	pixels[px_cord_F10] = (0, 0, 0)
	pixels[px_cord_E10] = (0, 0, 0)
	pixels[px_cord_D10] = (0, 0, 0)
	pixels[px_cord_C10] = (0, 0, 0)
	pixels[px_cord_B10] = (0, 0, 0)
	pixels[px_cord_A10] = (0, 0, 0)
	pixels[px_cord_A11] = (0, 0, 0)
	pixels[px_cord_B11] = (0, 0, 0)
	pixels[px_cord_C11] = (0, 0, 0)
	pixels[px_cord_D11] = (0, 0, 0)
	pixels[px_cord_E11] = (0, 0, 0)
	pixels[px_cord_F11] = (0, 0, 0)
	pixels[px_cord_G11] = (0, 0, 0)
	pixels[px_cord_H11] = (0, 0, 0)
	pixels[px_cord_I11] = (0, 0, 0)
	pixels[px_cord_J11] = (0, 0, 0)
	pixels[px_cord_K11] = (0, 0, 0)
	pixels[px_cord_L11] = (0, 0, 0)
	pixels[px_cord_M11] = (0, 0, 0)
	pixels[px_cord_N11] = (0, 0, 0)
	pixels[px_cord_O11] = (0, 0, 0)
	pixels[px_cord_O12] = (0, 0, 0)
	pixels[px_cord_N12] = (0, 0, 0)
	pixels[px_cord_M12] = (0, 0, 0)
	pixels[px_cord_L12] = (0, 0, 0)
	pixels[px_cord_K12] = (0, 0, 0)
	pixels[px_cord_J12] = (0, 0, 0)
	pixels[px_cord_I12] = (0, 0, 0)
	pixels[px_cord_H12] = (0, 0, 0)
	pixels[px_cord_G12] = (0, 0, 0)
	pixels[px_cord_F12] = (0, 0, 0)
	pixels[px_cord_E12] = (0, 0, 0)
	pixels[px_cord_D12] = (0, 0, 0)
	pixels[px_cord_C12] = (0, 0, 0)
	pixels[px_cord_B12] = (0, 0, 0)
	pixels[px_cord_A12] = (0, 0, 0)
	pixels[px_cord_A13] = (0, 0, 0)
	pixels[px_cord_B13] = (0, 0, 0)
	pixels[px_cord_C13] = (0, 0, 0)
	pixels[px_cord_D13] = (0, 0, 0)
	pixels[px_cord_E13] = (0, 0, 0)
	pixels[px_cord_F13] = (0, 0, 0)
	pixels[px_cord_G13] = (0, 0, 0)
	pixels[px_cord_H13] = (0, 0, 0)
	pixels[px_cord_I13] = (0, 0, 0)
	pixels[px_cord_J13] = (0, 0, 0)
	pixels[px_cord_K13] = (0, 0, 0)
	pixels[px_cord_L13] = (0, 0, 0)
	pixels[px_cord_M13] = (0, 0, 0)
	pixels[px_cord_N13] = (0, 0, 0)
	pixels[px_cord_O13] = (0, 0, 0)
	pixels[px_cord_O14] = (0, 0, 0)
	pixels[px_cord_N14] = (0, 0, 0)
	pixels[px_cord_M14] = (0, 0, 0)
	pixels[px_cord_L14] = (0, 0, 0)
	pixels[px_cord_K14] = (0, 0, 0)
	pixels[px_cord_J14] = (0, 0, 0)
	pixels[px_cord_I14] = (0, 0, 0)
	pixels[px_cord_H14] = (0, 0, 0)
	pixels[px_cord_G14] = (0, 0, 0)
	pixels[px_cord_F14] = (0, 0, 0)
	pixels[px_cord_E14] = (0, 0, 0)
	pixels[px_cord_D14] = (0, 0, 0)
	pixels[px_cord_C14] = (0, 0, 0)
	pixels[px_cord_B14] = (0, 0, 0)
	pixels[px_cord_A14] = (0, 0, 0)
	pixels[px_cord_A15] = (0, 0, 0)
	pixels[px_cord_B15] = (0, 0, 0)
	pixels[px_cord_C15] = (0, 0, 0)
	pixels[px_cord_D15] = (0, 0, 0)
	pixels[px_cord_E15] = (0, 0, 0)
	pixels[px_cord_F15] = (0, 0, 0)
	pixels[px_cord_G15] = (0, 0, 0)
	pixels[px_cord_H15] = (0, 0, 0)
	pixels[px_cord_I15] = (0, 0, 0)
	pixels[px_cord_J15] = (0, 0, 0)
	pixels[px_cord_K15] = (0, 0, 0)
	pixels[px_cord_L15] = (0, 0, 0)
	pixels[px_cord_M15] = (0, 0, 0)
	pixels[px_cord_N15] = (0, 0, 0)
	pixels[px_cord_O15] = (0, 0, 0)
	pixels[px_cord_O16] = (0, 0, 0)
	pixels[px_cord_N16] = (0, 0, 0)
	pixels[px_cord_M16] = (0, 0, 0)
	pixels[px_cord_L16] = (0, 0, 0)
	pixels[px_cord_K16] = (0, 0, 0)
	pixels[px_cord_J16] = (0, 0, 0)
	pixels[px_cord_I16] = (0, 0, 0)
	pixels[px_cord_H16] = (0, 0, 0)
	pixels[px_cord_G16] = (0, 0, 0)
	pixels[px_cord_F16] = (0, 0, 0)
	pixels[px_cord_E16] = (0, 0, 0)
	pixels[px_cord_D16] = (0, 0, 0)
	pixels[px_cord_C16] = (0, 0, 0)
	pixels[px_cord_B16] = (0, 0, 0)
	pixels[px_cord_A16] = (0, 0, 0)
	pixels[px_cord_A17] = (0, 0, 0)
	pixels[px_cord_B17] = (0, 0, 0)
	pixels[px_cord_C17] = (0, 0, 0)
	pixels[px_cord_D17] = (0, 0, 0)
	pixels[px_cord_E17] = (0, 0, 0)
	pixels[px_cord_F17] = (0, 0, 0)
	pixels[px_cord_G17] = (0, 0, 0)
	pixels[px_cord_H17] = (0, 0, 0)
	pixels[px_cord_I17] = (0, 0, 0)
	pixels[px_cord_J17] = (0, 0, 0)
	pixels[px_cord_K17] = (0, 0, 0)
	pixels[px_cord_L17] = (0, 0, 0)
	pixels[px_cord_M17] = (0, 0, 0)
	pixels[px_cord_N17] = (0, 0, 0)
	pixels[px_cord_O17] = (0, 0, 0)
	pixels[px_cord_CONTROL0] = (0, 0, 0)


def candy_cake_pos_1(wait):
	# Candy Cane Position 1
	pixels[px_cord_D5] = (255, 255, 255)
	pixels[px_cord_D6] = (255, 0, 0)
	pixels[px_cord_D7] = (255, 255, 255)
	pixels[px_cord_D8] = (255, 0, 0)

	pixels[px_cord_E3] = (255, 0, 0)
	pixels[px_cord_E4] = (255, 255, 255)
	pixels[px_cord_E5] = (255, 0, 0)
	pixels[px_cord_E6] = (255, 255, 255)
	pixels[px_cord_E7] = (255, 0, 0)
	pixels[px_cord_E8] = (255, 255, 255)

	pixels[px_cord_F3] = (255, 255, 255)
	pixels[px_cord_F4] = (255, 0, 0)

	pixels[px_cord_G3] = (255, 0, 0)
	pixels[px_cord_G4] = (255, 255, 255)

	pixels[px_cord_H3] = (255, 255, 255)
	pixels[px_cord_H4] = (255, 0, 0)

	pixels[px_cord_I3] = (255, 0, 0)
	pixels[px_cord_I4] = (255, 255, 255)

	pixels[px_cord_J3] = (255, 255, 255)
	pixels[px_cord_J4] = (255, 0, 0)
	pixels[px_cord_J5] = (255, 255, 255)
	pixels[px_cord_J6] = (255, 0, 0)
	pixels[px_cord_J7] = (255, 255, 255)
	pixels[px_cord_J8] = (255, 0, 0)
	pixels[px_cord_J9] = (255, 255, 255)
	pixels[px_cord_J10] = (255, 0, 0)
	pixels[px_cord_J11] = (255, 255, 255)
	pixels[px_cord_J12] = (255, 0, 0)
	pixels[px_cord_J13] = (255, 255, 255)
	pixels[px_cord_J14] = (255, 0, 0)
	pixels[px_cord_J15] = (255, 255, 255)
	pixels[px_cord_J16] = (255, 0, 0)
	pixels[px_cord_J17] = (255, 255, 255)

	pixels[px_cord_K5] = (255, 0, 0)
	pixels[px_cord_K6] = (255, 255, 255)
	pixels[px_cord_K7] = (255, 0, 0)
	pixels[px_cord_K8] = (255, 255, 255)
	pixels[px_cord_K9] = (255, 0, 0)
	pixels[px_cord_K10] = (255, 255, 255)
	pixels[px_cord_K11] = (255, 0, 0)
	pixels[px_cord_K12] = (255, 255, 255)
	pixels[px_cord_K13] = (255, 0, 0)
	pixels[px_cord_K14] = (255, 255, 255)
	pixels[px_cord_K15] = (255, 0, 0)
	pixels[px_cord_K16] = (255, 255, 255)
	pixels[px_cord_K17] = (255, 0, 0)

	pixels.show()
	time.sleep(wait)

def candy_cake_pos_2(wait):
	# Candy Cane Position 2
	pixels[px_cord_D5] = (255, 0, 0)
	pixels[px_cord_D6] = (255, 255, 255)
	pixels[px_cord_D7] = (255, 0, 0)
	pixels[px_cord_D8] = (255, 255, 255)

	pixels[px_cord_E3] = (255, 255, 255)
	pixels[px_cord_E4] = (255, 0, 0)
	pixels[px_cord_E5] = (255, 255, 255)
	pixels[px_cord_E6] = (255, 0, 0)
	pixels[px_cord_E7] = (255, 255, 255)
	pixels[px_cord_E8] = (255, 0, 0)

	pixels[px_cord_F3] = (255, 0, 0)
	pixels[px_cord_F4] = (255, 255, 255)

	pixels[px_cord_G3] = (255, 255, 255)
	pixels[px_cord_G4] = (255, 0, 0)

	pixels[px_cord_H3] = (255, 0, 0)
	pixels[px_cord_H4] = (255, 255, 255)

	pixels[px_cord_I3] = (255, 255, 255)
	pixels[px_cord_I4] = (255, 0, 0)

	pixels[px_cord_J3] = (255, 0, 0)
	pixels[px_cord_J4] = (255, 255, 255)
	pixels[px_cord_J5] = (255, 0, 0)
	pixels[px_cord_J6] = (255, 255, 255)
	pixels[px_cord_J7] = (255, 0, 0)
	pixels[px_cord_J8] = (255, 255, 255)
	pixels[px_cord_J9] = (255, 0, 0)
	pixels[px_cord_J10] = (255, 255, 255)
	pixels[px_cord_J11] = (255, 0, 0)
	pixels[px_cord_J12] = (255, 255, 255)
	pixels[px_cord_J13] = (255, 0, 0)
	pixels[px_cord_J14] = (255, 255, 255)
	pixels[px_cord_J15] = (255, 0, 0)
	pixels[px_cord_J16] = (255, 255, 255)
	pixels[px_cord_J17] = (255, 0, 0)

	pixels[px_cord_K5] = (255, 255, 255)
	pixels[px_cord_K6] = (255, 0, 0)
	pixels[px_cord_K7] = (255, 255, 255)
	pixels[px_cord_K8] = (255, 0, 0)
	pixels[px_cord_K9] = (255, 255, 255)
	pixels[px_cord_K10] = (255, 0, 0)
	pixels[px_cord_K11] = (255, 255, 255)
	pixels[px_cord_K12] = (255, 0, 0)
	pixels[px_cord_K13] = (255, 255, 255)
	pixels[px_cord_K14] = (255, 0, 0)
	pixels[px_cord_K15] = (255, 255, 255)
	pixels[px_cord_K16] = (255, 0, 0)
	pixels[px_cord_K17] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

def let_it_snow(wait):
	# Snowing Animation From Top Down
	pixels[px_cord_A1] = (255, 255, 255)
	pixels[px_cord_C1] = (255, 255, 255)
	pixels[px_cord_E1] = (255, 255, 255)
	pixels[px_cord_G1] = (255, 255, 255)
	pixels[px_cord_I1] = (255, 255, 255)
	pixels[px_cord_K1] = (255, 255, 255)
	pixels[px_cord_M1] = (255, 255, 255)
	pixels[px_cord_O1] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B2] = (255, 255, 255)
	pixels[px_cord_D2] = (255, 255, 255)
	pixels[px_cord_F2] = (255, 255, 255)
	pixels[px_cord_H2] = (255, 255, 255)
	pixels[px_cord_J2] = (255, 255, 255)
	pixels[px_cord_L2] = (255, 255, 255)
	pixels[px_cord_N2] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A3] = (255, 255, 255)
	pixels[px_cord_C3] = (255, 255, 255)
	pixels[px_cord_E3] = (255, 255, 255)
	pixels[px_cord_G3] = (255, 255, 255)
	pixels[px_cord_I3] = (255, 255, 255)
	pixels[px_cord_K3] = (255, 255, 255)
	pixels[px_cord_M3] = (255, 255, 255)
	pixels[px_cord_O3] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B4] = (255, 255, 255)
	pixels[px_cord_D4] = (255, 255, 255)
	pixels[px_cord_F4] = (255, 255, 255)
	pixels[px_cord_H4] = (255, 255, 255)
	pixels[px_cord_J4] = (255, 255, 255)
	pixels[px_cord_L4] = (255, 255, 255)
	pixels[px_cord_N4] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A5] = (255, 255, 255)
	pixels[px_cord_C5] = (255, 255, 255)
	pixels[px_cord_E5] = (255, 255, 255)
	pixels[px_cord_G5] = (255, 255, 255)
	pixels[px_cord_I5] = (255, 255, 255)
	pixels[px_cord_K5] = (255, 255, 255)
	pixels[px_cord_M5] = (255, 255, 255)
	pixels[px_cord_O5] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B6] = (255, 255, 255)
	pixels[px_cord_D6] = (255, 255, 255)
	pixels[px_cord_F6] = (255, 255, 255)
	pixels[px_cord_H6] = (255, 255, 255)
	pixels[px_cord_J6] = (255, 255, 255)
	pixels[px_cord_L6] = (255, 255, 255)
	pixels[px_cord_N6] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A7] = (255, 255, 255)
	pixels[px_cord_C7] = (255, 255, 255)
	pixels[px_cord_E7] = (255, 255, 255)
	pixels[px_cord_G7] = (255, 255, 255)
	pixels[px_cord_I7] = (255, 255, 255)
	pixels[px_cord_K7] = (255, 255, 255)
	pixels[px_cord_M7] = (255, 255, 255)
	pixels[px_cord_O7] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B8] = (255, 255, 255)
	pixels[px_cord_D8] = (255, 255, 255)
	pixels[px_cord_F8] = (255, 255, 255)
	pixels[px_cord_H8] = (255, 255, 255)
	pixels[px_cord_J8] = (255, 255, 255)
	pixels[px_cord_L8] = (255, 255, 255)
	pixels[px_cord_N8] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A9] = (255, 255, 255)
	pixels[px_cord_C9] = (255, 255, 255)
	pixels[px_cord_E9] = (255, 255, 255)
	pixels[px_cord_G9] = (255, 255, 255)
	pixels[px_cord_I9] = (255, 255, 255)
	pixels[px_cord_K9] = (255, 255, 255)
	pixels[px_cord_M9] = (255, 255, 255)
	pixels[px_cord_O9] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B10] = (255, 255, 255)
	pixels[px_cord_D10] = (255, 255, 255)
	pixels[px_cord_F10] = (255, 255, 255)
	pixels[px_cord_H10] = (255, 255, 255)
	pixels[px_cord_J10] = (255, 255, 255)
	pixels[px_cord_L10] = (255, 255, 255)
	pixels[px_cord_N10] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)	

	pixels[px_cord_A11] = (255, 255, 255)
	pixels[px_cord_C11] = (255, 255, 255)
	pixels[px_cord_E11] = (255, 255, 255)
	pixels[px_cord_G11] = (255, 255, 255)
	pixels[px_cord_I11] = (255, 255, 255)
	pixels[px_cord_K11] = (255, 255, 255)
	pixels[px_cord_M11] = (255, 255, 255)
	pixels[px_cord_O11] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B12] = (255, 255, 255)
	pixels[px_cord_D12] = (255, 255, 255)
	pixels[px_cord_F12] = (255, 255, 255)
	pixels[px_cord_H12] = (255, 255, 255)
	pixels[px_cord_J12] = (255, 255, 255)
	pixels[px_cord_L12] = (255, 255, 255)
	pixels[px_cord_N12] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A13] = (255, 255, 255)
	pixels[px_cord_C13] = (255, 255, 255)
	pixels[px_cord_E13] = (255, 255, 255)
	pixels[px_cord_G13] = (255, 255, 255)
	pixels[px_cord_I13] = (255, 255, 255)
	pixels[px_cord_K13] = (255, 255, 255)
	pixels[px_cord_M13] = (255, 255, 255)
	pixels[px_cord_O13] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B14] = (255, 255, 255)
	pixels[px_cord_D14] = (255, 255, 255)
	pixels[px_cord_F14] = (255, 255, 255)
	pixels[px_cord_H14] = (255, 255, 255)
	pixels[px_cord_J14] = (255, 255, 255)
	pixels[px_cord_L14] = (255, 255, 255)
	pixels[px_cord_N14] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A15] = (255, 255, 255)
	pixels[px_cord_C15] = (255, 255, 255)
	pixels[px_cord_E15] = (255, 255, 255)
	pixels[px_cord_G15] = (255, 255, 255)
	pixels[px_cord_I15] = (255, 255, 255)
	pixels[px_cord_K15] = (255, 255, 255)
	pixels[px_cord_M15] = (255, 255, 255)
	pixels[px_cord_O15] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_B16] = (255, 255, 255)
	pixels[px_cord_D16] = (255, 255, 255)
	pixels[px_cord_F16] = (255, 255, 255)
	pixels[px_cord_H16] = (255, 255, 255)
	pixels[px_cord_J16] = (255, 255, 255)
	pixels[px_cord_L16] = (255, 255, 255)
	pixels[px_cord_N16] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

	pixels[px_cord_A17] = (255, 255, 255)
	pixels[px_cord_C17] = (255, 255, 255)
	pixels[px_cord_E17] = (255, 255, 255)
	pixels[px_cord_G17] = (255, 255, 255)
	pixels[px_cord_I17] = (255, 255, 255)
	pixels[px_cord_K17] = (255, 255, 255)
	pixels[px_cord_M17] = (255, 255, 255)
	pixels[px_cord_O17] = (255, 255, 255)

	pixels.show()
	time.sleep(wait)

def ho_ho(wait):
	# Green H
	pixels[px_cord_B3] = (0, 255, 0)
	pixels[px_cord_B4] = (0, 255, 0)
	pixels[px_cord_B5] = (0, 255, 0)
	pixels[px_cord_B6] = (0, 255, 0)
	pixels[px_cord_B7] = (0, 255, 0)
	pixels[px_cord_B8] = (0, 255, 0)

	pixels[px_cord_C3] = (0, 255, 0)
	pixels[px_cord_C4] = (0, 255, 0)
	pixels[px_cord_C5] = (0, 255, 0)
	pixels[px_cord_C6] = (0, 255, 0)
	pixels[px_cord_C7] = (0, 255, 0)
	pixels[px_cord_C8] = (0, 255, 0)

	pixels[px_cord_D5] = (0, 255, 0)
	pixels[px_cord_D6] = (0, 255, 0)

	pixels[px_cord_E5] = (0, 255, 0)
	pixels[px_cord_E6] = (0, 255, 0)

	pixels[px_cord_F3] = (0, 255, 0)
	pixels[px_cord_F4] = (0, 255, 0)
	pixels[px_cord_F5] = (0, 255, 0)
	pixels[px_cord_F6] = (0, 255, 0)
	pixels[px_cord_F7] = (0, 255, 0)
	pixels[px_cord_F8] = (0, 255, 0)

	pixels[px_cord_G3] = (0, 255, 0)
	pixels[px_cord_G4] = (0, 255, 0)
	pixels[px_cord_G5] = (0, 255, 0)
	pixels[px_cord_G6] = (0, 255, 0)
	pixels[px_cord_G7] = (0, 255, 0)
	pixels[px_cord_G8] = (0, 255, 0)

	# Green O
	pixels[px_cord_J3] = (0, 255, 0)
	pixels[px_cord_J4] = (0, 255, 0)
	pixels[px_cord_J5] = (0, 255, 0)
	pixels[px_cord_J6] = (0, 255, 0)
	pixels[px_cord_J7] = (0, 255, 0)
	pixels[px_cord_J8] = (0, 255, 0)

	pixels[px_cord_K3] = (0, 255, 0)
	pixels[px_cord_K4] = (0, 255, 0)
	pixels[px_cord_K5] = (0, 255, 0)
	pixels[px_cord_K6] = (0, 255, 0)
	pixels[px_cord_K7] = (0, 255, 0)
	pixels[px_cord_K8] = (0, 255, 0)

	pixels[px_cord_L3] = (0, 255, 0)
	pixels[px_cord_L8] = (0, 255, 0)

	pixels[px_cord_M3] = (0, 255, 0)
	pixels[px_cord_M4] = (0, 255, 0)
	pixels[px_cord_M5] = (0, 255, 0)
	pixels[px_cord_M6] = (0, 255, 0)
	pixels[px_cord_M7] = (0, 255, 0)
	pixels[px_cord_M8] = (0, 255, 0)

	pixels[px_cord_N3] = (0, 255, 0)
	pixels[px_cord_N4] = (0, 255, 0)
	pixels[px_cord_N5] = (0, 255, 0)
	pixels[px_cord_N6] = (0, 255, 0)
	pixels[px_cord_N7] = (0, 255, 0)
	pixels[px_cord_N8] = (0, 255, 0)

	# Show Green Ho
	pixels.show()
	time.sleep(wait)

	# Red Ho
	pixels[px_cord_B10] = (255, 0, 0)
	pixels[px_cord_B11] = (255, 0, 0)
	pixels[px_cord_B12] = (255, 0, 0)
	pixels[px_cord_B13] = (255, 0, 0)
	pixels[px_cord_B14] = (255, 0, 0)
	pixels[px_cord_B15] = (255, 0, 0)

	pixels[px_cord_C10] = (255, 0, 0)
	pixels[px_cord_C11] = (255, 0, 0)
	pixels[px_cord_C12] = (255, 0, 0)
	pixels[px_cord_C13] = (255, 0, 0)
	pixels[px_cord_C14] = (255, 0, 0)
	pixels[px_cord_C15] = (255, 0, 0)

	pixels[px_cord_D12] = (255, 0, 0)
	pixels[px_cord_D13] = (255, 0, 0)

	pixels[px_cord_E12] = (255, 0, 0)
	pixels[px_cord_E13] = (255, 0, 0)

	pixels[px_cord_F10] = (255, 0, 0)
	pixels[px_cord_F11] = (255, 0, 0)
	pixels[px_cord_F12] = (255, 0, 0)
	pixels[px_cord_F13] = (255, 0, 0)
	pixels[px_cord_F14] = (255, 0, 0)
	pixels[px_cord_F15] = (255, 0, 0)

	pixels[px_cord_G10] = (255, 0, 0)
	pixels[px_cord_G11] = (255, 0, 0)
	pixels[px_cord_G12] = (255, 0, 0)
	pixels[px_cord_G13] = (255, 0, 0)
	pixels[px_cord_G14] = (255, 0, 0)
	pixels[px_cord_G15] = (255, 0, 0)

	# Red O
	pixels[px_cord_J10] = (255, 0, 0)
	pixels[px_cord_J11] = (255, 0, 0)
	pixels[px_cord_J12] = (255, 0, 0)
	pixels[px_cord_J13] = (255, 0, 0)
	pixels[px_cord_J14] = (255, 0, 0)
	pixels[px_cord_J15] = (255, 0, 0)

	pixels[px_cord_K10] = (255, 0, 0)
	pixels[px_cord_K11] = (255, 0, 0)
	pixels[px_cord_K12] = (255, 0, 0)
	pixels[px_cord_K13] = (255, 0, 0)
	pixels[px_cord_K14] = (255, 0, 0)
	pixels[px_cord_K15] = (255, 0, 0)

	pixels[px_cord_L10] = (255, 0, 0)
	pixels[px_cord_L15] = (255, 0, 0)

	pixels[px_cord_M10] = (255, 0, 0)
	pixels[px_cord_M11] = (255, 0, 0)
	pixels[px_cord_M12] = (255, 0, 0)
	pixels[px_cord_M13] = (255, 0, 0)
	pixels[px_cord_M14] = (255, 0, 0)
	pixels[px_cord_M15] = (255, 0, 0)

	pixels[px_cord_N10] = (255, 0, 0)
	pixels[px_cord_N11] = (255, 0, 0)
	pixels[px_cord_N12] = (255, 0, 0)
	pixels[px_cord_N13] = (255, 0, 0)
	pixels[px_cord_N14] = (255, 0, 0)
	pixels[px_cord_N15] = (255, 0, 0)

	# Show Red Ho
	pixels.show()
	time.sleep(wait)

def ho_ho(wait):
	# White H
	pixels[px_cord_B4] = (255, 255, 255)
	pixels[px_cord_B5] = (255, 255, 255)
	pixels[px_cord_B6] = (255, 255, 255)
	pixels[px_cord_B7] = (255, 255, 255)
	pixels[px_cord_B8] = (255, 255, 255)
	pixels[px_cord_B9] = (255, 255, 255)
	pixels[px_cord_B10] = (255, 255, 255)
	pixels[px_cord_B11] = (255, 255, 255)
	pixels[px_cord_B12] = (255, 255, 255)
	pixels[px_cord_B13] = (255, 255, 255)
	pixels[px_cord_B14] = (255, 255, 255)

	pixels[px_cord_C4] = (255, 255, 255)
	pixels[px_cord_C5] = (255, 255, 255)
	pixels[px_cord_C6] = (255, 255, 255)
	pixels[px_cord_C7] = (255, 255, 255)
	pixels[px_cord_C8] = (255, 255, 255)
	pixels[px_cord_C9] = (255, 255, 255)
	pixels[px_cord_C10] = (255, 255, 255)
	pixels[px_cord_C11] = (255, 255, 255)
	pixels[px_cord_C12] = (255, 255, 255)
	pixels[px_cord_C13] = (255, 255, 255)
	pixels[px_cord_C14] = (255, 255, 255)

	pixels[px_cord_D9] = (255, 255, 255)
	pixels[px_cord_E9] = (255, 255, 255)

	pixels[px_cord_F4] = (255, 255, 255)
	pixels[px_cord_F5] = (255, 255, 255)
	pixels[px_cord_F6] = (255, 255, 255)
	pixels[px_cord_F7] = (255, 255, 255)
	pixels[px_cord_F8] = (255, 255, 255)
	pixels[px_cord_F9] = (255, 255, 255)
	pixels[px_cord_F10] = (255, 255, 255)
	pixels[px_cord_F11] = (255, 255, 255)
	pixels[px_cord_F12] = (255, 255, 255)
	pixels[px_cord_F13] = (255, 255, 255)
	pixels[px_cord_F14] = (255, 255, 255)

	pixels[px_cord_G4] = (255, 255, 255)
	pixels[px_cord_G5] = (255, 255, 255)
	pixels[px_cord_G6] = (255, 255, 255)
	pixels[px_cord_G7] = (255, 255, 255)
	pixels[px_cord_G8] = (255, 255, 255)
	pixels[px_cord_G9] = (255, 255, 255)
	pixels[px_cord_G10] = (255, 255, 255)
	pixels[px_cord_G11] = (255, 255, 255)
	pixels[px_cord_G12] = (255, 255, 255)
	pixels[px_cord_G13] = (255, 255, 255)
	pixels[px_cord_G14] = (255, 255, 255)

	# White o
	pixels[px_cord_J4] = (255, 255, 255)
	pixels[px_cord_J5] = (255, 255, 255)
	pixels[px_cord_J6] = (255, 255, 255)
	pixels[px_cord_J7] = (255, 255, 255)
	pixels[px_cord_J8] = (255, 255, 255)
	pixels[px_cord_J9] = (255, 255, 255)
	pixels[px_cord_J10] = (255, 255, 255)
	pixels[px_cord_J11] = (255, 255, 255)
	pixels[px_cord_J12] = (255, 255, 255)
	pixels[px_cord_J13] = (255, 255, 255)
	pixels[px_cord_J14] = (255, 255, 255)

	pixels[px_cord_K4] = (255, 255, 255)
	pixels[px_cord_K5] = (255, 255, 255)
	pixels[px_cord_K6] = (255, 255, 255)
	pixels[px_cord_K7] = (255, 255, 255)
	pixels[px_cord_K8] = (255, 255, 255)
	pixels[px_cord_K9] = (255, 255, 255)
	pixels[px_cord_K10] = (255, 255, 255)
	pixels[px_cord_K11] = (255, 255, 255)
	pixels[px_cord_K12] = (255, 255, 255)
	pixels[px_cord_K13] = (255, 255, 255)
	pixels[px_cord_K14] = (255, 255, 255)

	pixels[px_cord_L4] = (255, 255, 255)
	pixels[px_cord_L5] = (255, 255, 255)
	pixels[px_cord_L13] = (255, 255, 255)
	pixels[px_cord_L14] = (255, 255, 255)

	pixels[px_cord_M4] = (255, 255, 255)
	pixels[px_cord_M5] = (255, 255, 255)
	pixels[px_cord_M6] = (255, 255, 255)
	pixels[px_cord_M7] = (255, 255, 255)
	pixels[px_cord_M8] = (255, 255, 255)
	pixels[px_cord_M9] = (255, 255, 255)
	pixels[px_cord_M10] = (255, 255, 255)
	pixels[px_cord_M11] = (255, 255, 255)
	pixels[px_cord_M12] = (255, 255, 255)
	pixels[px_cord_M13] = (255, 255, 255)
	pixels[px_cord_M14] = (255, 255, 255)

	pixels[px_cord_N4] = (255, 255, 255)
	pixels[px_cord_N5] = (255, 255, 255)
	pixels[px_cord_N6] = (255, 255, 255)
	pixels[px_cord_N7] = (255, 255, 255)
	pixels[px_cord_N8] = (255, 255, 255)
	pixels[px_cord_N9] = (255, 255, 255)
	pixels[px_cord_N10] = (255, 255, 255)
	pixels[px_cord_N11] = (255, 255, 255)
	pixels[px_cord_N12] = (255, 255, 255)
	pixels[px_cord_N13] = (255, 255, 255)
	pixels[px_cord_N14] = (255, 255, 255)

	# Show White Ho
	pixels.show()
	time.sleep(wait)


# Main Display Loop
while True:
	# Let it Snow
	# let_it_snow(1)

	# Ho Ho Ho
	ho_ho(5)
	clear_all_pixels()
	only_ho(5)

	#Clear Screen
	clear_all_pixels()

	# Candy Cane Animation
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)
	candy_cake_pos_1(0.5)
	candy_cake_pos_2(0.5)

