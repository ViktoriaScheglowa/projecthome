def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return ''


def get_mask_account(acc_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"**{acc_number[-4::]}"
    else:
        return ''
