.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================
Generate and manage tasks from RMA claims
=========================================

Allow creation of project tasks from an RMA claim. 

Relates tasks and crm_claims through a Smart Button so new tasks can be created
and associated with a claim.

If a deadline is filled in the RMA, it's value is taken into new tasks.

The user responsible in the RMA is assigned as the reviewer of the new task.

Priority is also copied to new tasks. 

The related partner is the one in the Delivery Address RMA field. 

Configuration.
--------------

Check option 'Consume Material' in Task Stage to generate a stock move when the
task is in that stage.

Go to Settings -> Configuration - > Projects and enable option "Manage time 
estimation on tasks"


TODO: README en inglés.

Documentación previa:
---------------------

+ Si hay que llevar materiales, se necesita la dependencia que lo permite.
  https://github.com/OCA/project-service
+ Los materiales se tomarán del pedido de venta/pedido de compra/devolución
asociadas al RMA.
Campo de materiales en la RMA:
picking_ids -(O2M)-> stock.picking
En la tarea:
material_ids  -(O2M)-> project.task.materials
stock_move_ids -(M2M)-> stock.move

+ Crear en data etapas para las tareas que sean de las que generan movimiento
  de stock. 


It mainly contains the following features:


For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================

* Would it be interesting to check for incoming pickings in the RMA and take 
  those products into account in materials tab? 

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/rma/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/rma/issues/new?body=module:%20crm_claim_rma%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors:
-------------

* Emmanuel Samyn <esamyn@gmail.com>
* Sébastien Beau <sebastien.beau@akretion.com.br>
* Benoît Guillot <benoit.guillot@akretion.com.br>
* Joel Grand-Guillaume <joel.grandguillaume@camptocamp.com>
* Guewen Baconnier <guewen.baconnier@camptocamp.com>
* Yannick Vaucher <yannick.vaucher@camptocamp.com>
* Javier Carrasco <javier.carrasco@eezee-it.com>
* Yanina Aular <yanina.aular@vauxoo.com>
* Osval Reyes <osval@vauxoo.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
