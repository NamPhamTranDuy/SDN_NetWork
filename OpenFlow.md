OpenFlow là một giao thức tiêu chuẩn trong Software-Defined Networking (SDN), cho phép sự phân tách giữa Control Plane (mặt phẳng điều khiển) và Data Plane (mặt phẳng dữ liệu) trong các thiết bị mạng như Switch và Router. Giao thức này cho phép một bộ điều khiển trung tâm (Controller) quản lý luồng dữ liệu của mạng bằng cách gửi các quy tắc luồng (flow rules) trực tiếp đến các thiết bị mạng, thay vì để chúng tự động định tuyến dữ liệu dựa trên các thuật toán tích hợp sẵn.

<img width="476" height="382" alt="image" src="https://github.com/user-attachments/assets/5771347a-e91b-434b-b539-43c1ce8a2f56" />

<img width="466" height="279" alt="image" src="https://github.com/user-attachments/assets/c0c33745-ec04-4165-b9d5-97408aea0996" />

Ưu điểm: OpenFlow mang lại tính linh hoạt, khả năng mở rộng và dễ quản lý nhờ tách biệt Control Plane và Data Plane, tập trung điều khiển qua Controller. Bên cạnh đó, OpenFlow hỗ trợ lập trình mạng, tối ưu lưu lượng, nâng cao hiệu suất, giảm chi phí phần cứng và tăng khả năng tương thích, tích hợp và mở rộng giữa các thiết bị mạng.

OpenFlow Switch: là thành phần cốt lõi của SDN, chịu trách nhiệm xử lý và chuyển tiếp gói tin theo các quy tắc từ Controller. Switch gồm Flow Table, Group Table, Meter Table, Secure Channel và OpenFlow Protocol. Hoạt động theo cơ chế “match-action”, tức là kiểm tra thông tin gói tin và thực hiện hành động tương ứng, giúp quản lý lưu lượng linh hoạt và hiệu quả.

<img width="448" height="325" alt="image" src="https://github.com/user-attachments/assets/dde1070f-2feb-4d57-8df8-4a0f1f8d3d7b" />

Quá trình xử lý pipeline của OpenFlow Switch:
 + Flow là tập hợp các gói tin có chung một số trường header. Trong OpenFlow Switch, Flow Table được đánh số từ table 0, quá trình xử lý luôn bắt đầu tại table 0 và có thể chuyển sang các table khác tùy kết quả match.

 + Flow Entry là quy tắc xác định cách switch xử lý gói tin dựa trên các trường header và hành động tương ứng. Gói tin sẽ được match với Flow Entry, cập nhật counter và thực hiện action; nếu không khớp, switch kiểm tra Table-Miss Entry, nếu vẫn không có quy tắc phù hợp thì gói tin có thể bị drop. Cơ chế nhiều Flow Table giúp xử lý và quản lý lưu lượng hiệu quả hơn.

<img width="624" height="191" alt="image" src="https://github.com/user-attachments/assets/0b7fa8f3-7c13-40dd-b52d-b091b07051d9" />

<img width="499" height="315" alt="image" src="https://github.com/user-attachments/assets/2772d644-dfdd-47be-9b84-7e09e997e675" />

