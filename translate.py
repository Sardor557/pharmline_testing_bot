from aiogram.utils.markdown import hbold, hlink

translate = {
    'ru': {
        'clear_instruction': f'«❌{hbold("Наименование")} - удалить одну позицию»\n\n'
                             f'« - и + Уменьшить или увеличить продукт»\n\n'
                             f'«{hbold("Очистить корзину")}♻ - полная очистка корзины»',
        'show_basket': f'''{hbold('🛒Корзина')}\n\n''',
        'total': 'Общая сумма корзины:',
        'amount_in_basket': 'Кол-во продуктов:',
        'sum': 'сум',
        'about_text': f'''Адрес: {hlink("Ташкент, ул. Узбекистон Овози, 2", "https://yandex.uz/maps/org/88862986165")}\n''',
        'greetings': f'Я БОТ команды {hbold("Tokyobae")}. Я могу принять ваш заказ, объявить о скидках и акциях.',
    },
    'uz': {
        'clear_instruction': f'''«❌{hbold('Mahsulot')} nomi - savatdan o'chirish»\n
« - va + Mahsulot sonini kamaytirish yoki qo’shish»\n
«{hbold("Savatni tozalash")}♻ - savatni butunlay bo'shatish»''',
        'show_basket': f'''{hbold('🛒Savat')}\n\n''',
        'total': 'Savat jami miqdori:',
        'amount_in_basket': 'Mahsulotlar soni:',
        'sum': "so'm",
'about_text': f'''Manzil: {hlink("Ташкент, ул. Узбекистон Овози, 2", "https://yandex.uz/maps/org/88862986165")}\n''',
        'greetings': f'''Men {hbold ("Tokyobae")} jamoasining BOTiman. Men sizning buyurtmangizni qabul qila olaman, chegirmalar va aktsiyalar haqida elon qilaman.'''
    },
    'en': {
        'clear_instruction': f'''«❌{hbold('Name')} - remove one item»\n
« - and + Reduce or enlarge a product»\n
«{hbold("Empty cart")}♻ - complete emptying of the basket»''',
        'show_basket': f'''{hbold('🛒Basket')}\n\n''',
        'total': 'Basket total:',
        'amount_in_basket': 'No. of products:',
        'sum': "som",
'about_text': f'''Manzil: {hlink("Ташкент, ул. Узбекистон Овози, 2", "https://yandex.uz/maps/org/88862986165")}\n''',
        'greetings': f'''Men {hbold ("Tokyobae")} jamoasining BOTiman. Men sizning buyurtmangizni qabul qila olaman, chegirmalar va aktsiyalar haqida elon qilaman.'''
    },
}
