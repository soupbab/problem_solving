def dfs(word_now, words, target, min_root, word_len, len_first):
    words_ = words.copy()
    words_.remove(word_now)
    len_now = len(words_)
    for word in words_:
        if count_overlap(word_now, word, word_len) == word_len - 1:
            if word == target:
                min_root = min(min_root, len_first - len_now)
                
                return min_root
            else:
                temp = dfs(word, words_, target, min_root, word_len, len_first)
                if temp is not None:
                    min_root = min(min_root, temp)
                    
    return min_root


def count_overlap(a, b, word_len):
    a_ = list(a)
    b_ = list(b)
    count = 0
    for i in range(word_len):
        if a_[i] == b_[i]:
            count += 1
            
    return count


def solution(begin, target, words):
    if target not in words:
        return 0
    
    word_len = len(begin)
    words.append(begin)
    len_first = len(words)
    min_root = len(words) + 1
    
    return dfs(begin, words, target, min_root, word_len, len_first)
