import unittest
from app.services.validators import OrderValidator
from app.services.transformers import OrderTransformer

class TestOrderValidator(unittest.TestCase):

    def setUp(self):
        self.validator = OrderValidator()

    # 測試金額超過 2000
    def test_price_over_2000(self):
        order_data = {
            "price": "2050"
        }
        valid, error = self.validator.validate_price(order_data["price"])
        self.assertFalse(valid)
        self.assertEqual(error, "Price is over 2000")

    # 測試金額未超過 2000
    def test_price_under_2000(self):
        order_data = {
            "price": "1500"
        }
        valid, error = self.validator.validate_price(order_data["price"])
        self.assertTrue(valid)
        self.assertIsNone(error)

    # 測試貨幣格式非 TWD, USD
    def test_invalid_currency_format(self):
        order_data = {
            "currency": "EUR"  # 非 TWD 或 USD
        }
        valid, error = self.validator.validate_currency(order_data["currency"])
        self.assertFalse(valid)
        self.assertEqual(error, "Currency format is wrong")

    # 測試貨幣格式為 TWD
    def test_valid_currency_twd(self):
        order_data = {
            "currency": "TWD"
        }
        valid, error = self.validator.validate_currency(order_data["currency"])
        self.assertTrue(valid)
        self.assertIsNone(error)

    # 測試貨幣格式為 USD
    def test_valid_currency_usd(self):
        order_data = {
            "currency": "USD"
        }
        valid, error = self.validator.validate_currency(order_data["currency"])
        self.assertTrue(valid)
        self.assertIsNone(error)

    def test_non_english_name(self):
        order_data = {
            "name": "中文"
        }
        valid, error = self.validator.validate_name(order_data["name"])
        self.assertFalse(valid)
        self.assertEqual(error, "Name contains non-English characters")

    def test_non_capitalized_name(self):
        order_data = {
            "name": "melody"
        }
        valid, error = self.validator.validate_name(order_data["name"])
        self.assertFalse(valid)
        self.assertEqual(error, "Name is not capitalized")

    def test_valid_name(self):
        order_data = {
            "name": "Melody"
        }
        valid, error = self.validator.validate_name(order_data["name"])
        self.assertTrue(valid)
        self.assertIsNone(error)

class TestOrderTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = OrderTransformer()

    # 測試將 USD 轉換為 TWD
    def test_convert_currency_usd_to_twd(self):
        price = "100"
        currency = "USD"
        converted_price, converted_currency = self.transformer.convert_currency(price, currency)
        self.assertEqual(converted_price, "3100")  # 100 USD * 31 匯率
        self.assertEqual(converted_currency, "TWD")

    # 測試 TWD 不進行轉換
    def test_convert_currency_twd(self):
        price = "100"
        currency = "TWD"
        converted_price, converted_currency = self.transformer.convert_currency(price, currency)
        self.assertEqual(converted_price, "100")
        self.assertEqual(converted_currency, "TWD")
