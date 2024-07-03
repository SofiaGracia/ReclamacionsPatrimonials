# -*- coding: utf-8 -*-
from odoo import models, fields

class ReclamacionMatricula(models.Model):
    _name = 'reclamacio.matricula'

    matricula = fields.Char('Matrícula', required=True)