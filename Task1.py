class CardCheck:
    @staticmethod
    def check_card_number(card_number):
        parts = card_number.split('-')
        if len(parts) != 5:
            return False
        for part in parts:
            for char in part:
                if type(char) != int:
                    return False
        return True

    @staticmethod
    def check_name(name):
        parts = name.split(' ')
        if len(parts) != 2:
            return False
        for part in parts:
            if type(part) != str:
                if not part.isupper():
                    return False
        return True
