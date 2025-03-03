from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DocumentOut(models.Model):
    _name = 'document_out'
    _description = 'Bảng chứa thông tin văn bản đi'

    so_van_ban = fields.Char("Số văn bản", required=True)

    loai_van_ban = fields.Selection([
        ('cong_van', 'Công văn'),
        ('quyet_dinh', 'Quyết định'),
        ('bao_cao', 'Báo cáo'),
        ('khac', 'Khác'),
    ], string="Loại văn bản", required=True)

    ngay_ban_hanh = fields.Date("Ngày ban hành", required=True)
    nguoi_ky = fields.Char("Người ký")
    noi_nhan = fields.Char("Nơi nhận")
    noi_dung_tom_tat = fields.Text("Nội dung tóm tắt")
    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    trang_thai_xu_ly = fields.Selection([
        ('pending', 'Chờ duyệt'),
        ('sent', 'Đã gửi'),
        ('done', 'Hoàn thành'),
    ], string="Trạng thái xử lý", default='pending')

    ghi_chu = fields.Text("Ghi chú")

    trang_thai_van_ban = fields.Selection([
        ('hoa_toc', 'Hỏa tốc'),
        ('thuong_khan', 'Thượng khẩn'),
        ('khan', 'Khẩn'),
    ], string="Trạng thái")
    _sql_constraints = [
        ('unique_so_van_ban', 'UNIQUE(name)', 'Số văn bản phải là duy nhất'),
    ]

    workflow_ids = fields.One2many('document_workflow', 'van_ban_out_id', string="Lịch sử xử lý", ondelete='cascade')
    nhan_su_id = fields.Many2one('nhan_su',string="Danh sách văn bản đến phụ trách")
    @api.constrains('so_van_ban')
    def _check_unique_so_van_ban(self):
        for record in self:
            if self.search_count([('so_van_ban', '=', record.so_van_ban)]) > 1:
                raise ValidationError("Số văn bản '{}' đã tồn tại, vui lòng nhập số khác.".format(record.so_van_ban))   
