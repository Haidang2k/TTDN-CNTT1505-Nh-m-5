# -*- coding: utf-8 -*-
{
    'name': "Quản lý Văn Bản",
    'summary': """
        Hệ thống quản lý văn bản đến, văn bản đi và lịch sử xử lý trong doanh nghiệp""",
    'description': """
        Mô-đun giúp quản lý toàn bộ quy trình xử lý văn bản trong tổ chức, bao gồm:
        - Quản lý văn bản đến (lưu trữ, theo dõi, xử lý)
        - Quản lý văn bản đi (soạn thảo, duyệt, gửi)
        - Lịch sử xử lý văn bản (theo dõi quá trình xử lý)
        - Quản lý nhân sự liên quan đến văn bản
    """,
    'author': "Your Name",
    'website': "http://www.yourcompany.com",
    'category': 'Document Management',
    'version': '1.0',

    # Các mô-đun cần thiết để hoạt động
    'depends': ['base', 'mail'],  # mail để hỗ trợ thông báo và theo dõi

    # Dữ liệu được tải khi cài đặt mô-đun
    'data': [
        'security/ir.model.access.csv',  
        'views/document_in.xml', 
        'views/document_out.xml',  
        'views/document_workflow.xml',  
        'views/nhan_su.xml',
        'views/menu.xml',  
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
