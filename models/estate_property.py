

from odoo import models, fields, Command


class InheritedEstateModel(models.Model):
    _inherit = "estate.property"

    dummy = fields.Char()

    def action_sold(self):
        super(InheritedEstateModel, self).action_sold()
        # create account.move
        data = {
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    "name": "6% of the selling price",
                    "quantity": 1,
                    "price_unit": self.selling_price*0.06,
                }),
                Command.create({
                    "name": "an additional 100.00 from administrative fees",
                    "quantity": 1,
                    "price_unit": 100,
                })
            ]
        }

        self.env["account.move"].create(data)
        return True