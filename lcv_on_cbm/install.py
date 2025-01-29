import frappe
from lcv_on_cbm.custom_fields_property_setter.custom_fields import CUSTOM_FIELDS
from lcv_on_cbm.custom_fields_property_setter.property_setter import get_property_setters
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import  make_property_setter
def after_install():
    create_custom_fields(CUSTOM_FIELDS, ignore_validate=True)
    make_property_setters()
def make_property_setters():
    for property_setter in get_property_setters():
        frappe.make_property_setter(property_setter, validate_fields_for_doctype=False)

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