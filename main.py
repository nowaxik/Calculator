import tkinter as tk


def on_button_click(event):
    """Funkcja wywoływana po kliknięciu przycisku kalkulatora."""
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            current_text = entry.get()
            if is_valid_input(current_text):
                result = eval(current_text)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Błąd")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


def is_valid_input(text):
    """Sprawdza, czy wprowadzony tekst zawiera dozwolone znaki."""
    allowed_characters = "0123456789./*-+"
    return all(char in allowed_characters for char in text)


# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Kalkulator")

# Tworzenie pola tekstowego dla wprowadzania i wyświetlania wyników
entry = tk.Entry(root, font=("Helvetica", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definicja przycisków numerycznych i operatorów
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Tworzenie przycisków i ich rozmieszczanie w siatce
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 18))
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    button.bind("<Button-1>", lambda event, t=text: on_button_click(event))

# Ustawienie równego rozmieszczenia przycisków w siatce
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Rozpoczęcie głównej pętli programu
root.mainloop()
