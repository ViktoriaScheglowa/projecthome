from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(nums: str) -> str:
    if "Счет" in nums:
        return f"{nums[:-20]}**{nums[-4::]}"

    else:
        return f"{nums[:-12]} {nums[-12:-10]}** **** {nums[-4::]}"


def get_date(date: str) -> str:
    if date == '':
        return ''
    else:
        return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
