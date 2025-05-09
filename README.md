# 🔐 Cryptography Project

This project implements several cryptographic algorithms across three main categories: classical, symmetric, and asymmetric cryptography. It also includes a final mini-project for **secure communication** using **Wi-Fi sockets** (with Caesar and AES encryption) and a basic GUI.

---

## 🗂️ Project Structure

```
cryptography_project/
│
├── gui.py                  # Optional graphical interface
├── main.py                 # Entry point if using GUI
│
├── TP1_classic/            # Classical Cryptography Algorithms
│   ├── affine.py
│   ├── cesar.py
│   ├── hill.py
│   ├── otp.py
│   ├── playfair.py
│   ├── substitution.py
│   ├── vigenere.py
│   └── cryptanalysis/
│       ├── frequency_analysis.py
│       ├── index_of_coincidence.py
│       └── kasiski.py
│
├── TP2_symmetric/          # Symmetric Key Algorithms
│   ├── aes.py
│   ├── des.py
│   ├── rc4.py
│
├── TP3_asymmetric/         # Asymmetric Key Algorithms
│   ├── rsa.py
│   ├── elgamal.py
│   └── diffie_hellman.py
│
├── Final_Project/          # Real-time encrypted communication
│   ├── client.py           # Caesar cipher chat client
│   ├── server.py           # Caesar cipher chat server
│   ├── client2.py          # AES encrypted client
│   └── server2.py          # AES encrypted server
│
└── README.md
```

---

## ⚙️ Requirements

Ensure Python 3.6+ is installed. Then, install required libraries:

```bash
pip install pycryptodome
```

---

## ▶️ How to Use

### 🧪 Classical Algorithms (TP1)

Each script (e.g., `cesar.py`, `vigenere.py`, etc.) can be run directly:

```bash
cd TP1_classic
python cesar.py
```

The `cryptanalysis/` folder contains tools like:
- Frequency analysis
- Index of coincidence
- Kasiski method

### 🔐 Symmetric Algorithms (TP2)

```bash
cd TP2_symmetric
python aes.py
python des.py
python rc4.py
```

### 🔑 Asymmetric Algorithms (TP3)

```bash
cd TP3_asymmetric
python rsa.py
python elgamal.py
python diffie_hellman.py
```

---

## 📡 Final Project: Secure Wi-Fi Communication

### 🔁 Caesar Cipher Chat

- Run on **PC**:

```bash
cd Final_Project
python server.py
```

- Run on **Phone** (or another device in same Wi-Fi):

```bash
python client.py
```

📌 Edit `HOST` in `client.py` to your PC's IP address (e.g., `192.168.1.X`)

---

### 🛡️ AES Encrypted Chat

- Run on **PC**:

```bash
cd Final_Project
python server2.py
```

- Run on **Phone**:

```bash
python client2.py
```

📌 Edit `HOST` in `client2.py` to your PC's IP address.

---

## 🧰 Optional: GUI

If `gui.py` and `main.py` are connected to algorithm execution:

```bash
python main.py
```

---

## ✅ Tested On

- Windows 10
- Termux (Android)
- Python 3.10
- pycryptodome 3.18+

