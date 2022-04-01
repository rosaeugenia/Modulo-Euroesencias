# -*- coding: utf-8 -*-

from odoo import models, fields


class Europroduct(models.Model):
    _name = "euro.europroduct"  # eu_europroduct nombre de la tabla
    _description = "products Euroesencias"
    _inherit = 'product.template'

    date_launching = fields.Datetime(string="Fecha de Lanzamiento")
    orientation = fields.Char(string="Orientación o contratipo")
    uso = fields.Char(string="Uso")
    category_id = fields.Many2one("euro.category", string="Categoría")
    maker = fields.Char(string="Fabricante")
    description_euro = fields.Text(string="Descripción Euroesencias")
    top_note = fields.Char(string="Top Note")
    heart_note = fields.Char(string="Heart Note")
    base_note = fields.Char(string="Base Note")


class Eurocategory(models.Model):
    _name = "euro.category"
    _description = "Categoría"
    name = fields.Char("Nombre")

"""class productEuro(models.Model):
    _inherit = 'product.template'
    europroduct_ids = fields.One2many("euro.europroduct", "categ_id")"""
