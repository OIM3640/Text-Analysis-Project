##This was my first attempt at remove_preamble. It does not work. It is only here to supplement my writing.


def remove_preamble(text):
    count = 0
    checker = 0
    key = build_key()
    key_tooth = key[0]

    for letter in text:
        count = count + 1
        if letter == key_tooth:
            if checker < len(key) - 1:
                # print(key_tooth)
                key_tooth = key[checker + 1]
            checker = checker + 1
        if checker == len(key) - 1:
            # print(key_tooth)
            print("checker")
            break
    return text[count:]

    print("done!")


def build_key():
    print(
        "Type the unique heading of the section immediately following the preamble EXACTLY as it appears. Everything before this heading will be removed."
    )
    chosen = input("Type here: ")
    key = []
    for i in range(len(chosen)):
        key.append(chosen[i])
    return key
