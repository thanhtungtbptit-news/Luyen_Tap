text=input("Nhập vào một chuỗi kí tự : ")
if text.isalnum():
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự chữ và số")
elif text.istitle():
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự viết hoa chữ cái đầu mỗi từ")
elif text.isalpha():
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự chữ")
elif text.isnumeric():
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự số")
elif text.islower():
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự viết thường")
elif text.isupper():
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự viết hoa")
else:
    print("Chuỗi kí tự vừa nhập là chuỗi kí tự đặc biệt")