from pathlib import Path

def next_magic_num(number: int) -> int:

    #hatvany
    for i in range(len(number)):
        if number[i] =="^":
            base, exp = map(int, number.split("^"))
            number = str(base ** exp)

    numberAsArray = list(map(int, str(number)))
    number = int(number)

    #elso eset
    for i in range(len(numberAsArray)):
        if numberAsArray[i] != 9:
            break
        else:
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
    if leftPart[-1] != 9:
        leftPart[-1] += 1
    else:
        leftPart[-1] = 0
        leftPart[-2] += 1

    if lenght % 2 == 0:
        FlippedNumberArray = leftPart + leftPart[::-1]
    else:
        FlippedNumberArray = leftPart + leftPart[:-1][::-1]

    FlippedNumber = int("".join(map(str, FlippedNumberArray)))
    return FlippedNumber



def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    lines = data.strip().splitlines()
    for line in lines:
        print(next_magic_num(line))


if __name__ == "__main__":
    main()
