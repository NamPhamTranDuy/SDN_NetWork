Yêu cầu:
 + Tập trung vào việc tìm hiểu và phân tích giao thức OpenFlow, một thành phần cốt lõi trong kiến trúc mạng định nghĩa bằng phần mềm (SDN). Tìm hiểu về vai trò của OpenFlow trong quá trình giao tiếp giữa bộ điều khiển và các thiết bị trong mô hình mạng, sau đó phân tích cấu trúc và cách hoạt động của OpenFlow, cách quản lý các luồng dữ liệu trong mô hình mạng. Xây dựng mô hình mạng SDN sử dụng OpenDaylight làm controller trung tâm, kết nối với hệ thống mạng ảo và kiểm tra và đánh giá. Mục tiêu chính là triển khai và quản lý trong mạng SDN nhằm minh họa khả năng phân chia và điều khiển lưu lượng một cách linh hoạt và hiệu quả.

 + Trong quá trình thực hiện, Mininet được sử dụng để mô phỏng mạng, kết hợp với OpenDaylight để quản lý và cấu hình các thiết bị mạng thông qua giao thức OpenFlow. Các VLAN được tạo và cấu hình để kiểm tra tính biệt lập và khả năng định tuyến lưu lượng giữa chúng.

 + Kết quả của dự án cho thấy được vai trò to lớn của giao thức OpenFlow trong mô hình mạng SDN. OpenDaylight không chỉ giúp tối ưu hóa quản lý mạng mà còn cải thiện đáng kể tính linh hoạt trong việc triển khai và vận hành các mô hình mạng. Đây là tiền đềquan trọng để mở rộng nghiên cứu và ứng dụng các giải pháp SDN vào quản lý mạng phức tạp hơn trong tương lai.

Công nghệ sử dụng:
 + Máy ảo sử dụng: Oracle VM VirtualBox, VMware,... 
 + Công cụ: OpenDayLight, Mininet,...
 + Giao thức OpenFlow

Giới thiệu chung: 
Mạng định nghĩa bằng phần mềm - Software Defined Networking (SDN): kiến trúc mạng tách biệt phần điều khiển (Control Plane) và phần chuyển tiếp dữ liệu (Data Plane) hoạt động độc lập, cho phép việc điều khiển mạng có thể lập trình dễ dàng và cơ sở hạ tầng mạng hoạt động độc lập với các ứng dụng và dịch vụ.

<img width="456" height="209" alt="image" src="https://github.com/user-attachments/assets/d594e611-138b-471d-a487-5ebb52590a92" />

Sự khác nhau giữa kiến trúc mạng truyền thống và mạng SDN:
 + Về kiến trúc: Mạng truyền thống tích hợp cả Control Plane và Data Plane trên từng thiết bị, khiến việc quản lý phức tạp và dễ xảy ra phân mảnh do phụ thuộc vào từng nhà sản xuất. SDN tách biệt hai chức năng này, tập trung điều khiển tại SDN Controller, còn thiết bị mạng chủ yếu thực hiện chuyển tiếp dữ liệu, giúp quản lý tập trung và tăng khả năng tương thích.

 + Về tính năng: SDN cho phép lập trình và điều khiển mạng thông qua phần mềm và API, giúp cấu hình linh hoạt, dễ thay đổi và triển khai dịch vụ mới. Ngược lại, mạng truyền thống phụ thuộc nhiều vào phần cứng và thường phải cấu hình thủ công trên từng thiết bị, gây mất thời gian và khó quản lý.

 <img width="472" height="244" alt="image" src="https://github.com/user-attachments/assets/d0d0715c-9637-42fd-8a65-3abb977abc31" />

