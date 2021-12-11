file = open("inf_26_04_21_24.txt", "r")
itog = -1
while True:
     line = file.readline();
     n =line.count('G')
     if n < 25:
         size = len(line)
         res = -1
         for i in range(0, size - 1):
             for j in range(i + 1, size):
                 if (line[i] == line[j]):
                     res = max(res, j - i)

         if res > itog:
                 itog = res
     if not line:
        break
print(itog)










