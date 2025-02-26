import logging


logging.basicConfig(
    filename='masks.log',
    filemode='w',
    format='%(asctime)s %(name)s %(Levelname)s:%(message)s')


logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logging.info("Start")
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logging.info("Return of mask card number")
    else:
        logging.error("Return  an empty string")
        return ''
    logging.info("Stop")


def get_mask_account(acc_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logging.info("Start")
    if acc_number.isdigit() and len(acc_number) == 20:
        logging.info("Return of mask account number")
        return f"**{acc_number[-4::]}"
    else:
        logging.error("Return  an empty string")
        return ''
    logging.info("Stop")
