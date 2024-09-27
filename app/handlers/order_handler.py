from app.services.interface import ValidatorInterface, TransformerInterface

class OrderHandler:
    def __init__(self, validator: ValidatorInterface, transformer: TransformerInterface):
        self.validator = validator
        self.transformer = transformer

    def process_order(self, order):
        # 驗證訂單
        valid, error = self.validator.validate(order)
        if not valid:
            return { "detail":error }

        # 轉換訂單
        converted_price, converted_currency = self.transformer.convert_currency(order["price"], order["currency"])

        order["price"] = converted_price
        order["currency"] = converted_currency
        
        return order
