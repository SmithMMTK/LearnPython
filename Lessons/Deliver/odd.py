def is_odd(number):
    # Check if number is odd by check if the reminder by %
    return number % 2 != 0

def Hacktober(array_integers):
    count_odd_sums = 0
    current_sum = 0
    for i in range(len(array_integers)):
        for j in range(len(array_integers)):
            # Check if i != j skip otherwise if i == j, add the value to current_sum
            # Check if current_sum is odd, if odd, increment count_odd_sums
            if i != j:
              #  print("i:", array_integers[i] , "+ j:", array_integers[j], " = ", array_integers[i] + array_integers[j])
                current_sum = array_integers[i] + array_integers[j]
                if is_odd(current_sum):
                    count_odd_sums += 1

    return count_odd_sums

array_integers = [5, 4, 8, 26, 4, 5]
count = Hacktober(array_integers)
print("Count of odd sums:", count)
