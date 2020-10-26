def main():
    input_string = input()
    splited_array = input_string.split(' ')
    print(splited_array)
    res=[]
    new_string = ""
    strt_index = 0 
    last_index = len(splited_array)
    for i in range(len(splited_array)-1):
        first_word ="".join(splited_array[strt_index:i +1])
        second_word = "".join(splited_array[i+1:last_index])
        res.append(first_word+ " " + second_word)

    print()


if __name__ == "__main__":
    main()