import convert
import xor
import scoreboard
import scoring


def single_byte_xor(input_bytes, results=1):
    board = scoreboard.Scoreboard(results, ("Guess", "Result"))
    for i in range(256):
        char = chr(i)
        temp_byte_array = xor.byte_array_with_string(input_bytes, char)
        decoded_string = convert.bytes_to_string(temp_byte_array)
        a_score = scoring.score_string(decoded_string)
        print(decoded_string)
        board.update(a_score, (char, decoded_string))
    return board


def single_byte_xor_in_iterable(iterable, results=1):
    board = scoreboard.Scoreboard(results, ("Guess", "Result"))
    if True:  # for aLine in aIterable
        line = iterable.readlines()[171].strip()
        byte_array = convert.hex_string_to_bytes(line)
        another_board = single_byte_xor(byte_array, 10)
        #        a_scoreboard.update(another_scoreboard.topScore(), another_scoreboard.topMeta())
        print(another_board)
    return board
