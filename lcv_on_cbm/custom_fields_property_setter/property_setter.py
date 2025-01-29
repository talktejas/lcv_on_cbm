
import frappe
def get_property_setters():
    return[
        get_options_property_setter(
            "Landed Cost Voucher",
            "distribute_charges_based_on",
            ["TCbm"],
             prepend=False,
        ),
    ]
    
def get_options_property_setter(doctype, fieldname, new_options, prepend=True):
    existing_options = frappe.get_meta(doctype).get_options(fieldname).split("\n")
    if prepend:
        options = new_options + existing_options
    else:
        options = existing_options + new_options

    # using dict.fromkeys to get unique ordered options
    options = "\n".join(dict.fromkeys(options))

    return {
        "doctype": doctype,
        "doctype_or_field": "DocField",
        "fieldname": fieldname,
        "property": "options",
        "is_system_generated": 0,  
        "value": options,
    }