from collections import defaultdict

def solution(genres, plays):
    play_count = defaultdict(int)
    for genre, play in zip(genres, plays):
        play_count[genre] += play

    zipped_list = [(genre, play, index) for index, (genre, play) in enumerate(zip(genres, plays))]
    zipped_list.sort(key=lambda x: x[2])
    zipped_list.sort(key=lambda x: x[1], reverse=True)
    zipped_list.sort(key=lambda x: play_count[x[0]], reverse=True)
    
    answer = []
    genre_count = defaultdict(int)
    for item in zipped_list:
        if genre_count[item[0]] < 2:
            answer.append(item[2])
            genre_count[item[0]] += 1
    return answer
