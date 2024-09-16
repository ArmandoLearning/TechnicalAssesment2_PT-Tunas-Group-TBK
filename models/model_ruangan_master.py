from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterRuangan(models.Model):
    _name = 'ruangan.master'
    _description = 'Master Ruangan'

    name = fields.Char('Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('meeting_room_kecil', 'Meeting Room Kecil'),
        ('meeting_room_besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], 'Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1a', '1A'),
        ('1b', '1B'),
        ('1c', '1C'),
        ('2a', '2A'),
        ('2b', '2B'),
        ('2c', '2C')
    ], 'Lokasi Ruangan', required=True)
    foto_ruangan = fields.Binary('Foto Ruangan', required=True)
    kapasitas_ruangan = fields.Integer('Kapasitas Ruangan', required=True)
    keterangan = fields.Text('Keterangan')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Nama Ruangan Tidak Boleh Sama!')
    ]

