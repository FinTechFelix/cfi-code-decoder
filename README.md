# 🔍 CFI Code Decoder

This Python package provides a decoder for **CFI codes** based on the ISO 10962 standard. It translates 6-character CFI codes into human-readable descriptions of financial instruments.

---

## 📘 What is a CFI Code?

A **CFI (Classification of Financial Instruments)** code is a 6-character identifier used to classify financial instruments.

- The **first character** indicates the *category* (e.g. equity, debt).
- The **second character** indicates the *group* (e.g. common shares, bonds).
- The **remaining four characters** describe specific *attributes* such as voting rights, payment status, interest type, and more — depending on the instrument type.

---

## 🧠 How It Works

The decoder uses three core mappings:

- `CATEGORY_MAP`: maps the first character to a category.
- `GROUP_MAP`: maps the second character to a group, depending on the category.
- `ATTRIBUTE_MAP`: provides mappings for the last 4 characters, specific to (category, group) combinations.

If a detailed mapping for a category/group is not available, the raw character values will be returned with `null` attribute names.

---

## ✅ Example Usage

```python
from cfi_code_decoder import Decoder

decoder = Decoder()

print(decoder.decode("ESVUFR"))
print(decoder.decode("RWSNCA"))

```

## ➡️ Example Output
```json 
{
  "category": "equity",
  "group": "common/ordinary shares",
  "attributes": [
    {
      "position": 3,
      "name": "voting_right",
      "value": "voting"
    },
    {
      "position": 4,
      "name": "ownership",
      "value": "free"
    },
    {
      "position": 5,
      "name": "payment_status",
      "value": "fully paid"
    },
    {
      "position": 6,
      "name": "form",
      "value": "registered"
    }
  ]
}

{
   "category":"entitlements",
   "group":"warrants",
   "attributes":[
      {
         "position":3,
         "name":"underlying_assets",
         "value":"equities"
      },
      {
         "position":4,
         "name":"type",
         "value":"naked warrants"
      },
      {
         "position":5,
         "name":"call_put",
         "value":"call"
      },
      {
         "position":6,
         "name":"exercise_option_style",
         "value":"american"
      }
   ]
}

```