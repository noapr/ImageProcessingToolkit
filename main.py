from src.user_input import get_photo_from_user
from src.menu import print_menu
if __name__ == '__main__':
    image_path = get_photo_from_user()
    if image_path is None:
        print("Bye bye")
    else:
        print_menu()
        user_choice = input('')
