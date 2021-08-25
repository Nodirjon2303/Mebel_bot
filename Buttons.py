from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from Rooms import *

con_keyboard = KeyboardButton(text='Send Contact', request_contact=True)
phone_button = ReplyKeyboardMarkup(
    [
        [con_keyboard]
    ], resize_keyboard=True
)

main_buttons = ReplyKeyboardMarkup(
    [
        ['Mening xonalarim'],
        ['Mening buyurtmalarim'],
        ['Xona qo\'shish']
    ],
    resize_keyboard=True
)


def Room_button(xona_id):
    ROOM_Buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton('Xonani tahrirlash', callback_data=f'editroom_{xona_id}')],
        [InlineKeyboardButton('Xonani mebellash', callback_data=f'addfurniture_{xona_id}')],
        [InlineKeyboardButton('xonani o\'chirish', callback_data=f'deleteroom_{xona_id}')],
        [InlineKeyboardButton('Ortga', callback_data='back_1')]
    ])

    return ROOM_Buttons


def button_room(user_id):
    rooms = get_rooms()
    my_room = []
    buttons = []
    temp_b = []
    for i in rooms:
        if i[1] == user_id:
            my_room.append(i)
    print(my_room)
    if my_room:
        for i in my_room:
            pass
            print(i)
            temp_b.append(InlineKeyboardButton(i[2], callback_data=i[0]))
            buttons.append(temp_b)
            temp_b = []
        return InlineKeyboardMarkup(buttons)


def edit_room_button(room_id):
    room = get_rooms_by_id(room_id)
    buttons = []
    temp = []
    temp.append(InlineKeyboardButton(f"Rangi: {room[3]}", callback_data=f'editcolor_{room[0]}'))
    buttons.append(temp)
    temp = []
    temp.append(InlineKeyboardButton(f"Eni: {room[4]}", callback_data=f'editeni_{room[0]}'))
    buttons.append(temp)
    temp = []
    temp.append(InlineKeyboardButton(f"Bo'yi: {room[5]}", callback_data=f'editbuyi_{room[0]}'))
    buttons.append(temp)
    temp = []
    temp.append(InlineKeyboardButton(f"Balanlagi: {room[6]}", callback_data=f'edith_{room[0]}'))
    buttons.append(temp)
    temp = []
    temp.append(InlineKeyboardButton(f"Bosh sahifa", callback_data=f'main_{room[0]}'))
    buttons.append(temp)
    return InlineKeyboardMarkup(buttons)

def Button_furnitures():
    furniture_category = get_furniture()
    print(furniture_category)
    temp_b =[]
    buttons = []
    for i in furniture_category:
        temp_b.append(InlineKeyboardButton(i[1], callback_data=i[0]))
        buttons.append(temp_b)
        temp_b = []
    return InlineKeyboardMarkup(buttons)
def Button_furniture_by_id(cat_id):
    furniture_category = get_fur_by_id(cat_id)
    print(furniture_category)
    temp_b = []
    buttons = []
    for i in furniture_category:
        temp_b.append(InlineKeyboardButton(i[1], callback_data=i[0]))
        buttons.append(temp_b)
        temp_b = []
    return InlineKeyboardMarkup(buttons)

