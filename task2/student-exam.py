def calculate_Score(midterm1, midterm2, final):
    

    exam1 = midterm1 * 30 / 100

    
    exam2 = midterm2 * 30 / 100

    
    exam3 = final * 40 / 100

    total_score = exam1 + exam2 + exam3

    if total_score <= 100 and total_score >= 91:
        print((midterm1, midterm2, final))
        print('>>> A')
    
    elif total_score <= 90 and total_score >= 81:
        print((midterm1, midterm2, final))
        print('>>> B')


    elif total_score <= 80 and total_score >= 71:
        print((midterm1, midterm2, final))
        print('>>> C')


    elif total_score <= 70 and total_score >= 61:
        print((midterm1, midterm2, final))
        print('>>> D')


    elif total_score <= 60 and total_score >= 0:
        print((midterm1, midterm2, final))
        print('>>> F')


    print('A 100-91')
    print('B 90-81')
    print('C 80-71')
    print('D 70-61')
    print('F 60-0')

    check = str(input('Check:  ')).upper()
    if check == 'A':
        print('Əla')

    elif check == 'B':
        print('Çox yaxşı')

    elif check == 'C':
        print('Yaxşı')

    elif check == 'D':
        print('Kafi')

    elif check == 'F':
        print('Pis')

    else:
        print('Yanlış  məlumat')



midterm1 = int(input('Midterm1:  '))
if midterm1 <= 100 and midterm1 >= 0:

    midterm2 = int(input('Midterm2:  '))
    if midterm2 <= 100 and midterm2 >= 0:

        final = int(input('Final:  '))
        if final <= 100 and final >= 0:

            calculate_Score(midterm1, midterm2, final)

        else:
            print('Yanlış  məlumat')
    else:
        print('Yanlış  məlumat')
else:
    print('Yanlış  məlumat')





