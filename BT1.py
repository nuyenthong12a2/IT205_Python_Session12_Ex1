
cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
    }
]


while True:
    print("\n" + "="*20 + " SHOPEE CART MANAGEMENT CLI " + "="*20)
    print("1. Xem chi tiết giỏ hàng và Tổng tiền")
    print("2. Thêm sản phẩm mới hoặc Tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("="*68)
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    
    if choice == "1":
        if len(cart_items) == 0:
            print("\n[THÔNG BÁO] Giỏ hàng hiện đang trống.")
            continue  
            
        print("\n" + "="*70)
        print(f"{'MÃ SP':<10}{'TÊN SẢN PHẨM':<25}{'SỐ LƯỢNG':<12}{'ĐƠN GIÁ':<12}{'THÀNH TIỀN':<12}")
        print("-" * 70)
        
        tong_so_luong = 0
        tong_tien = 0
        
        for item in cart_items:
            thanh_tien = item["number"] * item["price"]
            tong_so_luong += item["number"]
            tong_tien += thanh_tien
         
            print(f"{item['id']:<10}{item['name']:<25}{item['number']:<12}{item['price']:<12,}{thanh_tien:<12,}")
            
        print("-" * 70)
        print(f"Tổng số lượng sản phẩm: {tong_so_luong}")
        print(f"Tổng tiền giỏ hàng    : {tong_tien:,} VND")
        print("="*70)

  
    elif choice == "2":
        print("\n--- THÊM SẢN PHẨM MỚI / TĂNG SỐ LƯỢNG ---")
        ma_sp = input("Nhập mã sản phẩm: ").strip()
        if ma_sp == "":
            print("[LỖI] Mã sản phẩm không được để trống.")
            continue
            
       
        so_luong_nhap = input("Nhập số lượng: ").strip()
        if not so_luong_nhap.isdigit():
            print("[LỖI] Số lượng phải là số nguyên dương hợp lệ (không nhập chữ, số âm hoặc số thập phân).")
            continue
            
        so_luong = int(so_luong_nhap)
        if so_luong == 0:
            print("[LỖI] Số lượng sản phẩm phải lớn hơn 0.")
            continue
            
      
        san_pham_tim_thay = None
        for item in cart_items:
            if item["id"].strip().upper() == ma_sp.upper():
                san_pham_tim_thay = item
                break 
        
        if san_pham_tim_thay is not None:
            san_pham_tim_thay["number"] += so_luong
            print(f"[THÀNH CÔNG] Đã cộng dồn {so_luong} sản phẩm vào mã '{ma_sp}'.")
            
        
        else:
            ten_sp = input("Nhập tên sản phẩm: ").strip()
            if ten_sp == "":
                print("[LỖI] Tên sản phẩm không được để trống.")
                continue
                
            don_gia_nhap = input("Nhập đơn giá: ").strip()
            if not don_gia_nhap.isdigit():
                print("[LỖI] Đơn giá phải là số nguyên dương hợp lệ.")
                continue
                
            don_gia = int(don_gia_nhap)
            
           
            new_item = {
                "id": ma_sp,
                "name": ten_sp,
                "number": so_luong,
                "price": don_gia
            }
            cart_items.append(new_item)
            print(f"[THÀNH CÔNG] Đã thêm mới sản phẩm '{ten_sp}' vào giỏ hàng.")

   
    elif choice == "3":
        print("\n--- CẬP NHẬT SỐ LƯỢNG SẢN PHẨM ---")
        ma_sp = input("Nhập mã sản phẩm cần sửa: ").strip()
        
        
        san_pham_tim_thay = None
        for item in cart_items:
            if item["id"].strip().upper() == ma_sp.upper():
                san_pham_tim_thay = item
                break
                
        if san_pham_tim_thay is None:
            print("[THÔNG BÁO] Mã sản phẩm không tồn tại trong giỏ hàng.")
            continue
            
        
        so_luong_moi_nhap = input("Nhập số lượng mới: ").strip()
        if not so_luong_moi_nhap.isdigit():
            print("[LỖI] Số lượng phải là số nguyên dương hợp lệ.")
            continue
            
        so_luong_moi = int(so_luong_moi_nhap)
        if so_luong_moi == 0:
            print("[LỖI] Số lượng sản phẩm phải lớn hơn 0.")
            continue
            
       
        san_pham_tim_thay["number"] = so_luong_moi
        print(f"[THÀNH CÔNG] Đã cập nhật số lượng mã '{ma_sp}' thành {so_luong_moi}.")

   
    elif choice == "4":
        print("\n--- XÓA SẢN PHẨM KHỎI GIỎ HÀNG ---")
        ma_sp = input("Nhập mã sản phẩm cần xóa: ").strip()
        
        
        san_pham_tim_thay = None
        for item in cart_items:
            if item["id"].strip().upper() == ma_sp.upper():
                san_pham_tim_thay = item
                break
                
        if san_pham_tim_thay is None:
            print("[THÔNG BÁO] Mã sản phẩm không tồn tại trong giỏ hàng.")
            continue
            
        
        cart_items.remove(san_pham_tim_thay)
        print(f"[THÀNH CÔNG] Đã xóa hoàn toàn sản phẩm có mã '{ma_sp}' khỏi giỏ hàng.")

  
    elif choice == "5":
        print("\nCảm ơn bạn đã sử dụng hệ thống quản lý giỏ hàng. Tạm biệt!")
        break  # Thoát khỏi vòng lặp while True, kết thúc chương trình

   
    else:
        print("[LỖI] Lựa chọn không hợp lệ! Vui lòng nhập số nguyên từ 1 đến 5.")