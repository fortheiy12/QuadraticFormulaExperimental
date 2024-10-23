lookupTable = {
  'A': 1, 
  'B': 2, 
  'G': 3,
  'D': 4, 
  'E': 5, 
  '#': 6, 
  'Z': 7, 
  'Y': 8, 
  'H': 9, 
  'I': 10, 
  'K': 20, 
  'L': 30, 
  'M': 40, 
  'N': 50, 
  'X': 60, 
  'O': 70, 
  'P': 80, 
  'Q': 90, 
  'R': 100, 
  'S': 200, 
  'T': 300, 
  'U': 400, 
  'F': 500, 
  'C': 600, 
  '$': 700, 
  'W': 800, 
  '3': 900 
}

def convertNumber(turianNumber):
  total = 0
  for symbol in turianNumber :
    total += lookupTable.get(symbol, 0)
  return total

def processNumber():
  turianNumbers = []

  while True:
        turianNumber = input().strip() 
        if turianNumber == '00000':
            break 
        turianNumbers.append(turianNumber)


  humanNumbers = [convertNumber(num) for num in turianNumbers]
  return humanNumbers

output = processNumber()

for num in output:
  print(num)