def flames_game(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common characters
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    # Calculate the total number of remaining letters
    remaining_count = len(name1) + len(name2)

    # FLAMES acronym
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

    # Determine the relationship
    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1

        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    # Final result
    return flames[0]


# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get the FLAMES result
result = flames_game(name1, name2)

# Display the result
print(f"The relationship between {name1} and {name2} is: {result}")