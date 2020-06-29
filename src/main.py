import requests
from bs4 import BeautifulSoup
import validators
import retrieve_html as htm


if __name__ == "__main__":
    isValid = True
    isInvalid = False
    while isValid:

        # Attempt to read input and throw an exception if invalid
        try:
            init_message = input("Enter space separated URLs or exit: ")
            init_message = init_message.strip()

            if not init_message:
                raise ValueError("Empty string entered! Try again!")
        except ValueError as exc:
            print(exc)
            continue
        except KeyboardInterrupt:
            print("\nProgram stopped. Goodbye!")
            break

        # Checks where the user has entered the command to exit
        if init_message == "exit":
            print("Goodbye!")
            isValid = False
        else:
            if validators.url(init_message):
                print(htm.get_html(init_message, 0))
            else:
                print("Invalid url submitted: '" +
                      init_message + "'. Skipping....")
