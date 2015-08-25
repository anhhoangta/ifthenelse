while True:

    soDuong = int(input("Nhap so duong: "))
    soDiem = int(input("Nhap so diem: "))

    isPrinted = False

    for i in range(soDiem):
        for j in range(soDuong*(soDiem-1)+1):
            for k in range(1, soDuong+1):
                if k%2 != 0:
                    if (j+i)==(soDiem-1)*k or (j-i)==(soDiem-1)*k:
                        print("*", end="")
                        isPrinted = True
                        break
            if (isPrinted == False):
                print(" ", end="")
            else: isPrinted = False
        print()

