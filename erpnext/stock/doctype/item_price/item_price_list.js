frappe.listview_settings['Item Price'] = {
	add_fields: ["valid_upto", "is_active"],
	get_indicator: function(doc) {
		if (doc.is_active && (doc.valid_upto && doc.valid_upto < frappe.datetime.nowdate())) {
			return [__("Expired"), "darkgrey", "valid_upto,<," + frappe.datetime.nowdate()];
		}
		else if(doc.is_active) {
			return [__("Active"), "blue", "is_active,=,Yes"];
		} 
		else if(!doc.is_active) {
			return [__("Not active"), "darkgrey", "is_active,=,No"];
		}
	}	
};