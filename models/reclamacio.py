# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Reclamacio(models.Model):
    _name = 'reclamacio.patrimonial'
    _description = 'Reclamació Patrimonial'

    name = fields.Char(string='Identificador', required=True, copy=False, readonly=True, default='Nova Reclamació')

    tipus_dany = fields.Selection([
        ('persones', 'Persones'),
        ('vehicle', 'Vehicle'),
        ('be_concessionat', 'Be concessionat'),
        ('edifici', 'Edifici'),
        ('agricola', 'Agrícola'),
        ('altre', 'Altre')
    ], string='Tipus de Dany')

    matriculas_afectadas = fields.Many2many('reclamacio.matricula', string='Matrículas afectadas')

    ciudadano_id = fields.Many2many('res.partner', string='Ciudadano')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('reclamacio.patrimonial') or 'New'
        return super(Reclamacio, self).create(vals)
    
    @api.onchange('tipus_dany')
    def _onchange_tipus_dany(self):
        if self.tipus_dany != 'vehicle':
            self.matriculas_afectadas = False

