num = int(input("Enter the number: "))
#  Decide the row count.
row = num
# i is for rows
# stop: row+1 (range never include stop number in result)
for i in range(1, row+1):
        # Run inner loop i+1 times
        # j is for columns
        for j in range(1, i+1):
                # end is empty because we don't want space after each number
                print(j, end='')
                # # empty line after each row
        print("")