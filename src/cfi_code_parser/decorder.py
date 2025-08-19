from src.cfi_code_parser.map import CATEGORY_MAP, GROUP_MAP, ATTRIBUTE_MAP

class Decoder:
    
    CATEGORY_MAP = CATEGORY_MAP
    GROUP_MAP = GROUP_MAP
    ATTRIBUTE_MAP = ATTRIBUTE_MAP
    
    def decode(self, cfi_code: str, show_options: bool = False) -> dict:
        
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