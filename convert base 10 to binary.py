while True:
    number_to_convert = int(input("Enter any number: "))
    binary = []

    def convert_from_base_ten_to_binary(number):

        newnumber =  number // 2
        print(newnumber)
        binary.append(number%2)
        if 0 < newnumber < 2:
            print(str(binary))
            return
        else:
            convert_from_base_ten_to_binary(newnumber)

    convert_from_base_ten_to_binary(number_to_convert)