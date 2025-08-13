import os
import qrcode
from qrcode.constants import ERROR_CORRECT_M



def create_siple_qrcode():
    link = input("Enter link for qrcode: ")
    file_name = input("Enter file name: ")

    if not file_name.endswith(('.png', '.jpg', 'jpeg')):
        file_name += '.png'

    try:
        img = qrcode.make(link)
        img.save(file_name)

        file_location = os.path.abspath(file_name)
        print(f"file saved to {file_location}")

    except Exception as e:
        print(e)

def create_costume_qrcode():
    print("---- Costume Qrcode ----")
    link = input("Enter link for qrcode: ")
    fill_color = input("Enter Qrcode color: ")
    back_color = input("Enter Qrcode background color: ")
    file_name = input("Enter file name: ")

    if not file_name.endswith(('.png', '.jpg', 'jpeg')):
        file_name += '.png'

    try:
        qr = qrcode.QRCode(
            error_correction = ERROR_CORRECT_M,
            box_size = 10,
            border = 4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(file_name)

        file_location = os.path.abspath(file_name)
        print(f"file saved to {file_location}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu = input('''
1. Simple Qrcode
2. Costume Qrcode
3. Exit
pick one of the options: ''')

        if menu == '1':
            create_siple_qrcode()
        elif menu == '2':
            create_costume_qrcode()
        elif menu == '3':
            print("Exit . . .")
            break
        else:
            print("Invalid input")

        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')