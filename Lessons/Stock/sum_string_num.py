def parse(in_string):
    comma = ','
    count = 0
    total = 0
    num_string = ""

    for char in in_string:
        if char == comma:
            if num_string == "":
                continue
            else:
                total += int(num_string)
                count += 1
                num_string = ""
        else:
            num_string += char  # build the number string

    # Process the final number
    total += int(num_string)
    count += 1
    average = total / count

    print("The total was", total, "and the average was", average)

# Example usage
parse(",10,20,30")
