def Library(Books_find):

    try:
        print(f" Searching for Book {Books_find} ..... ")
        if Books_find=="unknown":
            raise ValueError ("We donot have this Book")
    except ValueError as e:
        print("Error : " , e)
    else:
        print(f"Yes Your Books is found . Book is of {Books_find}")
    finally:
        print("Next Customer Please")

Library("Programming")
Library("unknown")