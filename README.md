# 🔐 Image Encryption Tool – Pixel-Level Security in Python

**SkillCraft Cybersecurity Internship – Task 2**  
**Author:** Piyush Kumar  
**Domain:** Cybersecurity

---

## 📘 Project Overview

This project is a Python-based image encryption and decryption tool developed as part of Task 2 during my internship at SkillCraft Technology. The tool performs pixel-level manipulation to obfuscate and subsequently restore image data using simple yet effective techniques.

It demonstrates the integration of cryptographic logic into image processing workflows, providing a foundation for secure image transmission and storage.

---

## 🚀 Key Features

- 🔐 Supports encryption and decryption of `.jpg` and `.png` images
- Implements **two reversible encryption methods**:
  - **Pixel Swap** – Swaps adjacent pixels to scramble image content
  - **Mathematical Pixel Transformation** – Alters pixel values using a mathematical constant
- 📂 Automated folder-based workflow for organized input and output management
- 💻 Command-line interface (CLI) with `argparse` for seamless interaction

---

## 🎯 Learning Outcomes

- Gained practical understanding of **image obfuscation and encryption principles**
- Developed image manipulation logic using **NumPy** and **Pillow (PIL)**
- Implemented modular and user-friendly **CLI tools in Python**
- Practiced **reversible encryption** techniques using pixel-based logic
- Explored cybersecurity applications in the context of image processing

---

## 💡 Usage Examples

### 🔄 Encrypting an Image Using Pixel Swap

```bash
python main.py encrypt input/sample.jpg output/encrypted_swap.jpg --method swap
