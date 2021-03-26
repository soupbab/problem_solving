def solution(name):
    ascii_list = list(map(ord, name)) # A = 65, Z = 90
    a_is_zero = list(map(lambda x: x - 65, ascii_list)) # A = 0, Z = 25
    vertical_moves = list(map(lambda x: min(x, 26 - x), a_is_zero))

    answer = 0
    index = 0
    while sum(vertical_moves) != 0:
        if vertical_moves[index] != 0:
            horizontal_move = 0
        else:
            nonzero_indices = [index for index, count in enumerate(vertical_moves) if count > 0]    
            nonzero_indices.sort()
            nonzero_min_idx = nonzero_indices[0]
            nonzero_max_idx = nonzero_indices[-1]

            if index < nonzero_min_idx:
                right_move = nonzero_min_idx - index
                left_move = len(vertical_moves) - nonzero_max_idx + index
            else:
                right_move = len(vertical_moves) - index + nonzero_min_idx
                left_move = index - nonzero_max_idx

            if right_move <= left_move:
                horizontal_move = right_move
                index = nonzero_min_idx
            else:
                horizontal_move = left_move
                index = nonzero_max_idx
        
        answer += horizontal_move
        answer += vertical_moves[index]
        vertical_moves[index] = 0

    return answer
