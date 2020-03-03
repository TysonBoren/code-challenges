def get_grade(s1, s2, s3):
    if (s1 + s2 + s3) / 3 <= 100 and (s1 + s2 + s3) / 3 >= 90:
      print("A")
    elif (s1 + s2 + s3) / 3 <= 90 and (s1 + s2 + s3) / 3 >= 80:
      print("B")
    elif (s1 + s2 + s3) / 3 <= 80 and (s1 + s2 + s3) / 3 >= 70:
      print("C")
    elif (s1 + s2 + s3) / 3 <= 70 and (s1 + s2 + s3) / 3 >= 60:
      print("D")
    else:
      print('F')
    print((s1 + s2 + s3) / 3)
get_grade(70, 70, 100)
get_grade(100, 85, 96)
get_grade(92, 93, 94)
get_grade(66, 68, 68)
get_grade(58, 56, 58)