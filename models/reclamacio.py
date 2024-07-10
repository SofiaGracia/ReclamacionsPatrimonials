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

    descripcio_dany = fields.Text(string='Descripció del dany')

    #Localització del dany
    tipus_via = fields.Selection([
        ('avinguda', 'Avinguda'),
        ('cami', 'Cami'),
        ('carrer', 'Carrer'),
        ('carretera', 'Carretera'),
        ('passeig', 'Passeig'),
        ('plaça', 'Plaça'),
        ('travessera', 'Travessera'),
    ], string='Tipus de via')

    nom_via = fields.Text(string='Nom de la via')

    numero_via = fields.Char(string='Número de la via')

    pis = fields.Char(string='Pis')

    escala = fields.Char(string='Escala')

    planta = fields.Char(string='Planta')

    porta = fields.Char(string='Porta')

    referencia_cadastral = fields.Text(string='Referència Cadastral')

    poligon_parcela = fields.Char(string='Poligon i parcel·la')

    adreca_no_estructurada = fields.Text(string='Adreça no estructurada')

    import_valoracio = fields.Text(string='Import Valoració')#No ho tinc massa clar

    #Ens falta lo de la subsanació dels danys
    #I persones interesades??

    observacions = fields.Text(string='Observacions')

    #Relacionar amb documents
    documents_ids = fields.One2many('az_documents.document', 'reclamacio_id', string = 'Documentos')

    #Redactor del document (A part de la informació que ja haurem posat en la relació amb documents)
    redactor_doc = fields.Selection([
        ('particular', 'Particular'),
        ('inspector', 'Inspector'),
        ('brigada', 'Brigada'),
        ('policia', 'Policia'),
        ('empresa concessionària', 'Empresa concessionària'),
        ('tècnic ajuntament', 'Tècnic ajuntament'),
        ('tècnic extern', 'Tècnic extern')
    ], string='Redactor del document')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('reclamacio.patrimonial') or 'New'
        return super(Reclamacio, self).create(vals)
    
    @api.onchange('tipus_dany')
    def _onchange_tipus_dany(self):
        if self.tipus_dany != 'vehicle':
            self.matriculas_afectadas = False

