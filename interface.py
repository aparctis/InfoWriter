from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# Функция для отправки сообщения
def send_message(event=None):
    message = gpt_input.get()  # Получаем текст из поля ввода
    if message:  # Проверяем, что сообщение не пустое
        add_message("Вы", message)  # Добавляем сообщение отправителя в чат
        gpt_input.delete(0, END)  # Очищаем поле ввода

        generate_other_person_message()

# Функция для добавления сообщения в чат
def add_message(sender, message):
    chat_box.config(state='normal')  # Разрешаем редактирование текстового поля
    chat_box.insert(END, sender + ": " + message + "\n")  # Добавляем сообщение в текстовое поле
    if sender == "Другой человек":
        add_copy_button(message)  # Добавляем кнопку для копирования сообщения
    chat_box.config(state='disabled')  # Запрещаем редактирование текстового поля

# Функция для добавления кнопки копирования сообщения
def add_copy_button(message):
    button = Button(chat_box, text="Копировать", command=lambda: copy_message_to_clipboard(message))
    chat_box.window_create(END, window=button)
    chat_box.insert(END, "\n\n")

# Функция для копирования сообщения в буфер обмена
def copy_message_to_clipboard(message):
    root.clipboard_clear()  # Очищаем буфер обмена
    root.clipboard_append(message)  # Копируем сообщение в буфер обмена
    tkinter.messagebox.showinfo("Сообщение скопировано", "Сообщение успешно скопировано в буфер обмена.")

# Генерация сообщения от другого человека (примерная реализация)
def generate_other_person_message():
    # Здесь можно реализовать логику генерации сообщения от другого человека
    # В данном примере просто добавляется фиксированное сообщение от другого человека
    add_message("Другой человек", "Привет, как дела?")

# Main window
root = Tk()
root.title('Помічник для постів')
root.geometry('850x460')
root.resizable(width=False, height=False)

# TABS
tab_controll = ttk.Notebook(root)
tab_1 = ttk.Frame(tab_controll)
tab_2 = ttk.Frame(tab_controll)

tab_controll.add(tab_1, text='Генерація постів')
tab_controll.add(tab_2, text='GPT 4')

tab_controll.pack(expand=1, fill='both')
# FUNCs


# GPT CHAT
chat_frame = Frame(tab_2)
chat_frame.pack(pady=10)

chat_scroll = Scrollbar(chat_frame)
chat_scroll.pack(side=RIGHT, fill=Y)

chat_box = Text(chat_frame, width=80, height=20, bg='light grey', wrap=WORD, yscrollcommand=chat_scroll.set)
chat_box.pack()

chat_scroll.config(command=chat_box.yview)

gpt_input = Entry(tab_2, bg='white', width=95)
gpt_input.place(x=20, y=400)

gpt_button = Button(tab_2, text='Send', bg='white', width=8, height=1)
gpt_button.place(x=610, y=400)




# POST GENERATION
text_field = Text(tab_1, width=80, height=20)
text_field.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

buttons_frame = Frame(tab_1)
buttons_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

currency_var = BooleanVar(value=True)
advantage_var = BooleanVar(value=True)
church_var = BooleanVar(value=True)
holiday_var = BooleanVar(value=True)
weather_var = BooleanVar(value=True)

currency_toggle = Checkbutton(buttons_frame, text="Курс валют", variable=currency_var)
currency_toggle.pack(anchor="w", padx=10, pady=5)

advantage_toggle = Checkbutton(buttons_frame, text="Авантаж 7", variable=advantage_var)
advantage_toggle.pack(anchor="w", padx=10, pady=5)

church_toggle = Checkbutton(buttons_frame, text="Церковные праздники", variable=church_var)
church_toggle.pack(anchor="w", padx=10, pady=5)

holiday_toggle = Checkbutton(buttons_frame, text="Праздники", variable=holiday_var)
holiday_toggle.pack(anchor="w", padx=10, pady=5)

weather_toggle = Checkbutton(buttons_frame, text="Погода", variable=weather_var)
weather_toggle.pack(anchor="w", padx=10, pady=5)

weather_hours_label = Label(buttons_frame, text="Часы для погоды:")
weather_hours_label.pack(anchor="w", padx=10, pady=5)

weather_hours_scale = Scale(buttons_frame, from_=1, to=12, orient=HORIZONTAL)
weather_hours_scale.pack(anchor="w", padx=10, pady=5)

generate_button = Button(tab_1, text="Сгенерировать пост", width=20, height=3)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
copy_button = Button(tab_1, text="Скопировать текст", width=20, height=3)
copy_button.grid(row=1, column=1, pady=10)

root.mainloop()
