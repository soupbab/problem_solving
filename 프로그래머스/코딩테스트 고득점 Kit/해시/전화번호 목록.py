def solution(phone_book):
    len_set = set()
    for phone_number in phone_book:
        len_set.add(len(phone_number))
        
    phone_dict = {phone_number: 0 for phone_number in phone_book}
        
    for phone_number in phone_book:
        for num_len in len_set:
            if len(phone_number) > num_len and phone_number[:num_len] in phone_dict:
                return False        
    
    return True
