# CFI Decoder

**CFIDecoder** is a Python utility for decoding CFI (Classification of Financial Instruments) codes according to the ISO 10962 standard. A CFI code is a six-character string that classifies financial instruments based on their characteristics, such as category, group, and specific attributes.

---

## 📦 Features

- Decodes 6-character CFI codes
- Interprets:
  - **Category** (1st character)
  - **Group** (2nd character, dependent on Category)
  - **Attributes** (3rd to 6th characters, optionally decoded using provided mappings)
- Handles unknown or unmapped characters gracefully
- Based on ISO 10962 standard

---

## 🧠 How It Works

The `CFIDecoder` relies on three mapping dictionaries:

- `CATEGORY_MAP`: Maps the first character to a high-level asset class (e.g., Equities, Bonds)
- `GROUP_MAP`: Maps the second character (contextual to the category) to subtypes
- `ATTRIBUTE_MAP`: Nested mappings for decoding characters 3 to 6, specific to a (category, group) tuple

These mappings must be provided externally via a `map.py` module.

---

## 🔧 Usage

```python
from cfidecoder import CFIDecoder

decoder = CFIDecoder()
result = decoder.decode("SCBCCA")
print(result)
