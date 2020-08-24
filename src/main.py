import src.pre_processing as pp
import src.retrieve_html as htm
import validators

from src.keyword_selection import keyword_selection

if __name__ == "__main__":
    IS_VALID = True
    protocols = ["https://", "http://"]

    while IS_VALID:

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
            IS_VALID = False
        else:
            if not any(init_message.startswith(s) for s in protocols):
                init_message = protocols[0] + init_message

                if validators.url(init_message):
                    html_raw = htm.get_html(init_message)
                    html_extracted = htm.extract_relevant_html(html_raw)
                    pp_tokens, pp_tags = pp.tokenization(html_extracted)
                    keyword_selection(pp_tokens, pp_tags)
                else:
                    print("Invalid url submitted: '" +
                          init_message + "'. Skipping....")
