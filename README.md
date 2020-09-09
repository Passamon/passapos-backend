# PassaPOS Backend
Clean and lush point of sale program
![main-page](https://i.ibb.co/QYwKdFq/Web-1920-1.png)
![login-page](https://i.ibb.co/hB4LTr5/Web-1920-3.png)
![operating-page](https://i.ibb.co/Ttg2VSx/Web-1920-2.png)

# Installation
Prerequisite:
- Python 3+
- Django 3+

1 Let's clone the project!
```
git clone https://github.com/Passamon/passapos-backend
```

2 Change Directory to passapos-backend
```
cd passapos-backend
```

3 Run server (HTTP Server)
```
python manage.py runserver
```

4 Let's do some query to http://127.0.0.1:8000/{API_ENDPOINT}


# API Docs
## endpoint api/product/
HTTP GET: ดึงข้อมูลสินค้า
```JSON 
INPUT:
{
    "token": "User token",
    "product_id": 123 <-- (Optional หากใส่จะดึง product เฉพาะ product_id ที่ระบุ)
}
```
```JSON 
OUTPUT:
{
    "data": [
        {
            "product_id": 123,
            "product_name": "abc",
            "product_price": 123.00,
            "product_img": "abc.png"
        },
        ...
        ...
    ]
}
```
HTTP POST: เพิ่มสินค้า
```JSON 
INPUT:
{
    "token": "User token",
    "product_name": "abc",
    "product_price": 123.00,
    "product_img": "abc.png"
}
```
```JSON
OUTPUT:
{
    "data": "201"
}
```

HTTP PUT: แก้ไขสินค้า
```JSON
INPUT: 
{
    "token": "User token",
    "product_id": "id ของ Product ที่จะแก้ไข",
    "product_name": "abc",
    "product_price": 123.00,
    "product_img": "abc.png"
}
```
```JSON 
OUTPUT:
{
    "data": "200"
}
```
HTTP DELETE: ลบสินค้า
```JSON 
INPUT:
{
    "token": "User Token",
    "product_id": 123
}
```
```JSON 
OUTPUT:
{
    "data": "200"
}
```

## api/user/
HTTP GET: ดึง Username 
```JSON 
INPUT:
{
    "token": "",
    "user_id": ""
}
```
```JSON 
OUTPUT:
{
    "data": {
        "user_username": "",
        "user_password": ""
    }
}
```

HTTP POST: เข้าสู่ระบบ (Login)
```JSON 
INPUT:
{
    "user_username": "",
    "user_password": ""
}
```
```JSON 
OUTPUT:
{
    "data": "token"
}
```
HTTP PUT: เปลี่ยน username และ 
```JSON 
INPUT:
{
    "token": "",
    "user_id": "",
    "username": "",
    "password": ""
}
```
```JSON
OUTPUT:
{
    "data": "token"
}
```

## api/payment/
HTTP GET: รายงานยอดขาย
```JSON 
OUTPUT:
{
    "data": [
        ข้อมูลทุก Transaction
    ]
}
```

HTTP POST: ชำระเงิน
```JSON
INPUT:
{
    "token": "User token",
    "user_id": "",
    "product_id: "",
    "transaction_amount": ""
}
```
```JSON 
OUTPUT:
{
    "data": "201"
}
```