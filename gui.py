import tkinter as tk
from tkinter import ttk, messagebox
from TP1_classic import affine, cesar, hill, otp, playfair, substitution, vigenere
from TP1_classic.cryptanalysis import frequency_analysis, index_of_coincidence, kasiski

from TP3_asymmetric import (elgamal ,rsa,diffie_hellman)
from TP2_symmetric import aes, des, rc4

dark_mode = False

# Initialiser la fenêtre principale
root = tk.Tk()
root.title("Crypto Project GUI")
root.geometry("700x500")

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Menu principal
def show_main_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Crypto Project Menu", font=("Helvetica", 16)).pack(pady=20)
    
    ttk.Button(main_frame, text="1. Classical Algorithms", command=show_classical_menu).pack(pady=5)
    ttk.Button(main_frame, text="2. Symmetric Algorithms", command=show_symmetric_menu).pack(pady=5)
    ttk.Button(main_frame, text="3. Asymmetric Algorithms", command=show_asymmetric_menu).pack(pady=5)
    ttk.Button(main_frame, text="Exit", command=root.quit).pack(pady=20)

# Menu des algorithmes classiques
def show_classical_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Classical Algorithms", font=("Helvetica", 14)).pack(pady=10)
    ttk.Button(main_frame, text="Affine Cipher", command=show_affine_menu).pack(pady=5)
    ttk.Button(main_frame, text="Cesar Cipher", command=show_cesar_menu).pack(pady=5)
    ttk.Button(main_frame, text="Hill Cipher", command=show_hill_menu).pack(pady=5)
    ttk.Button(main_frame, text="OTP", command=show_otp_menu).pack(pady=5)
    ttk.Button(main_frame, text="Playfair Cipher", command=show_playfair_menu).pack(pady=5)
    ttk.Button(main_frame, text="Substitution Cipher", command=show_substitution_menu).pack(pady=5)
    ttk.Button(main_frame, text="Vigenere Cipher", command=show_vigenere_menu).pack(pady=5)
    ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
    ttk.Button(main_frame, text="Frequency Analysis", command=show_frequency_analysis_menu).pack(pady=5)
    ttk.Button(main_frame, text="Index of Coincidence", command=show_index_of_coincidence_menu).pack(pady=5)
    ttk.Button(main_frame, text="Kasiski Examination", command=show_kasiski_menu).pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu).pack(pady=20)

# Affine Cipher UI
def show_affine_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Affine Cipher", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key a (coprime with 26):").pack()
    a_entry = ttk.Entry(main_frame)
    a_entry.pack()

    ttk.Label(main_frame, text="Key b:").pack()
    b_entry = ttk.Entry(main_frame)
    b_entry.pack()

    result_label = ttk.Label(main_frame, text="")
    result_label.pack(pady=10)

    def run_affine():
        action = action_var.get()
        text = text_entry.get()
        try:
            a = int(a_entry.get())
            b = int(b_entry.get())
            if action == 'e':
                result = affine.affine_encrypt(text, a, b)
                result_label.config(text=f"Ciphertext: {result}")
            else:
                result = affine.affine_decrypt(text, a, b)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_affine).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_cesar_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Cesar Cipher", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Shift (integer):").pack()
    shift_entry = ttk.Entry(main_frame)
    shift_entry.pack()

    result_label = ttk.Label(main_frame, text="")
    result_label.pack(pady=10)

    def run_cesar():
        try:
            text = text_entry.get()
            shift = int(shift_entry.get())
            if action_var.get() == 'e':
                result = cesar.caesar_encrypt(text, shift)
                result_label.config(text=f"Ciphertext: {result}")
            else:
                result = cesar.caesar_decrypt(text, shift)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_cesar).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_hill_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Hill Cipher", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key matrix (e.g. 3,3;2,5 for [[3,3],[2,5]] or leave blank for default):").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def parse_matrix(s):
        if not s.strip():
            return None
        try:
            rows = s.split(';')
            matrix = [list(map(int, row.split(','))) for row in rows]
            import numpy as np
            return np.array(matrix)
        except Exception:
            raise ValueError("Invalid matrix format.")

    def run_hill():
        try:
            text = text_entry.get()
            key = parse_matrix(key_entry.get())
            if action_var.get() == 'e':
                result = hill.hill_encrypt(text, key)
                result_label.config(text=f"Ciphertext: {result}")
            else:
                result = hill.hill_decrypt(text, key)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_hill).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_otp_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="One-Time Pad (OTP)", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt (random key)", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (provide key)", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (for decryption):").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_otp():
        try:
            text = text_entry.get()
            if action_var.get() == 'e':
                ciphertext, key = otp.otp_encrypt(text)
                result_label.config(text=f"Ciphertext: {ciphertext}\nKey: {key}")
            else:
                key = key_entry.get()
                result = otp.otp_decrypt(text, key)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_otp).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_playfair_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Playfair Cipher", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (default MONARCHY):").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_playfair():
        try:
            text = text_entry.get()
            key = key_entry.get() or "MONARCHY"
            if action_var.get() == 'e':
                result = playfair.playfair_encrypt(text, key)
                result_label.config(text=f"Ciphertext: {result}")
            else:
                result = playfair.playfair_decrypt(text, key)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_playfair).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_substitution_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Substitution Cipher", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt (random key)", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (provide key)", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (26-letter permutation, leave blank for random on encrypt):").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_substitution():
        try:
            text = text_entry.get()
            key = key_entry.get()
            if action_var.get() == 'e':
                if not key:
                    key = substitution.generate_random_alphabet()
                result = substitution.substitution_encrypt(text, key)
                result_label.config(text=f"Ciphertext: {result}\nKey: {key}")
            else:
                substitution.validate_key(key)
                result = substitution.substitution_decrypt(text, key)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_substitution).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_vigenere_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Vigenere Cipher", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (letters only):").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_vigenere():
        try:
            text = text_entry.get()
            key = key_entry.get()
            if action_var.get() == 'e':
                result = vigenere.vigenere_encrypt(text, key)
                result_label.config(text=f"Ciphertext: {result}")
            else:
                result = vigenere.vigenere_decrypt(text, key)
                result_label.config(text=f"Plaintext: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_vigenere).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_frequency_analysis_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Frequency Analysis", font=("Helvetica", 14)).pack(pady=10)

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600)
    result_label.pack(pady=10)

    def run_frequency():
        try:
            text = text_entry.get()
            result = frequency_analysis.analyze_frequency(text)
            # Format result as a string for display
            result_str = "\n".join(f"{char}: {freq:.2f}%" for char, freq in result.items())
            result_label.config(text=result_str)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_frequency).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_index_of_coincidence_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Index of Coincidence", font=("Helvetica", 14)).pack(pady=10)

    ttk.Label(main_frame, text="Text:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600)
    result_label.pack(pady=10)

    def run_ioc():
        try:
            text = text_entry.get()
            result = index_of_coincidence.index_of_coincidence(text)
            result_label.config(text=f"Index of Coincidence: {result:.4f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_ioc).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

def show_kasiski_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Kasiski Examination", font=("Helvetica", 14)).pack(pady=10)

    ttk.Label(main_frame, text="Ciphertext:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600)
    result_label.pack(pady=10)

    def run_kasiski():
        try:
            text = text_entry.get()
            result = kasiski.kasiski_examination(text)
            result_label.config(text=f"Kasiski Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_kasiski).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu).pack()

# Menu des algorithmes asymétriques
def show_asymmetric_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Asymmetric Algorithms", font=("Helvetica", 14)).pack(pady=10)
    
    ttk.Button(main_frame, text="ElGamal", command=show_elgamal_menu).pack(pady=5)
    ttk.Button(main_frame, text="RSA", command=show_rsa_menu).pack(pady=5)
    ttk.Button(main_frame, text="Diffie-Hellman", command=show_diffie_hellman_menu).pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu).pack(pady=20)

# ElGamal UI
def show_elgamal_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="ElGamal Encryption", font=("Helvetica", 14)).pack(pady=10)

    ttk.Label(main_frame, text="Prime number (p):").pack()
    p_entry = ttk.Entry(main_frame)
    p_entry.insert(0, "467")
    p_entry.pack()

    ttk.Label(main_frame, text="Message:").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_elgamal():
        try:
            p = int(p_entry.get())
            msg = msg_entry.get()
            pub, priv = elgamal.elgamal_keygen(p)
            a, b = elgamal.elgamal_encrypt(pub, msg)
            decrypted = elgamal.elgamal_decrypt(priv, a, b, p)
            result_label.config(text=f"Encrypted: a={a}, b={b}\nDecrypted: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_elgamal).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_asymmetric_menu).pack()

# RSA UI
def show_rsa_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="RSA Encryption", font=("Helvetica", 14)).pack(pady=10)

    ttk.Label(main_frame, text="Prime p:").pack()
    p_entry = ttk.Entry(main_frame)
    p_entry.insert(0, "61")
    p_entry.pack()

    ttk.Label(main_frame, text="Prime q:").pack()
    q_entry = ttk.Entry(main_frame)
    q_entry.insert(0, "53")
    q_entry.pack()

    ttk.Label(main_frame, text="Message:").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_rsa():
        try:
            p = int(p_entry.get())
            q = int(q_entry.get())
            msg = msg_entry.get()
            pub, priv = rsa.generate_keypair(p, q)
            encrypted = rsa.encrypt(pub, msg)
            decrypted = rsa.decrypt(priv, encrypted)
            result_label.config(text=f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_rsa).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_asymmetric_menu).pack()

# Diffie-Hellman UI
def show_diffie_hellman_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Diffie-Hellman Key Exchange", font=("Helvetica", 14)).pack(pady=10)

    ttk.Label(main_frame, text="Prime p:").pack()
    p_entry = ttk.Entry(main_frame)
    p_entry.insert(0, "23")
    p_entry.pack()

    ttk.Label(main_frame, text="Generator g:").pack()
    g_entry = ttk.Entry(main_frame)
    g_entry.insert(0, "5")
    g_entry.pack()

    ttk.Label(main_frame, text="Alice's private key (a):").pack()
    a_entry = ttk.Entry(main_frame)
    a_entry.insert(0, "6")
    a_entry.pack()

    ttk.Label(main_frame, text="Bob's private key (b):").pack()
    b_entry = ttk.Entry(main_frame)
    b_entry.insert(0, "15")
    b_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_dh():
        try:
            p = int(p_entry.get())
            g = int(g_entry.get())
            a = int(a_entry.get())
            b = int(b_entry.get())
            A, B, shared = diffie_hellman.diffie_hellman_key_exchange(p, g, a, b)
            result_label.config(text=f"Alice sends A = {A}\nBob sends B = {B}\nShared Key: {shared}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_dh).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_asymmetric_menu).pack()


# Menu des algorithmes symétriques
def show_symmetric_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Symmetric Algorithms", font=("Helvetica", 14)).pack(pady=10)
    
    ttk.Button(main_frame, text="AES", command=show_aes_menu).pack(pady=5)
    ttk.Button(main_frame, text="DES", command=show_des_menu).pack(pady=5)
    ttk.Button(main_frame, text="RC4", command=show_rc4_menu).pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu).pack(pady=20)


# AES UI
def show_aes_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="AES Encryption (ECB - 128bit)", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (Hex input)", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text / Hex:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_aes():
        try:
            if action_var.get() == 'e':
                plaintext = text_entry.get()
                encrypted = aes.aes_encrypt(plaintext)
                result_label.config(text=f"Encrypted (hex): {encrypted.hex()}")
            else:
                hex_input = text_entry.get()
                decrypted = aes.aes_decrypt(bytes.fromhex(hex_input))
                result_label.config(text=f"Decrypted: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_aes).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_symmetric_menu).pack()

# DES UI
def show_des_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="DES Encryption (ECB)", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (Hex input)", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Text / Hex:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_des():
        try:
            if action_var.get() == 'e':
                plaintext = text_entry.get()
                encrypted = des.des_encrypt(plaintext)
                result_label.config(text=f"Encrypted (hex): {encrypted.hex()}")
            else:
                hex_input = text_entry.get()
                decrypted = des.des_decrypt(bytes.fromhex(hex_input))
                result_label.config(text=f"Decrypted: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_des).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_symmetric_menu).pack()

# RC4 UI
def show_rc4_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="RC4 Encryption", font=("Helvetica", 14)).pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (Hex input)", variable=action_var, value="d").pack()

    ttk.Label(main_frame, text="Key:").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    ttk.Label(main_frame, text="Text / Hex:").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500)
    result_label.pack(pady=10)

    def run_rc4():
        try:
            key = key_entry.get()
            if action_var.get() == 'e':
                plaintext = text_entry.get().encode()
                encrypted = rc4.rc4(key, plaintext)
                result_label.config(text=f"Encrypted (hex): {encrypted.hex()}")
            else:
                ciphertext = bytes.fromhex(text_entry.get())
                decrypted = rc4.rc4(key, ciphertext).decode()
                result_label.config(text=f"Decrypted: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_rc4).pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_symmetric_menu).pack()


# Frame principal
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)
show_main_menu()

root.mainloop()
