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


def candy_cane_pos_1(wait):
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

def candy_cane_pos_2(wait):
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

def let_it_snow(red, green, blue, SparkleDelay, SpeedDelay):

    # Set Background
    pixels.fill((red, green, blue))

    # Pick the snow sparkle Pixel
    pixels[px_cord_C1] = (255, 255, 255)
    pixels[px_cord_F1] = (255, 255, 255)
    pixels[px_cord_J1] = (255, 255, 255)
    pixels[px_cord_L1] = (255, 255, 255)
    pixels[px_cord_O1] = (255, 255, 255)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B2] = (255, 255, 255)
    pixels[px_cord_E2] = (255, 255, 255)
    pixels[px_cord_I2] = (255, 255, 255)
    pixels[px_cord_K2] = (255, 255, 255)
    pixels[px_cord_N2] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C1] = (red, green, blue)
    pixels[px_cord_F1] = (red, green, blue)
    pixels[px_cord_J1] = (red, green, blue)
    pixels[px_cord_L1] = (red, green, blue)
    pixels[px_cord_O1] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C3] = (255, 255, 255)
    pixels[px_cord_F3] = (255, 255, 255)
    pixels[px_cord_J3] = (255, 255, 255)
    pixels[px_cord_L3] = (255, 255, 255)
    pixels[px_cord_O3] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B2] = (red, green, blue)
    pixels[px_cord_E2] = (red, green, blue)
    pixels[px_cord_I2] = (red, green, blue)
    pixels[px_cord_K2] = (red, green, blue)
    pixels[px_cord_N2] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B4] = (255, 255, 255)
    pixels[px_cord_E4] = (255, 255, 255)
    pixels[px_cord_I4] = (255, 255, 255)
    pixels[px_cord_K4] = (255, 255, 255)
    pixels[px_cord_N4] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C3] = (red, green, blue)
    pixels[px_cord_F3] = (red, green, blue)
    pixels[px_cord_J3] = (red, green, blue)
    pixels[px_cord_L3] = (red, green, blue)
    pixels[px_cord_O3] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C5] = (255, 255, 255)
    pixels[px_cord_F5] = (255, 255, 255)
    pixels[px_cord_J5] = (255, 255, 255)
    pixels[px_cord_L5] = (255, 255, 255)
    pixels[px_cord_O5] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B4] = (red, green, blue)
    pixels[px_cord_E4] = (red, green, blue)
    pixels[px_cord_I4] = (red, green, blue)
    pixels[px_cord_K4] = (red, green, blue)
    pixels[px_cord_N4] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B6] = (255, 255, 255)
    pixels[px_cord_E6] = (255, 255, 255)
    pixels[px_cord_I6] = (255, 255, 255)
    pixels[px_cord_K6] = (255, 255, 255)
    pixels[px_cord_N6] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C5] = (red, green, blue)
    pixels[px_cord_F5] = (red, green, blue)
    pixels[px_cord_J5] = (red, green, blue)
    pixels[px_cord_L5] = (red, green, blue)
    pixels[px_cord_O5] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C7] = (255, 255, 255)
    pixels[px_cord_F7] = (255, 255, 255)
    pixels[px_cord_J7] = (255, 255, 255)
    pixels[px_cord_L7] = (255, 255, 255)
    pixels[px_cord_O7] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B6] = (red, green, blue)
    pixels[px_cord_E6] = (red, green, blue)
    pixels[px_cord_I6] = (red, green, blue)
    pixels[px_cord_K6] = (red, green, blue)
    pixels[px_cord_N6] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B8] = (255, 255, 255)
    pixels[px_cord_E8] = (255, 255, 255)
    pixels[px_cord_I8] = (255, 255, 255)
    pixels[px_cord_K8] = (255, 255, 255)
    pixels[px_cord_N8] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C7] = (red, green, blue)
    pixels[px_cord_F7] = (red, green, blue)
    pixels[px_cord_J7] = (red, green, blue)
    pixels[px_cord_L7] = (red, green, blue)
    pixels[px_cord_O7] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C9] = (255, 255, 255)
    pixels[px_cord_F9] = (255, 255, 255)
    pixels[px_cord_J9] = (255, 255, 255)
    pixels[px_cord_L9] = (255, 255, 255)
    pixels[px_cord_O9] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B8] = (red, green, blue)
    pixels[px_cord_E8] = (red, green, blue)
    pixels[px_cord_I8] = (red, green, blue)
    pixels[px_cord_K8] = (red, green, blue)
    pixels[px_cord_N8] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B10] = (255, 255, 255)
    pixels[px_cord_E10] = (255, 255, 255)
    pixels[px_cord_I10] = (255, 255, 255)
    pixels[px_cord_K10] = (255, 255, 255)
    pixels[px_cord_N10] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C9] = (red, green, blue)
    pixels[px_cord_F9] = (red, green, blue)
    pixels[px_cord_J9] = (red, green, blue)
    pixels[px_cord_L9] = (red, green, blue)
    pixels[px_cord_O9] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C11] = (255, 255, 255)
    pixels[px_cord_F11] = (255, 255, 255)
    pixels[px_cord_J11] = (255, 255, 255)
    pixels[px_cord_L11] = (255, 255, 255)
    pixels[px_cord_O11] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B10] = (red, green, blue)
    pixels[px_cord_E10] = (red, green, blue)
    pixels[px_cord_I10] = (red, green, blue)
    pixels[px_cord_K10] = (red, green, blue)
    pixels[px_cord_N10] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B12] = (255, 255, 255)
    pixels[px_cord_E12] = (255, 255, 255)
    pixels[px_cord_I12] = (255, 255, 255)
    pixels[px_cord_K12] = (255, 255, 255)
    pixels[px_cord_N12] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C11] = (red, green, blue)
    pixels[px_cord_F11] = (red, green, blue)
    pixels[px_cord_J11] = (red, green, blue)
    pixels[px_cord_L11] = (red, green, blue)
    pixels[px_cord_O11] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C13] = (255, 255, 255)
    pixels[px_cord_F13] = (255, 255, 255)
    pixels[px_cord_J13] = (255, 255, 255)
    pixels[px_cord_L13] = (255, 255, 255)
    pixels[px_cord_O13] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B12] = (red, green, blue)
    pixels[px_cord_E12] = (red, green, blue)
    pixels[px_cord_I12] = (red, green, blue)
    pixels[px_cord_K12] = (red, green, blue)
    pixels[px_cord_N12] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B14] = (255, 255, 255)
    pixels[px_cord_E14] = (255, 255, 255)
    pixels[px_cord_I14] = (255, 255, 255)
    pixels[px_cord_K14] = (255, 255, 255)
    pixels[px_cord_N14] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C13] = (red, green, blue)
    pixels[px_cord_F13] = (red, green, blue)
    pixels[px_cord_J13] = (red, green, blue)
    pixels[px_cord_L13] = (red, green, blue)
    pixels[px_cord_O13] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C15] = (255, 255, 255)
    pixels[px_cord_F15] = (255, 255, 255)
    pixels[px_cord_J15] = (255, 255, 255)
    pixels[px_cord_L15] = (255, 255, 255)
    pixels[px_cord_O15] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B14] = (red, green, blue)
    pixels[px_cord_E14] = (red, green, blue)
    pixels[px_cord_I14] = (red, green, blue)
    pixels[px_cord_K14] = (red, green, blue)
    pixels[px_cord_N14] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_B16] = (255, 255, 255)
    pixels[px_cord_E16] = (255, 255, 255)
    pixels[px_cord_I16] = (255, 255, 255)
    pixels[px_cord_K16] = (255, 255, 255)
    pixels[px_cord_N16] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_C15] = (red, green, blue)
    pixels[px_cord_F15] = (red, green, blue)
    pixels[px_cord_J15] = (red, green, blue)
    pixels[px_cord_L15] = (red, green, blue)
    pixels[px_cord_O15] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C17] = (255, 255, 255)
    pixels[px_cord_F17] = (255, 255, 255)
    pixels[px_cord_J17] = (255, 255, 255)
    pixels[px_cord_L17] = (255, 255, 255)
    pixels[px_cord_O17] = (255, 255, 255)
    pixels.show()
    time.sleep(SparkleDelay)
    pixels[px_cord_B16] = (red, green, blue)
    pixels[px_cord_E16] = (red, green, blue)
    pixels[px_cord_I16] = (red, green, blue)
    pixels[px_cord_K16] = (red, green, blue)
    pixels[px_cord_N16] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)
    pixels[px_cord_C17] = (red, green, blue)
    pixels[px_cord_F17] = (red, green, blue)
    pixels[px_cord_J17] = (red, green, blue)
    pixels[px_cord_L17] = (red, green, blue)
    pixels[px_cord_O17] = (red, green, blue)
    pixels.show()
    time.sleep(SpeedDelay)

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

def only_ho(wait):
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

def snowman(wait):
	# Snowman

	# Body
	pixels[px_cord_D11] = (255, 255, 255)
	pixels[px_cord_D12] = (255, 255, 255)
	pixels[px_cord_D13] = (255, 255, 255)
	pixels[px_cord_D14] = (255, 255, 255)
	pixels[px_cord_D15] = (255, 255, 255)

	pixels[px_cord_E10] = (255, 255, 255)
	pixels[px_cord_E11] = (255, 255, 255)
	pixels[px_cord_E12] = (255, 255, 255)
	pixels[px_cord_E13] = (255, 255, 255)
	pixels[px_cord_E14] = (255, 255, 255)
	pixels[px_cord_E15] = (255, 255, 255)
	pixels[px_cord_E16] = (255, 255, 255)

	pixels[px_cord_F9] = (255, 255, 255)
	pixels[px_cord_F10] = (255, 255, 255)
	pixels[px_cord_F11] = (255, 255, 255)
	pixels[px_cord_F12] = (255, 255, 255)
	pixels[px_cord_F13] = (255, 255, 255)
	pixels[px_cord_F14] = (255, 255, 255)
	pixels[px_cord_F15] = (255, 255, 255)
	pixels[px_cord_F16] = (255, 255, 255)
	pixels[px_cord_F17] = (255, 255, 255)

	pixels[px_cord_G9] = (255, 255, 255)
	pixels[px_cord_G10] = (255, 255, 255)
	pixels[px_cord_G11] = (255, 255, 255)
	pixels[px_cord_G12] = (255, 255, 255)
	pixels[px_cord_G13] = (255, 255, 255)
	pixels[px_cord_G14] = (255, 255, 255)
	pixels[px_cord_G15] = (255, 255, 255)
	pixels[px_cord_G16] = (255, 255, 255)
	pixels[px_cord_G17] = (255, 255, 255)

	pixels[px_cord_H9] = (255, 255, 255)
	pixels[px_cord_H10] = (255, 255, 255)
	pixels[px_cord_H12] = (255, 255, 255)
	pixels[px_cord_H14] = (255, 255, 255)
	pixels[px_cord_H16] = (255, 255, 255)
	pixels[px_cord_H17] = (255, 255, 255)

	pixels[px_cord_I9] = (255, 255, 255)
	pixels[px_cord_I10] = (255, 255, 255)
	pixels[px_cord_I12] = (255, 255, 255)
	pixels[px_cord_I14] = (255, 255, 255)
	pixels[px_cord_I16] = (255, 255, 255)
	pixels[px_cord_I17] = (255, 255, 255)

	pixels[px_cord_J9] = (255, 255, 255)
	pixels[px_cord_J10] = (255, 255, 255)
	pixels[px_cord_J11] = (255, 255, 255)
	pixels[px_cord_J12] = (255, 255, 255)
	pixels[px_cord_J13] = (255, 255, 255)
	pixels[px_cord_J14] = (255, 255, 255)
	pixels[px_cord_J15] = (255, 255, 255)
	pixels[px_cord_J16] = (255, 255, 255)
	pixels[px_cord_J17] = (255, 255, 255)

	pixels[px_cord_K9] = (255, 255, 255)
	pixels[px_cord_K10] = (255, 255, 255)
	pixels[px_cord_K11] = (255, 255, 255)
	pixels[px_cord_K12] = (255, 255, 255)
	pixels[px_cord_K13] = (255, 255, 255)
	pixels[px_cord_K14] = (255, 255, 255)
	pixels[px_cord_K15] = (255, 255, 255)
	pixels[px_cord_K16] = (255, 255, 255)
	pixels[px_cord_K17] = (255, 255, 255)

	pixels[px_cord_L10] = (255, 255, 255)
	pixels[px_cord_L11] = (255, 255, 255)
	pixels[px_cord_L12] = (255, 255, 255)
	pixels[px_cord_L13] = (255, 255, 255)
	pixels[px_cord_L14] = (255, 255, 255)
	pixels[px_cord_L15] = (255, 255, 255)
	pixels[px_cord_L16] = (255, 255, 255)

	pixels[px_cord_M11] = (255, 255, 255)
	pixels[px_cord_M12] = (255, 255, 255)
	pixels[px_cord_M13] = (255, 255, 255)
	pixels[px_cord_M14] = (255, 255, 255)
	pixels[px_cord_M15] = (255, 255, 255)

	# Head
	pixels[px_cord_F4] = (255, 255, 255)
	pixels[px_cord_F5] = (255, 255, 255)
	pixels[px_cord_F6] = (255, 255, 255)

	pixels[px_cord_G3] = (255, 255, 255)
	pixels[px_cord_G5] = (255, 255, 255)
	pixels[px_cord_G6] = (255, 255, 255)
	pixels[px_cord_G7] = (255, 255, 255)

	pixels[px_cord_H2] = (255, 255, 255)
	pixels[px_cord_H3] = (255, 255, 255)
	pixels[px_cord_H4] = (255, 255, 255)
	pixels[px_cord_H5] = (255, 255, 255)
	pixels[px_cord_H7] = (255, 255, 255)
	pixels[px_cord_H8] = (255, 255, 255)

	pixels[px_cord_I2] = (255, 255, 255)
	pixels[px_cord_I3] = (255, 255, 255)
	pixels[px_cord_I4] = (255, 255, 255)
	pixels[px_cord_I5] = (255, 255, 255)
	pixels[px_cord_I7] = (255, 255, 255)
	pixels[px_cord_I8] = (255, 255, 255)

	pixels[px_cord_J3] = (255, 255, 255)
	pixels[px_cord_J5] = (255, 255, 255)
	pixels[px_cord_J6] = (255, 255, 255)
	pixels[px_cord_J7] = (255, 255, 255)

	pixels[px_cord_K4] = (255, 255, 255)
	pixels[px_cord_K5] = (255, 255, 255)
	pixels[px_cord_K6] = (255, 255, 255)

	# Eyes
	pixels[px_cord_G4] = (61, 181, 250)
	pixels[px_cord_J4] = (61, 181, 250)

	# Nose
	pixels[px_cord_H6] = (250, 139, 28)
	pixels[px_cord_I6] = (250, 139, 28)

	# Buttons
	pixels[px_cord_H11] = (10, 0, 145)
	pixels[px_cord_I11] = (10, 0, 145)

	pixels[px_cord_H13] = (10, 0, 145)
	pixels[px_cord_I13] = (10, 0, 145)

	pixels[px_cord_H15] = (10, 0, 145)
	pixels[px_cord_I15] = (10, 0, 145)

	# Show White Snowman
	pixels.show()
	time.sleep(wait)

def tree_pos_1(wait):
	# Christmas Tree
	# Star
	pixels[px_cord_H3] = (255, 233, 30)
	pixels[px_cord_G4] = (255, 233, 30)
	pixels[px_cord_H4] = (255, 233, 30)
	pixels[px_cord_I4] = (255, 233, 30)
	pixels[px_cord_H5] = (255, 233, 30)

	# Base
	pixels[px_cord_F15] = (81, 74, 11)
	pixels[px_cord_J15] = (81, 74, 11)
	pixels[px_cord_G16] = (81, 74, 11)
	pixels[px_cord_H16] = (81, 74, 11)
	pixels[px_cord_I16] = (81, 74, 11)
	pixels[px_cord_G17] = (81, 74, 11)
	pixels[px_cord_H17] = (81, 74, 11)
	pixels[px_cord_I17] = (81, 74, 11)

	# Trunk
	pixels[px_cord_H14] = (81, 74, 11)
	pixels[px_cord_H15] = (81, 74, 11)

	# Tree (Baubles get over drawn over tree below)
	pixels[px_cord_B12] = (0, 255, 0)
	pixels[px_cord_B13] = (0, 255, 0)

	pixels[px_cord_C11] = (0, 255, 0)
	pixels[px_cord_C12] = (0, 255, 0)
	pixels[px_cord_C13] = (0, 255, 0)

	pixels[px_cord_D10] = (0, 255, 0)
	pixels[px_cord_D11] = (0, 255, 0)
	pixels[px_cord_D12] = (0, 255, 0)
	pixels[px_cord_D13] = (0, 255, 0)

	pixels[px_cord_E9] = (0, 255, 0)
	pixels[px_cord_E10] = (0, 255, 0)
	pixels[px_cord_E11] = (0, 255, 0)
	pixels[px_cord_E12] = (0, 255, 0)
	pixels[px_cord_E13] = (0, 255, 0)

	pixels[px_cord_F8] = (0, 255, 0)
	pixels[px_cord_F9] = (0, 255, 0)
	pixels[px_cord_F10] = (0, 255, 0)
	pixels[px_cord_F11] = (0, 255, 0)
	pixels[px_cord_F12] = (0, 255, 0)
	pixels[px_cord_F13] = (0, 255, 0)

	pixels[px_cord_G7] = (0, 255, 0)
	pixels[px_cord_G8] = (0, 255, 0)
	pixels[px_cord_G9] = (0, 255, 0)
	pixels[px_cord_G10] = (0, 255, 0)
	pixels[px_cord_G11] = (0, 255, 0)
	pixels[px_cord_G12] = (0, 255, 0)
	pixels[px_cord_G13] = (0, 255, 0)

	pixels[px_cord_H7] = (0, 255, 0)
	pixels[px_cord_H6] = (0, 255, 0)
	pixels[px_cord_H8] = (0, 255, 0)
	pixels[px_cord_H9] = (0, 255, 0)
	pixels[px_cord_H10] = (0, 255, 0)
	pixels[px_cord_H11] = (0, 255, 0)
	pixels[px_cord_H12] = (0, 255, 0)
	pixels[px_cord_H13] = (0, 255, 0)

	pixels[px_cord_I7] = (0, 255, 0)
	pixels[px_cord_I8] = (0, 255, 0)
	pixels[px_cord_I9] = (0, 255, 0)
	pixels[px_cord_I10] = (0, 255, 0)
	pixels[px_cord_I11] = (0, 255, 0)
	pixels[px_cord_I12] = (0, 255, 0)
	pixels[px_cord_I13] = (0, 255, 0)

	pixels[px_cord_J8] = (0, 255, 0)
	pixels[px_cord_J9] = (0, 255, 0)
	pixels[px_cord_J10] = (0, 255, 0)
	pixels[px_cord_J11] = (0, 255, 0)
	pixels[px_cord_J12] = (0, 255, 0)
	pixels[px_cord_J13] = (0, 255, 0)

	pixels[px_cord_K9] = (0, 255, 0)
	pixels[px_cord_K10] = (0, 255, 0)
	pixels[px_cord_K11] = (0, 255, 0)
	pixels[px_cord_K12] = (0, 255, 0)
	pixels[px_cord_K13] = (0, 255, 0)

	pixels[px_cord_L10] = (0, 255, 0)
	pixels[px_cord_L11] = (0, 255, 0)
	pixels[px_cord_L12] = (0, 255, 0)
	pixels[px_cord_L13] = (0, 255, 0)

	pixels[px_cord_M11] = (0, 255, 0)
	pixels[px_cord_M12] = (0, 255, 0)
	pixels[px_cord_M13] = (0, 255, 0)

	pixels[px_cord_N12] = (0, 255, 0)
	pixels[px_cord_N13] = (0, 255, 0)

	# Red Baubles
	pixels[px_cord_H7] = (255, 57, 117)
	pixels[px_cord_G9] = (255, 57, 117)
	pixels[px_cord_I9] = (255, 57, 117)
	pixels[px_cord_K10] = (255, 57, 117)
	pixels[px_cord_E11] = (255, 57, 117)
	pixels[px_cord_C12] = (255, 57, 117)
	pixels[px_cord_K12] = (255, 57, 117)

	# Yellow Baubles
	pixels[px_cord_G8] = (253, 219, 49)
	pixels[px_cord_I8] = (253, 219, 49)
	pixels[px_cord_J9] = (253, 219, 49)
	pixels[px_cord_F10] = (253, 219, 49)
	pixels[px_cord_H11] = (253, 219, 49)
	pixels[px_cord_J11] = (253, 219, 49)
	pixels[px_cord_D12] = (253, 219, 49)
	pixels[px_cord_F12] = (253, 219, 49)
	pixels[px_cord_L12] = (253, 219, 49)

	# Show Tree Pos 1
	pixels.show()
	time.sleep(wait)

def tree_pos_2(wait):
	# Christmas Tree
	# Star
	pixels[px_cord_H3] = (255, 233, 30)
	pixels[px_cord_G4] = (255, 233, 30)
	pixels[px_cord_H4] = (255, 233, 30)
	pixels[px_cord_I4] = (255, 233, 30)
	pixels[px_cord_H5] = (255, 233, 30)

	# Base
	pixels[px_cord_F15] = (81, 74, 11)
	pixels[px_cord_J15] = (81, 74, 11)
	pixels[px_cord_G16] = (81, 74, 11)
	pixels[px_cord_H16] = (81, 74, 11)
	pixels[px_cord_I16] = (81, 74, 11)
	pixels[px_cord_G17] = (81, 74, 11)
	pixels[px_cord_H17] = (81, 74, 11)
	pixels[px_cord_I17] = (81, 74, 11)

	# Trunk
	pixels[px_cord_H14] = (81, 74, 11)
	pixels[px_cord_H15] = (81, 74, 11)

	# Tree (Baubles get over drawn over tree below)
	pixels[px_cord_B12] = (0, 255, 0)
	pixels[px_cord_B13] = (0, 255, 0)

	pixels[px_cord_C11] = (0, 255, 0)
	pixels[px_cord_C12] = (0, 255, 0)
	pixels[px_cord_C13] = (0, 255, 0)

	pixels[px_cord_D10] = (0, 255, 0)
	pixels[px_cord_D11] = (0, 255, 0)
	pixels[px_cord_D12] = (0, 255, 0)
	pixels[px_cord_D13] = (0, 255, 0)

	pixels[px_cord_E9] = (0, 255, 0)
	pixels[px_cord_E10] = (0, 255, 0)
	pixels[px_cord_E11] = (0, 255, 0)
	pixels[px_cord_E12] = (0, 255, 0)
	pixels[px_cord_E13] = (0, 255, 0)

	pixels[px_cord_F8] = (0, 255, 0)
	pixels[px_cord_F9] = (0, 255, 0)
	pixels[px_cord_F10] = (0, 255, 0)
	pixels[px_cord_F11] = (0, 255, 0)
	pixels[px_cord_F12] = (0, 255, 0)
	pixels[px_cord_F13] = (0, 255, 0)

	pixels[px_cord_G7] = (0, 255, 0)
	pixels[px_cord_G8] = (0, 255, 0)
	pixels[px_cord_G9] = (0, 255, 0)
	pixels[px_cord_G10] = (0, 255, 0)
	pixels[px_cord_G11] = (0, 255, 0)
	pixels[px_cord_G12] = (0, 255, 0)
	pixels[px_cord_G13] = (0, 255, 0)

	pixels[px_cord_H7] = (0, 255, 0)
	pixels[px_cord_H6] = (0, 255, 0)
	pixels[px_cord_H8] = (0, 255, 0)
	pixels[px_cord_H9] = (0, 255, 0)
	pixels[px_cord_H10] = (0, 255, 0)
	pixels[px_cord_H11] = (0, 255, 0)
	pixels[px_cord_H12] = (0, 255, 0)
	pixels[px_cord_H13] = (0, 255, 0)

	pixels[px_cord_I7] = (0, 255, 0)
	pixels[px_cord_I8] = (0, 255, 0)
	pixels[px_cord_I9] = (0, 255, 0)
	pixels[px_cord_I10] = (0, 255, 0)
	pixels[px_cord_I11] = (0, 255, 0)
	pixels[px_cord_I12] = (0, 255, 0)
	pixels[px_cord_I13] = (0, 255, 0)

	pixels[px_cord_J8] = (0, 255, 0)
	pixels[px_cord_J9] = (0, 255, 0)
	pixels[px_cord_J10] = (0, 255, 0)
	pixels[px_cord_J11] = (0, 255, 0)
	pixels[px_cord_J12] = (0, 255, 0)
	pixels[px_cord_J13] = (0, 255, 0)

	pixels[px_cord_K9] = (0, 255, 0)
	pixels[px_cord_K10] = (0, 255, 0)
	pixels[px_cord_K11] = (0, 255, 0)
	pixels[px_cord_K12] = (0, 255, 0)
	pixels[px_cord_K13] = (0, 255, 0)

	pixels[px_cord_L10] = (0, 255, 0)
	pixels[px_cord_L11] = (0, 255, 0)
	pixels[px_cord_L12] = (0, 255, 0)
	pixels[px_cord_L13] = (0, 255, 0)

	pixels[px_cord_M11] = (0, 255, 0)
	pixels[px_cord_M12] = (0, 255, 0)
	pixels[px_cord_M13] = (0, 255, 0)

	pixels[px_cord_N12] = (0, 255, 0)
	pixels[px_cord_N13] = (0, 255, 0)

	# Red Baubles
	pixels[px_cord_H7] = (253, 219, 49)
	pixels[px_cord_G9] = (253, 219, 49)
	pixels[px_cord_I9] = (253, 219, 49)
	pixels[px_cord_K10] = (253, 219, 49)
	pixels[px_cord_E11] = (253, 219, 49)
	pixels[px_cord_C12] = (253, 219, 49)
	pixels[px_cord_K12] = (253, 219, 49)

	# Yellow Baubles
	pixels[px_cord_G8] = (255, 57, 117)
	pixels[px_cord_I8] = (255, 57, 117)
	pixels[px_cord_J9] = (255, 57, 117)
	pixels[px_cord_F10] = (255, 57, 117)
	pixels[px_cord_H11] = (255, 57, 117)
	pixels[px_cord_J11] = (255, 57, 117)
	pixels[px_cord_D12] = (255, 57, 117)
	pixels[px_cord_F12] = (255, 57, 117)
	pixels[px_cord_L12] = (255, 57, 117)

	# Show Tree Pos 2
	pixels.show()
	time.sleep(wait)

def snowflake(wait, red, green, blue):
	# Snowflake
	pixels[px_cord_B8] = (red, green, blue)
	pixels[px_cord_B10] = (red, green, blue)

	pixels[px_cord_C9] = (red, green, blue)

	pixels[px_cord_D5] = (red, green, blue)
	pixels[px_cord_D7] = (red, green, blue)
	pixels[px_cord_D9] = (red, green, blue)
	pixels[px_cord_D11] = (red, green, blue)
	pixels[px_cord_D13] = (red, green, blue)

	pixels[px_cord_E6] = (red, green, blue)
	pixels[px_cord_E9] = (red, green, blue)
	pixels[px_cord_E12] = (red, green, blue)

	pixels[px_cord_F5] = (red, green, blue)
	pixels[px_cord_F7] = (red, green, blue)
	pixels[px_cord_F9] = (red, green, blue)
	pixels[px_cord_F11] = (red, green, blue)
	pixels[px_cord_F13] = (red, green, blue)

	pixels[px_cord_G2] = (red, green, blue)
	pixels[px_cord_G8] = (red, green, blue)
	pixels[px_cord_G9] = (red, green, blue)
	pixels[px_cord_G10] = (red, green, blue)
	pixels[px_cord_G16] = (red, green, blue)

	pixels[px_cord_H3] = (red, green, blue)
	pixels[px_cord_H4] = (red, green, blue)
	pixels[px_cord_H5] = (red, green, blue)
	pixels[px_cord_H6] = (red, green, blue)
	pixels[px_cord_H7] = (red, green, blue)
	pixels[px_cord_H8] = (red, green, blue)
	pixels[px_cord_H9] = (red, green, blue)
	pixels[px_cord_H10] = (red, green, blue)
	pixels[px_cord_H11] = (red, green, blue)
	pixels[px_cord_H12] = (red, green, blue)
	pixels[px_cord_H13] = (red, green, blue)
	pixels[px_cord_H14] = (red, green, blue)
	pixels[px_cord_H15] = (red, green, blue)

	pixels[px_cord_I2] = (red, green, blue)
	pixels[px_cord_I8] = (red, green, blue)
	pixels[px_cord_I9] = (red, green, blue)
	pixels[px_cord_I10] = (red, green, blue)
	pixels[px_cord_I16] = (red, green, blue)

	pixels[px_cord_J5] = (red, green, blue)
	pixels[px_cord_J7] = (red, green, blue)
	pixels[px_cord_J9] = (red, green, blue)
	pixels[px_cord_J11] = (red, green, blue)
	pixels[px_cord_J13] = (red, green, blue)

	pixels[px_cord_K6] = (red, green, blue)
	pixels[px_cord_K9] = (red, green, blue)
	pixels[px_cord_K12] = (red, green, blue)

	pixels[px_cord_L5] = (red, green, blue)
	pixels[px_cord_L7] = (red, green, blue)
	pixels[px_cord_L9] = (red, green, blue)
	pixels[px_cord_L11] = (red, green, blue)
	pixels[px_cord_L13] = (red, green, blue)

	pixels[px_cord_M9] = (red, green, blue)

	pixels[px_cord_N8] = (red, green, blue)
	pixels[px_cord_N10] = (red, green, blue)

	# Show Snowflake
	pixels.show()
	time.sleep(wait)

def santa_hat(wait):
	# Santa Hat
	# Hat Base
	pixels[px_cord_B13] = (255, 0, 0)
	pixels[px_cord_B14] = (255, 255, 255)
	pixels[px_cord_B15] = (255, 255, 255)

	pixels[px_cord_C12] = (255, 0, 0)
	pixels[px_cord_C13] = (255, 0, 0)
	pixels[px_cord_C14] = (255, 255, 255)
	pixels[px_cord_C15] = (255, 255, 255)

	pixels[px_cord_D10] = (255, 0, 0)
	pixels[px_cord_D11] = (255, 0, 0)
	pixels[px_cord_D12] = (255, 0, 0)
	pixels[px_cord_D13] = (255, 0, 0)
	pixels[px_cord_D14] = (255, 255, 255)
	pixels[px_cord_D15] = (255, 255, 255)

	pixels[px_cord_E8] = (255, 0, 0)
	pixels[px_cord_E9] = (255, 0, 0)
	pixels[px_cord_E10] = (255, 0, 0)
	pixels[px_cord_E11] = (255, 0, 0)
	pixels[px_cord_E12] = (255, 0, 0)
	pixels[px_cord_E13] = (255, 0, 0)
	pixels[px_cord_E14] = (255, 255, 255)
	pixels[px_cord_E15] = (255, 255, 255)

	pixels[px_cord_F6] = (255, 0, 0)
	pixels[px_cord_F7] = (255, 0, 0)
	pixels[px_cord_F8] = (255, 0, 0)
	pixels[px_cord_F9] = (255, 0, 0)
	pixels[px_cord_F10] = (255, 0, 0)
	pixels[px_cord_F11] = (255, 0, 0)
	pixels[px_cord_F12] = (255, 0, 0)
	pixels[px_cord_F13] = (255, 0, 0)
	pixels[px_cord_F14] = (255, 255, 255)
	pixels[px_cord_F15] = (255, 255, 255)

	pixels[px_cord_G5] = (255, 0, 0)
	pixels[px_cord_G6] = (255, 0, 0)
	pixels[px_cord_G7] = (255, 0, 0)
	pixels[px_cord_G8] = (255, 0, 0)
	pixels[px_cord_G9] = (255, 0, 0)
	pixels[px_cord_G10] = (255, 0, 0)
	pixels[px_cord_G11] = (255, 0, 0)
	pixels[px_cord_G12] = (255, 0, 0)
	pixels[px_cord_G13] = (255, 0, 0)
	pixels[px_cord_G14] = (255, 255, 255)
	pixels[px_cord_G15] = (255, 255, 255)

	pixels[px_cord_H4] = (255, 0, 0)
	pixels[px_cord_H5] = (255, 0, 0)
	pixels[px_cord_H6] = (255, 0, 0)
	pixels[px_cord_H7] = (255, 0, 0)
	pixels[px_cord_H8] = (255, 0, 0)
	pixels[px_cord_H9] = (255, 0, 0)
	pixels[px_cord_H10] = (255, 0, 0)
	pixels[px_cord_H11] = (255, 0, 0)
	pixels[px_cord_H12] = (255, 0, 0)
	pixels[px_cord_H13] = (255, 0, 0)
	pixels[px_cord_H14] = (255, 255, 255)
	pixels[px_cord_H15] = (255, 255, 255)

	pixels[px_cord_I5] = (255, 0, 0)
	pixels[px_cord_I6] = (255, 0, 0)
	pixels[px_cord_I7] = (255, 0, 0)
	pixels[px_cord_I8] = (255, 0, 0)
	pixels[px_cord_I9] = (255, 0, 0)
	pixels[px_cord_I10] = (255, 0, 0)
	pixels[px_cord_I11] = (255, 0, 0)
	pixels[px_cord_I12] = (255, 0, 0)
	pixels[px_cord_I13] = (255, 0, 0)
	pixels[px_cord_I14] = (255, 255, 255)
	pixels[px_cord_I15] = (255, 255, 255)

	pixels[px_cord_J6] = (255, 0, 0)
	pixels[px_cord_J7] = (255, 0, 0)
	pixels[px_cord_J8] = (255, 0, 0)
	pixels[px_cord_J9] = (255, 0, 0)
	pixels[px_cord_J10] = (255, 0, 0)
	pixels[px_cord_J11] = (255, 0, 0)
	pixels[px_cord_J12] = (255, 0, 0)
	pixels[px_cord_J13] = (255, 0, 0)
	pixels[px_cord_J14] = (255, 255, 255)
	pixels[px_cord_J15] = (255, 255, 255)

	pixels[px_cord_K8] = (255, 0, 0)
	pixels[px_cord_K9] = (255, 0, 0)
	pixels[px_cord_K10] = (255, 0, 0)
	pixels[px_cord_K11] = (255, 0, 0)
	pixels[px_cord_K12] = (255, 0, 0)
	pixels[px_cord_K13] = (255, 0, 0)
	pixels[px_cord_K14] = (255, 255, 255)
	pixels[px_cord_K15] = (255, 255, 255)

	pixels[px_cord_L10] = (255, 0, 0)
	pixels[px_cord_L11] = (255, 0, 0)
	pixels[px_cord_L12] = (255, 0, 0)
	pixels[px_cord_L13] = (255, 0, 0)
	pixels[px_cord_L14] = (255, 255, 255)
	pixels[px_cord_L15] = (255, 255, 255)

	pixels[px_cord_M12] = (255, 0, 0)
	pixels[px_cord_M13] = (255, 0, 0)
	pixels[px_cord_M14] = (255, 255, 255)
	pixels[px_cord_M15] = (255, 255, 255)

	pixels[px_cord_N13] = (255, 0, 0)
	pixels[px_cord_N14] = (255, 255, 255)
	pixels[px_cord_N15] = (255, 255, 255)

	# Hat Animation loop
	hat_move = 0
	while hat_move < 10:
		# Hat Top Position 1
		pixels[px_cord_I3] = (255, 0, 0)
		pixels[px_cord_I4] = (255, 0, 0)
		pixels[px_cord_J2] = (255, 0, 0)
		pixels[px_cord_J3] = (255, 0, 0)
		pixels[px_cord_K3] = (255, 0, 0)
		pixels[px_cord_L4] = (255, 255, 255)

		# Show the hat in Postion 1
		pixels.show()
		time.sleep(wait)

		# Clear Hat Top Position 1
		pixels[px_cord_I3] = (0, 0, 0)
		pixels[px_cord_I4] = (0, 0, 0)
		pixels[px_cord_J2] = (0, 0, 0)
		pixels[px_cord_J3] = (0, 0, 0)
		pixels[px_cord_K3] = (0, 0, 0)
		pixels[px_cord_L4] = (0, 0, 0)

		# Hat Top Position 2
		pixels[px_cord_G3] = (255, 0, 0)
		pixels[px_cord_G4] = (255, 0, 0)
		pixels[px_cord_F2] = (255, 0, 0)
		pixels[px_cord_F3] = (255, 0, 0)
		pixels[px_cord_E3] = (255, 0, 0)
		pixels[px_cord_E4] = (255, 255, 255)

		# Show the hat in Postion 2
		pixels.show()
		time.sleep(wait)

		# Clear Hat Top Position 2
		pixels[px_cord_G3] = (0, 0, 0)
		pixels[px_cord_G4] = (0, 0, 0)
		pixels[px_cord_F2] = (0, 0, 0)
		pixels[px_cord_F3] = (0, 0, 0)
		pixels[px_cord_E3] = (0, 0, 0)
		pixels[px_cord_E4] = (0, 0, 0)

		# Clear Hat Top Position 2 for loop
		pixels.show()

		# Up the animation counter by 1
		hat_move = hat_move + 1

def merry_xmas_138_text(wait):
	# Merry Xmas From 138 Scrolling Text
	# Starting Positions!
	# M
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)

	#E
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)

	#R
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L10] = (255,0,0)
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_M11] = (255,0,0)

	#R
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	# M
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)

	#E
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)

	#R
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)

	#R
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	# M
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)

	#E
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)

	#R
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I10] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)

	#R
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] =  (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_O7] =  (0,255,0)
	pixels[px_cord_O8] =  (0,255,0)
	pixels[px_cord_O9] =  (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	# M
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)

	#E
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)

	#R
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H10] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I10] = (255,0,0)
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)

	#R
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	# M
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)

	#E
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)

	#R
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G10] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H10] = (255,0,0)
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)

	#R
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)

	#Y
	pixels[px_cord_O7] = (255,0,0)
	pixels[px_cord_O11] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#E
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)

	#R
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G10] = (255,0,0)
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)

	#R
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)

	#Y
	pixels[px_cord_N7] = (255,0,0)
	pixels[px_cord_N11] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)
	pixels[px_cord_O10] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#E
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)

	#R
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)

	#R
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)

	#Y
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M11] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_N10] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#E
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)

	#R
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)

	#R
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)

	#Y
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_M10] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#E
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)

	#R
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)

	#R
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)

	#Y
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_L10] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_O7] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)

	#R
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)

	#Y
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_N7] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)

	#R
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)

	#Y
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_M7] = (255,0,0)

	#X
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)

	#R
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)

	#Y
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_I10] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_L7] = (255,0,0)

	#X
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)

	#R
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)

	#Y
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_H10] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_K7] = (255,0,0)

	#X
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)

	#Y
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_G10] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_J7] = (255,0,0)

	#X
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)

	#Y
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_I7] = (255,0,0)

	#X
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)

	#Y
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_H7] = (255,0,0)

	#X
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#R
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)

	#Y
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_G7] = (255,0,0)

	#X
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)

	#M
	pixels[px_cord_O7] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)
	pixels[px_cord_O10] = (255,0,0)
	pixels[px_cord_O11] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Y
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_F7] = (255,0,0)

	#X
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)

	#M
	pixels[px_cord_N7] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_N10] = (255,0,0)
	pixels[px_cord_N11] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Y
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)

	#X
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)

	#M
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_M10] = (255,0,0)
	pixels[px_cord_M11] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Y
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)

	#X
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)

	#M
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L10] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Y
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)

	#X
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)

	#M
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_O7] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)
	pixels[px_cord_O10] = (255,0,0)
	pixels[px_cord_O11] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Y
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)

	#X
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)

	#M
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_N7] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_N10] = (255,0,0)
	pixels[px_cord_N11] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Y
	pixels[px_cord_A7] = (255,0,0)

	#X
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)

	#M
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I10] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_M10] = (255,0,0)
	pixels[px_cord_M11] = (255,0,0)

	#A
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#X
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)

	#M
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H10] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L10] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)

	#A
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#X
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)

	#M
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G10] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)

	#A
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#X
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)

	#M
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)

	#A
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#X
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)

	#M
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I10] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)

	#A
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#X
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)

	#M
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H10] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)

	#A
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)

	#S
	pixels[px_cord_O7] = (255,0,0)
	pixels[px_cord_O8] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)
	pixels[px_cord_O11] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#X
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)

	#M
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G10] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)

	#A
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)

	#S
	pixels[px_cord_N7] = (255,0,0)
	pixels[px_cord_N8] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_N11] = (255,0,0)
	pixels[px_cord_O7] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)
	pixels[px_cord_O11] = (255,0,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#M
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)

	#A
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)

	#S
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M8] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_M11] = (255,0,0)
	pixels[px_cord_N7] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_N11] = (255,0,0)
	pixels[px_cord_O7] = (255,0,0)
	pixels[px_cord_O9] = (255,0,0)
	pixels[px_cord_O11] = (255,0,0)	

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#M
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)

	#A
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)

	#S
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L8] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_M11] = (255,0,0)
	pixels[px_cord_N7] = (255,0,0)
	pixels[px_cord_N9] = (255,0,0)
	pixels[px_cord_N10] = (255,0,0)
	pixels[px_cord_N11] = (255,0,0)	


	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#M
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)

	#A
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)

	#S
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K8] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)
	pixels[px_cord_M7] = (255,0,0)
	pixels[px_cord_M9] = (255,0,0)
	pixels[px_cord_M10] = (255,0,0)	
	pixels[px_cord_M11] = (255,0,0)	

	#Heart
	pixels[px_cord_O8] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)
	pixels[px_cord_O10] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#M
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)

	#A
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)

	#S
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J8] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)
	pixels[px_cord_L7] = (255,0,0)
	pixels[px_cord_L9] = (255,0,0)
	pixels[px_cord_L10] = (255,0,0)
	pixels[px_cord_L11] = (255,0,0)	

	#Heart
	pixels[px_cord_N8] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)
	pixels[px_cord_O7] = (255,255,255)
	pixels[px_cord_O8] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)
	pixels[px_cord_O10] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#M
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)

	#A
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)

	#S
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I8] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J11] = (255,0,0)
	pixels[px_cord_K7] = (255,0,0)
	pixels[px_cord_K9] = (255,0,0)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_K11] = (255,0,0)	

	#Heart
	pixels[px_cord_M8] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)
	pixels[px_cord_N7] = (255,255,255)
	pixels[px_cord_N8] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)
	pixels[px_cord_N10] = (255,255,255)
	pixels[px_cord_O8] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)
	pixels[px_cord_O10] = (255,255,255)
	pixels[px_cord_O11] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#M
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)

	#A
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)

	#S
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H8] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)
	pixels[px_cord_J7] = (255,0,0)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)	
	pixels[px_cord_J11] = (255,0,0)	

	#Heart
	pixels[px_cord_L8] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)
	pixels[px_cord_M7] = (255,255,255)
	pixels[px_cord_M8] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)
	pixels[px_cord_M10] = (255,255,255)
	pixels[px_cord_N8] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)
	pixels[px_cord_N10] = (255,255,255)
	pixels[px_cord_N11] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)
	pixels[px_cord_O10] = (255,255,255)
	pixels[px_cord_O11] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#A
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)

	#S
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G8] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H11] = (255,0,0)
	pixels[px_cord_I7] = (255,0,0)
	pixels[px_cord_I9] = (255,0,0)
	pixels[px_cord_I10] = (255,0,0)
	pixels[px_cord_I11] = (255,0,0)	

	#Heart
	pixels[px_cord_K8] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)
	pixels[px_cord_L7] = (255,255,255)
	pixels[px_cord_L8] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)
	pixels[px_cord_L10] = (255,255,255)
	pixels[px_cord_M8] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)
	pixels[px_cord_M10] = (255,255,255)
	pixels[px_cord_M11] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)
	pixels[px_cord_N10] = (255,255,255)
	pixels[px_cord_N11] = (255,255,255)
	pixels[px_cord_O8] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)
	pixels[px_cord_O10] = (255,255,255)
	pixels[px_cord_O11] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#A
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)

	#S
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F8] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G11] = (255,0,0)
	pixels[px_cord_H7] = (255,0,0)
	pixels[px_cord_H9] = (255,0,0)
	pixels[px_cord_H10] = (255,0,0)	
	pixels[px_cord_H11] = (255,0,0)	

	#Heart
	pixels[px_cord_J8] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)
	pixels[px_cord_K7] = (255,255,255)
	pixels[px_cord_K8] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)
	pixels[px_cord_K10] = (255,255,255)
	pixels[px_cord_L8] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)
	pixels[px_cord_L10] = (255,255,255)
	pixels[px_cord_L11] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)
	pixels[px_cord_M10] = (255,255,255)
	pixels[px_cord_M11] = (255,255,255)
	pixels[px_cord_N8] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)
	pixels[px_cord_N10] = (255,255,255)
	pixels[px_cord_N11] = (255,255,255)
	pixels[px_cord_O7] = (255,255,255)
	pixels[px_cord_O8] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)
	pixels[px_cord_O10] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#A
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)

	#S
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E8] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F11] = (255,0,0)
	pixels[px_cord_G7] = (255,0,0)
	pixels[px_cord_G9] = (255,0,0)
	pixels[px_cord_G10] = (255,0,0)	
	pixels[px_cord_G11] = (255,0,0)	

	#Heart
	pixels[px_cord_I8] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)
	pixels[px_cord_J7] = (255,255,255)
	pixels[px_cord_J8] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)
	pixels[px_cord_J10] = (255,255,255)
	pixels[px_cord_K8] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)
	pixels[px_cord_K10] = (255,255,255)
	pixels[px_cord_K11] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)
	pixels[px_cord_L10] = (255,255,255)
	pixels[px_cord_L11] = (255,255,255)
	pixels[px_cord_M8] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)
	pixels[px_cord_M10] = (255,255,255)
	pixels[px_cord_M11] = (255,255,255)
	pixels[px_cord_N7] = (255,255,255)
	pixels[px_cord_N8] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)
	pixels[px_cord_N10] = (255,255,255)
	pixels[px_cord_O8] = (255,255,255)
	pixels[px_cord_O9] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#A
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)

	#S
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D8] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)
	pixels[px_cord_F7] = (255,0,0)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)	
	pixels[px_cord_F11] = (255,0,0)	

	#Heart
	pixels[px_cord_H8] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)
	pixels[px_cord_I7] = (255,255,255)
	pixels[px_cord_I8] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)
	pixels[px_cord_I10] = (255,255,255)
	pixels[px_cord_J8] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)
	pixels[px_cord_J10] = (255,255,255)
	pixels[px_cord_J11] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)
	pixels[px_cord_K10] = (255,255,255)
	pixels[px_cord_K11] = (255,255,255)
	pixels[px_cord_L8] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)
	pixels[px_cord_L10] = (255,255,255)
	pixels[px_cord_L11] = (255,255,255)
	pixels[px_cord_M7] = (255,255,255)
	pixels[px_cord_M8] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)
	pixels[px_cord_M10] = (255,255,255)
	pixels[px_cord_N8] = (255,255,255)
	pixels[px_cord_N9] = (255,255,255)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#A
	pixels[px_cord_A7] = (0,255,0)
	pixels[px_cord_A8] = (0,255,0)
	pixels[px_cord_A9] = (0,255,0)
	pixels[px_cord_A10] = (0,255,0)
	pixels[px_cord_A11] = (0,255,0)

	#S
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C8] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D11] = (255,0,0)
	pixels[px_cord_E7] = (255,0,0)
	pixels[px_cord_E9] = (255,0,0)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_E11] = (255,0,0)	

	#Heart
	pixels[px_cord_G8] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)
	pixels[px_cord_H7] = (255,255,255)
	pixels[px_cord_H8] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)
	pixels[px_cord_H10] = (255,255,255)
	pixels[px_cord_I8] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)
	pixels[px_cord_I10] = (255,255,255)
	pixels[px_cord_I11] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)
	pixels[px_cord_J10] = (255,255,255)
	pixels[px_cord_J11] = (255,255,255)
	pixels[px_cord_K8] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)
	pixels[px_cord_K10] = (255,255,255)
	pixels[px_cord_K11] = (255,255,255)
	pixels[px_cord_L7] = (255,255,255)
	pixels[px_cord_L8] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)
	pixels[px_cord_L10] = (255,255,255)
	pixels[px_cord_M8] = (255,255,255)
	pixels[px_cord_M9] = (255,255,255)

	#1
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#S
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B8] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C11] = (255,0,0)
	pixels[px_cord_D7] = (255,0,0)
	pixels[px_cord_D9] = (255,0,0)
	pixels[px_cord_D10] = (255,0,0)	
	pixels[px_cord_D11] = (255,0,0)	

	#Heart
	pixels[px_cord_F8] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)
	pixels[px_cord_G7] = (255,255,255)
	pixels[px_cord_G8] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)
	pixels[px_cord_G10] = (255,255,255)
	pixels[px_cord_H8] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)
	pixels[px_cord_H10] = (255,255,255)
	pixels[px_cord_H11] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)
	pixels[px_cord_I10] = (255,255,255)
	pixels[px_cord_I11] = (255,255,255)
	pixels[px_cord_J8] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)
	pixels[px_cord_J10] = (255,255,255)
	pixels[px_cord_J11] = (255,255,255)
	pixels[px_cord_K7] = (255,255,255)
	pixels[px_cord_K8] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)
	pixels[px_cord_K10] = (255,255,255)
	pixels[px_cord_L8] = (255,255,255)
	pixels[px_cord_L9] = (255,255,255)

	#1
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#S
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A8] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B11] = (255,0,0)
	pixels[px_cord_C7] = (255,0,0)
	pixels[px_cord_C9] = (255,0,0)
	pixels[px_cord_C10] = (255,0,0)	
	pixels[px_cord_C11] = (255,0,0)	

	#Heart
	pixels[px_cord_E8] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)
	pixels[px_cord_F7] = (255,255,255)
	pixels[px_cord_F8] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)
	pixels[px_cord_F10] = (255,255,255)
	pixels[px_cord_G8] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)
	pixels[px_cord_G10] = (255,255,255)
	pixels[px_cord_G11] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)
	pixels[px_cord_H10] = (255,255,255)
	pixels[px_cord_H11] = (255,255,255)
	pixels[px_cord_I8] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)
	pixels[px_cord_I10] = (255,255,255)
	pixels[px_cord_I11] = (255,255,255)
	pixels[px_cord_J7] = (255,255,255)
	pixels[px_cord_J8] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)
	pixels[px_cord_J10] = (255,255,255)
	pixels[px_cord_K8] = (255,255,255)
	pixels[px_cord_K9] = (255,255,255)

	#1
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)

	#3
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#S
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A11] = (255,0,0)
	pixels[px_cord_B7] = (255,0,0)
	pixels[px_cord_B9] = (255,0,0)
	pixels[px_cord_B10] = (255,0,0)	
	pixels[px_cord_B11] = (255,0,0)	

	#Heart
	pixels[px_cord_D8] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)
	pixels[px_cord_E7] = (255,255,255)
	pixels[px_cord_E8] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)
	pixels[px_cord_E10] = (255,255,255)
	pixels[px_cord_F8] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)
	pixels[px_cord_F10] = (255,255,255)
	pixels[px_cord_F11] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)
	pixels[px_cord_G10] = (255,255,255)
	pixels[px_cord_G11] = (255,255,255)
	pixels[px_cord_H8] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)
	pixels[px_cord_H10] = (255,255,255)
	pixels[px_cord_H11] = (255,255,255)
	pixels[px_cord_I7] = (255,255,255)
	pixels[px_cord_I8] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)
	pixels[px_cord_I10] = (255,255,255)
	pixels[px_cord_J8] = (255,255,255)
	pixels[px_cord_J9] = (255,255,255)

	#1
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)

	#3
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#S
	pixels[px_cord_A7] = (255,0,0)
	pixels[px_cord_A9] = (255,0,0)
	pixels[px_cord_A10] = (255,0,0)	
	pixels[px_cord_A11] = (255,0,0)	

	#Heart
	pixels[px_cord_C8] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)
	pixels[px_cord_D7] = (255,255,255)
	pixels[px_cord_D8] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)
	pixels[px_cord_D10] = (255,255,255)
	pixels[px_cord_E8] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)
	pixels[px_cord_E10] = (255,255,255)
	pixels[px_cord_E11] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)
	pixels[px_cord_F10] = (255,255,255)
	pixels[px_cord_F11] = (255,255,255)
	pixels[px_cord_G8] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)
	pixels[px_cord_G10] = (255,255,255)
	pixels[px_cord_G11] = (255,255,255)
	pixels[px_cord_H7] = (255,255,255)
	pixels[px_cord_H8] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)
	pixels[px_cord_H10] = (255,255,255)
	pixels[px_cord_I8] = (255,255,255)
	pixels[px_cord_I9] = (255,255,255)

	#1
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)

	#3
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_B8] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)
	pixels[px_cord_C7] = (255,255,255)
	pixels[px_cord_C8] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)
	pixels[px_cord_C10] = (255,255,255)
	pixels[px_cord_D8] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)
	pixels[px_cord_D10] = (255,255,255)
	pixels[px_cord_D11] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)
	pixels[px_cord_E10] = (255,255,255)
	pixels[px_cord_E11] = (255,255,255)
	pixels[px_cord_F8] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)
	pixels[px_cord_F10] = (255,255,255)
	pixels[px_cord_F11] = (255,255,255)
	pixels[px_cord_G7] = (255,255,255)
	pixels[px_cord_G8] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)
	pixels[px_cord_G10] = (255,255,255)
	pixels[px_cord_H8] = (255,255,255)
	pixels[px_cord_H9] = (255,255,255)

	#1
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)

	#3
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A8] = (255,255,255)
	pixels[px_cord_A9] = (255,255,255)
	pixels[px_cord_B7] = (255,255,255)
	pixels[px_cord_B8] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)
	pixels[px_cord_B10] = (255,255,255)
	pixels[px_cord_C8] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)
	pixels[px_cord_C10] = (255,255,255)
	pixels[px_cord_C11] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)
	pixels[px_cord_D10] = (255,255,255)
	pixels[px_cord_D11] = (255,255,255)
	pixels[px_cord_E8] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)
	pixels[px_cord_E10] = (255,255,255)
	pixels[px_cord_E11] = (255,255,255)
	pixels[px_cord_F7] = (255,255,255)
	pixels[px_cord_F8] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)
	pixels[px_cord_F10] = (255,255,255)
	pixels[px_cord_G8] = (255,255,255)
	pixels[px_cord_G9] = (255,255,255)

	#1
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)

	#3
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A7] = (255,255,255)
	pixels[px_cord_A8] = (255,255,255)
	pixels[px_cord_A9] = (255,255,255)
	pixels[px_cord_A10] = (255,255,255)
	pixels[px_cord_B8] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)
	pixels[px_cord_B10] = (255,255,255)
	pixels[px_cord_B11] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)
	pixels[px_cord_C10] = (255,255,255)
	pixels[px_cord_C11] = (255,255,255)
	pixels[px_cord_D8] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)
	pixels[px_cord_D10] = (255,255,255)
	pixels[px_cord_D11] = (255,255,255)
	pixels[px_cord_E7] = (255,255,255)
	pixels[px_cord_E8] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)
	pixels[px_cord_E10] = (255,255,255)
	pixels[px_cord_F8] = (255,255,255)
	pixels[px_cord_F9] = (255,255,255)

	#1
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)

	#3
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)

	#8
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A8] = (255,255,255)
	pixels[px_cord_A9] = (255,255,255)
	pixels[px_cord_A10] = (255,255,255)
	pixels[px_cord_A11] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)
	pixels[px_cord_B10] = (255,255,255)
	pixels[px_cord_B11] = (255,255,255)
	pixels[px_cord_C8] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)
	pixels[px_cord_C10] = (255,255,255)
	pixels[px_cord_C11] = (255,255,255)
	pixels[px_cord_D7] = (255,255,255)
	pixels[px_cord_D8] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)
	pixels[px_cord_D10] = (255,255,255)
	pixels[px_cord_E8] = (255,255,255)
	pixels[px_cord_E9] = (255,255,255)

	#1
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)

	#3
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)

	#8
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A9] = (255,255,255)
	pixels[px_cord_A10] = (255,255,255)
	pixels[px_cord_A11] = (255,255,255)
	pixels[px_cord_B8] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)
	pixels[px_cord_B10] = (255,255,255)
	pixels[px_cord_B11] = (255,255,255)
	pixels[px_cord_C7] = (255,255,255)
	pixels[px_cord_C8] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)
	pixels[px_cord_C10] = (255,255,255)
	pixels[px_cord_D8] = (255,255,255)
	pixels[px_cord_D9] = (255,255,255)

	#1
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F8] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F10] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)

	#3
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)

	#8
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A8] = (255,255,255)
	pixels[px_cord_A9] = (255,255,255)
	pixels[px_cord_A10] = (255,255,255)
	pixels[px_cord_A11] = (255,255,255)
	pixels[px_cord_B7] = (255,255,255)
	pixels[px_cord_B8] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)
	pixels[px_cord_B10] = (255,255,255)
	pixels[px_cord_C8] = (255,255,255)
	pixels[px_cord_C9] = (255,255,255)

	#1
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E8] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E10] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)

	#3
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)

	#8
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)
	pixels[px_cord_O7] = (0,255,0)
	pixels[px_cord_O8] = (0,255,0)
	pixels[px_cord_O9] = (0,255,0)
	pixels[px_cord_O10] = (0,255,0)
	pixels[px_cord_O11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A7] = (255,255,255)
	pixels[px_cord_A8] = (255,255,255)
	pixels[px_cord_A9] = (255,255,255)
	pixels[px_cord_A10] = (255,255,255)
	pixels[px_cord_B8] = (255,255,255)
	pixels[px_cord_B9] = (255,255,255)

	#1
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D8] = (0,255,0)
	pixels[px_cord_D9] = (0,255,0)
	pixels[px_cord_D10] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)

	#3
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)

	#8
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K8] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K10] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)
	pixels[px_cord_N7] = (0,255,0)
	pixels[px_cord_N8] = (0,255,0)
	pixels[px_cord_N9] = (0,255,0)
	pixels[px_cord_N10] = (0,255,0)
	pixels[px_cord_N11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#Heart
	pixels[px_cord_A8] = (255,255,255)
	pixels[px_cord_A9] = (255,255,255)

	#1
	pixels[px_cord_C7] = (0,255,0)
	pixels[px_cord_C8] = (0,255,0)
	pixels[px_cord_C9] = (0,255,0)
	pixels[px_cord_C10] = (0,255,0)
	pixels[px_cord_C11] = (0,255,0)

	#3
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)
	pixels[px_cord_H7] = (0,255,0)
	pixels[px_cord_H8] = (0,255,0)
	pixels[px_cord_H9] = (0,255,0)
	pixels[px_cord_H10] = (0,255,0)
	pixels[px_cord_H11] = (0,255,0)

	#8
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J8] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J10] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)
	pixels[px_cord_M7] = (0,255,0)
	pixels[px_cord_M8] = (0,255,0)
	pixels[px_cord_M9] = (0,255,0)
	pixels[px_cord_M10] = (0,255,0)
	pixels[px_cord_M11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Next Position
	clear_all_pixels()
	#1
	pixels[px_cord_B7] = (0,255,0)
	pixels[px_cord_B8] = (0,255,0)
	pixels[px_cord_B9] = (0,255,0)
	pixels[px_cord_B10] = (0,255,0)
	pixels[px_cord_B11] = (0,255,0)

	#3
	pixels[px_cord_D7] = (0,255,0)
	pixels[px_cord_D11] = (0,255,0)
	pixels[px_cord_E7] = (0,255,0)
	pixels[px_cord_E9] = (0,255,0)
	pixels[px_cord_E11] = (0,255,0)
	pixels[px_cord_F7] = (0,255,0)
	pixels[px_cord_F9] = (0,255,0)
	pixels[px_cord_F11] = (0,255,0)
	pixels[px_cord_G7] = (0,255,0)
	pixels[px_cord_G8] = (0,255,0)
	pixels[px_cord_G9] = (0,255,0)
	pixels[px_cord_G10] = (0,255,0)
	pixels[px_cord_G11] = (0,255,0)

	#8
	pixels[px_cord_I7] = (0,255,0)
	pixels[px_cord_I8] = (0,255,0)
	pixels[px_cord_I9] = (0,255,0)
	pixels[px_cord_I10] = (0,255,0)
	pixels[px_cord_I11] = (0,255,0)
	pixels[px_cord_J7] = (0,255,0)
	pixels[px_cord_J9] = (0,255,0)
	pixels[px_cord_J11] = (0,255,0)
	pixels[px_cord_K7] = (0,255,0)
	pixels[px_cord_K9] = (0,255,0)
	pixels[px_cord_K11] = (0,255,0)
	pixels[px_cord_L7] = (0,255,0)
	pixels[px_cord_L8] = (0,255,0)
	pixels[px_cord_L9] = (0,255,0)
	pixels[px_cord_L10] = (0,255,0)
	pixels[px_cord_L11] = (0,255,0)

	# Show Postion
	pixels.show()
	time.sleep(wait)

	#Hold on end of text for 5 seconds
	time.sleep(wait)

def stocking(wait):
	# Stocking
	pixels[px_cord_C12] = (255, 0, 0)
	pixels[px_cord_C13] = (255, 0, 0)

	pixels[px_cord_D11] = (255, 0, 0)
	pixels[px_cord_D12] = (255, 0, 0)
	pixels[px_cord_D13] = (255, 0, 0)
	pixels[px_cord_D14] = (255, 0, 0)

	pixels[px_cord_E11] = (255, 0, 0)
	pixels[px_cord_E12] = (255, 0, 0)
	pixels[px_cord_E13] = (255, 0, 0)
	pixels[px_cord_E14] = (255, 0, 0)
	pixels[px_cord_E15] = (255, 0, 0)

	pixels[px_cord_F11] = (255, 0, 0)
	pixels[px_cord_F12] = (255, 0, 0)
	pixels[px_cord_F13] = (255, 0, 0)
	pixels[px_cord_F14] = (255, 0, 0)
	pixels[px_cord_F15] = (255, 0, 0)

	pixels[px_cord_G12] = (255, 0, 0)
	pixels[px_cord_G13] = (255, 0, 0)
	pixels[px_cord_G14] = (255, 0, 0)
	pixels[px_cord_G15] = (255, 0, 0)

	pixels[px_cord_H13] = (255, 0, 0)
	pixels[px_cord_H14] = (255, 0, 0)
	pixels[px_cord_H15] = (255, 0, 0)

	pixels[px_cord_I13] = (255, 0, 0)
	pixels[px_cord_I14] = (255, 0, 0)
	pixels[px_cord_I15] = (255, 0, 0)

	pixels[px_cord_J3] = (0, 0, 255)
	pixels[px_cord_J4] = (255, 0, 0)
	pixels[px_cord_J5] = (255, 0, 0)
	pixels[px_cord_J6] = (255, 0, 0)
	pixels[px_cord_J7] = (255, 0, 0)
	pixels[px_cord_J8] = (255, 0, 0)
	pixels[px_cord_J9] = (255, 0, 0)
	pixels[px_cord_J10] = (255, 0, 0)
	pixels[px_cord_J11] = (255, 0, 0)
	pixels[px_cord_J12] = (255, 0, 0)
	pixels[px_cord_J13] = (255, 0, 0)
	pixels[px_cord_J14] = (255, 0, 0)
	pixels[px_cord_J15] = (255, 0, 0)

	pixels[px_cord_K3] = (0, 0, 255)
	pixels[px_cord_K4] = (255, 0, 0)
	pixels[px_cord_K5] = (255, 0, 0)
	pixels[px_cord_K6] = (255, 0, 0)
	pixels[px_cord_K7] = (255, 0, 0)
	pixels[px_cord_K8] = (255, 0, 0)
	pixels[px_cord_K9] = (255, 0, 0)
	pixels[px_cord_K10] = (255, 0, 0)
	pixels[px_cord_K11] = (255, 0, 0)
	pixels[px_cord_K12] = (255, 0, 0)
	pixels[px_cord_K13] = (255, 0, 0)
	pixels[px_cord_K14] = (255, 0, 0)
	pixels[px_cord_K15] = (255, 0, 0)

	pixels[px_cord_L3] = (0, 255, 0)
	pixels[px_cord_L4] = (255, 0, 0)
	pixels[px_cord_L5] = (255, 0, 0)
	pixels[px_cord_L6] = (255, 0, 0)
	pixels[px_cord_L7] = (255, 0, 0)
	pixels[px_cord_L8] = (255, 0, 0)
	pixels[px_cord_L9] = (255, 0, 0)
	pixels[px_cord_L10] = (255, 0, 0)
	pixels[px_cord_L11] = (255, 0, 0)
	pixels[px_cord_L12] = (255, 0, 0)
	pixels[px_cord_L13] = (255, 0, 0)
	pixels[px_cord_L14] = (255, 0, 0)
	pixels[px_cord_L15] = (255, 0, 0)

	pixels[px_cord_M3] = (0, 0, 255)
	pixels[px_cord_M4] = (255, 0, 0)
	pixels[px_cord_M5] = (255, 0, 0)
	pixels[px_cord_M6] = (255, 0, 0)
	pixels[px_cord_M7] = (255, 0, 0)
	pixels[px_cord_M8] = (255, 0, 0)
	pixels[px_cord_M9] = (255, 0, 0)
	pixels[px_cord_M10] = (255, 0, 0)
	pixels[px_cord_M11] = (255, 0, 0)
	pixels[px_cord_M12] = (255, 0, 0)
	pixels[px_cord_M13] = (255, 0, 0)
	pixels[px_cord_M14] = (255, 0, 0)

	pixels[px_cord_N3] = (0, 0, 255)
	pixels[px_cord_N4] = (255, 0, 0)
	pixels[px_cord_N5] = (255, 0, 0)
	pixels[px_cord_N6] = (255, 0, 0)
	pixels[px_cord_N7] = (255, 0, 0)
	pixels[px_cord_N8] = (255, 0, 0)
	pixels[px_cord_N9] = (255, 0, 0)
	pixels[px_cord_N10] = (255, 0, 0)
	pixels[px_cord_N11] = (255, 0, 0)
	pixels[px_cord_N12] = (255, 0, 0)
	pixels[px_cord_N13] = (255, 0, 0)

	# Show Stocking
	pixels.show()
	time.sleep(wait)

def fireplace(wait):
	# Fireplace
	pixels[px_cord_A12] = (165,42,42)
	pixels[px_cord_A13] = (165,42,42)
	pixels[px_cord_B12] = (165,42,42)
	pixels[px_cord_B13] = (165,42,42)
	pixels[px_cord_C9] = (165,42,42)
	pixels[px_cord_C10] = (165,42,42)
	pixels[px_cord_C11] = (165,42,42)
	pixels[px_cord_C12] = (165,42,42)
	pixels[px_cord_C13] = (165,42,42)
	pixels[px_cord_D9] = (165,42,42)
	pixels[px_cord_D10] = (165,42,42)
	pixels[px_cord_D11] = (165,42,42)
	pixels[px_cord_D12] = (165,42,42)
	pixels[px_cord_D13] = (165,42,42)
	pixels[px_cord_E9] = (165,42,42)
	pixels[px_cord_E10] = (255,0,0)
	pixels[px_cord_E11] = (165,42,42)
	pixels[px_cord_E12] = (165,42,42)
	pixels[px_cord_E13] = (165,42,42)
	pixels[px_cord_F1] = (165,42,42)
	pixels[px_cord_F2] = (165,42,42)
	pixels[px_cord_F3] = (165,42,42)
	pixels[px_cord_F4] = (165,42,42)
	pixels[px_cord_F5] = (165,42,42)
	pixels[px_cord_F6] = (165,42,42)
	pixels[px_cord_F7] = (165,42,42)
	pixels[px_cord_F9] = (255,0,0)
	pixels[px_cord_F10] = (255,0,0)
	pixels[px_cord_G1] = (165,42,42)
	pixels[px_cord_G2] = (165,42,42)
	pixels[px_cord_G3] = (165,42,42)
	pixels[px_cord_G4] = (165,42,42)
	pixels[px_cord_G5] = (165,42,42)
	pixels[px_cord_G6] = (165,42,42)
	pixels[px_cord_G7] = (165,42,42)
	pixels[px_cord_G9] = (165,42,42)
	pixels[px_cord_H1] = (165,42,42)
	pixels[px_cord_H2] = (165,42,42)
	pixels[px_cord_H3] = (165,42,42)
	pixels[px_cord_H4] = (165,42,42)
	pixels[px_cord_H5] = (165,42,42)
	pixels[px_cord_H6] = (165,42,42)
	pixels[px_cord_H7] = (165,42,42)
	pixels[px_cord_H9] = (165,42,42)
	pixels[px_cord_I1] = (165,42,42)
	pixels[px_cord_I2] = (165,42,42)
	pixels[px_cord_I3] = (165,42,42)
	pixels[px_cord_I4] = (165,42,42)
	pixels[px_cord_I5] = (165,42,42)
	pixels[px_cord_I6] = (165,42,42)
	pixels[px_cord_I7] = (165,42,42)
	pixels[px_cord_I9] = (165,42,42)
	pixels[px_cord_J1] = (165,42,42)
	pixels[px_cord_J2] = (165,42,42)
	pixels[px_cord_J3] = (165,42,42)
	pixels[px_cord_J4] = (165,42,42)
	pixels[px_cord_J5] = (165,42,42)
	pixels[px_cord_J6] = (165,42,42)
	pixels[px_cord_J7] = (165,42,42)
	pixels[px_cord_J9] = (255,0,0)
	pixels[px_cord_J10] = (255,0,0)
	pixels[px_cord_K9] = (165,42,42)
	pixels[px_cord_K10] = (255,0,0)
	pixels[px_cord_K11] = (165,42,42)
	pixels[px_cord_K12] = (165,42,42)
	pixels[px_cord_K13] = (165,42,42)
	pixels[px_cord_L9] = (165,42,42)
	pixels[px_cord_L10] = (165,42,42)
	pixels[px_cord_L11] = (165,42,42)
	pixels[px_cord_L12] = (165,42,42)
	pixels[px_cord_L13] = (165,42,42)
	pixels[px_cord_M9] = (165,42,42)
	pixels[px_cord_M10] = (165,42,42)
	pixels[px_cord_M11] = (165,42,42)
	pixels[px_cord_M12] = (165,42,42)
	pixels[px_cord_M13] = (165,42,42)
	pixels[px_cord_N12] = (165,42,42)
	pixels[px_cord_N13] = (165,42,42)
	pixels[px_cord_O12] = (165,42,42)
	pixels[px_cord_O13] = (165,42,42)

	# Presents
	pixels[px_cord_A15] = (0,100,0)
	pixels[px_cord_A16] = (255,253,208)
	pixels[px_cord_A17] = (0,100,0)
	pixels[px_cord_B15] = (255,253,208)
	pixels[px_cord_B16] = (255,253,208)
	pixels[px_cord_B17] = (255,253,208)
	pixels[px_cord_C15] = (0,100,0)
	pixels[px_cord_C16] = (255,253,208)
	pixels[px_cord_C17] = (0,100,0)

	pixels[px_cord_E15] = (255,0,0)
	pixels[px_cord_E16] = (0,100,0)
	pixels[px_cord_E17] = (255,0,0)
	pixels[px_cord_F15] = (0,100,0)
	pixels[px_cord_F16] = (0,100,0)
	pixels[px_cord_F17] = (0,100,0)
	pixels[px_cord_G15] = (255,0,0)
	pixels[px_cord_G16] = (0,100,0)
	pixels[px_cord_G17] = (255,0,0)

	pixels[px_cord_I15] = (0,0,255)
	pixels[px_cord_I16] = (192,192,192)
	pixels[px_cord_I17] = (0,0,255)
	pixels[px_cord_J15] = (192,192,192)
	pixels[px_cord_J16] = (192,192,192)
	pixels[px_cord_J17] = (192,192,192)
	pixels[px_cord_K15] = (0,0,255)
	pixels[px_cord_K16] = (192,192,192)
	pixels[px_cord_K17] = (0,0,255)

	pixels[px_cord_M15] = (0,255,0)
	pixels[px_cord_M16] = (255,0,0)
	pixels[px_cord_M17] = (0,255,0)
	pixels[px_cord_N15] = (255,0,0)
	pixels[px_cord_N16] = (255,0,0)
	pixels[px_cord_N17] = (255,0,0)
	pixels[px_cord_O15] = (0,255,0)
	pixels[px_cord_O16] = (255,0,0)
	pixels[px_cord_O17] = (0,255,0)

	# Fireplace Blaze
	fire = 0
	while fire < 20:
		# Fire Pos 1
		pixels[px_cord_G12] = (226,88,34)
		pixels[px_cord_G13] = (139,69,19)
		pixels[px_cord_H12] = (139,69,19)
		pixels[px_cord_H13] = (226,88,34)
		pixels[px_cord_I12] = (226,88,34)
		pixels[px_cord_I13] = (139,69,19)

		# Show Fire Pos 1
		pixels.show()
		time.sleep(wait)

		# Clear Fire Pos 1
		pixels[px_cord_G12] = (0,0,0)
		pixels[px_cord_G13] = (0,0,0)
		pixels[px_cord_H12] = (0,0,0)
		pixels[px_cord_H13] = (0,0,0)
		pixels[px_cord_I12] = (0,0,0)
		pixels[px_cord_I13] = (0,0,0)

		# Fire Pos 2
		pixels[px_cord_G12] = (139,69,19)
		pixels[px_cord_G13] = (226,88,34)
		pixels[px_cord_H12] = (226,88,34)
		pixels[px_cord_H13] = (139,69,19)
		pixels[px_cord_I12] = (139,69,19)
		pixels[px_cord_I13] = (226,88,34)

		# Show First Pos 2
		pixels.show()
		time.sleep(wait)

		# Clear Fire Pos 2
		pixels[px_cord_G12] = (0,0,0)
		pixels[px_cord_G13] = (0,0,0)
		pixels[px_cord_H12] = (0,0,0)
		pixels[px_cord_H13] = (0,0,0)
		pixels[px_cord_I12] = (0,0,0)
		pixels[px_cord_I13] = (0,0,0)

		# Clear First Pos 2 for loop
		pixels.show()

		# Up the animation counter by 1
		fire = fire + 1

def reindeer(wait):
	# Head
	pixels[px_cord_C4] = (169, 169, 169)
	pixels[px_cord_C4] = (169, 169, 169)

	pixels[px_cord_D3] = (169, 169, 169)
	pixels[px_cord_D6] = (169, 169, 169)

	pixels[px_cord_E5] = (169, 169, 169)
	pixels[px_cord_E7] = (169, 169, 169)

	pixels[px_cord_F8] = (169, 169, 169)
	pixels[px_cord_F9] = (169, 169, 169)
	pixels[px_cord_F10] = (169, 169, 169)
	pixels[px_cord_F11] = (169, 169, 169)

	pixels[px_cord_G8] = (169, 169, 169)
	# Eye (off in G9)
	pixels[px_cord_G10] = (169, 169, 169)
	pixels[px_cord_G11] = (169, 169, 169)
	pixels[px_cord_G12] = (169, 169, 169)

	pixels[px_cord_H8] = (169, 169, 169)
	pixels[px_cord_H9] = (169, 169, 169)
	pixels[px_cord_H10] = (169, 169, 169)
	# Nose in H11 and animated below in loop
	pixels[px_cord_H12] = (169, 169, 169)
	pixels[px_cord_H13] = (169, 169, 169)

	pixels[px_cord_I8] = (169, 169, 169)
	# Eye (off in I9)
	pixels[px_cord_I10] = (169, 169, 169)
	pixels[px_cord_I11] = (169, 169, 169)
	pixels[px_cord_I12] = (169, 169, 169)

	pixels[px_cord_J8] = (169, 169, 169)
	pixels[px_cord_J9] = (169, 169, 169)
	pixels[px_cord_J10] = (169, 169, 169)
	pixels[px_cord_J11] = (169, 169, 169)

	pixels[px_cord_K5] = (169, 169, 169)
	pixels[px_cord_K7] = (169, 169, 169)

	pixels[px_cord_L3] = (169, 169, 169)
	pixels[px_cord_L6] = (169, 169, 169)

	pixels[px_cord_M4] = (169, 169, 169)
	pixels[px_cord_M4] = (169, 169, 169)

	# Flashing Red Nose
	nose = 0
	while nose < 10:
		# Nose Red
		pixels[px_cord_H11] = (255, 0, 0)

		# Show Nose On
		pixels.show()
		time.sleep(wait)

		# Clear Nose
		pixels[px_cord_H11] = (0, 0, 0)

		# Nose Brown
		pixels[px_cord_H11] = (160,82,45)

		# Show Nose Brown
		pixels.show()
		time.sleep(wait)

		# Clear Nose
		pixels[px_cord_H11] = (0, 0, 0)

		# Clear Nose for loop
		pixels.show()

		# Up the animation counter by 1
		nose = nose + 1

def multi_reindeer(wait):
	# Heads
	pixels[px_cord_A2] = (169, 169, 169)
	pixels[px_cord_A3] = (169, 169, 169)
	pixels[px_cord_A12] = (169, 169, 169)
	pixels[px_cord_A13] = (169, 169, 169)

	pixels[px_cord_B1] = (169, 169, 169)
	pixels[px_cord_B4] = (169, 169, 169)
	pixels[px_cord_B11] = (169, 169, 169)
	pixels[px_cord_B14] = (169, 169, 169)

	pixels[px_cord_C5] = (169, 169, 169)
	pixels[px_cord_C6] = (169, 169, 169)
	pixels[px_cord_C7] = (169, 169, 169)
	pixels[px_cord_C15] = (169, 169, 169)
	pixels[px_cord_C16] = (169, 169, 169)
	pixels[px_cord_C17] = (169, 169, 169)

	pixels[px_cord_D5] = (169, 169, 169)
	pixels[px_cord_D7] = (169, 169, 169)
	pixels[px_cord_D15] = (169, 169, 169)
	pixels[px_cord_D17] = (169, 169, 169)

	pixels[px_cord_E5] = (169, 169, 169)
	pixels[px_cord_E6] = (169, 169, 169)
	pixels[px_cord_E7] = (169, 169, 169)
	pixels[px_cord_E15] = (169, 169, 169)
	pixels[px_cord_E16] = (169, 169, 169)
	pixels[px_cord_E17] = (169, 169, 169)

	pixels[px_cord_F1] = (169, 169, 169)
	pixels[px_cord_F4] = (169, 169, 169)
	pixels[px_cord_F11] = (169, 169, 169)
	pixels[px_cord_F14] = (169, 169, 169)

	pixels[px_cord_G2] = (169, 169, 169)
	pixels[px_cord_G3] = (169, 169, 169)
	pixels[px_cord_G12] = (169, 169, 169)
	pixels[px_cord_G13] = (169, 169, 169)

	pixels[px_cord_I2] = (169, 169, 169)
	pixels[px_cord_I3] = (169, 169, 169)
	pixels[px_cord_I12] = (169, 169, 169)
	pixels[px_cord_I13] = (169, 169, 169)

	pixels[px_cord_J1] = (169, 169, 169)
	pixels[px_cord_J4] = (169, 169, 169)
	pixels[px_cord_J11] = (169, 169, 169)
	pixels[px_cord_J14] = (169, 169, 169)

	pixels[px_cord_K5] = (169, 169, 169)
	pixels[px_cord_K6] = (169, 169, 169)
	pixels[px_cord_K7] = (169, 169, 169)
	pixels[px_cord_K15] = (169, 169, 169)
	pixels[px_cord_K16] = (169, 169, 169)
	pixels[px_cord_K17] = (169, 169, 169)

	pixels[px_cord_L5] = (169, 169, 169)
	pixels[px_cord_L7] = (169, 169, 169)
	pixels[px_cord_L15] = (169, 169, 169)
	pixels[px_cord_L17] = (169, 169, 169)

	pixels[px_cord_M5] = (169, 169, 169)
	pixels[px_cord_M6] = (169, 169, 169)
	pixels[px_cord_M7] = (169, 169, 169)
	pixels[px_cord_M15] = (169, 169, 169)
	pixels[px_cord_M16] = (169, 169, 169)
	pixels[px_cord_M17] = (169, 169, 169)

	pixels[px_cord_N1] = (169, 169, 169)
	pixels[px_cord_N4] = (169, 169, 169)
	pixels[px_cord_N11] = (169, 169, 169)
	pixels[px_cord_N14] = (169, 169, 169)

	pixels[px_cord_O2] = (169, 169, 169)
	pixels[px_cord_O3] = (169, 169, 169)
	pixels[px_cord_O12] = (169, 169, 169)
	pixels[px_cord_O13] = (169, 169, 169)

	# Flashing Red Noses
	noses = 0
	while noses < 10:
		# Noses Red
		pixels[px_cord_D6] = (255, 0, 0)
		pixels[px_cord_L6] = (255, 0, 0)
		pixels[px_cord_D16] = (255, 0, 0)
		pixels[px_cord_L16] = (255, 0, 0)

		# Show Noses On
		pixels.show()
		time.sleep(wait)

		# Clear Noses
		pixels[px_cord_D6] = (0, 0, 0)
		pixels[px_cord_L6] = (0, 0, 0)
		pixels[px_cord_D16] = (0, 0, 0)
		pixels[px_cord_L16] = (0, 0, 0)

		# Show Noses Off
		pixels.show()
		time.sleep(wait)

		# Up the animation counter by 1
		noses = noses + 1

def present(wait):
	# Christmas Present
	# Bow
	pixels[px_cord_A10] = (233, 245, 66)
	pixels[px_cord_A11] = (233, 245, 66)
	pixels[px_cord_A12] = (233, 245, 66)

	pixels[px_cord_B2] = (233, 245, 66)
	pixels[px_cord_B10] = (233, 245, 66)
	pixels[px_cord_B11] = (233, 245, 66)
	pixels[px_cord_B12] = (233, 245, 66)

	pixels[px_cord_C1] = (233, 245, 66)
	pixels[px_cord_C3] = (233, 245, 66)
	pixels[px_cord_C10] = (233, 245, 66)
	pixels[px_cord_C11] = (233, 245, 66)
	pixels[px_cord_C12] = (233, 245, 66)

	pixels[px_cord_D1] = (233, 245, 66)
	pixels[px_cord_D4] = (233, 245, 66)
	pixels[px_cord_D10] = (233, 245, 66)
	pixels[px_cord_D11] = (233, 245, 66)
	pixels[px_cord_D12] = (233, 245, 66)

	pixels[px_cord_E2] = (233, 245, 66)
	pixels[px_cord_E5] = (233, 245, 66)
	pixels[px_cord_E10] = (233, 245, 66)
	pixels[px_cord_E11] = (233, 245, 66)
	pixels[px_cord_E12] = (233, 245, 66)

	pixels[px_cord_F3] = (233, 245, 66)
	pixels[px_cord_F5] = (233, 245, 66)
	pixels[px_cord_F10] = (233, 245, 66)
	pixels[px_cord_F11] = (233, 245, 66)
	pixels[px_cord_F12] = (233, 245, 66)

	pixels[px_cord_G4] = (233, 245, 66)
	pixels[px_cord_G5] = (233, 245, 66)
	pixels[px_cord_G6] = (233, 245, 66)
	pixels[px_cord_G7] = (233, 245, 66)
	pixels[px_cord_G8] = (233, 245, 66)
	pixels[px_cord_G9] = (233, 245, 66)
	pixels[px_cord_G10] = (233, 245, 66)
	pixels[px_cord_G11] = (233, 245, 66)
	pixels[px_cord_G12] = (233, 245, 66)
	pixels[px_cord_G13] = (233, 245, 66)
	pixels[px_cord_G14] = (233, 245, 66)
	pixels[px_cord_G15] = (233, 245, 66)
	pixels[px_cord_G16] = (233, 245, 66)
	pixels[px_cord_G17] = (233, 245, 66)

	pixels[px_cord_H5] = (233, 245, 66)
	pixels[px_cord_H6] = (233, 245, 66)
	pixels[px_cord_H7] = (233, 245, 66)
	pixels[px_cord_H8] = (233, 245, 66)
	pixels[px_cord_H9] = (233, 245, 66)
	pixels[px_cord_H10] = (233, 245, 66)
	pixels[px_cord_H11] = (233, 245, 66)
	pixels[px_cord_H12] = (233, 245, 66)
	pixels[px_cord_H13] = (233, 245, 66)
	pixels[px_cord_H14] = (233, 245, 66)
	pixels[px_cord_H15] = (233, 245, 66)
	pixels[px_cord_H16] = (233, 245, 66)
	pixels[px_cord_H17] = (233, 245, 66)

	pixels[px_cord_I4] = (233, 245, 66)
	pixels[px_cord_I5] = (233, 245, 66)
	pixels[px_cord_I6] = (233, 245, 66)
	pixels[px_cord_I7] = (233, 245, 66)
	pixels[px_cord_I8] = (233, 245, 66)
	pixels[px_cord_I9] = (233, 245, 66)
	pixels[px_cord_I10] = (233, 245, 66)
	pixels[px_cord_I11] = (233, 245, 66)
	pixels[px_cord_I12] = (233, 245, 66)
	pixels[px_cord_I13] = (233, 245, 66)
	pixels[px_cord_I14] = (233, 245, 66)
	pixels[px_cord_I15] = (233, 245, 66)
	pixels[px_cord_I16] = (233, 245, 66)
	pixels[px_cord_I17] = (233, 245, 66)

	pixels[px_cord_J3] = (233, 245, 66)
	pixels[px_cord_J5] = (233, 245, 66)
	pixels[px_cord_J10] = (233, 245, 66)
	pixels[px_cord_J11] = (233, 245, 66)
	pixels[px_cord_J12] = (233, 245, 66)

	pixels[px_cord_K2] = (233, 245, 66)
	pixels[px_cord_K5] = (233, 245, 66)
	pixels[px_cord_K10] = (233, 245, 66)
	pixels[px_cord_K11] = (233, 245, 66)
	pixels[px_cord_K12] = (233, 245, 66)

	pixels[px_cord_L1] = (233, 245, 66)
	pixels[px_cord_L4] = (233, 245, 66)
	pixels[px_cord_L10] = (233, 245, 66)
	pixels[px_cord_L11] = (233, 245, 66)
	pixels[px_cord_L12] = (233, 245, 66)

	pixels[px_cord_M1] = (233, 245, 66)
	pixels[px_cord_M3] = (233, 245, 66)
	pixels[px_cord_M10] = (233, 245, 66)
	pixels[px_cord_M11] = (233, 245, 66)
	pixels[px_cord_M12] = (233, 245, 66)

	pixels[px_cord_N2] = (233, 245, 66)
	pixels[px_cord_N10] = (233, 245, 66)
	pixels[px_cord_N11] = (233, 245, 66)
	pixels[px_cord_N12] = (233, 245, 66)

	pixels[px_cord_O10] = (233, 245, 66)
	pixels[px_cord_O11] = (233, 245, 66)
	pixels[px_cord_O12] = (233, 245, 66)


	# Present Box
	pixels[px_cord_A6] = (255, 0, 0)
	pixels[px_cord_A7] = (255, 0, 0)
	pixels[px_cord_A8] = (255, 0, 0)
	pixels[px_cord_A9] = (255, 0, 0)
	pixels[px_cord_A13] = (255, 0, 0)
	pixels[px_cord_A14] = (255, 0, 0)
	pixels[px_cord_A15] = (255, 0, 0)
	pixels[px_cord_A16] = (255, 0, 0)
	pixels[px_cord_A17] = (255, 0, 0)

	pixels[px_cord_B6] = (255, 0, 0)
	pixels[px_cord_B7] = (255, 0, 0)
	pixels[px_cord_B8] = (255, 0, 0)
	pixels[px_cord_B9] = (255, 0, 0)
	pixels[px_cord_B13] = (255, 0, 0)
	pixels[px_cord_B14] = (255, 0, 0)
	pixels[px_cord_B15] = (255, 0, 0)
	pixels[px_cord_B16] = (255, 0, 0)
	pixels[px_cord_B17] = (255, 0, 0)

	pixels[px_cord_C6] = (255, 0, 0)
	pixels[px_cord_C7] = (255, 0, 0)
	pixels[px_cord_C8] = (255, 0, 0)
	pixels[px_cord_C9] = (255, 0, 0)
	pixels[px_cord_C13] = (255, 0, 0)
	pixels[px_cord_C14] = (255, 0, 0)
	pixels[px_cord_C15] = (255, 0, 0)
	pixels[px_cord_C16] = (255, 0, 0)
	pixels[px_cord_C17] = (255, 0, 0)

	pixels[px_cord_D6] = (255, 0, 0)
	pixels[px_cord_D7] = (255, 0, 0)
	pixels[px_cord_D8] = (255, 0, 0)
	pixels[px_cord_D9] = (255, 0, 0)
	pixels[px_cord_D13] = (255, 0, 0)
	pixels[px_cord_D14] = (255, 0, 0)
	pixels[px_cord_D15] = (255, 0, 0)
	pixels[px_cord_D16] = (255, 0, 0)
	pixels[px_cord_D17] = (255, 0, 0)

	pixels[px_cord_E6] = (255, 0, 0)
	pixels[px_cord_E7] = (255, 0, 0)
	pixels[px_cord_E8] = (255, 0, 0)
	pixels[px_cord_E9] = (255, 0, 0)
	pixels[px_cord_E13] = (255, 0, 0)
	pixels[px_cord_E14] = (255, 0, 0)
	pixels[px_cord_E15] = (255, 0, 0)
	pixels[px_cord_E16] = (255, 0, 0)
	pixels[px_cord_E17] = (255, 0, 0)

	pixels[px_cord_F6] = (255, 0, 0)
	pixels[px_cord_F7] = (255, 0, 0)
	pixels[px_cord_F8] = (255, 0, 0)
	pixels[px_cord_F9] = (255, 0, 0)
	pixels[px_cord_F13] = (255, 0, 0)
	pixels[px_cord_F14] = (255, 0, 0)
	pixels[px_cord_F15] = (255, 0, 0)
	pixels[px_cord_F16] = (255, 0, 0)
	pixels[px_cord_F17] = (255, 0, 0)

	pixels[px_cord_J6] = (255, 0, 0)
	pixels[px_cord_J7] = (255, 0, 0)
	pixels[px_cord_J8] = (255, 0, 0)
	pixels[px_cord_J9] = (255, 0, 0)
	pixels[px_cord_J13] = (255, 0, 0)
	pixels[px_cord_J14] = (255, 0, 0)
	pixels[px_cord_J15] = (255, 0, 0)
	pixels[px_cord_J16] = (255, 0, 0)
	pixels[px_cord_J17] = (255, 0, 0)

	pixels[px_cord_K6] = (255, 0, 0)
	pixels[px_cord_K7] = (255, 0, 0)
	pixels[px_cord_K8] = (255, 0, 0)
	pixels[px_cord_K9] = (255, 0, 0)
	pixels[px_cord_K13] = (255, 0, 0)
	pixels[px_cord_K14] = (255, 0, 0)
	pixels[px_cord_K15] = (255, 0, 0)
	pixels[px_cord_K16] = (255, 0, 0)
	pixels[px_cord_K17] = (255, 0, 0)

	pixels[px_cord_L6] = (255, 0, 0)
	pixels[px_cord_L7] = (255, 0, 0)
	pixels[px_cord_L8] = (255, 0, 0)
	pixels[px_cord_L9] = (255, 0, 0)
	pixels[px_cord_L13] = (255, 0, 0)
	pixels[px_cord_L14] = (255, 0, 0)
	pixels[px_cord_L15] = (255, 0, 0)
	pixels[px_cord_L16] = (255, 0, 0)
	pixels[px_cord_L17] = (255, 0, 0)

	pixels[px_cord_M6] = (255, 0, 0)
	pixels[px_cord_M7] = (255, 0, 0)
	pixels[px_cord_M8] = (255, 0, 0)
	pixels[px_cord_M9] = (255, 0, 0)
	pixels[px_cord_M13] = (255, 0, 0)
	pixels[px_cord_M14] = (255, 0, 0)
	pixels[px_cord_M15] = (255, 0, 0)
	pixels[px_cord_M16] = (255, 0, 0)
	pixels[px_cord_M17] = (255, 0, 0)

	pixels[px_cord_N6] = (255, 0, 0)
	pixels[px_cord_N7] = (255, 0, 0)
	pixels[px_cord_N8] = (255, 0, 0)
	pixels[px_cord_N9] = (255, 0, 0)
	pixels[px_cord_N13] = (255, 0, 0)
	pixels[px_cord_N14] = (255, 0, 0)
	pixels[px_cord_N15] = (255, 0, 0)
	pixels[px_cord_N16] = (255, 0, 0)
	pixels[px_cord_N17] = (255, 0, 0)

	pixels[px_cord_O6] = (255, 0, 0)
	pixels[px_cord_O7] = (255, 0, 0)
	pixels[px_cord_O8] = (255, 0, 0)
	pixels[px_cord_O9] = (255, 0, 0)
	pixels[px_cord_O13] = (255, 0, 0)
	pixels[px_cord_O14] = (255, 0, 0)
	pixels[px_cord_O15] = (255, 0, 0)
	pixels[px_cord_O16] = (255, 0, 0)
	pixels[px_cord_O17] = (255, 0, 0)

	#Show Christmas Present
	pixels.show()
	time.sleep(wait)

def santa_stop_here_pos1(wait):
	# Santa Stop Here Position 1
	# Santa
	pixels[px_cord_A1] = (255, 0, 0)
	pixels[px_cord_B1] = (255, 0, 0)
	pixels[px_cord_C1] = (255, 0, 0)
	pixels[px_cord_D1] = (0, 255, 0)
	pixels[px_cord_E1] = (0, 255, 0)
	pixels[px_cord_F1] = (0, 255, 0)
	pixels[px_cord_G1] = (255, 0, 0)
	pixels[px_cord_H1] = (255, 0, 0)
	pixels[px_cord_I1] = (255, 0, 0)
	pixels[px_cord_J1] = (0, 255, 0)
	pixels[px_cord_K1] = (0, 255, 0)
	pixels[px_cord_L1] = (0, 255, 0)
	pixels[px_cord_M1] = (255, 0, 0)
	pixels[px_cord_N1] = (255, 0, 0)
	pixels[px_cord_O1] = (255, 0, 0)

	pixels[px_cord_A2] = (255, 0, 0)
	pixels[px_cord_D2] = (0, 255, 0)
	pixels[px_cord_F2] = (0, 255, 0)
	pixels[px_cord_G2] = (255, 0, 0)
	pixels[px_cord_I2] = (255, 0, 0)
	pixels[px_cord_K2] = (0, 255, 0)
	pixels[px_cord_M2] = (255, 0, 0)
	pixels[px_cord_O2] = (255, 0, 0)

	pixels[px_cord_A3] = (255, 0, 0)
	pixels[px_cord_B3] = (255, 0, 0)
	pixels[px_cord_C3] = (255, 0, 0)
	pixels[px_cord_D3] = (0, 255, 0)
	pixels[px_cord_E3] = (0, 255, 0)
	pixels[px_cord_F3] = (0, 255, 0)
	pixels[px_cord_G3] = (255, 0, 0)
	pixels[px_cord_I3] = (255, 0, 0)
	pixels[px_cord_K3] = (0, 255, 0)
	pixels[px_cord_M3] = (255, 0, 0)
	pixels[px_cord_N3] = (255, 0, 0)
	pixels[px_cord_O3] = (255, 0, 0)

	pixels[px_cord_C4] = (255, 0, 0)
	pixels[px_cord_D4] = (0, 255, 0)
	pixels[px_cord_F4] = (0, 255, 0)
	pixels[px_cord_G4] = (255, 0, 0)
	pixels[px_cord_I4] = (255, 0, 0)
	pixels[px_cord_K4] = (0, 255, 0)
	pixels[px_cord_M4] = (255, 0, 0)
	pixels[px_cord_O4] = (255, 0, 0)

	pixels[px_cord_A5] = (255, 0, 0)
	pixels[px_cord_B5] = (255, 0, 0)
	pixels[px_cord_C5] = (255, 0, 0)
	pixels[px_cord_D5] = (0, 255, 0)
	pixels[px_cord_F5] = (0, 255, 0)
	pixels[px_cord_G5] = (255, 0, 0)
	pixels[px_cord_I5] = (255, 0, 0)
	pixels[px_cord_K5] = (0, 255, 0)
	pixels[px_cord_M5] = (255, 0, 0)
	pixels[px_cord_O5] = (255, 0, 0)

	# Stop
	pixels[px_cord_B7] = (255, 0, 0)
	pixels[px_cord_C7] = (255, 0, 0)
	pixels[px_cord_D7] = (255, 0, 0)
	pixels[px_cord_E7] = (0, 255, 0)
	pixels[px_cord_F7] = (0, 255, 0)
	pixels[px_cord_G7] = (0, 255, 0)
	pixels[px_cord_H7] = (255, 0, 0)
	pixels[px_cord_I7] = (255, 0, 0)
	pixels[px_cord_J7] = (255, 0, 0)
	pixels[px_cord_K7] = (0, 255, 0)
	pixels[px_cord_L7] = (0, 255, 0)
	pixels[px_cord_M7] = (0, 255, 0)

	pixels[px_cord_B8] = (255, 0, 0)
	pixels[px_cord_F8] = (0, 255, 0)
	pixels[px_cord_H8] = (255, 0, 0)
	pixels[px_cord_J8] = (255, 0, 0)
	pixels[px_cord_K8] = (0, 255, 0)
	pixels[px_cord_M8] = (0, 255, 0)

	pixels[px_cord_B9] = (255, 0, 0)
	pixels[px_cord_C9] = (255, 0, 0)
	pixels[px_cord_D9] = (255, 0, 0)
	pixels[px_cord_F9] = (0, 255, 0)
	pixels[px_cord_H9] = (255, 0, 0)
	pixels[px_cord_J9] = (255, 0, 0)
	pixels[px_cord_K9] = (0, 255, 0)
	pixels[px_cord_L9] = (0, 255, 0)
	pixels[px_cord_M9] = (0, 255, 0)

	pixels[px_cord_D10] = (255, 0, 0)
	pixels[px_cord_F10] = (0, 255, 0)
	pixels[px_cord_H10] = (255, 0, 0)
	pixels[px_cord_J10] = (255, 0, 0)
	pixels[px_cord_K10] = (0, 255, 0)

	pixels[px_cord_B11] = (255, 0, 0)
	pixels[px_cord_C11] = (255, 0, 0)
	pixels[px_cord_D11] = (255, 0, 0)
	pixels[px_cord_F11] = (0, 255, 0)
	pixels[px_cord_H11] = (255, 0, 0)
	pixels[px_cord_I11] = (255, 0, 0)
	pixels[px_cord_J11] = (255, 0, 0)
	pixels[px_cord_K11] = (0, 255, 0)

	#Here
	pixels[px_cord_B13] = (255, 0, 0)
	pixels[px_cord_D13] = (255, 0, 0)
	pixels[px_cord_E13] = (0, 255, 0)
	pixels[px_cord_F13] = (0, 255, 0)
	pixels[px_cord_G13] = (0, 255, 0)
	pixels[px_cord_H13] = (255, 0, 0)
	pixels[px_cord_I13] = (255, 0, 0)
	pixels[px_cord_K13] = (0, 255, 0)
	pixels[px_cord_L13] = (0, 255, 0)
	pixels[px_cord_M13] = (0, 255, 0)

	pixels[px_cord_B14] = (255, 0, 0)
	pixels[px_cord_D14] = (255, 0, 0)
	pixels[px_cord_E14] = (0, 255, 0)
	pixels[px_cord_H14] = (255, 0, 0)
	pixels[px_cord_J14] = (255, 0, 0)
	pixels[px_cord_K14] = (0, 255, 0)

	pixels[px_cord_B15] = (255, 0, 0)
	pixels[px_cord_C15] = (255, 0, 0)
	pixels[px_cord_D15] = (255, 0, 0)
	pixels[px_cord_E15] = (0, 255, 0)
	pixels[px_cord_F15] = (0, 255, 0)
	pixels[px_cord_H15] = (255, 0, 0)
	pixels[px_cord_I15] = (255, 0, 0)
	pixels[px_cord_K15] = (0, 255, 0)
	pixels[px_cord_L15] = (0, 255, 0)

	pixels[px_cord_B16] = (255, 0, 0)
	pixels[px_cord_D16] = (255, 0, 0)
	pixels[px_cord_E16] = (0, 255, 0)
	pixels[px_cord_H16] = (255, 0, 0)
	pixels[px_cord_J16] = (255, 0, 0)
	pixels[px_cord_K16] = (0, 255, 0)

	pixels[px_cord_B17] = (255, 0, 0)
	pixels[px_cord_D17] = (255, 0, 0)
	pixels[px_cord_E17] = (0, 255, 0)
	pixels[px_cord_F17] = (0, 255, 0)
	pixels[px_cord_G17] = (0, 255, 0)
	pixels[px_cord_H17] = (255, 0, 0)
	pixels[px_cord_J17] = (255, 0, 0)
	pixels[px_cord_K17] = (0, 255, 0)
	pixels[px_cord_L17] = (0, 255, 0)
	pixels[px_cord_M17] = (0, 255, 0)

	#Display Santa Stop Here Position 1
	pixels.show()
	time.sleep(wait)

def santa_stop_here_pos2(wait):
	# Santa Stop Here Position 2
	# Santa
	pixels[px_cord_A1] = (0, 255, 0)
	pixels[px_cord_B1] = (0, 255, 0)
	pixels[px_cord_C1] = (0, 255, 0)
	pixels[px_cord_D1] = (255, 0, 0)
	pixels[px_cord_E1] = (255, 0, 0)
	pixels[px_cord_F1] = (255, 0, 0)
	pixels[px_cord_G1] = (0, 255, 0)
	pixels[px_cord_H1] = (0, 255, 0)
	pixels[px_cord_I1] = (0, 255, 0)
	pixels[px_cord_J1] = (255, 0, 0)
	pixels[px_cord_K1] = (255, 0, 0)
	pixels[px_cord_L1] = (255, 0, 0)
	pixels[px_cord_M1] = (0, 255, 0)
	pixels[px_cord_N1] = (0, 255, 0)
	pixels[px_cord_O1] = (0, 255, 0)

	pixels[px_cord_A2] = (0, 255, 0)
	pixels[px_cord_D2] = (255, 0, 0)
	pixels[px_cord_F2] = (255, 0, 0)
	pixels[px_cord_G2] = (0, 255, 0)
	pixels[px_cord_I2] = (0, 255, 0)
	pixels[px_cord_K2] = (255, 0, 0)
	pixels[px_cord_M2] = (0, 255, 0)
	pixels[px_cord_O2] = (0, 255, 0)

	pixels[px_cord_A3] = (0, 255, 0)
	pixels[px_cord_B3] = (0, 255, 0)
	pixels[px_cord_C3] = (0, 255, 0)
	pixels[px_cord_D3] = (255, 0, 0)
	pixels[px_cord_E3] = (255, 0, 0)
	pixels[px_cord_F3] = (255, 0, 0)
	pixels[px_cord_G3] = (0, 255, 0)
	pixels[px_cord_I3] = (0, 255, 0)
	pixels[px_cord_K3] = (255, 0, 0)
	pixels[px_cord_M3] = (0, 255, 0)
	pixels[px_cord_N3] = (0, 255, 0)
	pixels[px_cord_O3] = (0, 255, 0)

	pixels[px_cord_C4] = (0, 255, 0)
	pixels[px_cord_D4] = (255, 0, 0)
	pixels[px_cord_F4] = (255, 0, 0)
	pixels[px_cord_G4] = (0, 255, 0)
	pixels[px_cord_I4] = (0, 255, 0)
	pixels[px_cord_K4] = (255, 0, 0)
	pixels[px_cord_M4] = (0, 255, 0)
	pixels[px_cord_O4] = (0, 255, 0)

	pixels[px_cord_A5] = (0, 255, 0)
	pixels[px_cord_B5] = (0, 255, 0)
	pixels[px_cord_C5] = (0, 255, 0)
	pixels[px_cord_D5] = (255, 0, 0)
	pixels[px_cord_F5] = (255, 0, 0)
	pixels[px_cord_G5] = (0, 255, 0)
	pixels[px_cord_I5] = (0, 255, 0)
	pixels[px_cord_K5] = (255, 0, 0)
	pixels[px_cord_M5] = (0, 255, 0)
	pixels[px_cord_O5] = (0, 255, 0)

	# Stop
	pixels[px_cord_B7] = (0, 255, 0)
	pixels[px_cord_C7] = (0, 255, 0)
	pixels[px_cord_D7] = (0, 255, 0)
	pixels[px_cord_E7] = (255, 0, 0)
	pixels[px_cord_F7] = (255, 0, 0)
	pixels[px_cord_G7] = (255, 0, 0)
	pixels[px_cord_H7] = (0, 255, 0)
	pixels[px_cord_I7] = (0, 255, 0)
	pixels[px_cord_J7] = (0, 255, 0)
	pixels[px_cord_K7] = (255, 0, 0)
	pixels[px_cord_L7] = (255, 0, 0)
	pixels[px_cord_M7] = (255, 0, 0)

	pixels[px_cord_B8] = (0, 255, 0)
	pixels[px_cord_F8] = (255, 0, 0)
	pixels[px_cord_H8] = (0, 255, 0)
	pixels[px_cord_J8] = (0, 255, 0)
	pixels[px_cord_K8] = (255, 0, 0)
	pixels[px_cord_M8] = (255, 0, 0)

	pixels[px_cord_B9] = (0, 255, 0)
	pixels[px_cord_C9] = (0, 255, 0)
	pixels[px_cord_D9] = (0, 255, 0)
	pixels[px_cord_F9] = (255, 0, 0)
	pixels[px_cord_H9] = (0, 255, 0)
	pixels[px_cord_J9] = (0, 255, 0)
	pixels[px_cord_K9] = (255, 0, 0)
	pixels[px_cord_L9] = (255, 0, 0)
	pixels[px_cord_M9] = (255, 0, 0)

	pixels[px_cord_D10] = (0, 255, 0)
	pixels[px_cord_F10] = (255, 0, 0)
	pixels[px_cord_H10] = (0, 255, 0)
	pixels[px_cord_J10] = (0, 255, 0)
	pixels[px_cord_K10] = (255, 0, 0)

	pixels[px_cord_B11] = (0, 255, 0)
	pixels[px_cord_C11] = (0, 255, 0)
	pixels[px_cord_D11] = (0, 255, 0)
	pixels[px_cord_F11] = (255, 0, 0)
	pixels[px_cord_H11] = (0, 255, 0)
	pixels[px_cord_I11] = (0, 255, 0)
	pixels[px_cord_J11] = (0, 255, 0)
	pixels[px_cord_K11] = (255, 0, 0)

	#Here
	pixels[px_cord_B13] = (0, 255, 0)
	pixels[px_cord_D13] = (0, 255, 0)
	pixels[px_cord_E13] = (255, 0, 0)
	pixels[px_cord_F13] = (255, 0, 0)
	pixels[px_cord_G13] = (255, 0, 0)
	pixels[px_cord_H13] = (0, 255, 0)
	pixels[px_cord_I13] = (0, 255, 0)
	pixels[px_cord_K13] = (255, 0, 0)
	pixels[px_cord_L13] = (255, 0, 0)
	pixels[px_cord_M13] = (255, 0, 0)

	pixels[px_cord_B14] = (0, 255, 0)
	pixels[px_cord_D14] = (0, 255, 0)
	pixels[px_cord_E14] = (255, 0, 0)
	pixels[px_cord_H14] = (0, 255, 0)
	pixels[px_cord_J14] = (0, 255, 0)
	pixels[px_cord_K14] = (255, 0, 0)

	pixels[px_cord_B15] = (0, 255, 0)
	pixels[px_cord_C15] = (0, 255, 0)
	pixels[px_cord_D15] = (0, 255, 0)
	pixels[px_cord_E15] = (255, 0, 0)
	pixels[px_cord_F15] = (255, 0, 0)
	pixels[px_cord_H15] = (0, 255, 0)
	pixels[px_cord_I15] = (0, 255, 0)
	pixels[px_cord_K15] = (255, 0, 0)
	pixels[px_cord_L15] = (255, 0, 0)

	pixels[px_cord_B16] = (0, 255, 0)
	pixels[px_cord_D16] = (0, 255, 0)
	pixels[px_cord_E16] = (255, 0, 0)
	pixels[px_cord_H16] = (0, 255, 0)
	pixels[px_cord_J16] = (0, 255, 0)
	pixels[px_cord_K16] = (255, 0, 0)

	pixels[px_cord_B17] = (0, 255, 0)
	pixels[px_cord_D17] = (0, 255, 0)
	pixels[px_cord_E17] = (255, 0, 0)
	pixels[px_cord_F17] = (255, 0, 0)
	pixels[px_cord_G17] = (255, 0, 0)
	pixels[px_cord_H17] = (0, 255, 0)
	pixels[px_cord_J17] = (0, 255, 0)
	pixels[px_cord_K17] = (255, 0, 0)
	pixels[px_cord_L17] = (255, 0, 0)
	pixels[px_cord_M17] = (255, 0, 0)

	#Display Santa Stop Here Position 2
	pixels.show()
	time.sleep(wait)

# Main Display Loop
while True:
	#Multi Deer!
	clear_all_pixels()
	multi_reindeer(1)

	# Santa Stop Here
	clear_all_pixels()
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)
	santa_stop_here_pos1(0.5)
	santa_stop_here_pos2(0.5)

	# Fireplace
	clear_all_pixels()
	fireplace(0.5)

	# Reindeer
	clear_all_pixels()
	reindeer(1)

	# Stocking
	clear_all_pixels()
	stocking(10)

	# Merry Christmas Text
	clear_all_pixels()
	merry_xmas_138_text(0.5)

	# Santa Hat Animation
	clear_all_pixels()
	santa_hat(1)

	# Snowflake
	clear_all_pixels()
	snowflake(0.5, 10, 0, 145)
	snowflake(0.5, 255, 255, 255)
	snowflake(0.5, 10, 0, 145)
	snowflake(0.5, 255, 255, 255)
	snowflake(0.5, 10, 0, 145)
	snowflake(0.5, 255, 255, 255)
	snowflake(0.5, 10, 0, 145)
	snowflake(0.5, 255, 255, 255)
	snowflake(0.5, 10, 0, 145)
	snowflake(0.5, 255, 255, 255)

	# Let it Snow
	clear_all_pixels()
	let_it_snow(10, 10, 10, 0.1, 1)

	# Christmas Present
	clear_all_pixels()
	present(10)

	# Christmas Tree
	clear_all_pixels()
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)
	tree_pos_1(0.5)
	tree_pos_2(0.5)

	# Snowman
	clear_all_pixels()
	snowman(10)

	# Ho Ho Ho
	clear_all_pixels()
	ho_ho(5)
	clear_all_pixels()
	only_ho(5)

	# Candy Cane Animation
	clear_all_pixels()
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
	candy_cane_pos_1(0.5)
	candy_cane_pos_2(0.5)
