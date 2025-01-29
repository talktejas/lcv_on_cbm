CUSTOM_FIELDS={
	'Contact': [
		{
			'label': 'Line ID',
			'fieldname': 'line_id',
			'fieldtype': 'Data',
			'insert_after': 'mobile_no',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Whatsapp',
			'fieldname': 'whatsapp',
			'fieldtype': 'Data',
			'insert_after': 'line_id',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Wechat',
			'fieldname': 'wechat',
			'fieldtype': 'Data',
			'insert_after': 'whatsapp',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Facebook Messenger',
			'fieldname': 'facebook_messenger',
			'fieldtype': 'Data',
			'insert_after': 'wechat',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Facebook URL',
			'fieldname': 'facebook_url',
			'fieldtype': 'Data',
			'insert_after': 'facebook_messenger',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Nick Name in English',
			'fieldname': 'nick_name_in_english',
			'fieldtype': 'Data',
			'insert_after': 'contact_section',
			'in_list_view': 0,
			'reqd': 1,
			'translatable': 1
		}
	],
	'Customer': [
		{
			'label': 'Customer Line ID',
			'fieldname': 'customer_line_id',
			'fieldtype': 'Data',
			'insert_after': 'customer_facebook_url',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Customer Facebook URL',
			'fieldname': 'customer_facebook_url',
			'fieldtype': 'Data',
			'insert_after': 'customer_web_url',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Customer Email ',
			'fieldname': 'customer_email_',
			'fieldtype': 'Data',
			'insert_after': 'lead_name',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Customer Web URL',
			'fieldname': 'customer_web_url',
			'fieldtype': 'Data',
			'insert_after': 'customer_email_',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Customer Whatsapp',
			'fieldname': 'customer_whatsapp',
			'fieldtype': 'Data',
			'insert_after': 'customer_line_id',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Customer FB Messenger ID',
			'fieldname': 'customer_fb_messenger_id',
			'fieldtype': 'Data',
			'insert_after': 'customer_wechat_id',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Customer Wechat ID',
			'fieldname': 'customer_wechat_id',
			'fieldtype': 'Data',
			'insert_after': 'customer_whatsapp',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Known As in English',
			'fieldname': 'known_as_in_english',
			'fieldtype': 'Data',
			'insert_after': 'naming_series',
			'in_list_view': 0,
			'reqd': 1,
			'translatable': 1
		}
	],
	'Item': [
		{
			'label': 'Length',
			'fieldname': 'length',
			'fieldtype': 'Float',
			'insert_after': 'purchase_details_cb',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Breadth',
			'fieldname': 'breadth',
			'fieldtype': 'Float',
			'insert_after': 'length',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Height',
			'fieldname': 'height',
			'fieldtype': 'Float',
			'insert_after': 'breadth',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'CbmCtn',
			'fieldname': 'cbmctn',
			'fieldtype': 'Float',
			'insert_after': 'height',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'GwCtn',
			'fieldname': 'gwctn',
			'fieldtype': 'Float',
			'insert_after': 'cbmctn',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Measurements',
			'fieldname': 'measurements',
			'fieldtype': 'Section Break',
			'insert_after': 'warranty_period',
			'in_list_view': 0
		},
		{
			'label': 'Ctn Height',
			'fieldname': 'ctn_height',
			'fieldtype': 'Float',
			'insert_after': 'measurements',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Breadth',
			'fieldname': 'ctn_breadth',
			'fieldtype': 'Float',
			'insert_after': 'ctn_height',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Length',
			'fieldname': 'ctn_length',
			'fieldtype': 'Float',
			'insert_after': 'ctn_breadth',
			'in_list_view': 0,
			'precision': 2
		}
	],
	'Landed Cost Item': [
		{
			'label': 'TCbm',
			'fieldname': 'tcbm',
			'fieldtype': 'Float',
			'insert_after': 'amount',
			'in_list_view': 1,
			'precision': 5
		}
	],
	'Purchase Invoice': [
		{
			'label': 'Do Nos',
			'fieldname': 'do_nos',
			'fieldtype': 'Text',
			'insert_after': 'supplier_name',
			'in_list_view': 0,
			'translatable': 1
		}
	],
	'Purchase Invoice Item': [
		{
			'label': 'TCbm',
			'fieldname': 'tcbm',
			'fieldtype': 'Float',
			'insert_after': 'item_weight_details',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'Measurements',
			'fieldname': 'measurements',
			'fieldtype': 'Section Break',
			'insert_after': 'item_weight_details',
			'in_list_view': 0
		},
		{
			'label': 'Ctn Length',
			'fieldname': 'ctn_length',
			'fieldtype': 'Float',
			'insert_after': 'measurements',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Breadth',
			'fieldname': 'ctn_breadth',
			'fieldtype': 'Float',
			'insert_after': 'ctn_length',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Height',
			'fieldname': 'ctn_height',
			'fieldtype': 'Float',
			'insert_after': 'ctn_breadth',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'GwCtn',
			'fieldname': 'gwctn',
			'fieldtype': 'Float',
			'insert_after': 'item_weight_details',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'CbmCtn',
			'fieldname': 'cbmctn',
			'fieldtype': 'Float',
			'insert_after': 'tcbm',
			'in_list_view': 0,
			'precision': 5
		}
	],
	'Purchase Order': [
		{
			'label': 'Do Nos',
			'fieldname': 'do_nos',
			'fieldtype': 'Text',
			'insert_after': 'supplier_section',
			'in_list_view': 1,
			'translatable': 1
		}
	],
	'Purchase Order Item': [
		{
			'label': 'TCbm',
			'fieldname': 'tcbm',
			'fieldtype': 'Float',
			'insert_after': 'item_weight_details',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'CBM',
			'fieldname': 'cbm',
			'fieldtype': 'Float',
			'insert_after': 'cbmctn',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'Measurements',
			'fieldname': 'measurements',
			'fieldtype': 'Section Break',
			'insert_after': 'tcbm',
			'in_list_view': 0
		},
		{
			'label': 'Ctn Length',
			'fieldname': 'ctn_length',
			'fieldtype': 'Float',
			'insert_after': 'measurements',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Breadth',
			'fieldname': 'ctn_breadth',
			'fieldtype': 'Float',
			'insert_after': 'ctn_length',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Height',
			'fieldname': 'ctn_height',
			'fieldtype': 'Float',
			'insert_after': 'ctn_breadth',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'GwCtn',
			'fieldname': 'gwctn',
			'fieldtype': 'Float',
			'insert_after': 'weight_per_unit',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'CbmCtn',
			'fieldname': 'cbmctn',
			'fieldtype': 'Float',
			'insert_after': 'ctn_height',
			'in_list_view': 0,
			'precision': 5
		}
	],
	'Purchase Receipt': [
		{
			'label': 'Do Nos',
			'fieldname': 'do_nos',
			'fieldtype': 'Data',
			'insert_after': 'supplier_delivery_note',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Transporter Voucher No',
			'fieldname': 'transporter_voucher_no',
			'fieldtype': 'Data',
			'insert_after': 'transporter_name',
			'in_list_view': 0,
			'translatable': 1
		},
		{
			'label': 'Transporter DO No',
			'fieldname': 'transporter_do_no',
			'fieldtype': 'Data',
			'insert_after': 'lr_date',
			'in_list_view': 0,
			'translatable': 1
		}
	],
	'Purchase Receipt Item': [
		{
			'label': 'TCbm',
			'fieldname': 'tcbm',
			'fieldtype': 'Float',
			'insert_after': 'item_weight_details',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'CBM',
			'fieldname': 'cbm',
			'fieldtype': 'Float',
			'insert_after': 'tcbm',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'Measurements',
			'fieldname': 'measurements',
			'fieldtype': 'Section Break',
			'insert_after': 'weight_uom',
			'in_list_view': 0
		},
		{
			'label': 'CbmCtn',
			'fieldname': 'cbmctn',
			'fieldtype': 'Float',
			'insert_after': 'tcbm',
			'in_list_view': 0,
			'precision': 5
		},
		{
			'label': 'GwCtn',
			'fieldname': 'gwctn',
			'fieldtype': 'Float',
			'insert_after': 'weight_uom',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Length',
			'fieldname': 'ctn_length',
			'fieldtype': 'Float',
			'insert_after': 'measurements',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Breadth',
			'fieldname': 'ctn_breadth',
			'fieldtype': 'Float',
			'insert_after': 'ctn_length',
			'in_list_view': 0,
			'precision': 2
		},
		{
			'label': 'Ctn Height',
			'fieldname': 'ctn_height',
			'fieldtype': 'Float',
			'insert_after': 'ctn_breadth',
			'in_list_view': 0,
			'precision': 2
		}
	]
}