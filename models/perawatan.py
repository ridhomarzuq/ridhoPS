from odoo import models, fields, api


class ridhops(models.Model):
    _name = "ridhops.service"
    _description = "Teknik Perawatan PS"

    nama = fields.Selection(
        string='Jenis Perawatan',
        selection=[('biasa', 'biasa'), ('istimewa', 'istimewa'), ('special', 'special')])

    teknik = fields.Selection(
        string='Teknik Perawatan',
        selection=[('Small', 'Sedot debu'), ('Medium', 'Sedot Debu + Lap Body'), ('Large', 'Full Service')])

    hasil = fields.Selection(
        string='Hasil Service',
        selection=[('Bersih Mengkilap', 'Bersih Mengkilap'), ('Bening', 'Bening'), ('Seperti Baru', 'Sepetri Baru')])

    tersedia = fields.Boolean(
        string='Tersedia',
        deafault=True)

    deskripsi = fields.Char(
        string='Deskripsi',
        help='Isi Dengan Kotornya PS')

    models_id = fields.One2many(
        comodel_name='ridhops.jenisps',
        inverse_name='perawatan_id',
        string='Deskripsi PS')
