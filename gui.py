import tkinter as tk
from tkinter import ttk, messagebox
from TP1_classic import affine, cesar, hill, otp, playfair, substitution, vigenere
from TP1_classic.cryptanalysis import frequency_analysis, index_of_coincidence, kasiski

from TP3_asymmetric import (elgamal ,rsa,diffie_hellman)
from TP2_symmetric import aes, des, rc4
from TP4_hash_and_signature import signature_rsa, signature_elgamal

dark_mode = False

# Initialiser la fenêtre principale
root = tk.Tk()
root.title("Crypto Project GUI")
root.geometry("700x500")

# --- DARK MODE ---
style = ttk.Style(root)
style.theme_use('clam')
root.configure(bg="#181818")
style.configure("Dark.TFrame", background="#181818")
style.configure("Dark.TLabel", background="#181818", foreground="#EEEEEE")
style.configure("Dark.TButton", background="#222222", foreground="#EEEEEE")
style.configure("Dark.TRadiobutton", background="#181818", foreground="#EEEEEE")
style.configure("Dark.TCheckbutton", background="#181818", foreground="#EEEEEE")

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Menu des algorithmes classiques
def show_classical_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Classical Algorithms", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)
    ttk.Button(main_frame, text="Affine Cipher", command=show_affine_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Cesar Cipher", command=show_cesar_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Hill Cipher", command=show_hill_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="OTP", command=show_otp_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Playfair Cipher", command=show_playfair_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Substitution Cipher", command=show_substitution_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Vigenere Cipher", command=show_vigenere_menu, style="Dark.TButton").pack(pady=5)
    ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
    ttk.Button(main_frame, text="Frequency Analysis", command=show_frequency_analysis_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Index of Coincidence", command=show_index_of_coincidence_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Kasiski Examination", command=show_kasiski_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu, style="Dark.TButton").pack(pady=20)

# Affine Cipher UI
def show_affine_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Affine Cipher", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key a (coprime with 26):", style="Dark.TLabel").pack()
    a_entry = ttk.Entry(main_frame)
    a_entry.pack()

    ttk.Label(main_frame, text="Key b:", style="Dark.TLabel").pack()
    b_entry = ttk.Entry(main_frame)
    b_entry.pack()

    result_label = ttk.Label(main_frame, text="", style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_affine, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_cesar_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Cesar Cipher", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Shift (integer):", style="Dark.TLabel").pack()
    shift_entry = ttk.Entry(main_frame)
    shift_entry.pack()

    result_label = ttk.Label(main_frame, text="", style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_cesar, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_hill_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Hill Cipher", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key matrix (e.g. 3,3;2,5 for [[3,3],[2,5]] or leave blank for default):", style="Dark.TLabel").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_hill, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_otp_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="One-Time Pad (OTP)", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt (random key)", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (provide key)", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (for decryption):", style="Dark.TLabel").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_otp, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_playfair_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Playfair Cipher", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (default MONARCHY):", style="Dark.TLabel").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_playfair, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_substitution_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Substitution Cipher", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt (random key)", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (provide key)", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (26-letter permutation, leave blank for random on encrypt):", style="Dark.TLabel").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_substitution, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_vigenere_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Vigenere Cipher", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    ttk.Label(main_frame, text="Key (letters only):", style="Dark.TLabel").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_vigenere, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_frequency_analysis_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Frequency Analysis", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_frequency, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_index_of_coincidence_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Index of Coincidence", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    ttk.Label(main_frame, text="Text:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600, style="Dark.TLabel")
    result_label.pack(pady=10)

    def run_ioc():
        try:
            text = text_entry.get()
            result = index_of_coincidence.index_of_coincidence(text)
            result_label.config(text=f"Index of Coincidence: {result:.4f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_ioc, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

def show_kasiski_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Kasiski Examination", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    ttk.Label(main_frame, text="Ciphertext:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600, style="Dark.TLabel")
    result_label.pack(pady=10)

    def run_kasiski():
        try:
            text = text_entry.get()
            result = kasiski.kasiski_examination(text)
            result_label.config(text=f"Kasiski Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Run", command=run_kasiski, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_classical_menu, style="Dark.TButton").pack()

# Menu des algorithmes asymétriques
def show_asymmetric_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Asymmetric Algorithms", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)
    
    ttk.Button(main_frame, text="ElGamal", command=show_elgamal_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="RSA", command=show_rsa_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Diffie-Hellman", command=show_diffie_hellman_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu, style="Dark.TButton").pack(pady=20)

# ElGamal UI
def show_elgamal_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="ElGamal Encryption", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    ttk.Label(main_frame, text="Prime number (p):", style="Dark.TLabel").pack()
    p_entry = ttk.Entry(main_frame)
    p_entry.insert(0, "467")
    p_entry.pack()

    ttk.Label(main_frame, text="Message:", style="Dark.TLabel").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_elgamal, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_asymmetric_menu, style="Dark.TButton").pack()

# RSA UI
def show_rsa_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="RSA Encryption", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    ttk.Label(main_frame, text="Prime p:", style="Dark.TLabel").pack()
    p_entry = ttk.Entry(main_frame)
    p_entry.insert(0, "61")
    p_entry.pack()

    ttk.Label(main_frame, text="Prime q:", style="Dark.TLabel").pack()
    q_entry = ttk.Entry(main_frame)
    q_entry.insert(0, "53")
    q_entry.pack()

    ttk.Label(main_frame, text="Message:", style="Dark.TLabel").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_rsa, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_asymmetric_menu, style="Dark.TButton").pack()

# Diffie-Hellman UI
def show_diffie_hellman_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Diffie-Hellman Key Exchange", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    ttk.Label(main_frame, text="Prime p:", style="Dark.TLabel").pack()
    p_entry = ttk.Entry(main_frame)
    p_entry.insert(0, "23")
    p_entry.pack()

    ttk.Label(main_frame, text="Generator g:", style="Dark.TLabel").pack()
    g_entry = ttk.Entry(main_frame)
    g_entry.insert(0, "5")
    g_entry.pack()

    ttk.Label(main_frame, text="Alice's private key (a):", style="Dark.TLabel").pack()
    a_entry = ttk.Entry(main_frame)
    a_entry.insert(0, "6")
    a_entry.pack()

    ttk.Label(main_frame, text="Bob's private key (b):", style="Dark.TLabel").pack()
    b_entry = ttk.Entry(main_frame)
    b_entry.insert(0, "15")
    b_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_dh, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_asymmetric_menu, style="Dark.TButton").pack()


# Menu des algorithmes symétriques
def show_symmetric_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Symmetric Algorithms", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)
    
    ttk.Button(main_frame, text="AES", command=show_aes_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="DES", command=show_des_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="RC4", command=show_rc4_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu, style="Dark.TButton").pack(pady=20)


# AES UI
def show_aes_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="AES Encryption (ECB - 128bit)", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (Hex input)", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text / Hex:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_aes, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_symmetric_menu, style="Dark.TButton").pack()

# DES UI
def show_des_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="DES Encryption (ECB)", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (Hex input)", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Text / Hex:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_des, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_symmetric_menu, style="Dark.TButton").pack()

# RC4 UI
def show_rc4_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="RC4 Encryption", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    action_var = tk.StringVar(value="e")
    ttk.Radiobutton(main_frame, text="Encrypt", variable=action_var, value="e", style="Dark.TRadiobutton").pack()
    ttk.Radiobutton(main_frame, text="Decrypt (Hex input)", variable=action_var, value="d", style="Dark.TRadiobutton").pack()

    ttk.Label(main_frame, text="Key:", style="Dark.TLabel").pack()
    key_entry = ttk.Entry(main_frame)
    key_entry.pack()

    ttk.Label(main_frame, text="Text / Hex:", style="Dark.TLabel").pack()
    text_entry = ttk.Entry(main_frame, width=50)
    text_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
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

    ttk.Button(main_frame, text="Run", command=run_rc4, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_symmetric_menu, style="Dark.TButton").pack()


# Frame principal
main_frame = ttk.Frame(root, padding=20, style="Dark.TFrame")
main_frame.pack(fill="both", expand=True)

def show_signature_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Signatures", font=("Helvetica", 16), style="Dark.TLabel").pack(pady=20)
    
    ttk.Button(main_frame, text="1. ElGamal Signature", command=show_signature_elgamal_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="2. RSA Signature", command=show_signature_rsa_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Back", command=show_main_menu, style="Dark.TButton").pack(pady=20)

def show_signature_elgamal_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="ElGamal Signature", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    use_custom = tk.BooleanVar(value=False)
    ttk.Checkbutton(main_frame, text="Entrer vos propres clés", variable=use_custom, style="Dark.TCheckbutton").pack()

    p_entry = ttk.Entry(main_frame)
    alpha_entry = ttk.Entry(main_frame)
    x_entry = ttk.Entry(main_frame)

    def toggle_entries():
        if use_custom.get():
            ttk.Label(main_frame, text="p:", style="Dark.TLabel").pack()
            p_entry.pack()
            ttk.Label(main_frame, text="alpha:", style="Dark.TLabel").pack()
            alpha_entry.pack()
            ttk.Label(main_frame, text="x (privée):", style="Dark.TLabel").pack()
            x_entry.pack()
        else:
            p_entry.pack_forget()
            alpha_entry.pack_forget()
            x_entry.pack_forget()

    use_custom.trace_add('write', lambda *args: toggle_entries())
    toggle_entries()

    ttk.Label(main_frame, text="Message:", style="Dark.TLabel").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
    result_label.pack(pady=10)

    def run_elgamal_signature():
        try:
            msg = msg_entry.get()
            if use_custom.get():
                p = int(p_entry.get())
                alpha = int(alpha_entry.get())
                x = int(x_entry.get())
                y = pow(alpha, x, p)
            else:
                p, alpha, x, y = signature_elgamal.eg_key_generation()
                result_label.config(text=f"Clés générées : p={p}, alpha={alpha}, x={x}, y={y}")
            r, s = signature_elgamal.sign_message(msg, p, alpha, x)
            valid = signature_elgamal.verify_signature(msg, p, alpha, y, r, s)
            result_label.config(text=f"Signature (ElGamal): r={r}, s={s}\nVérification: {'valide' if valid else 'invalide'}")
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    ttk.Button(main_frame, text="Signer & Vérifier", command=run_elgamal_signature, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_signature_menu, style="Dark.TButton").pack()

def show_signature_rsa_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="RSA Signature", font=("Helvetica", 14), style="Dark.TLabel").pack(pady=10)

    use_custom = tk.BooleanVar(value=False)
    ttk.Checkbutton(main_frame, text="Entrer vos propres clés", variable=use_custom, style="Dark.TCheckbutton").pack()

    n_entry = ttk.Entry(main_frame)
    e_entry = ttk.Entry(main_frame)
    d_entry = ttk.Entry(main_frame)

    def toggle_entries():
        if use_custom.get():
            ttk.Label(main_frame, text="n:", style="Dark.TLabel").pack()
            n_entry.pack()
            ttk.Label(main_frame, text="e:", style="Dark.TLabel").pack()
            e_entry.pack()
            ttk.Label(main_frame, text="d:", style="Dark.TLabel").pack()
            d_entry.pack()
        else:
            n_entry.pack_forget()
            e_entry.pack_forget()
            d_entry.pack_forget()

    use_custom.trace_add('write', lambda *args: toggle_entries())
    toggle_entries()

    ttk.Label(main_frame, text="Message:", style="Dark.TLabel").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=500, style="Dark.TLabel")
    result_label.pack(pady=10)

    def run_rsa_signature():
        try:
            msg = msg_entry.get()
            if use_custom.get():
                n = int(n_entry.get())
                e = int(e_entry.get())
                d = int(d_entry.get())
            else:
                n, e, d = signature_rsa.generate_keys()
                result_label.config(text=f"Clés générées : n={n}, e={e}, d={d}")
            signature = signature_rsa.sign_message(msg, d, n)
            valid = signature_rsa.verify_signature(msg, signature, e, n)
            result_label.config(text=f"Signature (RSA): {signature}\nVérification: {'valide' if valid else 'invalide'}")
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    ttk.Button(main_frame, text="Signer & Vérifier", command=run_rsa_signature, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_signature_menu, style="Dark.TButton").pack()
# Menu principal

def show_main_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Crypto Project Menu", font=("Helvetica", 16), style="Dark.TLabel").pack(pady=20)
    
    ttk.Button(main_frame, text="1. Classical Algorithms", command=show_classical_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="2. Symmetric Algorithms", command=show_symmetric_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="3. Asymmetric Algorithms", command=show_asymmetric_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="4. Signatures", command=show_signature_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="5. Hash Functions", command=show_hash_menu, style="Dark.TButton").pack(pady=5)
    ttk.Button(main_frame, text="Exit", command=root.quit, style="Dark.TButton").pack(pady=20)

def show_hash_menu():
    clear_frame(main_frame)
    ttk.Label(main_frame, text="Hash Functions", font=("Helvetica", 16), style="Dark.TLabel").pack(pady=20)

    hash_var = tk.StringVar(value="md5")
    ttk.Radiobutton(main_frame, text="MD5", variable=hash_var, value="md5", style="Dark.TRadiobutton").pack(anchor='w')
    ttk.Radiobutton(main_frame, text="SHA1", variable=hash_var, value="sha1", style="Dark.TRadiobutton").pack(anchor='w')
    ttk.Radiobutton(main_frame, text="SHA256", variable=hash_var, value="sha256", style="Dark.TRadiobutton").pack(anchor='w')
    ttk.Radiobutton(main_frame, text="SHA3_256", variable=hash_var, value="sha3_256", style="Dark.TRadiobutton").pack(anchor='w')

    ttk.Label(main_frame, text="Message:", style="Dark.TLabel").pack()
    msg_entry = ttk.Entry(main_frame, width=50)
    msg_entry.pack()

    result_label = ttk.Label(main_frame, text="", wraplength=600, style="Dark.TLabel")
    result_label.pack(pady=10)

    def run_hash():
        import hashlib
        msg = msg_entry.get().encode()
        algo = hash_var.get()
        try:
            if algo == "md5":
                h = hashlib.md5(msg).hexdigest()
            elif algo == "sha1":
                h = hashlib.sha1(msg).hexdigest()
            elif algo == "sha256":
                h = hashlib.sha256(msg).hexdigest()
            elif algo == "sha3_256":
                h = hashlib.sha3_256(msg).hexdigest()
            else:
                h = "Unknown algorithm"
            result_label.config(text=f"Hash: {h}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Hash", command=run_hash, style="Dark.TButton").pack(pady=10)
    ttk.Button(main_frame, text="Back", command=show_main_menu, style="Dark.TButton").pack(pady=20)

show_main_menu()
root.mainloop()
