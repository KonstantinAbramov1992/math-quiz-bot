from Get_base import get_base
from operator import itemgetter

# get sorted list. each number is dictionary. key is rank(high for first, lower to last)
# mean is list (user_name, right_tries, wrong_tries)
def get_rank():
    # get unsorted list. each number is dictionary. key is user_id
    # mean is list (user_name, right_tries, wrong_tries)
    a = get_base()

    rank_list = []
    final_list = []
    # get list where each item is list[rank, user_id] and then sort it by rank(high to low)
    for k in a:
        for k_2 in k:
            user_id_list = k[k_2]
            rank = user_id_list[1] - user_id_list[2]
            rank_list.append([rank, user_id_list[0], user_id_list[1], user_id_list[2]])
    rank_list.sort(key=itemgetter(0), reverse=True)
    for i in rank_list:
        dict = {
            #'rank': i[0],
            #'username':i[1],
            #'right': i[2],
            #'wrong': i[3],
            i[0]:[i[1], i[2], i[3]]}

        final_list.append(dict)

    print(rank_list)
    print(a)
    # Create new list as we need
        



    print(final_list)
    return final_list
