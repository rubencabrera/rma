.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================================
Return Merchandise Authorization (RMA) without invoice
======================================================

This module is oriented to manage RMA claims when an invoice is not present
in odoo. The full RMA process usually requieres a reference to an invoice,
but in this particular case, we can only give an invoice number, not use it
to fetch data.



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
`here <https://github.com/OCA/rma/issues/new?body=module:%20crm_claim_rma_without_invoice%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors:
-------------

* Rubén Cabrera Martínez <rcabrera@praxya.com>

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
