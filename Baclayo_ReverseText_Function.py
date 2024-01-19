def reverse_text():
    while True:
        user_input = input("Enter a text (type 'exit' to end): ")

        if user_input.lower() == 'exit':
            break

        if user_input.isdigit():
            print("Error Reported! Enter text only.")
        else:
            reversed_text = user_input[::-1]
            print("Reversed Text:", reversed_text)

reverse_text()