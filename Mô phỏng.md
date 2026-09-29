Khởi tạo mô hình mạng:

<img width="552" height="385" alt="image" src="https://github.com/user-attachments/assets/4c0ecc45-7ac6-458d-b8d7-eca082123c84" />

Kết nối Switch với OpenDayLight Cotroller:

<img width="569" height="71" alt="image" src="https://github.com/user-attachments/assets/d913c128-ad68-43fa-a6f1-88da3eac29fb" />

Flow Entry được cập nhật sau khi kết nối OpenDayLight Controller:

<img width="606" height="380" alt="image" src="https://github.com/user-attachments/assets/2ba2bd04-bc0d-4c95-84f0-e61d8110e8c5" />

Kết quả sau quá trình giao tiếp của Host 1 đến Host 5:

<img width="601" height="311" alt="image" src="https://github.com/user-attachments/assets/9a54f8bc-4aae-44aa-af57-bf19097ef01a" />

Giải thích: Dựa theo Flow Table với các trường n_packet để quan sát thì ta sẽ thấy được đường đi của gói tin. Gói tin sẽ bắt đầu từ Switch 1 thông qua flow cookie=0x2b0000000000003d (in_port=4), tiếp tục qua Switch 2 thông qua flow cookie=0x2b0000000000003a (in_port=4) và đến Switch 3thông qua flow cookie=0x2b00000000000036 (in_port=4). Gói tin phản hồi lại từ Host 5 về Host 1 Bắt đầu từ Switch 3, thông qua flow cookie=0x2b00000000000039 (in_port=1), tiếp tục qua Switch 2 thông qua flow cookie=0x2b0000000000003b (in_port=2) và đến Switch thông qua flow cookie=0x2b0000000000003f (in_port=1).

Tiến hành ping toàn bộ hệ thống. không gói tin drop, như vậy khẳng định Flow Table được Controller cập nhật cho Switch là đúng.

<img width="333" height="157" alt="image" src="https://github.com/user-attachments/assets/bb1f4d25-e13e-449e-8edb-c59e3eb2723d" />

Bắt gói tin bằng WIRESHARK:

<img width="570" height="418" alt="image" src="https://github.com/user-attachments/assets/90edcc9b-829a-442e-b7e6-21a537bd7ffa" />

Giải thích: Qua Wireshark có thể quan sát quá trình giao tiếp giữa Controller và Switch bằng OpenFlow. Quá trình thiết lập kết nối gồm HELLO, FEATURE REQUEST/REPLY, BARRIER, ROLE, MULTIPART và SET CONFIG để xác nhận, trao đổi thông tin và cấu hình Switch. Sau đó, PACKET_OUT và FLOW_MOD được sử dụng để chuyển tiếp gói tin và cập nhật Flow Table. Khi gói tin không khớp Flow Entry hoặc được yêu cầu gửi lên Controller, Switch sử dụng PACKET_IN để thông báo và yêu cầu Controller xử lý.

Gói tin HELLO:

<img width="780" height="181" alt="image" src="https://github.com/user-attachments/assets/7aabc4a1-2bd6-47bb-a52e-81ee740416c0" />

Gói tin HELLO gửi lại từ Controller cùng gói FEATURE REQUEST:

<img width="780" height="339" alt="image" src="https://github.com/user-attachments/assets/aacaf83d-68d6-43b4-9f57-f38731333e4f" />

Gói tin FEATURE REPLY:

<img width="780" height="318" alt="image" src="https://github.com/user-attachments/assets/386535fd-0dc7-4332-8cba-ab0054cc21f5" />

2 gói tin BARRIER REQUEST/REPLY:

<img width="780" height="175" alt="image" src="https://github.com/user-attachments/assets/797688d1-3ffc-4212-ab15-d4de752e30da" />

<img width="780" height="181" alt="image" src="https://github.com/user-attachments/assets/07440cad-a829-4dc9-afe2-797881cd5ed3" />

Gói tin SET CONFIG cùng với FLOW MOD và PACKET OUT:

<img width="596" height="575" alt="image" src="https://github.com/user-attachments/assets/10cc758b-b4a1-4ada-8ba8-10f31513794a" />

Mô hình mạng trên OpenDayLight: 

<img width="780" height="418" alt="image" src="https://github.com/user-attachments/assets/8f1e3d9a-acd1-4546-bbc7-0323a42042a0" />

