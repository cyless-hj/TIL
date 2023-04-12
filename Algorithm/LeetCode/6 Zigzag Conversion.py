class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index_dict = {}
        zigzag_index = 0
        down = 1
        up = -1
        move = 0
        for character in s:
            if zigzag_index == 0:
                move = down
            elif zigzag_index == numRows - 1:
                move = up

            index_dict[zigzag_index] = index_dict.get(zigzag_index, '') + character
            zigzag_index += move

        return ''.join(index_dict.values())