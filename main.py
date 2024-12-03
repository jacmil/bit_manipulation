'''
inputs for 'hex' or 'binary' must be string format, with no leading '0#'
inputs for 'shift' take whole integers
'''

# Arithmetic shift right
def ASR(hex, shift):
    realhex = int(hex, 16)
    binary = bin(realhex)[2:]

    while len(binary) < 32:
        binary = f'{0}{binary}'

    if binary[:1] == '1':
        shifted = f'{shift*'1'}{binary[:32-shift]}'
    else:
        shifted = f'{shift*'0'}{binary[:32-shift]}'

    while len(shifted) % 4 != 0:
        shifted = '0' + shifted

    print(b2h(shifted))

# Logical shift left
def LSL(hex, shift):
    realhex = int(hex, 16)


    # Convert integer to binary (removing '0b' prefix) and ensure it's 32 bits long
    binary = bin(realhex)[2:].zfill(32)

    # Perform logical shift left (append zeros to the right)
    shifted = binary[shift:] + '0' * shift

    print(b2h(shifted))


# Logical shift right
def LSR(hex, shift):
    realhex = int(hex, 16)
    binary = bin(realhex)[2:]

    while len(binary) < 32:
        binary = f'{0}{binary}'

    shifted = f'{shift * '0'}{binary[:32 - shift]}'

    while len(shifted) % 4 != 0:
        shifted = '0' + shifted

    print(b2h(shifted))

# Binary to Hex
def b2h(binary):
    # Map binary chunks to their hexadecimal equivalents
    binary_to_hex_map = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }

    # Convert binary to hexadecimal
    hex_str = ''.join(binary_to_hex_map[binary[i:i + 4]] for i in range(0, len(binary), 4))

    return f'0x{hex_str[:8]}'

# Hexadecimal to Binary
def h2b(hex):
    realhex = int(hex, 16)
    binary = bin(realhex)[2:]

    while len(binary) < 32:
        binary = f'{0}{binary}'

    return binary

# To lazy to make this a class...
def operation(type, shift, hex):
    if type == 'ASR':
        ASR(hex, shift)
    elif type == 'LSR':
        LSR(hex, shift)
    elif type == 'LSL':
        LSL(hex, shift)
    print('\n')

# Rotation
def rot(binary, shift):
    result = f'{binary[32-shift:]}{binary[:32-shift]}'
    return result

# Binary to Decimal
def b2d(binary):
    length = len(binary)
    val = length - 1
    decimal = 0
    for i in range(length):
        decimal += int(binary[i]) * (2 ** val)
        val -= 1
    return decimal

# Trims lead zeros
def leadZeroTrimmer(binary):
    nonZero = False
    binary = str(binary)
    cb = []
    while nonZero is False:
        for i in range(4):
            cb.append(binary[i])
        if '1' in cb:
            nonZero = True
        else:
            binary = binary[4:]
        cb = []
    return binary

# Cheeky
def rotation_hw(hex):
    h = h2b(hex[1:])
    a = 2 * b2d(h2b(hex[:1]))
    r = rot(h, int(a))
    trim = leadZeroTrimmer(r)
    x = b2h(trim)
    print(x)
