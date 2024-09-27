import re
from app.services.interface import ValidatorInterface

class OrderValidator(ValidatorInterface):
    def validate_required_fields(self, order):
        required_fields = ["id", "name", "address", "price", "currency"]
        
        # 檢查必要欄位是否存在
        for field in required_fields:
            if field not in order:
                return False, f"{field} is required"
        
        # 檢查地址內部的欄位是否存在
        address_fields = ["city", "district", "street"]
        for field in address_fields:
            if field not in order["address"]:
                return False, f"address.{field} is required"
        
        return True, None
    
    def validate_field_types(self, order):
        # 檢查是否為正確的型別
        if not isinstance(order["id"], str):
            return False, "id must be a string"
        
        if not isinstance(order["name"], str):
            return False, "name must be a string"
        
        if not isinstance(order["address"], dict):
            return False, "address must be an object"
        
        if not isinstance(order["address"]["city"], str):
            return False, "address.city must be a string"
        
        if not isinstance(order["address"]["district"], str):
            return False, "address.district must be a string"
        
        if not isinstance(order["address"]["street"], str):
            return False, "address.street must be a string"
        
        # 檢查價格是否為數字或字串格式
        if not isinstance(order["price"], (str, int, float)):
            return False, "price must be a string or number"
        
        if not isinstance(order["currency"], str):
            return False, "currency must be a string"
        
        return True, None
    
    def validate_price(self, price):
        # 檢查價格是否超過 2000
        if float(price) > 2000:
            return False, "Price is over 2000"
        
        return True, None
    
    def validate_currency(self, currency):
        if currency not in ["TWD", "USD"]:
            return False, "Currency format is wrong"
        return True, None
        
    def validate_name(self, name):
        # 檢查是否包含非英文字母字符
        if not re.match("^[A-Za-z ]+$", name):
            return False, "Name contains non-English characters"

        # 檢查每個單字的首字母是否大寫
        words = name.split()
        for word in words:
            if not word[0].isupper():
                return False, "Name is not capitalized"

        return True, None
    
    def validate(self, order):
        # 驗證是否包含必要欄位
        valid, error = self.validate_required_fields(order)
        if not valid:
            return False, error
        
        # 驗證欄位型別是否正確
        valid, error = self.validate_field_types(order)
        if not valid:
            return False, error
        
        # 驗證價格是否符合要求
        valid, error = self.validate_price(order["price"])

        valid, error = self.validate_currency(order["currency"])

        if not valid:
            return False, error
        
        # 驗證名稱格式
        valid, error = self.validate_name(order["name"])
        if not valid:
            return False, error
        
        return True, None
