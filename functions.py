def CountFrequency(my_list):

   # Creating an empty dictionary
   count = {}
   for i in my_list:
    count[i] = count.get(i, 0) + 1
   return count

# Driver function
if __name__ == "__main__":
    my_list =["persi", "lalo", "lalo", "lalo", "lulu", "lulu", "lalo", "persi", "persi"]
    dicc_final = CountFrequency(my_list)
    sorted_dicc = {k: v for k, v in sorted(dicc_final.items(), key=lambda item: item[1])}
    print(list(sorted_dicc)[-1])
