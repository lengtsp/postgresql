# postgresql

แนวทางการเปิด Docker : Postgresql
reference : Abhinand i
https://medium.com/@abhin4nd6/install-postgres-using-docker-compose-4810ff3f0def

หมายเหตุ ควรนำไปรวมกับ docker compose ของ ollama, open webUI เพื่อที่ up และ down ไปพร้อมกันเลย

แนวทางการใช้งาน

1. สร้าง table student พร้อมข้อมูลตัวอย่าง
python postgresql_create_table.py

2. check ชื่อตารางใน db ทั้งหมด
python postgresql_check_table.py
