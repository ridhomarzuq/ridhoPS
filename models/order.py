from typing_extensions import Required
from odoo import api, fields, models


class orderps(models.Model):
    _name = 'ridhops.orderps'
    _description = 'New Description'

    name = fields.Char(
        string='Kode Order',
        required=True,
    )
    pemesan_id = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Pemesan',
        domain=[('is_customernya', '=', 'True')]
    )
    tanggal_pesan = fields.Datetime(
        string='Tanggal Pesanan',
        default=fields.Datetime.now
    )
