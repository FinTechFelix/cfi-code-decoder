from map import CATEGORY_MAP, GROUP_MAP, ATTRIBUTE_MAP

class Decoder:
    """
    A full CFI code decoder based on ISO 10962.
    The CFI (Classification of Financial Instruments) code consists of 6 characters,
    where the first two characters represent the Category and Group, and the remaining
    four are additional attributes.
    """
    
    CATEGORY_MAP = CATEGORY_MAP
    GROUP_MAP = GROUP_MAP
    ATTRIBUTE_MAP = ATTRIBUTE_MAP
    
    def decode(self, cfi_code: str, show_options: bool = False) -> dict:
        """
        Decodes a 6-character CFI code into its descriptive components.
        
        Parameters:
            cfi_code (str): A 6-character CFI code.
            show_options (bool): Flag to indicate whether to include options in the attributes.
        
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
        
        if not isinstance(cfi_code,str):
            raise ValueError("CFI code must be of type str.")
        
        cfi_code = cfi_code.upper()
        category_letter = cfi_code[0]
        group_letter = cfi_code[1]
        
        decoded = {
            "category": self.CATEGORY_MAP.get(category_letter, None).lower() if self.CATEGORY_MAP.get(category_letter, None) else None,
            "group": self.GROUP_MAP.get(category_letter, {}).get(group_letter, None).lower() if self.GROUP_MAP.get(category_letter, {}).get(group_letter, None) else None,
        }
        
        attributes = []
        mapping_key = (category_letter, group_letter)
        if mapping_key in self.ATTRIBUTE_MAP:
            attribute_mapping_list = self.ATTRIBUTE_MAP[mapping_key]
            for idx, attribute_info in enumerate(attribute_mapping_list):
                raw_char = cfi_code[2 + idx]
                attr_name = attribute_info.get("name")
                attr_value = attribute_info["mapping"].get(raw_char, None).lower() if attribute_info["mapping"].get(raw_char, None) else None
                attr_dict = {
                    "position": idx + 3,
                    "name": attr_name,
                    "value": attr_value,
                }
                if show_options:
                    attr_dict["options"] = [v.lower() for v in attribute_info["mapping"].values()]
                attributes.append(attr_dict)
        
        else:
            for i in range(4):
                raw_char = cfi_code[2 + i]
                attributes.append({
                    "position": i + 3,
                    "name": None,
                    "value": raw_char.lower(),
                    "options": []
                })

        return {
            "category": decoded["category"],
            "group": decoded["group"],
            "attributes": attributes
        }

if __name__ == "__main__":
    cfi_decoder = Decoder()
    
    print(cfi_decoder.decode("CIOIMS"))