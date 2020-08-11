import validators
import src.retrieve_html as htm
import src.pre_processing as pp

if __name__ == "__main__":
    isValid = True
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
            protocol = "https://www."
            if protocol not in init_message:
                init_message = protocol + init_message

                if validators.url(init_message):
                    html_raw = htm.get_html(init_message)
                    html_extracted = htm.extract_relevant_html(html_raw)
                    tokens, tags = pp.pre_processing(html_extracted)
                else:
                    print("Invalid url submitted: '" +
                          init_message + "'. Skipping....")
