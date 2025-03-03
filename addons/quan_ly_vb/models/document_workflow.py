from odoo import models, fields, api

class DocumentWorkflow(models.Model):
    _name = 'document_workflow'
    _description = 'Lịch sử xử lý văn bản'

    van_ban_in_id = fields.Many2one('document_in', string="Văn bản đến", ondelete='set null')
    van_ban_out_id = fields.Many2one('document_out', string="Văn bản đi", ondelete='set null')
    
    
    ngay_xu_ly = fields.Datetime("Ngày xử lý", default=fields.Datetime.now, required=True)
    
    hanh_dong = fields.Selection([
        ('approve', 'Duyệt'),
        ('forward', 'Chuyển tiếp'),
        ('reject', 'Từ chối'),
    ], string="Hành động", required=True)
    
    noi_dung_xu_ly = fields.Text("Nội dung xử lý")
    
    