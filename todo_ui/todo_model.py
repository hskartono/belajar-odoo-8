# -*- coding: utf-8 -*-
from openerp import models, fields, api

class NewTodoTask(models.Model):
    _inherit = 'todo.task'
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    # tag_ids = fields.Many2many('todo.task.tag', string='Tags')
    tag_ids = fields.Many2many(
        comodel_name='todo.task.tag',   # related model
        relation='todo_task_tag_rel',   # relation table name
        column1='task_id',              # field for "this" record
        column2='tag_id',               # field for "other" record
        string='Tags'
    )
    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute = '_compute_stage_fold'
    )

    @api.one
    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        self.stage_fold = self.stage_id.fold

class Tag(models.Model):
    _name = 'todo.task.tag'
    name = fields.Char('Name', 40, translate=True)
    task_ids = fields.Many2many(
        'todo.task',    # related_model
        string = 'Tasks'
    )

class Stage(models.Model):
    _name = 'todo.task.stage'
    _order = 'sequence,name'
    # String fields:
    name = fields.Char('Name', 40)
    desc = fields.Text('Description')
    state = fields.Selection(
        [('draft','New'), ('open','Started'), ('done','Closed')],
        'State'
    )
    docs = fields.Html('Documentation')
    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3,2))
    # Date fields:
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')
    # Other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')
    tasks = fields.One2many(
        'todo.task',    # related model
        'stage_id',     # field for "this" on related model
        'Task in this stage'
    )