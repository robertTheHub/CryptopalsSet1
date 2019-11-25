import convert
import xor
import scoreboard
import scoring


def single_byte_xor(input_bytes, num_results=1):
    board = scoreboard.Scoreboard(num_results, ("Guess", "Result"))
    for i in range(256):
        char = chr(i)
        temp_byte_array = xor.byte_array_with_string(input_bytes, char)
        decoded_string = convert.bytes_to_string(temp_byte_array)
        score = scoring.score_string(decoded_string)
        board.update([score], [[char], [decoded_string]])
    return board


def single_byte_xor_in_iterable(iterable, num_results=1):
    board = scoreboard.Scoreboard(num_results, ("Guess", "Result"))
    for line in iterable.readlines():
        line = line.strip()
        byte_array = convert.hex_string_to_bytes(line)
        another_board = single_byte_xor(byte_array, 10)
        board.update(another_board.get_rankings(), tuple(another_board.get_meta()))
    return board
