# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Documentacio(models.Model):
    _name = 'documentacio.patrimonial'
    _description = 'Documentació Patrimonial'

    name = fields.Char(string='Identificador', required=True, copy=False, readonly=True, default='Nova Documentació')

    descripcio_doc = fields.Text(string='Descripción de la documentació')

    tipus_documentacio = fields.Selection([
        ('foto', 'Foto'),
        ('informe I', 'Informe I'),
        ('valoració', 'Valoració')
    ], string='Tipus de Documentació')

    redactor_doc = fields.Selection([
        ('particular', 'Particular'),
        ('inspector', 'Inspector'),
        ('brigada', 'Brigada'),
        ('policia', 'Policia'),
        ('empresa concessionària', 'Empresa concessionària'),
        ('tècnic ajuntament', 'Técnic ajuntament'),
        ('tècnic extern', 'Tècnic extern')
    ], string='Redactor del document')
