import tkinter as tk
import qrcode
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser

def generate_qr_code():
    # Kullanıcının girdiği metni al
    text = entry.get()
    
    # Eğer metin boşsa, uyarı ver
    if not text:
        warning_label.config(text="Lütfen bir şey yazınız.", fg="red", bg="white")
        return
    
    # Eğer metin doluysa uyarıyı temizle
    warning_label.config(text="")
    
    # QR kodu oluştur
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    # QR kodunu bir PIL resmine dönüştür
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # PIL resmini tkinter ile göster
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo
    
    # QR kodunu geçici bir dosyaya kaydet
    global temp_filename
    temp_filename = "temp_qr.png"
    qr_image.save(temp_filename)

def open_link(event):
    webbrowser.open("https://linktr.ee/leaddy")

def download_qr_code():
    # QR kodunu kaydedilen konumdan seçilen bir konuma kopyala
    if temp_filename:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            import shutil
            shutil.copy(temp_filename, save_path)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("QR Kod Oluşturucu")
root.iconbitmap(default="")
# Pencere ölçeğini büyütme ve kilitleme
root.geometry("410x550")
root.resizable(False, False)

# Arka plan rengini değiştirme
root.configure(bg="white")

# Metin girişi
label = tk.Label(root, text="QR'a Çevirmek İstediğiniz Metin:")
label.configure(bg="white")
label.pack(pady=5)

entry = tk.Entry(root, bg="#DCDCDC")
entry.pack()

# QR kodunu göstermek için bir etiket
qr_label = tk.Label(root)
qr_label.configure(bg="white")
qr_label.pack()

# QR kodu oluşturma düğmesi
generate_button = ttk.Button(root, text="Oluştur", command=generate_qr_code)
generate_button.pack(pady=10)

# QR kodunu indirme düğmesi
download_button = ttk.Button(root, text="Kaydet", command=download_qr_code)
download_button.pack(pady=5)

# Uyarı etiketi
warning_label = tk.Label(root, text="", fg="red")
warning_label.configure(bg="white")
warning_label.pack()

link_label = tk.Label(root, text="Coded By Leaddy", fg="red", cursor="hand2")
link_label.pack(side="bottom", pady=10)
link_label.configure(bg="white")
link_label.bind("<Button-1>", open_link)

# Geçici dosya adı
temp_filename = None

# Uygulamayı başlat
root.mainloop()
