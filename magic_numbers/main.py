from pathlib import Path

def next_magic_num(number: int) -> int:
    numberAsArray = list(map(int, str(number)))


    #elso eset
    numberIsAllNines = False
    for i in range(len(numberAsArray)):
        if numberAsArray[i] != 9:
            break
        else:
            numberIsAllNines = True
    
    if numberIsAllNines == True:
        return number + 2

            
def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    print(next_magic_num(9999))
    


if __name__ == "__main__":
    main()
