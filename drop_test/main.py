from pathlib import Path


def eggDrop(numberOfPrototypes, numberOfFloors):
    
    matrix = [[0 for i in range(numberOfPrototypes + 1)] for i in range(numberOfFloors + 1)]
    numberOfDrops = 0
    
    while matrix[numberOfDrops][numberOfPrototypes] < numberOfFloors:
        numberOfDrops += 1
        for i in range(1, numberOfPrototypes + 1):
            matrix[numberOfDrops][i] = 1 + matrix[numberOfDrops - 1][i - 1] + matrix[numberOfDrops - 1][i]
    return numberOfDrops


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    lines = data.strip().splitlines()
    
    for line in lines:
        cleanLine = line.replace(',', ' ')
        parts = cleanLine.split()
        n = int(parts[0])
        h = int(parts[1])
        
        result = eggDrop(n, h)
        print(result)



if __name__ == "__main__":
    main()
