# -*- coding: utf-8 -*-
from odoo import models, fields, api



class AddFieldForContacts(models.Model):
    _inherit = 'res.partner'
    
    #boolean para ver los días
    see_days = fields.Boolean(string="Ver Días")

    #dias de contacto y de entrega
    days_visits = fields.Selection([('monday','Lunes'),('tuesday','Martes'),('wednesday','Miércoles'),('thursday','Jueves'),('friday','Viernes'),('saturday','Sábado'),('sunday','Domingo')],string="Día de Contacto",default='')
    delivery_day = fields.Selection([('monday','Lunes'),('tuesday','Martes'),('wednesday','Miércoles'),('thursday','Jueves'),('friday','Viernes'),('saturday','Sábado'),('sunday','Domingo'),('counter','Mostrador')],string="Día de Entrega",default='')
    
    #hora de recepcion y de visita
    hour_reception = fields.Char(string="Hora de Recepción")
    hour_visit =fields.Char(string="Hora de Visita")