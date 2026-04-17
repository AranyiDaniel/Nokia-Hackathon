from pathlib import Path

def next_magic_num(number: int) -> int:
    #hatvany
    if "^" in number:
        base, exp = map(int, number.split("^"))
        number = str(base ** exp)
    number = int(number)
    numberAsArray = list(map(int, str(number)))

    # #elso eset
    if all(c == '9' for c in str(number)):
        return number + 2

    #masodik eset
    lenght = len(numberAsArray)
    middleIndex = (lenght + 1) // 2
    leftPart = numberAsArray[:middleIndex]
    if lenght % 2 == 0:
        FlippedNumberArray = leftPart + leftPart[::-1]
    else:
        FlippedNumberArray = leftPart + leftPart[:-1][::-1]

    FlippedNumber = int("".join(map(str, FlippedNumberArray)))
    if FlippedNumber > number:
        return FlippedNumber
    

    #harmadik eset
    leftPartAdded = int("".join(map(str, leftPart)))
    leftPartAdded += 1

    if lenght % 2 == 0:
        FlippedNumberArray = str(leftPartAdded) + str(leftPartAdded)[::-1]
    else:
        FlippedNumberArray = str(leftPartAdded) + str(leftPartAdded)[:-1][::-1]

    FlippedNumber = int("".join(map(str, FlippedNumberArray)))
    return FlippedNumber



def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    lines = data.strip().splitlines()
    for line in lines:
        print(next_magic_num(line))


if __name__ == "__main__":
    main()
