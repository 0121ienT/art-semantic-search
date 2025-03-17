# Phân Tích Phong Cách Nghệ Thuật với Embeddings Đa Phương Thức

Kho lưu trữ này khám phá việc phân tích phong cách nghệ thuật trong hình ảnh bằng cách sử dụng **embeddings đa phương thức** và các thuộc tính tính toán. Sử dụng **tập dữ liệu WikiArt** từ 🤗 Hugging Face Hub, chúng tôi tận dụng **FiftyOne** để phân tích và trực quan hóa dữ liệu, cùng với mô hình **CLIP** được huấn luyện sẵn từ 🤗 Transformers để tạo embeddings. Dự án đi sâu vào phân tích dữ liệu không cấu trúc theo nhiều cách thú vị.

## Tính Năng

- **Tìm Kiếm Tương Đồng Hình Ảnh và Tìm Kiếm Ngữ Nghĩa**: Tạo embeddings đa phương thức cho hình ảnh bằng CLIP và lập chỉ mục tập dữ liệu để thực hiện tìm kiếm không cấu trúc nhanh chóng.
- **Phân Cụm và Trực Quan Hóa**: Phân cụm hình ảnh theo phong cách nghệ thuật dựa trên embeddings và trực quan hóa kết quả bằng phương pháp giảm chiều UMAP.
- **Phân Tích Tính Độc Đáo**: Gán điểm độc đáo cho mỗi hình ảnh dựa trên mức độ tương đồng với các hình ảnh khác trong tập dữ liệu.
- **Phân Tích Chất Lượng Hình Ảnh**: Tính toán các chỉ số chất lượng như độ sáng, độ tương phản và độ bão hòa, đồng thời khám phá mối liên hệ của chúng với phong cách nghệ thuật.

## Tập Dữ Liệu

Dự án sử dụng **tập dữ liệu WikiArt**, một bộ sưu tập phong phú các hình ảnh tác phẩm nghệ thuật, có sẵn qua 🤗 Hugging Face Hub.

## Công Cụ và Thư Viện

- **FiftyOne**: Dùng để tải dữ liệu, phân tích và trực quan hóa.
- **🤗 Transformers**: Cung cấp mô hình CLIP được huấn luyện sẵn để tạo embeddings.
- **UMAP**: Để giảm chiều và trực quan hóa các cụm embeddings.
- **Python**: Ngôn ngữ lập trình chính của dự án.

## Bắt Đầu

### Yêu Cầu

- Python 3.8 trở lên
- Cài đặt các thư viện cần thiết:
  ```bash
  pip install -r requirements.txt
  ```

### Cài Đặt

1. Tải kho lưu trữ về máy:
   ```bash
   git clone https://github.com/your-username/phan-tich-phong-cach-nghe-thuat.git
   cd phan-tich-phong-cach-nghe-thuat
   ```

2. Cài đặt các thư viện:
   ```bash
   pip install fiftyone transformers torch umap-learn
   ```

3. Tải tập dữ liệu WikiArt bằng FiftyOne hoặc Hugging Face Hub (hướng dẫn chi tiết trong notebook).

### Sử Dụng

Chạy tệp Jupyter notebook `phan_tich_phong_cach_nghe_thuat.ipynb` để khám phá toàn bộ quy trình:
```bash
jupyter notebook phan_tich_phong_cach_nghe_thuat.ipynb
```

Notebook bao gồm các bước chi tiết:
- Tải và tiền xử lý tập dữ liệu WikiArt.
- Tạo embeddings bằng CLIP.
- Thực hiện tìm kiếm tương đồng, phân cụm và phân tích tính độc đáo.
- Trực quan hóa kết quả với UMAP và các chỉ số chất lượng.

## Kết Quả Ví Dụ

- **Tìm Kiếm Tương Đồng**: Tìm các hình ảnh giống về mặt hình ảnh hoặc ngữ nghĩa với một hình ảnh đầu vào.
- **Phân Cụm**: Nhóm các tác phẩm nghệ thuật theo phong cách (ví dụ: Ấn tượng, Trừu tượng).
- **Điểm Độc Đáo**: Xác định các tác phẩm nổi bật trong tập dữ liệu.
- **Chỉ Số Chất Lượng**: Phân tích cách độ sáng và độ tương phản thay đổi theo phong cách.

## Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng mở một issue hoặc gửi pull request với ý tưởng hoặc cải tiến của bạn.

## Giấy Phép

Dự án này được cấp phép theo Giấy phép MIT. Xem tệp [LICENSE](LICENSE) để biết chi tiết.

## Lời Cảm Ơn

- Cảm ơn nhóm FiftyOne vì các công cụ phân tích dữ liệu mạnh mẽ.
- Tri ân 🤗 Hugging Face vì tập dữ liệu WikiArt và thư viện Transformers.
