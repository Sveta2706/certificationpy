notes = {}


def add_note():
    title = input("Введите название заметки: ")
    content = input("Введите содержимое заметки: ")
    notes[title] = content
    print(f"Заметка {title} успешно добавлена.")


def edit_note():
    title = input("Введите название заметки, которую хотите отредактировать: ")
    content = notes.get(title)
    if content:
        new_content = input("Введите новое содержимое заметки: ")
        notes[title] = new_content
        print(f"Заметка {title} успешно изменена.")
    else:
        print(f"Заметка {title} не найдена.")
        
        def delete_note():
    title = input("Введите название заметки, которую хотите удалить: ")
    if title in notes:
        del notes[title]
        print(f"Заметка {title} успешно удалена.")
    else:
        print(f"Заметка {title} не найдена.")


def print_notes():
    if notes:
        print("Список заметок:")
        for title, content in notes.items():
            print(f"{title}: {content}")
    else:
        print("Список заметок пуст.")


