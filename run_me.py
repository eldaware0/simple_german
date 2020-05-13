"""This is main package of the project"""

import mypkg.general as gl
import mypkg.functions as my_fn

def main():
    """Main method of the program module
    """
    # Create particular lesson
    lessn = gl.Lesson("konjunktor", "./myrsc/")

    # Get lesson details
    (lessn_cont, (frage, antwort, beishpiel)) = lessn.start()

    cont_lesson = True

    # Lopping through DataFrame content
    for row in lessn_cont:

        # Atempts are reset for each word/phrase
        attem_remain = lessn.get_attempts()
        
        while True:

            # Get reply from a user
            reply = input("Enter deutsch form of word '{}':".format(row[frage]))

            # Handle user interupting a lesson
            if reply == 'stop()':
                cont_lesson = False
                break

            # If reply is incorrect, check attempts left:
            elif reply != row[antwort]:

                attem_remain -= 1

                # If no attempts, print reply and ask next question:
                if not attem_remain:
                    my_fn.print_wcolor("red", "Reply is: " + row[antwort])
                    if not row[beishpiel] == '':
                        my_fn.print_wcolor("green", "Example: " + row[beishpiel])
                    break
                
                # If attempts available, populate repeat list & repeat question:
                else:
                    lessn.add_2_repeat_list((row[antwort]))
                    my_fn.print_wcolor("red", "Try again!")
                    continue

            # Print usage example in case of correct reply
            else:
                if row[beishpiel] == '':
                    my_fn.print_wcolor("green", row[antwort])
                else:
                    my_fn.print_wcolor("green", row[beishpiel])
                break
        
        # Break loop when user interrupts lesson:
        if not cont_lesson:
            break

    if cont_lesson:
        lessn.end()
    else:
        lessn.end(1)

    # Print lesson statistics
    lessn.stats()

if __name__ == '__main__':
    main()
