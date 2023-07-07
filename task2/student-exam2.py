def final_Score(midterm1, midterm2):

    exam1 = midterm1 * 30 / 100

    exam2 = midterm2 * 30 / 100

    total_score = exam1 + exam2

    exam_score = 61 - total_score
    final_score = 100 * exam_score / 40


    if final_score < 0:
        return 0
    else:
        print((midterm1, midterm2))
        print(final_score)




midterm1 = int(input('Midterm1:  '))
if midterm1 <= 100 and midterm1 >= 0:

    midterm2 = int(input('Midterm2:  '))
    if midterm2 <= 100 and midterm2 >= 0:

        final_Score(midterm1, midterm2)

    else:
        print('Yanlış  məlumat')
else:
    print('Yanlış  məlumat')