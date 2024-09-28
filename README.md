## 題目1
- Q:請寫出一條查詢語句 (SQL)，列出在 2023 年 5 月下訂的訂單，使用台幣付款且5月總金額最
多的前 10 筆的旅宿 ID (bnb_id), 旅宿名稱 (bnb_name), 5 月總金額 (may_amount)

```sql
SELECT
    bnbs.id AS bnb_id,
    bnbs.name AS bnb_name,
    SUM(orders.amouont) AS may_amount
FROM
    orders
JOIN
    bnbs ON orders.bnb_id = bnbs.id
WHERE
    orders.currency = 'TWD'
    AND orders.created_at BETWEEN '2023-05-01 00:00:00' AND '2023-05-31 23:59:59'
GROUP BY
    bnbs.id, bnbs.name
ORDER BY
    may_amount DESC
LIMIT 10;

```
---
## 題目2
- Q: 在題目一的執行下，我們發現 SQL 執行速度很慢，您會怎麼去優化？請闡述您怎麼判斷與優
化的方式

1. 使用`EXPLAIN`分析上述sql查詢語法，找出性能瓶頸
2. 替orders(orders.bnb_id)和bnbs (bnb.id)兩張table建立索引
3. 進行分區 根據`created_at`進行時間範圍的分區(Horizontal Partition)，避免掃描整張表
---
## API實作
### **SOLID 原則**：

1. **單一職責原則（Single Responsibility Principle, SRP）**：
   - 每個類別和模組都應該只有一個任務。`OrderValidator` class負責的是驗證訂單的不同屬性，而 `OrderTransformer` 負責的是將訂單的貨幣進行轉換。

2. **開放封閉原則（Open/Closed Principle, OCP）**：
   - 類別應該對擴充開放，對修改封閉。藉由引入interface讓`OrderHandler`依賴於抽象介面，萬一想要新增新的驗證邏輯or轉換邏輯，只需要建立新的class，不需要修改現有的`OrderHandler`, `OrderTransformer`, `OrderValidator`


3. **介面隔離原則（Interface Segregation Principle, ISP）**：
   - 使每個介面只關注單一的功能。`ValidatorInterface` 專注於驗證訂單的屬性，而 `TransformerInterface` 則專注於處理幣值的轉換邏輯，
   
4. **依賴反轉原則（Dependency Inversion Principle, DIP）**：
   - 高層模組不應依賴於低層模組，兩者都應該依賴於interface介面。使得高層邏輯（`OrderHandler`）不依賴具體的 `OrderValidator` 和 `OrderTransformer`，而是依賴它們的interface介面。這樣可以通過依賴注入來替換具體的實做
   

### **設計模式**：

1. **策略模式（Strategy Pattern）**：
   - Strategy Pattern 的概念是先定出多種不同做法之間共通的 interface，把不同的做法變成一個一個獨立的 strategy class，然後再根據需求去決定現在要使用哪一個 strategy
   - `OrderValidator` 和 `OrderTransformer` 是策略模式的應用。創建不同的驗證策略來處理不同類型的訂單，這些策略都符合相同的interface。
   





