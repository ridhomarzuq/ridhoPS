# -*- coding: utf-8 -*-
from odoo import models,fields,api


class ModelDasar(models.Model):
    _name = "ridhops.modeldasar"
    _description = "Sewa PS Ridho"

    kapasitas = fields.Char(
        string='Kapasitas PS', 
        required=True,
    )
    tipe = fields.Selection(
        string ="Jenis PS", 
        selection=[
        ('PS1', 'Ps1'),
        ('PS2', 'Ps2'),
        ('PS3', 'Ps3')
    ])

class ridhops(models.Model):
    _name = "ridhops.jenisps"
    _description = "Daftar Jenis-jenis PS"
    _inherit = "ridhops.modeldasar"

    name =fields.Char(
        string ="Jenis Sewa",
        Required = True 
    )
    harga = fields.Integer(
        string = "Harga Sewa",
        Required = True
    )
    active = fields.Boolean(
        default = True
    )
    perawatan_id = fields.Many2one(
        comodel_name='ridhops.service', 
        string='Perawatan',
        Required = True,
        delegate = True
    )
    