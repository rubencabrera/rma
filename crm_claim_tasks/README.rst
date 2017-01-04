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


TODO: README en inglés.

Documentación previa:
---------------------

El RMA ya se enlaza con tareas si en responsabilidades se asigna una tarea de
proyecto. Pero lo que ahí se enlaza no es la tarea en la que se repara, sino
el documento que da origen a la reclamación, por eso se llama 
"Responsabilidades"

+ Permite generar una tarea. El nombre se puede generar a partir del código de
RMA. Campo 'code'
+ ¿Debería asignarse un proyecto?
  Opciones:
  + Preguntar al crear la tarea.
  + Introducir un menú de configuración para proyectos de reparaciones.
  + Poner un campo en proyectos para indicar si son de reparaciones.
+ Puede asignarse un revisor por defecto en función de algún campo del RMA.
  El campo 'user_id' es el de responsable en el RMA.
+ La fecha límite de la tarea puede tomarse del rma.
  Campo 'date_deadline'.
+ La descripción de la tarea debe tomarse de algún sitio, la descripción del 
  RMA será poco útil para la tarea de reparación, pero para tener una referencia
  inicial está bien.
>>>>>>> tasks
+ Si hay que llevar materiales, se necesita la dependencia que lo permite.
  https://github.com/OCA/project-service
+ Los materiales se tomarán del pedido de venta/pedido de compra/devolución
asociadas al RMA.
<<<<<<< HEAD
Campo de materiales en la RMA:
picking_ids -(O2M)-> stock.picking
En la tarea:
material_ids  -(O2M)-> project.task.materials
stock_move_ids -(M2M)-> stock.move

+ Crear en data etapas para las tareas que sean de las que generan movimiento
  de stock. 
+ La prioridad de la tarea puede tomarse del RMA.
+ El cliente puede tomarse del RMA, delivery_address_id



It mainly contains the following features:


For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================

* Currently, the warranty duration used is the one configured on the
  products today, not the one which was configured when the product
  has been sold.

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
