column_c = int(input())
row_c = int(input())

if 1 <= column_c <= 8 and 1 <= row_c <= 8:
    if 2 <= column_c <= 7 and 2 <= row_c <= 7:
        print(8)
    else:
         if column_c == 1 or column_c == 8:
             if row_c == 1 or row_c == 8:
                print(3)
             elif 2 <= row_c <= 7:
                print(5)
         elif 2 <= column_c <= 7:
             if row_c == 1 or row_c == 8:
                 print(5)
else:
    print("Wrong column or row number")