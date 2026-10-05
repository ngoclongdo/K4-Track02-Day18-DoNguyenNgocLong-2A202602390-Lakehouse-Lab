# Reflection — Lakehouse Lab

## Anti-pattern lựa chọn: "The Small-File / Fragmented Append Problem"

Trong các kiến trúc Lakehouse (như Delta Lake hay Iceberg), việc ghi nhận dữ liệu streaming hoặc micro-batch liên tục mà không có chiến lược compaction định kỳ sẽ tạo ra hàng triệu file Parquet kích thước nhỏ (small files). 

- **Nguyên nhân:** Hệ thống ghi trực tiếp các tệp nhỏ với tần suất cao (ví dụ mỗi vài giây một file), làm phình to transaction log, tăng metadata overhead, làm chậm đáng kể thời gian lập kế hoạch truy vấn (query planning) và lãng phí I/O.
- **Cách phòng tránh:** Thiết lập quy trình bảo trì tự động định kỳ (Maintenance jobs) thực hiện compaction (gộp file nhỏ thành file chuẩn ~128MB–512MB) kết hợp Z-Ordering/Clustering trên các cột truy vấn phổ biến để tối ưu hóa file skipping.

## Khai báo sử dụng AI (AI Usage)

- **Công cụ:** Gemini CLI.
- **Phạm vi hỗ trợ:** Hỗ trợ cấu hình script tự động hóa thực thi 8 notebook lightweight, giải thích các cơ chế delta-rs / PyIceberg và xử lý các lỗi tương thích hệ thống (như mã hóa ký tự trên Windows). Toàn bộ kết quả chạy thực tế, số liệu đo đạc và mã nguồn đều đã được kiểm chứng thủ công qua test suite và smoke test.
