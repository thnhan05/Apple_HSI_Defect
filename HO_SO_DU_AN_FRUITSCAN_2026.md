# MẪU 3: HỒ SƠ DỰ ÁN DỰ THI BẢNG C
### Cuộc thi Sáng tạo trẻ Quốc gia trong lĩnh vực Trí tuệ nhân tạo năm 2026

> [!IMPORTANT]
> **LƯU Ý QUAN TRỌNG / DISCLAIMER:**  
> **ĐÂY LÀ BẢN KIỂM TRA TÍNH XÁC THỰC SƠ BỘ (BẢN CHECK LEGIT / PRELIMINARY VERIFICATION), KHÔNG PHẢI LÀ BẢN NỘP CHÍNH THỨC CUỐI CÙNG (FINAL VERSION).**  
> Bản hồ sơ này phục vụ việc rà soát dữ liệu, cấu trúc kỹ thuật và kiểm thử đối chứng các thuật toán trước khi hoàn thiện hồ sơ chính thức gửi Ban Tổ chức.

---

### THÔNG TIN ĐỘI THI
**Số lượng thí sinh trong đội thi:** 1 người ☐ &nbsp;&nbsp;&nbsp;&nbsp; 2 người ☐ &nbsp;&nbsp;&nbsp;&nbsp; 3 người ☒

| Thông tin | Thí sinh 1 (Đội trưởng) | Thí sinh 2 | Thí sinh 3 |
| :--- | :--- | :--- | :--- |
| **Họ và tên** | **Võ Thiện Nhân** | **Trần Tín Dũng** | **Đinh Thuy Thùy Linh** |
| **Ngày sinh** | 20/09/2005 | 03/05/2006 | 23/02/2007 |
| **Lớp, Ngành, Khoa, Trường** | Viện Kỹ thuật, Trường Đại học Công nghệ TP.HCM (HUTECH) | Marketing / K62NO / Trường ĐH Ngoại thương cơ sở II TP.HCM | Ngôn ngữ Anh / Trường ĐH Khoa học Xã hội và Nhân văn - ĐHQG TP.HCM |
| **Địa chỉ** | 10 Bùi Thị Xuân, TT. Chợ Lầu, Bắc Bình, Bình Thuận | 343 Nhật Tảo, Diên Hồng, Q.10, TP.HCM | TT. Nho Quan, H. Nho Quan, Ninh Bình |
| **Điện thoại** | 0982035143 | 0901389970 | 0969488243 |
| **Email** | thiennhan.math@gmail.com | tindung321@gmail.com | linhdinhthuythuy@gmail.com |
| **Vai trò dự án** | Trưởng nhóm - Nghiên cứu AI & Kỹ thuật hệ thống HSI | Phân tích thị trường, thương mại hóa & bài toán thực tiễn | Biên tập hồ sơ, tài liệu học thuật & đối chuẩn quốc tế |

---

## TÊN DỰ ÁN
### **FRUITSCAN: NỀN TẢNG PHÁT HIỆN VÀ PHÂN LOẠI KHUYẾT TẬT BỀ MẶT NÔNG SẢN KHÔNG PHÁ HỦY DỰA TRÊN ẢNH SIÊU PHỔ (HSI) VÀ TRÍ TUỆ NHÂN TẠO**

---

## TÓM TẮT DỰ ÁN (EXECUTIVE SUMMARY)
**Fruitscan** là giải pháp công nghệ lõi phục vụ kiểm soát chất lượng nông sản tự động sau thu hoạch, tích hợp công nghệ ảnh siêu phổ (**Hyperspectral Imaging - HSI**, dải Vis-NIR 450–990 nm) và các thuật toán học máy nhằm phát hiện, định lượng và phân loại khuyết tật bề mặt trái cây theo phương pháp quang học không phá hủy. 

Nghiên cứu được triển khai thực nghiệm trên giống táo tàu thương mại giá trị cao **Kaohsiung 11 "Honey"** (Đài Loan) qua hai pha công nghệ tiếp nối:
1. **Pha 1 - Phát hiện khuyết tật & chọn lọc bước sóng đặc trưng:** Ứng dụng giải thuật Phân tích thành phần chính (**PCA**) trích xuất 4 bước sóng then chốt (550, 680, 720, 954 nm), kết hợp chỉ số tỷ số phổ (**Band Ratio - BR**) và chỉ số thực vật hai băng phổ (**Two-Band Vegetation Index - TBVI**) để phân đoạn nhị phân các vùng tổn thương (Normal, Decay, Rusty spot, Fungal infection, Insect bite). Kết quả xác định cặp bước sóng tối ưu $720 - 680\text{ nm}$ cho độ tương phản vượt trội giữa mô bệnh và mô lành.
2. **Pha 2 - Phân loại đa lớp 7 trạng thái bề mặt bằng AI:** Xây dựng quy trình phân loại điểm ảnh (*pixel-level classification*) cho 7 trạng thái thực tế (Bình thường, Đốm gỉ, Thối, Nấm trắng, Nấm đen, Nứt, Phản xạ gương). Hai mô hình học máy **Support Vector Machine (SVM - nhân RBF)** và **Artificial Neural Network (ANN - cấu trúc 435-100-7)** đạt độ chính xác phân loại tổng thể lần lượt **97,3%** và **97,4%** trên tập kiểm định độc lập.

Hệ thống được thiết kế theo nguyên lý quét dòng **push-broom**, điều khiển đồng bộ bằng LabVIEW và xử lý dữ liệu qua MATLAB/Python. Đây là tiền đề kỹ thuật vững chắc để tích hợp mô-đun kiểm tra thời gian thực vào các dây chuyền phân loại tự động tại các nhà máy đóng gói, mở rộng thư viện dữ liệu HSI của nền tảng Fruitscan sang các nhóm trái cây vỏ mỏng và nông sản xuất khẩu chủ lực của Việt Nam.

---

## DANH MỤC TỪ VIẾT TẮT
| Từ viết tắt | Tên đầy đủ tiếng Anh | Ý nghĩa tiếng Việt |
| :--- | :--- | :--- |
| **HSI** | Hyperspectral Imaging | Công nghệ chụp ảnh siêu phổ |
| **ROI** | Region of Interest | Vùng quan tâm nghiên cứu |
| **PCA** | Principal Component Analysis | Phương pháp phân tích thành phần chính |
| **PC1 - PC7** | Principal Components 1 to 7 | Các thành phần chính từ 1 đến 7 |
| **BR** | Band Ratio | Chỉ số tỷ số phổ |
| **VI / TBVI**| Two-Band Vegetation Index | Chỉ số thực vật hai băng phổ |
| **SAM** | Spectral Angle Mapper | Thuật toán ánh xạ góc phổ |
| **SVM** | Support Vector Machine | Máy vectơ hỗ trợ |
| **RBF** | Radial Basis Function | Hàm nhân cơ sở xuyên tâm |
| **ANN** | Artificial Neural Network | Mạng nơ-ron nhân tạo |
| **LOESS** | Locally Estimated Scatterplot Smoothing | Bộ lọc hồi quy làm trơn cục bộ |
| **VIS-NIR** | Visible - Near Infrared | Vùng khả kiến - cận hồng ngoại (400–1000 nm) |
| **CCD** | Charge-Coupled Device | Cảm biến hình ảnh bán dẫn |

---

## NỘI DUNG CHI TIẾT HỒ SƠ DỰ ÁN

### 1. BÀI TOÁN VÀ VẤN ĐỀ THỰC TIỄN CẦN GIẢI QUYẾT
- **Thực trạng ngành nông nghiệp sau thu hoạch:** Trong chuỗi giá trị nông sản chất lượng cao, khâu kiểm tra và phân loại khuyết tật vỏ quả hiện vẫn phụ thuộc trên 85% vào lao động thủ công bằng mắt thường. Phương pháp này tồn tại nhiều nhược điểm: năng suất thấp, chi phí nhân công cao, độ chính xác giảm mạnh theo thời gian làm việc do mắt người mệt mỏi, và hoàn toàn không thể phát hiện các khuyết tật ẩn dưới lớp biểu bì ở giai đoạn sớm (vết bầm giập ẩn - *hidden bruise*, mầm nấm ủ bệnh).
- **Trường hợp điển hình của trái táo tàu (Jujube):** Táo tàu Kaohsiung 11 "Honey" là giống quả thương phẩm cao cấp với sản lượng thu hoạch trên 35.000 tấn/năm. Giá trị xuất khẩu đòi hỏi độ đồng đều ngoại quan gần như tuyệt đối; một vết thâm giập hoặc đốm gỉ nhỏ cũng khiến toàn bộ lô hàng bị loại bỏ hoặc hạ cấp loại B/C, gây thiệt hại kinh tế trực tiếp.
- **Giới hạn của camera màu RGB truyền thống:** Các camera thị giác máy (Machine Vision) thông thường chỉ ghi nhận 3 kênh màu Red - Green - Blue thông qua bộ lọc Bayer. Thông tin màu sắc này không có chiều sâu phổ và không nhạy cảm với biến đổi tế bào học hay thành phần sinh hóa của mô quả (nước, đường, diệp lục, anthocyanin).
- **Giải pháp của Fruitscan:** Ứng dụng công nghệ **Ảnh siêu phổ (HSI)**. Mỗi pixel trong khối ảnh HSI mang một đường cong phổ phản xạ liên tục qua hàng trăm bước sóng (tạo thành khối dữ liệu 3 chiều *hypercube*). Thách thức lớn nhất là dung lượng dữ liệu quá lớn gây nghẽn tính toán. **Fruitscan giải quyết bài toán cốt lõi này bằng cách:** sử dụng Trí tuệ nhân tạo (PCA, SAM, SVM, ANN) để trích xuất các dải phổ đặc trưng nhạy cảm nhất, giảm chiều dữ liệu tính toán từ hàng trăm kênh xuống một số ít kênh tối ưu, đảm bảo độ chính xác trên 97% trong khi khả thi hóa việc suy luận trực tuyến tốc độ cao trên dây chuyền công nghiệp.

---

### 2. MỤC TIÊU, PHẠM VI VÀ ĐỐI TƯỢNG ỨNG DỤNG
- **Mục tiêu tổng quát:** Xây dựng hoàn chỉnh mô-đun phần cứng và phần mềm ứng dụng ảnh siêu phổ Vis-NIR để phát hiện và phân loại không phá hủy 7 trạng thái bề mặt nông sản, làm lõi công nghệ cho hệ sinh thái phân loại tự động Fruitscan.
- **Mục tiêu kỹ thuật cụ thể:**
  1. Vận hành ổn định hệ thống thu nhận ảnh siêu phổ dạng quét dòng push-broom trong dải $450 - 990\text{ nm}$.
  2. Xây dựng pipeline tiền xử lý chuẩn hóa quang học: phân tách nền tự động, hiệu chuẩn phản xạ trắng/tối, lọc nhiễu LOESS.
  3. Xác định tập 4 bước sóng đặc trưng và cặp bước sóng tối ưu ($720 - 680\text{ nm}$) bằng PCA và chỉ số BR/TBVI.
  4. Huấn luyện thành công hai mô hình học máy đa lớp SVM (RBF) và ANN (435-100-7) phân loại chính xác 7 trạng thái tổn thương vỏ quả với độ chính xác kiểm định đạt trên 97%.
- **Phạm vi nghiên cứu:** Thực nghiệm chuyên sâu trên giống táo tàu Kaohsiung 11 "Honey" tại phòng thí nghiệm kiểm soát ánh sáng; thiết kế pipeline module hóa để sẵn sàng chuyển giao sang các loại trái cây vỏ mỏng tương tự (táo tây, lê, mận, đào, cà chua bi).
- **Đối tượng ứng dụng:** Các hợp tác xã nông nghiệp công nghệ cao, nhà máy chế biến - đóng gói xuất khẩu nông sản, và các nhà sản xuất máy phân loại nông sản tự động.

---

### 3. DỮ LIỆU SỬ DỤNG VÀ TÍNH HỢP LỆ
- **Nguồn gốc mẫu:** Quả táo tàu thu hoạch tại các trang trại chuyên canh ở Pingtung (Bình Đông, Đài Loan), vận chuyển và lưu trữ ở nhiệt độ $22^\circ\text{C}$, hoàn tất toàn bộ quá trình quét phổ trong 48 giờ để tránh suy giảm sinh lý tự nhiên.
- **Dung lượng và quy mô:**
  - Khối dữ liệu HSI thô: $960 \times 600\text{ pixels}$ (binning 2x2), gồm 435 kênh phổ hữu dụng ($468 - 950\text{ nm}$).
  - Mẫu phân loại đa lớp: 80 quả táo tàu thực tế mang các dạng bệnh tự nhiên. Gán nhãn cấp độ điểm ảnh (*pixel-level*) trên ảnh giả màu RGB chuẩn hóa ($622\text{ nm}, 530\text{ nm}, 465\text{ nm}$).
- **Số lượng mẫu phân bố theo trạng thái:**
  - Đốm gỉ (*Rusty spot*): 34 mẫu
  - Thối nhũn (*Decay*): 25 mẫu
  - Nấm trắng (*White fungus*): 16 mẫu
  - Nấm đen (*Black fungus*): 30 mẫu
  - Nứt vỏ (*Crack*): 38 mẫu
  *(Một quả có thể chứa đồng thời nhiều vùng bệnh khác nhau; 50 mẫu được chọn ngẫu nhiên để trích xuất tập điểm ảnh huấn luyện và kiểm định độc lập).*
- **Tính hợp lệ và an toàn:** Dữ liệu hoàn toàn là phép đo vật lý quang phổ phản xạ trên nông sản, không chứa bất kỳ thông tin cá nhân hay quyền riêng tư, do nhóm tự thực hiện độc lập, không phát sinh tranh chấp sở hữu trí tuệ.

---

### 4. QUY TRÌNH TIỀN XỬ LÝ VÀ CHUẨN HÓA DỮ LIỆU
Pipeline tiền xử lý dữ liệu của Fruitscan được thiết kế qua 4 công đoạn nghiêm ngặt:

1. **Hiệu chuẩn phản xạ quang học (Reflectance Calibration):**  
   Loại bỏ độ không đồng đều của nguồn sáng halogen và dòng tối cảm biến camera bằng công thức chuẩn hóa:
   $$R = \frac{R_{\text{sample}} - R_{\text{dark}}}{R_{\text{white}} - R_{\text{dark}}}$$
   Trong đó $R_{\text{white}}$ là ảnh tấm chuẩn trắng teflon (phản xạ 99%), $R_{\text{dark}}$ là ảnh trường tối thu được khi đậy nắp ống kính. Mỗi ảnh chuẩn được lấy trung bình từ 50–100 khung hình để triệt tiêu nhiễu ngẫu nhiên.
2. **Lọc làm trơn phổ (Spectral Smoothing):**  
   Áp dụng bộ lọc cục bộ **LOESS** (Locally Estimated Scatterplot Smoothing) theo chiều bước sóng cho từng pixel để làm phẳng nhiễu đo đạc mà không làm mất đi các đỉnh hấp thụ đặc trưng.
3. **Cắt lọc dải phổ tin cậy:**  
   Loại bỏ vùng biên tín hiệu yếu ($450-467\text{ nm}$ và $951-990\text{ nm}$) do đèn halogen và cảm biến CCD có hiệu suất lượng tử thấp ở hai rìa phổ. Dữ liệu làm sạch còn lại đúng **435 kênh phổ** ($468 - 950\text{ nm}$).
4. **Tách vùng quan tâm (ROI Masking) và Co viền:**  
   Thuật toán SAM kết hợp phân ngưỡng tạo mặt nạ nhị phân tách quả khỏi nền băng tải. Sau đó co viền mặt nạ khoảng 5% bằng phép biến đổi hình thái học (*morphological erosion*) để loại bỏ hiện tượng méo tín hiệu do góc nghiêng tán xạ ở rìa mép quả.

---

### 5. THUẬT TOÁN, MÔ HÌNH VÀ CÔNG CỤ TRÍ TUỆ NHÂN TẠO

#### A. Phân tích thành phần chính (PCA) & Lựa chọn bước sóng đặc trưng
Khối dữ liệu HSI có số chiều rất lớn. PCA phân tích ma trận hiệp phương sai của phổ và chiếu không gian đa chiều về các trục thành phần chính:
$$Z_k = X \cdot w_k$$
Hệ số tải (*loading coefficients*) của các vector riêng $w_k$ tại các thành phần $PC1 - PC3$ phản ánh mức độ đóng góp của từng bước sóng. Từ các cực trị của hệ số tải, 4 bước sóng đặc trưng then chốt được trích xuất:
- **$550\text{ nm}$ & $680\text{ nm}$ (Vùng khả kiến):** Phản ánh sắc tố vỏ quả và độ hấp thụ diệp lục.
- **$720\text{ nm}$ & $954\text{ nm}$ (Vùng cận hồng ngoại NIR):** Nhạy cảm với biến đổi cấu trúc tế bào, độ xốp mô và lượng nước tự do do nấm/thối gây ra.

#### B. Chỉ số phổ tăng cường tương phản (BR & TBVI)
- **Tỷ số phổ (Band Ratio):**
  $$BR_{jk} = \frac{R_j}{R_k}$$
- **Chỉ số thực vật hai băng phổ (Two-Band Vegetation Index):**
  $$TBVI_{jk} = \frac{R_j - R_k}{R_j + R_k}$$
Thử nghiệm 6 cặp bước sóng kết hợp từ tập 4 bước sóng đặc trưng chứng minh cặp **$720\text{ nm} - 680\text{ nm}$** tạo độ tương phản cực đại giữa mô lành và 4 loại khuyết tật (Decay, Rusty spot, Fungus, Insect bite).

#### C. Mô hình phân loại đa lớp Support Vector Machine (SVM)
Sử dụng hàm nhân cơ sở xuyên tâm (RBF kernel) để phân tách các ranh giới phi tuyến phức tạp:
$$K(x, x') = \exp\left(-\gamma \|x - x'\|^2\right)$$
Các siêu tham số phạt $C$ và độ rộng nhân $\gamma$ được tối ưu hóa toàn cục bằng thuật toán **Grid Search** kết hợp Cross-Validation trên không gian đa chiều 435 kênh phổ.

#### D. Mạng nơ-ron nhân tạo (ANN)
Kiến trúc Multi-Layer Perceptron (MLP) 3 lớp truyền thẳng:
- **Lớp đầu vào (Input layer):** 435 nút (tương ứng 435 kênh phản xạ phổ của 1 pixel).
- **Lớp ẩn (Hidden layer):** 100 nút, sử dụng hàm kích hoạt phi tuyến $\tanh$.
- **Lớp đầu ra (Output layer):** 7 nút tương ứng 7 trạng thái bề mặt, kích hoạt bằng hàm $\text{Softmax}$ để tính phân phối xác suất:
  $$P(y = i \mid x) = \frac{e^{z_i}}{\sum_{j=1}^7 e^{z_j}}$$

---

### 6. QUY TRÌNH HUẤN LUYỆN, TINH CHỈNH VÀ TÍCH HỢP
1. **Phân chia dữ liệu:** Bộ dữ liệu điểm ảnh gán nhãn được chia độc lập thành **70% tập huấn luyện (Training set)** và **30% tập kiểm định (Validation set)**.
2. **Huấn luyện mô hình:**
   - SVM được tối ưu tham số qua lưới $C \in [1, 1000]$, $\gamma \in [0.001, 1.0]$.
   - ANN được huấn luyện bằng thuật toán tối ưu Adam, hàm mất mát Categorical Cross-Entropy, theo dõi Early Stopping để ngăn chặn hiện tượng quá khớp (overfitting).
3. **Tích hợp kiểm tra tự động:**
   - Phần mềm điều khiển LabVIEW thu nhận ảnh quét dòng TIFF theo thời gian thực.
   - Script MATLAB/Python đóng gói chạy suy luận trên GPU/CPU, tự động hiển thị bản đồ khuyết tật 7 màu trực quan cho người vận hành.

---

### 7. CHỈ SỐ VÀ TIÊU CHÍ ĐÁNH GIÁ KẾT QUẢ

#### A. Kết quả phân loại đa lớp trên tập kiểm định (Validation 30%)
| Mô hình AI | Kiến trúc / Tham số tối ưu | Độ chính xác tổng thể (Accuracy) |
| :--- | :--- | :---: |
| **Support Vector Machine (SVM)** | RBF Kernel ($C, \gamma$ tối ưu qua Grid Search) | **97,3%** |
| **Artificial Neural Network (ANN)**| 3 lớp: 435 (vào) - 100 (ẩn) - 7 (ra), hàm tanh & softmax | **97,4%** |

#### B. Phân tích ma trận nhầm lẫn (Confusion Matrix Analysis)
Ma trận nhầm lẫn $7 \times 7$ chỉ ra rằng phần lớn các phân loại sai tập trung ở các cặp bệnh có cơ chế tổn thương tế bào tương đồng:
- **Thối nhũn $\rightarrow$ Đốm gỉ:** Nhầm lẫn $11,06\%$ (SVM) và $9,92\%$ (ANN) do giai đoạn đầu của thối nhũn làm sẫm màu biểu bì tương tự đốm gỉ.
- **Đốm gỉ $\rightarrow$ Thối nhũn:** Nhầm lẫn $2,39\%$ (SVM) và $2,72\%$ (ANN).
- **Thối nhũn $\leftrightarrow$ Nấm đen:** Nhầm lẫn từ $2,94\%$ đến $3,68\%$ do bào tử nấm đen và vết thối hoại tử đều có khả năng hấp thụ quang học rất mạnh ở toàn bộ dải Vis-NIR.

---

### 8. SO SÁNH VỚI MÔ HÌNH CƠ SỞ VÀ TÍNH MỚI CỦA GIẢI PHÁP
| Tiêu chí so sánh | Phương pháp cơ sở (Baseline cũ) | Giải pháp cải tiến của Fruitscan |
| :--- | :--- | :--- |
| **Phạm vi nhận diện** | Chỉ phát hiện vết bầm ẩn (*hidden bruise*) | Phát hiện và phân loại chi tiết **7 trạng thái bề mặt** |
| **Chọn bước sóng** | Chọn thủ công 2 bước sóng cố định (737 & 990 nm) | **Tự động hóa qua hệ số tải PCA** ($550, 680, 720, 954\text{ nm}$) |
| **Cặp bước sóng tối ưu** | $737 - 990\text{ nm}$ (chỉ nhạy với vết bầm) | **$720 - 680\text{ nm}$** (tối ưu đồng thời cho cả 4 loại bệnh vỏ quả) |
| **Khả năng phân loại** | Phát hiện nhị phân (Có bầm / Không bầm) | **Phân loại đa lớp 7 trạng thái đạt 97,4%** (SVM & ANN) |
| **Mặt nạ nền** | Ngưỡng cường độ cố định (dễ nhầm bóng đổ) | Thuật toán **SAM góc phổ + co biên 5%** triệt tiêu nhiễu mép quả |

---

### 9. KIẾN TRÚC HỆ THỐNG VÀ PHƯƠNG ÁN TRIỂN KHAI THỰC TẾ

```
[Mẫu quả trên băng chuyền] 
       │
       ▼ (Quét dòng Push-broom)
[Camera CCD Basler + Specim Inspector V10]
       │
       ▼ (Chuỗi ảnh TIFF dòng phổ)
[LabVIEW Điều khiển & Đồng bộ phần cứng]
       │
       ▼ (Khối Hypercube 468-950 nm)
[Module Tiền xử lý: ROI (SAM) + Hiệu chuẩn R + Lọc LOESS]
       │
       ▼ (Dữ liệu phổ chuẩn hóa 435 kênh)
┌────────────────────────────────────────────────────────┐
│               KHỐI XỬ LÝ TRÍ TUỆ NHÂN TẠO              │
│                                                        │
│  [Chế độ Nhanh - BR/TBVI]      [Chế độ Chi tiết - AI] │
│   - Cặp sóng: 720 & 680 nm      - Trích 7 PCs qua PCA  │
│   - Phân ngưỡng nhị phân       - Phân loại SVM / ANN   │
└────────────────────────────────────────────────────────┘
       │
       ▼
[Bản đồ bề mặt 7 màu + Tọa độ khuyết tật + Cờ phân loại Grade A/B/C]
       │
       ▼
[Cơ cấu tay gạt khí nén phân loại trên dây chuyền]
```

---

### 10. PHÂN TÍCH RỦI RO, ĐẠO ĐỨC AI VÀ AN TOÀN DỮ LIỆU
- **Hiện tượng phản xạ gương (Glare):** Vỏ quả nhẵn bóng tạo điểm chói sáng làm bão hòa cảm biến. **Giải pháp:** Nhóm đưa *Glare* thành một lớp nhãn độc lập trong mô hình 7 trạng thái để AI chủ động nhận diện và bỏ qua điểm chói thay vì nhận diện sai thành khuyết tật.
- **Hiện tượng trôi hiệu chuẩn (Calibration Drift):** Đèn halogen suy giảm quang thông theo thời gian. **Giải pháp:** Quy định quy trình quét tự động tấm chuẩn trắng/tối định kỳ mỗi 60 phút vận hành.
- **Đạo đức AI và tính minh bạch:** Hệ thống được định vị là công cụ sàng lọc tốc độ cao hỗ trợ con người, cung cấp bản đồ nhiệt giải thích lý do quả bị đánh trượt (Explainable AI qua đồ thị phổ đối chứng), không gây rủi ro về mặt an toàn sinh học.

---

### 11. HƯỚNG PHÁT TRIỂN TIẾP THEO
- **Ngắn hạn:** Ứng dụng các thuật toán lựa chọn đặc trưng phổ (SPA - Successive Projections Algorithm hoặc CARS) để rút gọn 435 kênh phổ xuống còn 10–15 bước sóng then chốt, rút ngắn thời gian suy luận xuống dưới $50\text{ ms/quả}$ phục vụ băng chuyền công nghiệp.
- **Trung hạn:** Xây dựng mô hình phân loại đa nhãn (*multi-label*) xử lý các vùng bệnh phức tạp chồng lấn (ví dụ: vết nấm mọc đè lên vết nứt vỏ); bổ sung nhận diện cuống và đài hoa quả để tránh nhầm với đốm gỉ.
- **Dài hạn:** Mở rộng thư viện phổ sang các nhóm nông sản xuất khẩu chủ lực của Việt Nam (xoài cát Hòa Lộc, thanh long ruột đỏ, bơ sáp, cà chua bi xuất khẩu), thương mại hóa thành trạm kiểm tra chất lượng cắm-và-chạy (*plug-and-play*).

---

### 12. PHỤ LỤC: TỔNG HỢP CÔNG THỨC TOÁN HỌC SỬ DỤNG
1. **Phản xạ tương đối:**
   $$R(\lambda) = \frac{R_{\text{sample}}(\lambda) - R_{\text{dark}}(\lambda)}{R_{\text{white}}(\lambda) - R_{\text{dark}}(\lambda)}$$
2. **Chỉ số tỷ số phổ:**
   $$BR = \frac{R(720\text{ nm})}{R(680\text{ nm})}$$
3. **Chỉ số thực vật hai băng phổ:**
   $$TBVI = \frac{R(720\text{ nm}) - R(680\text{ nm})}{R(720\text{ nm}) + R(680\text{ nm})}$$
4. **Độ dốc phổ phân biệt khuyết tật:**
   $$\text{Slope} = \frac{R(630\text{ nm}) - R(550\text{ nm})}{630 - 550} \quad \begin{cases} < 0: & \text{Bề mặt lành} \\ > 0: & \text{Bề mặt khuyết tật} \end{cases}$$
5. **Góc phổ SAM (Spectral Angle Mapper):**
   $$\alpha = \arccos\left( \frac{\sum_{i=1}^n t_i \cdot r_i}{\sqrt{\sum_{i=1}^n t_i^2} \cdot \sqrt{\sum_{i=1}^n r_i^2}} \right)$$
6. **Hàm nhân RBF trong mô hình SVM:**
   $$K(x, x') = \exp\left(-\gamma \sum_{i=1}^{435} (x_i - x'_i)^2\right)$$

---

### 13. MINH CHỨNG MÃ NGUỒN VÀ DỮ LIỆU
- **Kho mã nguồn và dữ liệu GitHub:** Toàn bộ mã nguồn xử lý MATLAB, script huấn luyện Python, mô hình phân loại SVM/ANN và dữ liệu siêu phổ thực nghiệm đã được đóng gói chuẩn hóa tại:  
  📁 `D:\normal\code_demo\new_version_2021_03_11\new_version\Apple_HSI_Defect_Project`
- **Tài liệu trực quan hóa:** Giao diện kiểm tra phổ tương tác Python [`view_apple_data.py`](file:///d:/normal/code_demo/new_version_2021_03_11/new_version/Apple_HSI_Defect_Project/python/view_apple_data.py) cho phép đo trực tiếp 7 PCs của PCA và phổ phản xạ 600 bước sóng của từng điểm ảnh.

---

*TP. Hồ Chí Minh, ngày 12 tháng 10 năm 2026*  
**ĐẠI DIỆN ĐỘI THI**  
*(Ký và ghi rõ họ tên)*  

**Võ Thiện Nhân**
