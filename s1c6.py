import convert
import cipher
import scoreboard


def createArrays(block, size):
    array = []
    count = 0
    temp = b""
    for byte in block:
        count += 1
        temp += bytes([byte])
        if count == size:
            count = 0
            array.append(temp)
            temp = b""
    return array


def transpose(array):
    outside = len(array)
    inside = len(array[0])
    print(outside, inside)
    tarray = []
    temp = b""
    for i in range(inside):
        for j in range(outside):
            temp +=  bytes([array[j][i]])
        tarray.append(temp)
        temp = b""
    return tarray


if __name__ == "__main__":
    block = ""
    with open("6.txt", "r") as theBlock:
        block = convert.base64_to_byte_array(theBlock.read())

    board = scoreboard.Scoreboard(4, ["Key Size"], -1000)

    for key in range(2, 41):
        dist = cipher.hamming_distance_of_bytes(block[:key], block[key:2 * key])
        dist2 = cipher.hamming_distance_of_bytes(block[2 * key:3 * key], block[3 * key:4 * key])
        avg = -(dist / (2 * key))
        board.update([avg], [[key]])

    print(board)

    arrays = transpose(createArrays(block, 2))
    for series in arrays:
        cipher.single_byte_xor_in_iterable(series, 3)
