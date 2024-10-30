import os
os.system('cls')

def tinh_tien_dien(kWh):
    if kWh <= 0:
        return 0

    tien_dien = 0

    # Bậc 1: 0 - 50 kWh
    if kWh <= 50:
        tien_dien = kWh * 1806
    else:
        tien_dien += 50 * 1806
        kWh -= 50

        # Bậc 2: 51 - 100 kWh
        if kWh <= 50:
            tien_dien += kWh * 1866
        else:
            tien_dien += 50 * 1866
            kWh -= 50

            # Bậc 3: 101 - 200 kWh
            if kWh <= 100:
                tien_dien += kWh * 2167
            else:
                tien_dien += 100 * 2167
                kWh -= 100

                # Bậc 4: 201 - 300 kWh
                if kWh <= 100:
                    tien_dien += kWh * 2729
                else:
                    tien_dien += 100 * 2729
                    kWh -= 100

                    # Bậc 5: 301 - 400 kWh
                    if kWh <= 100:
                        tien_dien += kWh * 3050
                    else:
                        tien_dien += 100 * 3050
                        kWh -= 100

                        # Bậc 6: 401 kWh trở lên
                        tien_dien += kWh * 3151

    return tien_dien

while True:
    os.system('cls') 

    kWh = float(input("Nhập số kWh đã tiêu thụ: "))
    tien_dien = tinh_tien_dien(kWh)

    tien_dien_sau_thue = round(tien_dien * 1.08)

    tien_dien_sau_thue_str = f"{tien_dien_sau_thue:,}".replace(",", ".")

    print(f"Số tiền điện phải trả (bao gồm thuế GTGT) là: {tien_dien_sau_thue_str}đ")

    tiep_tuc = input("Bạn có muốn tiếp tục không? (y/n): ").lower()

    if tiep_tuc != 'y':
        print("Kết thúc chương trình.")
        break
