from src.user_input import get_photo_from_user, is_valid_choice
from src.menu import print_menu, apply_user_choice

if __name__ == '__main__':
    image_path = get_photo_from_user()
    if image_path is None:
        exit()
    else:
        print_menu()
        user_choice = input('')
        if is_valid_choice(user_choice):
            user_choice = int(user_choice)
            result = apply_user_choice(user_choice, image_path)
            if result:
                print("A new image was created next to the image you chose to edit.")
            else:
                print("The request could not be executed")
        else:
            print("You have selected an invalid character.")
