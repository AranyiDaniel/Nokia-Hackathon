from pathlib import Path

def next_magic_num(number: int) -> int:
    numberAsArray = list(map(int, str(number)))


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
    




def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    # print(next_magic_num(999))
    # print(next_magic_num(808))

if __name__ == "__main__":
    main()
