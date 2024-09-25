import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox

# QR kodu oluşturma ve kaydetme fonksiyonu
def generate_qr():
    link = entry.get()
    if not link:
        messagebox.showerror("Hata", "Lütfen bir link girin!")
        return
    
    try:
        # QR kodunu oluştur
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        # QR kodunu bir image olarak oluştur
        img = qr.make_image(fill="black", back_color="white")
        img.save("qrcode.png")
        
        # QR kodunu tkinter üzerinde göster
        img = Image.open("qrcode.png")
        img = ImageTk.PhotoImage(img)
        qr_label.configure(image=img)
        qr_label.image = img

        messagebox.showinfo("Başarılı", "QR kodu başarıyla oluşturuldu ve 'qrcode.png' olarak kaydedildi!")
    
    except Exception as e:
        messagebox.showerror("Hata", f"QR kodu oluşturulurken bir hata oluştu: {str(e)}")

# CustomTkinter tema ayarları
ctk.set_appearance_mode("dark")  # 'dark' veya 'light'
ctk.set_default_color_theme("blue")  # 'blue', 'green', 'dark-blue'

# Tkinter pencere ayarları
window = ctk.CTk()
window.title("QR Kod Oluşturucu")
window.geometry("400x500")

# Başlık
label = ctk.CTkLabel(window, text="QR Kod Oluşturucu", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=20)

# Link giriş kutusu
entry = ctk.CTkEntry(window, width=300, placeholder_text="Linkinizi girin")
entry.pack(pady=10)

# QR kodu oluştur butonu
button = ctk.CTkButton(window, text="QR Kod Oluştur", command=generate_qr)
button.pack(pady=20)

# QR kodu gösterilecek label
qr_label = ctk.CTkLabel(window, text="")
qr_label.pack(pady=20)

# Pencereyi çalıştır
window.mainloop()
