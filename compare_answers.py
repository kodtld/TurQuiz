def compare_answers(right_answers,user_answers):
    imd = user_answers
    score = imd.to_dict(flat=False)
    user_answer_values = [i[0] for i in score.values()]
    right_answer_values = [i[1] for i in right_answers]
    counter = 0

    print(user_answer_values)
    print(right_answer_values)

    if len(user_answer_values) == len(right_answer_values):
        for i in range(0,len(right_answer_values)):
            if right_answer_values[i] == user_answer_values[i] :
                counter += 1
        
        result = (counter / len(user_answer_values)) * 100
        return result