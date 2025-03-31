
from map import CATEGORY_MAP, GROUP_MAP, ATTRIBUTE_MAP

class CFIDecoder:
    """
    A full CFI code decoder based on ISO 10962.
    The CFI (Classification of Financial Instruments) code consists of 6 characters,
    where the first two characters represent the Category and Group, and the remaining
    four are additional attributes.
    """
    
    CATEGORY_MAP = CATEGORY_MAP
    GROUP_MAP = GROUP_MAP
    ATTRIBUTE_MAP = ATTRIBUTE_MAP


    
    def decode(self, cfi_code: str) -> dict:
        """
        Decodes a 6-character CFI code into its descriptive components.
        
        Parameters:
            cfi_code (str): A 6-character CFI code.
        
        Returns:
            dict: A dictionary containing the decoded attributes:
                  - category: Description from the first character.
                  - group: Description from the second character based on the category.
                  Additional attributes may be decoded if mappings are provided for the specific (category, group).
        
        Raises:
            ValueError: If the provided CFI code is not exactly 6 characters long.
        """
        if not cfi_code or len(cfi_code) != 6:
            raise ValueError("CFI code must be exactly 6 characters long.")
        
        cfi_code = cfi_code.upper()
        category_letter = cfi_code[0]
        group_letter = cfi_code[1]
        
        decoded = {
            "category": self.CATEGORY_MAP.get(category_letter, "Unknown"),
            "group": self.GROUP_MAP.get(category_letter, {}).get(group_letter, "Unknown"),
        }
        
        # Determine if additional attribute mappings exist for this (category, group)
        mapping_key = (category_letter, group_letter)
        if mapping_key in self.ATTRIBUTE_MAP:
            attribute_mapping_list = self.ATTRIBUTE_MAP[mapping_key]
            # Apply the mapping for each additional attribute based on its position.
            for idx, attribute_info in enumerate(attribute_mapping_list):
                # The nth attribute corresponds to position index 2 + n in the CFI code
                raw_char = cfi_code[2 + idx]
                decoded[attribute_info["name"]] = attribute_info["mapping"].get(raw_char, "Unknown")
        else:
            # If no specific mapping exists, return raw attribute characters.
            decoded["attribute_3"] = cfi_code[2]
            decoded["attribute_4"] = cfi_code[3]
            decoded["attribute_5"] = cfi_code[4]
            decoded["attribute_6"] = cfi_code[5]
        
        return decoded

if __name__ == "__main__":
    cfi = CFIDecoder()
   
    print(cfi.decode("SCBCCA"))