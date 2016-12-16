# -*- coding: utf-8 -*-
# Copyright 2016 Rubén Cabrera Martínez, Praxya Soluciones
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "CRM Claim Lot Repair",
    "summary": "Create repair tasks from claim lines with related product lot",
    "version": "8.0.1.0.0",
    "category": "Generic Modules/CRM & SRM",
    "website": "https://www.praxya.com",
    "author": "Rubén Cabrera Martínez, Praxya Soluciones",
    "license": "AGPL-3",
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "crm_claim_tasks",
    ],
    "data": [
        # "security/some_model_security.xml",
        # "security/ir.model.access.csv",
        "views/crm_claim_view.xml",
    ],
}
