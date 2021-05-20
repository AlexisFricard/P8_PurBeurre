""" TO CLEAN A GIVEN SENTENCE """


def remove_special_char(msg, params):
    msg = msg.lower()
    for i in msg:
        if i in "[\"/\\:?!-}><(){,]&":
            if params == "all":
                msg = msg.replace(i, "")
            # To keep separate {it's -> it s etc..}
            elif params == "add_space":
                if i in ",-\"":
                    msg = msg.replace(i, " ")
                else:
                    msg = msg.replace(i, "")
    return msg
