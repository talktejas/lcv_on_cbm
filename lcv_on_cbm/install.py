import frappe
from lcv_on_cbm.custom_fields.custom_fields import CUSTOM_FIELDS
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
    create_custom_fields(CUSTOM_FIELDS, ignore_validate=True)

def before_uninstall():
    delete_custom_fields(CUSTOM_FIELDS)

def delete_custom_fields(custom_fields):
    for doctypes, fields in custom_fields.items():
        if isinstance(fields, dict):
            fields = [fields]

        if isinstance(doctypes, str):
            doctypes = (doctypes,)

        for doctype in doctypes:
            frappe.db.delete(
                "Custom Field",
                {
                    "fieldname": ("in", [field["fieldname"] for field in fields]),
                    "dt": doctype,
                },
            )
            frappe.clear_cache(doctype=doctype)