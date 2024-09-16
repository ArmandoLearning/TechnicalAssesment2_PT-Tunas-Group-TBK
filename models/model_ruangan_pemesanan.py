from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PemesananRuangan(models.Model):
    _name = 'ruangan.pemesanan'
    _description = 'Pemesanan Ruangan'

    def _default_status(self):
        return 'draft'

    name = fields.Char('Nomor Pemesanan', required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('ruangan.pemesanan'))
    ruangan_id = fields.Many2one('ruangan.master', 'Ruangan', required=True)
    nama_pemesanan = fields.Char('Nama Pemesanan', required=True)
    tanggal_pemesanan = fields.Datetime('Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], 'Status Pemesanan', default=_default_status)
    catatan_pemesanan = fields.Text('Catatan Pemesanan')

    _sql_constraints = [
        ('unique_pemesanan', 'unique(ruangan_id, tanggal_pemesanan)', 'Ruangan sudah dipesan pada tanggal ini!'),
        ('unique_nama_pemesanan', 'unique(nama_pemesanan)', 'Nama Pemesanan tidak boleh sama!')
    ]

    @api.constrains('nama_pemesanan')
    def _check_nama_pemesanan(self):
        for record in self:
            if self.search_count([
                ('nama_pemesanan', '=', record.nama_pemesanan),
                ('id', '!=', record.id)
            ]) > 0:
                raise ValidationError('Nama Pemesanan tidak boleh sama!')

    @api.constrains('tanggal_pemesanan', 'ruangan_id')
    def _check_pemesanan(self):
        for record in self:
            # Gunakan format 'date' untuk perbandingan jika hanya tanggal yang diperiksa
            domain = [
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)
            ]
            overlapping_pemesanan = self.search(domain)
            if overlapping_pemesanan:
                raise ValidationError('Ruangan sudah dipesan pada tanggal ini!')

    def action_ongoing(self):
        for record in self:
            if record.status_pemesanan == 'draft':
                record.status_pemesanan = 'ongoing'
            else:
                raise ValidationError('Status pemesanan tidak dapat diubah ke On Going.')

    def action_done(self):
        for record in self:
            if record.status_pemesanan == 'ongoing':
                record.status_pemesanan = 'done'
            else:
                raise ValidationError('Status pemesanan tidak dapat diubah ke Done.')
