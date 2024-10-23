a, b, c = input("").split(" ")
area = int(a)*int(b)
intc = int(c)
perimeter = int(a)*2 + int(b)*2
if area <= intc:
  print(str(perimeter) +" "+ str(area) +" "+ "ENOUGH SPACE")
else:
  print(str(perimeter) +" "+ str(area) +" "+ "NEED MORE SPACE")
