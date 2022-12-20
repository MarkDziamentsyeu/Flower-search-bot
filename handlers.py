from aiogram import types
from dispatcher import dp
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink, hbold
from parser.by_piese import collect_data_by_piese_all
from parser.rouses import collect_data_rouse_1, collect_data_rouse_2
from parser.сhrysanthemum import collect_data_chrysanthemum_1, collect_data_chrysanthemum_2
from parser.alstroemeria import collect_data_alstroemeria_1, collect_data_alstroemeria_2
from parser.eustoma import collect_data_eustoma_1, collect_data_eustoma_2
from parser.other import collect_data_other_1
import json

 
@dp.message_handler(commands='start')
async def start(message: types.Message):
    '''command menu start'''
    
    buttons = ['Букеты', 'Цветы поштучно']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Выберите категорию', reply_markup=kebyord)

@dp.message_handler(Text(equals='🔙 Назад'))
async def back(message: types.Message):
    '''command menu Назад'''

    buttons = ['Букеты', 'Цветы поштучно']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Выберите категорию', reply_markup=kebyord)


@dp.message_handler(Text(equals='Букеты'))
async def get_bouquets(message: types.Message):
    '''command menu Букеты'''

    buttons = ['Букеты с розами', 'Букеты с хризантемами', 'Букеты с \nальстромерией', 'Букеты с эустомой', 'Другие букеты','🔙 Назад']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons) 

    await message.answer('Выберите категорию', reply_markup=kebyord)


@dp.message_handler(Text(equals='Цветы поштучно'))
async def get_flowers(message: types.Message):
    '''command menu Цветы поштучно'''
    buttons = ['Розы', 'Гвоздики', 'Хризантемы', 'Эустомы', 'Ромашки', 'Альстромерия', 'Гиперикум', 'Статица', "Эвкалипт", 'Лилии', '🔙 Назад']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Выберите категорию', reply_markup=kebyord)




@dp.message_handler(Text(equals='Розы'))
async def get_rouse(message: types.Message):
    '''sending the first 10 items of rouses'''

    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('розы')

        count = 0
        flowers = []

        for i in data:

            if "Роза" in i['name'] or "роза" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')
        
        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)



@dp.message_handler(Text(equals='Гвоздики'))
async def get_carnation(message: types.Message):
    '''sending the first 10 items of catnation'''

    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Гвоздики')

        
        count = 0
        flowers = []

        for i in data:

            if "Гвоздика" in i['name'] or "гвоздика" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break
        
        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Хризантемы'))
async def get_chrysanthemum(message: types.Message):
    '''sending the first 10 items of chtysanthemum'''

    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Хризантемы')

        
        count = 0
        flowers = []

        for i in data:

            if "Хризантема" in i['name'] or "хризантема" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break
        
        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Эустомы'))
async def get_eustoma(message: types.Message):
    '''sending the first 10 items of eustoma'''
    
    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Эустомы')

        
        count = 0
        flowers = []

        for i in data:

            if "Эустома" in i['name'] or "эустома" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Ромашки'))
async def get_chamomile(message: types.Message):
    '''sending the first 10 items of chamomile'''
    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Ромашки')

        
        count = 0
        flowers = []

        for i in data:

            if "Ромашка" in i['name'] or "ромашка" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Альстромерия'))
async def get_alstroemeria(message: types.Message):
    '''sending the first 10 items of alstromeria'''
    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Альстромерии')

      
        count = 0
        flowers = []

        for i in data:

            if "Альстромери" in i['name'] or "Альстромери" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)



@dp.message_handler(Text(equals='Гиперикум'))
async def get_hypericum(message: types.Message):
    '''sending the first 10 items of hyptricum'''

    buttons = ['Цветы поштучно', 'Букеты ', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Гиперкум')

        
        count = 0
        flowers = []

        for i in data:

            if "Гиперикум" in i['name'] or "гиперикум" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)

@dp.message_handler(Text(equals='Статица'))
async def get_statice(message: types.Message):
    '''sending the first 10 items of statice'''

    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Статица')

        
        count = 0
        flowers = []

        for i in data:

            if "Статица" in i['name'] or "статица" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)



@dp.message_handler(Text(equals='Эвкалипт'))
async def get_eucalyptus(message: types.Message):
    '''sending the first 10 items of eucalyptus'''
    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Эвкалипт')

        
        count = 0
        flowers = []

        for i in data:

            if "Эвкалипт" in i['name'] or "Эвкалипт" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Лилии'))
async def get_lilies(message: types.Message):
    '''sending the first 10 items of lilies '''

    buttons = ['Цветы поштучно', 'Букеты', 'Ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_by_piese_all()

    with open('data/result_by_piese.json') as file:
        data = json.load(file)
        print('Лилии')

        
        count = 0
        flowers = []

        for i in data:

            if "Лилия" in i['name'] or "лилия" in i['name']:
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                
        count = 0
        for i in flowers:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        if len(flowers) > 10:
            await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё". \nПо данной категории ещё {len(flowers) - 10} позиций.')

        else:
            await message.answer('Это все результаты по данной категории')

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(flowers, file, indent=3, ensure_ascii=False)



@dp.message_handler(Text(equals='Ещё'))
async def get_flower_next(message: types.Message):
    '''sending next 10 items of some flower'''
    with open('data/flowers_by_piese.json') as file:
        cards = json.load(file)
        print(len(cards))
        del cards[0:10]
        print(len(cards))
        print('Нажали кнопку ещё')
        
        count = 0
        for i in cards:
            count += 1
            await message.answer(i)
            if count == 10: 
                break

        balanse = len(cards) - 10
        if balanse > 0:
            balanse = len(cards) - 10

        else:
            balanse = 0

        await message.answer(f'Осталось {balanse} позиций')
        

        with open('data/flowers_by_piese.json', 'w') as file:
            json.dump(cards, file, indent=3, ensure_ascii=False)
            



@dp.message_handler(Text(equals='Букеты с розами'))
async def get_rouse_buq(message: types.Message):
    '''sending the first 10 items of rouses'''
    buttons = ['Букеты', 'Цветы поштучно', 'Ещё букеты с розами']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_rouse_1()

    with open('data/rouse_buq_1.json') as file:
        data = json.load(file)
        print('Букеты с розами')

        
        count = 0
        flowers = []

        for i in data:

            
            card = f'{hlink( " ", i.get("image"))}' \
            f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
            f'{hbold("Цена: "), i.get("price")}\n '

            flowers.append(card)

                        
    count = 0
    for i in flowers:
        count += 1
        await message.answer(i)
        if count == 10: 
            break



    if len(flowers) > 10:
        await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё букеты с розами".\nПоиск может занять несколько секунд')

    else:
        await message.answer('Это все результаты по данной категории')

    with open('data/rouse_buq_1.json', 'w') as file:
        json.dump(flowers, file, indent=3, ensure_ascii=False)

    collect_data_rouse_2()


   

    

@dp.message_handler(Text(equals='Ещё букеты с розами'))
async def get_rouse_next(message: types.Message):
    '''sending next 10 items of rouses'''
    #await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...')
    with open('data/rouse_buq_1.json') as file:
        cards = json.load(file)
        del cards[0:10]
        print('Нажали кнопку ещё букеты роз')

        print(f'Колличество роз_1 после удаления первых 10 = {len(cards)}')
        

    with open('data/rouse_buq_2.json') as file_2:
        data_2 = json.load(file_2)
        

        flowers_2 = []
        for i in data_2:
            
            card_2 = f'{hlink( " ", i.get("image"))}' \
            f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
            f'{hbold("Цена: "), i.get("price")}\n '

            flowers_2.append(card_2)
    

    cards.extend(flowers_2)
        
    count = 0
    for i in cards:
        count += 1
        await message.answer(i)
        if count == 10: 
            break

    balanse = len(cards) - 10
    if balanse > 0:
        balanse = len(cards) - 10

    else:
        balanse = 0

    await message.answer(f'Осталось {balanse} позиций')
        

    with open('data/rouse_buq_1.json', 'w') as file:
        json.dump(cards, file, indent=3, ensure_ascii=False)

    with open('data/rouse_buq_2.json', "w") as file_2:
        flowers_2 = []
        json.dump(flowers_2,file_2, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Букеты с хризантемами'))
async def get_chrysanthemum_buq(message: types.Message):
    '''sending the first 10 items of chrysathemum'''
    
    buttons = ['Букеты', 'Цветы поштучно', 'Ещё букеты с хризантемами']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_chrysanthemum_1()

    with open('data/chrysanthemum_buq_1.json') as file:
        data = json.load(file)
        print('Букеты с хризантемами')

        
        count = 0
        flowers = []

        for i in data:

            
            card = f'{hlink( " ", i.get("image"))}' \
            f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
            f'{hbold("Цена: "), i.get("price")}\n '

            flowers.append(card)

                        
    count = 0
    for i in flowers:
        count += 1
        await message.answer(i)
        if count == 10: 
            break



    if len(flowers) > 10:
        await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё букеты с хризантемами".\nПоиск может занять несколько секунд')

    else:
        await message.answer('Это все результаты по данной категории')

    with open('data/chrysanthemum_buq_1.json', 'w') as file:
        json.dump(flowers, file, indent=3, ensure_ascii=False)

    collect_data_chrysanthemum_2()


@dp.message_handler(Text(equals='Ещё букеты с хризантемами'))
async def get_chrysanthemum_next(message: types.Message):
    '''sending next 10 items of chrysanthemum'''
    with open('data/chrysanthemum_buq_1.json') as file:
        cards = json.load(file)
        del cards[0:10]
        print('Нажали кнопку ещё букеты хризантем')

        print(f'Колличество хризантем_1 после удаления первых 10 = {len(cards)}')
        

    with open('data/chrysanthemum_buq_2.json') as file_2:
        data_2 = json.load(file_2)
        


        flowers_2 = []


        for i in data_2:

            if "Хриза" in i['name'] or "хриза" in i['name']:
                card_2 = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers_2.append(card_2)

            else:
                continue 
            
            
    

    cards.extend(flowers_2)
        
    count = 0
    for i in cards:
        count += 1
        await message.answer(i)
        if count == 10: 
            break

    balanse = len(cards) - 10
    if balanse > 0:
        balanse = len(cards) - 10

    else:
        balanse = 0

    await message.answer(f'Осталось {balanse} позиций')
        

    with open('data/chrysanthemum_buq_1.json', 'w') as file:
        json.dump(cards, file, indent=3, ensure_ascii=False)

    with open('data/chrysanthemum_buq_2.json', "w") as file_2:
        flowers_2 = []
        json.dump(flowers_2,file_2, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Букеты с \nальстромерией'))
async def get_alstroemeria_buq(message: types.Message):
    '''sending the first 10 items of alstromeria'''

    buttons = ['Букеты', 'Цветы поштучно', 'Ещё букеты с альстромерией']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_alstroemeria_1()

    with open('data/alstroemeria_buq_1.json') as file:
        data = json.load(file)
        print('Букеты с хризантемами')

        
        count = 0
        flowers = []

        for i in data:

            
            card = f'{hlink( " ", i.get("image"))}' \
            f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
            f'{hbold("Цена: "), i.get("price")}\n '

            flowers.append(card)

                        
    count = 0
    for i in flowers:
        count += 1
        await message.answer(i)
        if count == 10: 
            break



    if len(flowers) > 10:
        await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё букеты с альстромерией".\nПоиск может занять несколько секунд')

    else:
        await message.answer('Это все результаты по данной категории')

    with open('data/alstroemeria_buq_1.json', 'w') as file:
        json.dump(flowers, file, indent=3, ensure_ascii=False)

    collect_data_alstroemeria_2()


@dp.message_handler(Text(equals='Ещё букеты с альстромерией'))
async def get_alstroemeria_next(message: types.Message):
    '''sending next 10 items of alstromeria'''
   
    with open('data/alstroemeria_buq_1.json') as file:
        cards = json.load(file)
        del cards[0:10]
        print('Нажали кнопку ещё букеты альстромерией')

        print(f'Колличество альстромерией_1 после удаления первых 10 = {len(cards)}')
        

    with open('data/alstroemeria_buq_2.json') as file_2:
        data_2 = json.load(file_2)
        


        flowers_2 = []


        for i in data_2:

            if "Альстро" in i['name'] or "альстро" in i['name']:
                card_2 = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers_2.append(card_2)

            else:
                continue 
            
            
    

    cards.extend(flowers_2)
        
    count = 0
    for i in cards:
        count += 1
        await message.answer(i)
        if count == 10: 
            break

    balanse = len(cards) - 10
    if balanse > 0:
        balanse = len(cards) - 10

    else:
        balanse = 0

    await message.answer(f'Осталось {balanse} позиций')
        

    with open('data/alstroemeria_buq_1.json', 'w') as file:
        json.dump(cards, file, indent=3, ensure_ascii=False)

    with open('data/alstroemeria_buq_2.json', "w") as file_2:
        flowers_2 = []
        json.dump(flowers_2,file_2, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Букеты с эустомой'))
async def get_eustoma_buq(message: types.Message):
    '''sending the first 10 items of eustoma'''
    buttons = ['Букеты', 'Цветы поштучно', 'Ещё букеты с эустомой']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_eustoma_1()

    with open('data/eustoma_buq_1.json') as file:
        data = json.load(file)
        print('Букеты с эустомой')

        
        count = 0
        flowers = []

        for i in data:

            
            card = f'{hlink( " ", i.get("image"))}' \
            f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
            f'{hbold("Цена: "), i.get("price")}\n '

            flowers.append(card)

                        
    count = 0
    for i in flowers:
        count += 1
        await message.answer(i)
        if count == 10: 
            break



    if len(flowers) > 10:
        await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Ещё букеты с эустомой".\nПоиск может занять несколько секунд')

    else:
        await message.answer('Это все результаты по данной категории')

    with open('data/eustoma_buq_1.json', 'w') as file:
        json.dump(flowers, file, indent=3, ensure_ascii=False)

    collect_data_eustoma_2()


@dp.message_handler(Text(equals='Ещё букеты с эустомой'))
async def get_eustoma_next(message: types.Message):
    '''sending next 10 items'''
    
    with open('data/eustoma_buq_1.json') as file:
        cards = json.load(file)
        del cards[0:10]
        print('Нажали кнопку ещё букеты эустомой')

        print(f'Колличество эустом_1 после удаления первых 10 = {len(cards)}')
        

    with open('data/eustoma_buq_2.json') as file_2:
        data_2 = json.load(file_2)
        


        flowers_2 = []


        for i in data_2:

            if "Эустом" in i['name'] or "Эустом" in i['name']:
                card_2 = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers_2.append(card_2)

            else:
                continue 
            
            
    

    cards.extend(flowers_2)
        
    count = 0
    for i in cards:
        count += 1
        await message.answer(i)
        if count == 10: 
            break

    balanse = len(cards) - 10
    if balanse > 0:
        balanse = len(cards) - 10

    else:
        balanse = 0

    await message.answer(f'Осталось {balanse} позиций')
        

    with open('data/eustoma_buq_1.json', 'w') as file:
        json.dump(cards, file, indent=3, ensure_ascii=False)

    with open('data/eustoma_buq_2.json', "w") as file_2:
        flowers_2 = []
        json.dump(flowers_2,file_2, indent=3, ensure_ascii=False)


@dp.message_handler(Text(equals='Другие букеты'))
async def get_other_buq(message: types.Message):
    '''sending the first 10 items'''
    buttons = ['Букеты', 'Цветы поштучно', 'Показать ещё']
    kebyord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kebyord.add(*buttons)

    await message.answer('Ожидайте, идёт запрос...\nЭто займёт несколько секунд...', reply_markup=kebyord)

    collect_data_other_1()

    with open('data/other_buq_1.json') as file:
        data = json.load(file)
        print('Другие букеты')

        
        count = 0
        flowers = []

        for i in data:

            if "Альстро" not in i['name'] and "альстро" not in i['name'] and "Эустом" not in i['name'] and "эустом" not in i['name'] and "Хриза" not in i['name'] and "хриза" not in i['name'] and "Роз" not in i['name'] and "роз" not in i['name'] :
                card = f'{hlink( " ", i.get("image"))}' \
                f'{hlink(i.get("name") + " (ссылка на сайт)" , i.get("link"))}\n' \
                f'{hbold("Цена: "), i.get("price")}\n '

                flowers.append(card)

            else:
                continue 

                        
    count = 0
    for i in flowers:
        count += 1
        await message.answer(i)
        if count == 10: 
            break



    if len(flowers) > 10:
        await message.answer(f'Если хотите посмотреть другие результаты по данной категории нажмите кнопку "Показать ещё".\nПоиск может занять несколько секунд')

    else:
        await message.answer('Это все результаты по данной категории')

    with open('data/other_buq_1.json', 'w') as file:
        json.dump(flowers, file, indent=3, ensure_ascii=False)

    


@dp.message_handler(Text(equals='Показать ещё'))
async def get_other_next(message: types.Message):
    '''sending next 10 items'''

    with open('data/other_buq_1.json') as file:
        cards = json.load(file)

        del cards[0:10]
        print('Нажали кнопку Показать ещё(other)')

        print(f'Колличество сборных букетов  = {len(cards)}')
        
        
    count = 0
    for i in cards:
        count += 1
        await message.answer(i)
        if count == 10: 
            break

    balanse = len(cards) - 10
    if balanse > 0:
        balanse = len(cards) - 10

    else:
        balanse = 0

    await message.answer(f'Осталось {balanse} позиций')
        

    with open('data/other_buq_1.json', 'w') as file:
        json.dump(cards, file, indent=3, ensure_ascii=False)