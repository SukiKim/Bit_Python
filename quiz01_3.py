def quiz01_3():
    student = [{
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
        {
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
        }
    ]

    #Kim 학생의 국어, 영어, 수학 점수 구해서 딕셔너리에 넣기
    sum = student[0]['kor'] + student[0]['eng'] + student[0]['math']
    avg = sum / 3
    student[0]["sum"] = sum
    student[0]["avg"] = avg

    #Lee 학생의 국어, 영어, 수학 점수 구해서 딕셔너리에 넣기
    sum = student[1]['kor'] + student[1]['eng'] + student[1]['math']
    avg = sum / 3
    student[1]["sum"] = sum
    student[1]["avg"] = avg

    print(student)



quiz01_3()