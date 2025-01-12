import tkinter as tk
from tkinter import messagebox

# Tuşlara basıldığında sayıların veya işlemin giriş kutusunda görünmesi
# Bu fonksiyon, giriş kutusuna tıklanan tuşun değerini ekler
def button_click(item):
    entry_text.set(entry_text.get() + str(item))

# Ekranı temizlemek için kullanılan fonksiyon
# Giriş kutusundaki tüm metni siler
def clear():
    entry_text.set("")

# Sonucu hesaplamak için kullanılan fonksiyon
# eval() fonksiyonu ile matematiksel ifadeyi değerlendirir
# Hata durumunda kullanıcıya bir hata mesajı gösterir
def calculate():
    try:
        result = str(eval(entry_text.get()))  # Matematiksel ifadeyi değerlendir
        entry_text.set(result)  # Sonucu giriş kutusuna yerleştir
    except Exception as e:
        messagebox.showerror("Hata", "Geçersiz İşlem!")  # Hata mesajı göster
        entry_text.set("")  # Giriş kutusunu temizle

# Ana pencere oluşturma
# Tkinter uygulamasının ana penceresini başlatır
root = tk.Tk()
root.title("Hesap Makinesi")  # Pencere başlığını ayarlar
root.geometry("400x500")  # Pencere boyutlarını ayarlar
root.configure(bg="#2b2b2b")  # Arka plan rengini koyu bir tema yapar

# Giriş kutusu metni için bir StringVar değişkeni oluşturulur
entry_text = tk.StringVar()

# Giriş kutusunu oluşturma
# Kullanıcı girişlerini göstermek için bir Entry widget eklenir
tk.Entry(root, textvariable=entry_text, font=("Arial", 24), justify='right', bg="#1e1e1e", fg="white", bd=0, insertbackground="white").grid(row=0, column=0, columnspan=4, pady=15, padx=15)

# Tuş takımı tanımı
# Her bir tuşun metni, satırı ve sütunu belirlenir
tuşlar = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),  # İlk satır tuşları
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),  # İkinci satır tuşları
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),  # Üçüncü satır tuşları
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)   # Dördüncü satır tuşları
]

# Tuşları oluşturma ve pencereye yerleştirme
for (text, row, col) in tuşlar:
    btn_color = "#333333" if text not in ["C", "="] else ("#e74c3c" if text == "C" else "#27ae60")
    text_color = "white"
    tk.Button(
        root,
        text=text,
        font=("Arial", 18),
        command=calculate if text == "=" else clear if text == "C" else lambda t=text: button_click(t),
        bg=btn_color,
        fg=text_color,
        activebackground="#444444",
        activeforeground="white",
        bd=0
    ).grid(row=row, column=col, ipadx=20, ipady=20, padx=5, pady=5)

# Ana döngüyü çalıştır
# Uygulamanın kullanıcı ile etkileşime girmesini sağlar
root.mainloop()
