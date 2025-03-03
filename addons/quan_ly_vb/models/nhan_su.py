from odoo import models, fields

class HrEmployeeDocument(models.Model):
    _name = 'nhan_su'
    _description = 'Quản lý Nhân sự và Văn bản phụ trách'

    ten_nhan_vien = fields.Char("Tên nhân viên", required=True)
    chuc_vu = fields.Char("Chức vụ")  
    phong_ban = fields.Char("Phòng ban") 
    quyen_xu_ly = fields.Selection([
        ('soan_thao', 'Soạn thảo'),
        ('duyet', 'Duyệt'),
        ('gui', 'Gửi'),
    ], string="Quyền hạn xử lý", required=True, default='soan_thao')

    van_ban_den_ids = fields.One2many('document_in', 'nhan_su_id', string="Danh sách văn bản đến phụ trách")
    van_ban_di_ids = fields.One2many('document_out', 'nhan_su_id', string="Danh sách văn bản đi phụ trách")

    ghi_chu = fields.Text("Ghi chú")
