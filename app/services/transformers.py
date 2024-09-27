from app.services.interface import TransformerInterface
USD_TO_TWD_RATE = 31

class OrderTransformer(TransformerInterface):
    def convert_currency(self, price, currency):
        # 如果貨幣為 USD，轉換為 TWD
        if currency == "USD":
            return str(int(price) * USD_TO_TWD_RATE), "TWD"
        return price, currency
