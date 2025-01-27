frappe.ui.form.on('Landed Cost Purchase Receipt', 'receipt_document', function(frm,cdt,cdn) {
    var d = locals[cdt][cdn];
    frm.set_value("voucher_type",d.receipt_document_type);
    frm.set_value("voucher_name",d.receipt_document);
    
});

frappe.ui.form.on("Landed Cost Voucher", {
    "get_data": function(frm) {
        if(frm.doc.voucher_type == 'Purchase Invoice'){
            frappe.model.with_doc(frm.doc.voucher_type, frm.doc.voucher_name, function() {
                cur_frm.clear_table("items");
                var tabletransfer= frappe.model.get_doc(frm.doc.voucher_type, frm.doc.voucher_name);
                $.each(tabletransfer.items, function(index, row){
                    console.log(typeof(row.tcbm));
                    var d = frm.add_child("items");
                    d.item_code = row.item_code;
                    d.description = row.description;
                    d.receipt_document_type = tabletransfer.doctype;
                    d.receipt_document = tabletransfer.name;
                    d.qty = row.qty;
                    d.rate = row.rate;
                    d.amount = row.amount;
                    d.cbm = row.cbm;
                    d.tcbm = row.tcbm;
                    d.weight = row.weight;
                    d.cost_center = row.cost_center;
                    frm.refresh_field("items");
                });
            });
            
        }
        if(frm.doc.voucher_type == 'Purchase Receipt'){
            frappe.model.with_doc(frm.doc.voucher_type, frm.doc.voucher_name, function() {
                cur_frm.clear_table("items");
                var tabletransfer= frappe.model.get_doc(frm.doc.voucher_type, frm.doc.voucher_name);
                $.each(tabletransfer.items, function(index, row){
                    var d = frm.add_child("items");
                    console.log(typeof(row.tcbm));
                    d.item_code = row.item_code;
                    d.description = row.description;
                    d.receipt_document_type = tabletransfer.doctype;
                    d.receipt_document = tabletransfer.name;
                    d.qty = row.qty;
                    d.rate = row.rate;
                    d.amount = row.amount;
                    d.cbm = row.cbm;
                    d.tcbm = row.tcbm;
                    d.weight = row.weight;
                    d.cost_center = row.cost_center;
                    frm.refresh_field("items");
                    
                });
            });
        }
    }
});