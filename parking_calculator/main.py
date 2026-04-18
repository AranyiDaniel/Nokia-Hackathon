import math
from pathlib import Path
from datetime import datetime

def parking_fee_calculator(input):
    try:

        car = {
            "id" : input[0],
            "arrivalTime" : datetime.strptime(input[1] + input[2], "%Y-%m-%d%H:%M:%S"),
            "departureTime" : datetime.strptime(input[3] + input[4], "%Y-%m-%d%H:%M:%S")
        }
        durationOfStay = (car["departureTime"] - car["arrivalTime"]).total_seconds() / 60
        if durationOfStay < 0: return car["id"] + ": HIBA - Visszafelé parkolás!"

        days = int(durationOfStay // 1440)
        minutesLeft = durationOfStay % 1440
        fee = days * 10000

        if minutesLeft > 30:
            paidMinutes = minutesLeft - 30
            startedHours = math.ceil(paidMinutes / 60)
            
            if startedHours <= 3:
                fee += startedHours * 300
            else:
                fee += (3 * 300) + (startedHours - 3) * 500
                
        return f"{car['id']}\t\t{int(fee)}"
    
    except IndexError:
        return "HIBA: Hiányos adatsor (nincs elég oszlop)!"
    except ValueError:
        return "HIBA: Hibás dátum formátum vagy nem szám adat!"
    except Exception as e:
        return f"Váratlan hiba: {e}"

def main():
    try:
        data = Path("input.txt").read_text(encoding="utf-8")
        lines = data.strip().splitlines()
        
        with Path("output.txt").open("w", encoding="utf-8") as out_file:
            out_file.write("RENDSZAM\tDIJ\n")
            print("RENDSZAM\tDIJ")
            for line in lines[2:]:
                a = line.replace("\t", " ")
                b = a.split()
                if not b: continue

                eredmeny = parking_fee_calculator(b)
                
                szoveges_eredmeny = str(eredmeny)
                print(szoveges_eredmeny)
                out_file.write(szoveges_eredmeny + "\n")

    except Exception as e:
        print(f"Kritikus hiba a program futása során: {e}")

    
if __name__ == "__main__":
    main()
