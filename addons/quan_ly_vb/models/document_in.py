from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DocumentIn(models.Model):
    _name = 'document_in'
    _description = 'Bảng chứa thông tin văn bản đến'

    so_van_ban = fields.Char("Số văn bản", required=True)
    
    loai_van_ban = fields.Selection([
        ('quyet_dinh', 'Quyết định'),
        ('cong_van', 'Công văn'),
        ('bao_cao', 'Báo cáo'),
        ('khac', 'Khác'),
    ], string="Loại văn bản", required=True)

    ngay_den = fields.Date("Ngày đến", required=True)
    ngay_ban_hanh = fields.Date("Ngày ban hành")
    co_quan_ban_hanh = fields.Char("Cơ quan ban hành")
    nguoi_ky = fields.Char("Người ký")
    trich_yeu = fields.Text("Trích yếu nội dung")
    nhan_su_id = fields.Many2one('nhan_su',string="Danh sách văn bản đến phụ trách")
    tep_dinh_kem = fields.Binary("Tệp đính kèm (PDF, Word...)")
    
    trang_thai_xu_ly = fields.Selection([
        ('pending', 'Chờ xử lý'),
        ('processing', 'Đang xử lý'),
        ('done', 'Đã hoàn thành'),
    ], string="Trạng thái xử lý", default='pending')
    
    trang_thai_van_ban = fields.Selection([
        ('hoa_toc', 'Hỏa tốc'),
        ('khan', 'Khẩn'),
        ('thuong_khan', 'Thượng khẩn'),
    ], string="Trạng thái")
    _sql_constraints = [
        ('unique_so_van_ban', 'UNIQUE(so_van_ban)', 'Số văn bản phải là duy nhất'),
    ]
    ghi_chu = fields.Text("Ghi chú (Nếu có)")
    
    workflow_ids = fields.One2many('document_workflow', 'van_ban_in_id', string="Lịch sử xử lý", ondelete='cascade')
    @api.constrains('so_van_ban')
    def _check_unique_so_van_ban(self):
        for record in self:
            if self.search_count([('so_van_ban', '=', record.so_van_ban)]) > 1:
                raise ValidationError("Số văn bản '{}' đã tồn tại, vui lòng nhập số khác.".format(record.so_van_ban))
   
