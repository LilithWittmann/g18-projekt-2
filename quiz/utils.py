def generate_answers(question):
    answers = []
    for answer in question.get_answers():
        answers.append((answer.pk, answer.text))

    return answers