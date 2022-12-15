from models.color import rank_colors
from threads import get_answerank, get_createrank, update_answerank, update_createrank

def get_ranks(user_id):
    answer_rank = get_answerank(user_id)
    create_rank = get_createrank(user_id)
    
    answer_amount = answer_rank[0]
    answer_level = answer_rank[1]
    create_amount = create_rank[0]
    create_level = create_rank[1]
    return [answer_amount, answer_level, create_amount, create_level]

# def call_update_answerank(user_id, amount):
#     level = ""
#     amount += 1
#     if amount >= 5:
#         level = "Silver"

#     if amount >=10:
#         level = "Gold"

#     if amount >= 20:
#         level = "Platinum"

#     if amount >= 40:
#         level = "Diamond"

#     if amount >= 60:
#         level = "Champion"
    
#     if amount >= 80:
#         level = "Grand Champion"

#     if amount >= 100:
#         level = "Demi God"

#     update_answerank(user_id, amount,level)


# def call_update_createrank(user_id, amount):
#     level = ""
#     if amount >= 1:
#         level = "Silver"

#     if amount >=3:
#         level = "Gold"

#     if amount >= 5:
#         level = "Platinum"

#     if amount >= 7:
#         level = "Diamond"

#     if amount >= 10:
#         level = "Champion"
    
#     if amount >= 15:
#         level = "Grand Champion"

#     if amount >= 20:
#         level = "Demi God"
    
#     update_createrank(user_id, level)

def get_rankcolor(level):
    rank_color = [color for color in rank_colors if color.name == level]
    return rank_color[0]