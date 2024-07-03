# -*- coding: utf-8 -*-

from odoo import models, fields

class Reclamacio(models.Model):
    _name = 'reclamacio.patrimonial'
    _description = 'Reclamació Patrimonial'

    tipus_dany = fields.Selection([
        ('persones', 'Persones'),
        ('vehicle', 'Vehicle'),
        ('be_concessionat', 'Be concessionat'),
        ('edifici', 'Edifici'),
        ('agricola', 'Agrícola'),
        ('altre', 'Altre')
    ], string='Tipus de Dany')