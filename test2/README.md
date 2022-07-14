# e-Wallet!

e-Wallet là 1 giải pháp thay thế cho các phương pháp thanh toán truyền thống như tiền mặt hoặc dùng thẻ ngân hàng

#  Một số thuật ngữ sử dụng trong e-Wallet
**Account** : là đối tượng để e-Wallet quản lý tài khoản người dùng. Trong hệ e-Wallet sẽ có 3 loại account chính: 
 - Merchant: là account được tạo ra khi 1 merchant được đăng ký dùng để quản lý doanh thu của 1 cửa hàng
 - Personal: là account của người dùng để thanh toán
 - Issuer: là account được cấp phát cho các ngân hàng, các điểm thu tiền. Đây là loại account có quyền thực hiện gọi lệnh nạp tiền vài tài khoản

**Merchant** : là những cửa hàng online hoặc cửa hàng truyền thống có đăng ký với e-Wallet. Khi đăng ký Merchant e-Wallet sẽ cung cấp 1 account

**Transaction** : dùng để quản lý 1 phiên giao dịch, transaction sẽ có những trạng thái khác nhau
 - Initialized: transaction đã được tạo (đã xác định số tiền và account thụ hưởng)
 - Confirmed: transaction đã được confirm (đã xác định account thanh toán)
 - Verified: transaction đã được xác nhận (sẽ được thực hiện thanh toán sau đó)
 - Completed: transaction đã hoàn thành, thanh toán thành công
 - Expired: transaction đã vượt quá 5 phút nhưng chưa hoàn thành
 - Canceled: transaction bị cancel bởi /transaction/cancel
 - Failed: transaction bị Fail do balance không đủ 

**Signature** : Là một mã hash md5 (ví dụ: 68b344639ecd4fd9966abda41a59e689) được hash từ payload của Transaction (ngoại trừ signature). 
```Ví dụ:
{"merchantId": "3fa85f64-5717-4562-b3fc-2c963f66afa6","amount": 1.1,"extraData": "eyJvcmRlcklkIjogIjM1NzA2Y2ViLTRhYWEtNDcxYi04OTg1LTQ1M2IyYjY2ZGI1OSJ9"} 
sẽ có signature là: 225744eba143248ae232bf81d6366b66
```
**Merchant JWT Token** : Đối với thông tin transaction được gửi qua lại giữa Merchant và e-Wallet, các thông tin đã được hash bởi mã md5. Tuy nhiên hacker hoàn toàn có thể thay đổi dữ liệu này. Do đó các request gửi qua lại sẽ được bổ xung thông tin Signature trong JWT

**ExtraData** : ExtraData có thể là bất cứ thứ gì do hệ thống merchant định nghĩa. Mỗi khi e-Wallet update thông tin thay đổi transaction thì cần gửi kèm thông tin extraData. Dữ liệu này không có ý nghĩa trong hệ thống của e-Wallet, tuy nhiên sẽ có ý nghĩa ở hệ thống của merchant. Ví dụ: nếu merchant thêm thông tin orderId vào extraData, e-Wallet sẽ không hiểu orderId này là gì cả, tuy nhiên khi e-Wallet gửi thông tin transaction về cho Merchant, merchant sẽ đọc và biết transaction này đang sử lý cho orderId nào để có thể cập nhật trạng thái chính xác đến order đó.

**Transaction Flow**

![](./transaction.jpg)

**Transcation Canceling Flow**

![](./transactionCancel.jpg)

**Transaction Life Circle**

![](./transactionLifeCircle.jpg)
